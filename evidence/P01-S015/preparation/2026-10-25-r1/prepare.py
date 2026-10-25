"""Preparation evidence collector only; no controller or GitHub mutation code.

Run with the already-installed Python 3.13 from the repository root. This script
reads specifications and GitHub state and writes only this preparation directory.
It does not install packages, commit, push, or change program/story state.
"""
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = "ef2833a8fce8bbb11262b7890883c07ea9e73b31"
DATE = "2026-10-25"
PACKET = "ACT-P01-S015-2026-10-25-r1"


def run(*args):
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Read-only command failed: {args[0:3]!r}; exit={result.returncode}")
    return result.stdout.strip()


def gh_json(*args):
    result = json.loads(run("gh", *args))
    if isinstance(result, dict) and result.get("errors"):
        raise RuntimeError("GraphQL returned errors; stop before mutation")
    return result


def write(name, value):
    (HERE / name).write_bytes((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def source_digest(path):
    # Source documents are Git text; hash canonical LF content across platforms.
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


errors = []
checks = Counter()


def require(ok, message, category):
    checks[category] += 1
    if not ok:
        errors.append(message)


properties = ["Story ID", "Phase", "Sequence", "Status", "Step", "Hold reason", "Risk", "Actor", "Dependencies", "Unlocks", "Preferred route", "Research freshness"]
headings = ["User story", "Bounded objective", "Learning objective", "Current research requirements", "Preconditions and unlock conditions", "In scope", "Out of scope and prohibited changes", "Privilege and human approval", "Risk rationale", "Execution contract", "Automated acceptance tests", "Human validation", "Idempotency and rollback", "Required evidence", "Definition of done", "Pause-safe boundaries"]
enums = {
    "Status": ["Planned", "Ready", "In Progress", "Waiting", "Done", "Superseded"],
    "Step": ["Research", "Learning", "Implementation", "Testing", "Review", "Human Validation", "Merge"],
    "Hold reason": ["None", "Phase Not Activated", "Dependency", "Approval", "Paused", "Blocked", "Usage Budget", "External System"],
    "Risk": ["Low", "Medium", "High", "Critical"],
    "Actor": ["Human", "LLM", "Human + LLM"],
}
stories = []
story_files = sorted((ROOT / "docs/stories").glob("P??/P??-S???-*.md"))
require(len(story_files) == 137, f"Expected 137 stories; found {len(story_files)}", "inventory")
for path in story_files:
    body = path.read_text(encoding="utf-8-sig")
    metadata = dict(re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|\s*$", body, re.M))
    sid = metadata.get("Story ID", "")
    require(bool(re.fullmatch(r"P\d{2}-S\d{3}", sid)) and sid in path.name, str(path) + ": invalid ID", "properties")
    for key in properties:
        value = metadata.get(key, "").strip()
        require(bool(value) and not re.search(r"\b(?:TODO|TBD)\b|^N/A$|^Not applicable$", value, re.I), sid + ": invalid " + key, "properties")
    for key, values in enums.items():
        require(metadata.get(key) in values, sid + ": invalid enum " + key, "enums")
    for number, title in enumerate(headings, 1):
        section = re.search(rf"(?ms)^## {number}\. {re.escape(title)}\s*\n(.+?)(?=^## |\Z)", body)
        require(bool(section and section.group(1).strip()), sid + ": missing/empty section " + str(number), "sections")
    for label in ["Interface", "Provider", "Model class", "Effort", "Fallback"]:
        require(label + ":" in metadata.get("Preferred route", ""), sid + ": missing route " + label, "routes")
    phase = metadata["Phase"].split()[0]
    sequence = int(metadata["Sequence"])
    deps = re.findall(r"P\d{2}-S\d{3}", metadata["Dependencies"])
    unlocks = re.findall(r"P\d{2}-S\d{3}", metadata["Unlocks"])
    relative = path.relative_to(ROOT).as_posix()
    stories.append({"id": sid, "phase": phase, "sequence": sequence, "title": body.splitlines()[0].removeprefix("# "), "path": relative, "sha256": source_digest(path), "specificationUrl": f"https://github.com/banksjim/local-llm-setup/blob/{BASE}/{relative}", "status": metadata["Status"], "step": metadata["Step"], "holdReason": metadata["Hold reason"], "risk": metadata["Risk"], "actor": metadata["Actor"], "dependencies": deps, "unlocks": unlocks, "preferredRoute": metadata["Preferred route"], "researchFreshness": metadata["Research freshness"]})

by_id = {s["id"]: s for s in stories}
require(len(by_id) == 137, "Duplicate story IDs", "inventory")
expected_counts = dict(zip([f"P{n:02}" for n in range(1, 11)], [15, 12, 11, 14, 12, 14, 19, 12, 13, 15]))
for phase, count in expected_counts.items():
    members = [s for s in stories if s["phase"] == phase]
    require(len(members) == count, phase + ": wrong inventory", "phase_counts")
    require(sorted(s["sequence"] for s in members) == list(range(1, count + 1)), phase + ": sequence gap/duplicate", "sequence")
    phase_paths = list((ROOT / "docs/specifications/phases").glob(phase + "-*.md"))
    require(len(phase_paths) == 1, phase + ": phase document missing/ambiguous", "phase_tables")
    rows = re.findall(r"^\| (\d+) \| \[(P\d{2}-S\d{3}):.*?\]\([^\n]+?\) \| ([^|]+) \| ([^|]+) \|", phase_paths[0].read_text(encoding="utf-8"), re.M)
    expected = sorted((s["sequence"], s["id"], s["step"], s["risk"]) for s in members)
    actual = [(int(n), sid, step.strip(), risk.strip()) for n, sid, step, risk in rows]
    require(actual == expected, phase + ": phase table disagrees with stories", "phase_tables")
for story in stories:
    for dep in story["dependencies"]:
        require(dep in by_id and story["id"] in by_id[dep]["unlocks"], story["id"] + ": nonreciprocal dependency " + dep, "graph")
    for unlocked in story["unlocks"]:
        require(unlocked in by_id and story["id"] in by_id[unlocked]["dependencies"], story["id"] + ": nonreciprocal unlock " + unlocked, "graph")
visited, active = set(), set()


def visit(sid):
    if sid in active:
        errors.append("Dependency cycle: " + sid)
        return
    if sid in visited:
        return
    active.add(sid)
    for dep in by_id[sid]["dependencies"]:
        if dep in by_id:
            visit(dep)
    active.remove(sid)
    visited.add(sid)


for sid in by_id:
    visit(sid)
require(len(visited) == 137, "DAG did not visit all 137 stories", "graph")
require([s["id"] for s in sorted(stories, key=lambda s: (s["phase"], s["sequence"])) if not s["dependencies"]] == ["P01-S015"], "Unexpected initial root story", "graph")
require(all(s["status"] == "Planned" for s in stories), "Unexpected already-activated story", "lifecycle")

authority_paths = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
local_links = 0
for path in authority_paths:
    text = re.sub(r"(?ms)^```.*?^```\s*$", "", path.read_text(encoding="utf-8-sig"))
    for target in re.findall(r"\]\(([^\s)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target_path = target.split("#")[0]
        if target_path:
            local_links += 1
            require((path.parent / target_path).resolve().exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}", "local_links")

manifest = {"packetId": PACKET, "baselineCommit": BASE, "hashEncoding": "Canonical Git text bytes; normalize CRLF to LF when comparing working files", "files": [{"path": p.relative_to(ROOT).as_posix(), "gitBlob": run("git", "rev-parse", BASE + ":" + p.relative_to(ROOT).as_posix()), "sha256": source_digest(p)} for p in authority_paths]}
write("authority-manifest.json", manifest)
write("story-inventory.json", {"baselineCommit": BASE, "count": len(stories), "byPhase": expected_counts, "stories": sorted(stories, key=lambda s: (s["phase"], s["sequence"]))})

viewer = gh_json("api", "graphql", "-f", "query=query { viewer { id login projectsV2(first:100) { totalCount pageInfo { hasNextPage endCursor } nodes { id number title public closed url } } } }")["data"]["viewer"]
user = gh_json("api", "user", "--jq", "{login: .login, id: .id, type: .type}")
repo = gh_json("repo", "view", "banksjim/local-llm-setup", "--json", "id,nameWithOwner,url,visibility,defaultBranchRef,viewerPermission")
issues = gh_json("issue", "list", "--repo", "banksjim/local-llm-setup", "--state", "all", "--limit", "200", "--json", "number,title,state,url")
write("issue-inventory.json", {"accessDate": DATE, "repository": "banksjim/local-llm-setup", "query": "all states; limit 200", "items": issues, "emptyInventoryComplete": not issues})
require(viewer["login"] == user["login"] == "banksjim" and user["type"] == "User", "Wrong GitHub owner", "github")
require(not viewer["projectsV2"]["pageInfo"]["hasNextPage"], "Project inventory pagination incomplete", "github")
require(viewer["projectsV2"]["totalCount"] == 0, "Remote inventory drift: inspect Projects before proceeding", "github")
require(repo["nameWithOwner"] == "banksjim/local-llm-setup" and repo["viewerPermission"] == "ADMIN", "Repository mismatch/permissions", "github")
require(not issues, "Remote issue inventory drift: inspect before proceeding", "github")
auth = subprocess.run(["gh", "auth", "status"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
auth_text = auth.stdout + auth.stderr
scope_match = re.search(r"Token scopes:\s*(.+)", auth_text)
scopes = re.findall(r"'([^']+)'", scope_match.group(1)) if scope_match else []
require(auth.returncode == 0 and "project" in scopes and "repo" in scopes, "GitHub scope check failed", "github")
remote = run("git", "remote", "get-url", "origin")
remote_head = run("git", "ls-remote", "origin", "HEAD", "refs/heads/main")
require(remote == "https://github.com/banksjim/local-llm-setup.git", "Wrong origin", "git")
require(all(line.split()[0] == BASE for line in remote_head.splitlines()), "Remote main differs from specification baseline", "git")
dirty = run("git", "status", "--porcelain", "--untracked-files=all").splitlines()
foreign_dirty = [line for line in dirty if not line[3:].replace("\\", "/").startswith("evidence/P01-S015/preparation/2026-10-25-r1/")]
require(not foreign_dirty, "Unexpected worktree modifications", "git")
query = "query($name:String!) { inspected:__type(name:$name) { name inputFields { name type { kind name ofType { kind name ofType { kind name } } } } fields { name } enumValues { name } } }"
schema = {}
for type_name in ["CreateProjectV2Input", "UpdateProjectV2Input", "CreateProjectV2FieldInput", "UpdateProjectV2FieldInput", "CreateProjectV2ViewInput", "UpdateProjectV2ViewInput", "ProjectV2ViewConfigurationInput", "ProjectV2ViewLayout", "ConvertProjectV2DraftIssueItemToIssueInput", "ProjectV2View", "ProjectV2Field", "ProjectV2SingleSelectField"]:
    schema[type_name] = gh_json("api", "graphql", "-f", "query=" + query, "-f", "name=" + type_name)["data"]["inspected"]
    require(bool(schema[type_name]), "Missing GraphQL type " + type_name, "api_schema")
write("github-api-schema.json", {"accessDate": DATE, "types": schema})
write("prerequisites.json", {"accessDate": DATE, "capturedAtUtc": datetime.now(timezone.utc).isoformat(), "baselineCommit": BASE, "branch": run("git", "branch", "--show-current"), "origin": remote, "remoteRefs": remote_head.splitlines(), "initialWorktree": "Clean before preparation; only this authorized preparation directory added", "unrelatedWorktreeChanges": foreign_dirty, "workspaceIgnored": bool(run("git", "check-ignore", "--", "~local-llm-setup.code-workspace")), "versions": {"git": run("git", "--version"), "gh": run("gh", "--version").splitlines()[0], "python": run("python", "--version"), "codex": run("codex", "--version"), "claude": run("cmd", "/c", "claude", "--version")}, "github": {"identity": user, "viewerNodeId": viewer["id"], "authenticationPassed": auth.returncode == 0, "scopes": scopes, "credentialValueStored": False, "repository": repo, "projectInventory": viewer["projectsV2"], "writeCapability": "Not exercised: read access and granted scopes verified, live writes require authorization"}, "bootstrapRuntime": {"name": "Windows PowerShell", "version": "5.1.26100.8875", "edition": "Desktop", "externalTestFrameworkRequired": False}})
write("validation.json", {"accessDate": DATE, "verdict": "PASS" if not errors else "FAIL", "kind": "Preparation structural validation; not implementation acceptance or independent review", "storyCount": len(stories), "uniqueStoryIds": len(by_id), "dagVisited": len(visited), "localLinksChecked": local_links, "checksByCategory": dict(checks), "errors": errors, "unrunChecks": ["Full story semantic re-review", "External HTTP validation of every reference outside P01-S015 scope", "GitHub mutation acceptance/idempotency/rollback", "Independent cross-provider implementation review", "Genuine owner validation"]})
print(json.dumps({"verdict": "PASS" if not errors else "FAIL", "stories": len(stories), "checks": sum(checks.values()), "localLinks": local_links, "errors": errors}, indent=2))
if errors:
    raise SystemExit(1)
