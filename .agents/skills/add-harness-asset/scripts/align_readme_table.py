#!/usr/bin/env python3
"""README '수록 자산' 표에 행을 추가하고 CJK 폭 기준으로 재정렬한다.

harness-kit README의 표는 한글(전각 2칸)·영문(1칸)이 섞여 있어, 단순 글자 수가
아니라 East Asian Width(전각 W/F=2, 그 외=1)로 칸을 맞춘다. ambiguous(A: '—', '·' 등)는
이 레포 기존 정렬과 동일하게 1칸으로 센다(역검증으로 확인된 값). 이 스크립트는 표를
통째로 다시 정렬하므로, 새 행이 기존보다 길면 열을 자동으로 넓혀 모든 행을 다시 패딩한다.

사용:
  python3 align_readme_table.py --readme README.md --section "Skills" \
      --cells '`my-skill`' '한 줄 설명…'

--section 은 표 바로 위의 제목 텍스트(레벨 무관. 예: skill 카테고리 "프론트엔드" / Agents / Hooks / "AGENTS.md 스니펫").
--cells 는 표 컬럼 순서대로 넣는다(Skills/Agents=이름·설명, Hooks=이름·트리거,
스니펫=이름·용도). 개수는 대상 표의 헤더 열 수와 같아야 한다.
'_(아직 없음)_' placeholder 행은 자동으로 제거된다. 같은 이름 행이 이미 있으면 에러로 멈춘다.
"""
import argparse
import sys
import unicodedata


def width(s: str, amb: int = 1) -> int:
    w = 0
    for ch in s:
        ea = unicodedata.east_asian_width(ch)
        w += 2 if ea in ("W", "F") else (amb if ea == "A" else 1)
    return w


def pad(s: str, target: int) -> str:
    return s + " " * (target - width(s))


def split_cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def find_heading(lines, section):
    for i, l in enumerate(lines):
        if l.lstrip().startswith("#"):
            text = l.lstrip("#").strip()
            if text == section:
                return i
    raise SystemExit(f"[에러] '### {section}' 제목을 찾지 못했습니다. --section 값을 확인하세요.")


def find_table(lines, start):
    """heading 이후 첫 markdown 표의 (header_idx, sep_idx, [data_idx...]) 반환."""
    i = start + 1
    while i < len(lines) and not lines[i].lstrip().startswith("|"):
        # 다음 제목을 만나면 표가 없는 것
        if lines[i].lstrip().startswith("#") and i > start:
            raise SystemExit(f"[에러] 제목 다음에서 표를 찾지 못했습니다 (line {start + 1}).")
        i += 1
    if i >= len(lines):
        raise SystemExit("[에러] 표를 찾지 못했습니다.")
    header_idx = i
    sep_idx = i + 1
    data_idx = []
    j = sep_idx + 1
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        data_idx.append(j)
        j += 1
    return header_idx, sep_idx, data_idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", required=True)
    ap.add_argument("--section", required=True, help="표 위 ### 제목 텍스트")
    ap.add_argument("--cells", nargs="+", required=True, metavar="CELL")
    ap.add_argument("--amb", type=int, default=1, help="ambiguous 폭(기본 1)")
    args = ap.parse_args()

    text = open(args.readme, encoding="utf-8").read()
    nl = "\n"
    lines = text.split(nl)

    h = find_heading(lines, args.section)
    header_idx, sep_idx, data_idx = find_table(lines, h)

    header = split_cells(lines[header_idx])
    ncol = len(header)
    if len(args.cells) != ncol:
        raise SystemExit(f"[에러] 대상 표는 {ncol}열인데 --cells 는 {len(args.cells)}개입니다.")

    rows = [split_cells(lines[d]) for d in data_idx]
    # placeholder 행 제거
    rows = [r for r in rows if r and r[0] != "_(아직 없음)_"]

    new_name = args.cells[0]
    if any(r[0] == new_name for r in rows):
        raise SystemExit(f"[에러] '{new_name}' 행이 이미 있습니다. 중복 추가를 막았습니다. "
                         f"수정하려면 README에서 직접 고치세요.")

    rows.append(list(args.cells))

    # 열 폭 = 헤더+전체 행의 최대 시각 폭
    colw = [max(width(header[c], args.amb), max(width(r[c], args.amb) for r in rows)) for c in range(ncol)]

    def emit(cells):
        return "| " + " | ".join(pad(cells[c], colw[c]) for c in range(ncol)) + " |"

    block = [emit(header), "| " + " | ".join("-" * colw[c] for c in range(ncol)) + " |"]
    block += [emit(r) for r in rows]

    # 정합성: 모든 줄 시각 폭 동일해야 함
    wset = {width(b, args.amb) for b in block}
    if len(wset) != 1:
        raise SystemExit(f"[에러] 정렬 검증 실패: 줄 폭이 제각각 {sorted(wset)}")

    new_lines = lines[:header_idx] + block + lines[data_idx[-1] + 1:] if data_idx else lines[:sep_idx + 1] + block[2:] + lines[sep_idx + 1:]
    open(args.readme, "w", encoding="utf-8").write(nl.join(new_lines))

    print(f"[OK] '### {args.section}' 표에 행 추가/정렬 완료 (열 폭 {colw}, 줄 폭 {wset.pop()})")
    print("추가된 행:")
    print(emit(rows[-1]))


if __name__ == "__main__":
    main()
