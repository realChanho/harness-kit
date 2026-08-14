#!/usr/bin/env python3
"""`.claude` 정본에서 Codex용 `.agents` 미러를 다시 만든다.

이 레포는 같은 자산을 두 벌 갖고 있다. `.claude/`(Claude Code용)가 정본이고
`.agents/`(Codex용)는 경로·문서명만 바꾼 미러다. 손으로 두 벌을 맞추면 반드시
어긋나므로(실제로 카테고리 표 구조가 한쪽에만 반영된 적이 있다) 이 스크립트로 생성한다.

레포 루트에서 실행한다:

    python3 .claude/skills/add-harness-asset/scripts/sync_agents_mirror.py

`--check` 를 주면 파일을 쓰지 않고 어긋난 파일만 출력하고 1로 종료한다.

치환하면 안 되는 구간(예: 이 미러 규칙 자체를 설명하는 문단)은 마크다운에서
`mirror:verbatim` 주석으로 감싼다. 여는 주석과 닫는 주석 사이는 그대로 복사된다.

이 스크립트 자신은 미러에 복사하지 않는다. 미러를 만드는 도구는 정본 쪽에만 있으면 된다.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

# (정본, 미러) 쌍. 경로는 레포 루트 기준.
SKILL_DIR = Path(".claude/skills/add-harness-asset")
MIRROR_SKILL_DIR = Path(".agents/skills/add-harness-asset")

# 공통 치환 — 경로와 문서명만 바꾼다.
COMMON = [
    (r"\.claude/", ".agents/"),
    (r"claude-md/", "agents-md/"),
    (r"CLAUDE\.md", "AGENTS.md"),
]
# 루트 문서에만 추가로 적용 — 대상 에이전트 이름.
ROOT_ONLY = [(r"Claude Code", "Codex")]

OPEN_MARK = "<!-- mirror:verbatim -->"
CLOSE_MARK = "<!-- /mirror:verbatim -->"


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(out.stdout.strip())


def substitute(text: str, rules) -> str:
    """마커로 감싼 구간을 빼고 치환한다."""
    out = []
    verbatim = False
    for line in text.split("\n"):
        if OPEN_MARK in line:
            verbatim = True
        if verbatim:
            out.append(line)
        else:
            for pat, repl in rules:
                line = re.sub(pat, repl, line)
            out.append(line)
        if CLOSE_MARK in line:
            verbatim = False
    return "\n".join(out)


def pairs(root: Path):
    """(정본, 미러, 치환규칙) 목록. 이 스크립트 자신은 뺀다."""
    me = Path(__file__).name
    yield root / "CLAUDE.md", root / "AGENTS.md", COMMON + ROOT_ONLY
    yield root / SKILL_DIR / "SKILL.md", root / MIRROR_SKILL_DIR / "SKILL.md", COMMON
    for script in sorted((root / SKILL_DIR / "scripts").glob("*.py")):
        if script.name == me:
            continue
        yield script, root / MIRROR_SKILL_DIR / "scripts" / script.name, COMMON


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="쓰지 않고 어긋난 파일만 보고")
    args = ap.parse_args()

    root = repo_root()
    stale = []
    for src, dst, rules in pairs(root):
        if not src.exists():
            raise SystemExit(f"[에러] 정본을 찾지 못했습니다: {src}")
        want = substitute(src.read_text(encoding="utf-8"), rules)
        have = dst.read_text(encoding="utf-8") if dst.exists() else None
        rel = dst.relative_to(root)
        if want == have:
            print(f"[--] {rel}")
            continue
        stale.append(rel)
        if args.check:
            print(f"[!!] {rel} — 정본과 어긋남")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(want, encoding="utf-8")
            print(f"[갱신] {rel}")

    if args.check and stale:
        print(f"\n{len(stale)}개 파일이 정본과 어긋납니다. 인자 없이 다시 실행하세요.")
        sys.exit(1)
    print("\n[OK] 미러 동기화 완료" if not args.check else "\n[OK] 미러가 정본과 일치합니다")


if __name__ == "__main__":
    main()
