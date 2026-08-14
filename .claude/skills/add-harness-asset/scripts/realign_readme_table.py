#!/usr/bin/env python3
"""이미 있는 README 표를 행 추가 없이 다시 정렬한다.

`align_readme_table.py` 는 '행 추가 + 재정렬'을 함께 한다. 표에 이미 있는 셀을 손으로
고친 뒤(예: 이름 칸을 non-breaking hyphen 표기로 바꾼 뒤) 열 폭만 다시 맞추고 싶을 때
쓰는 스크립트다. 폭 계산 로직은 같은 폴더의 `align_readme_table.py` 에서 그대로 가져오므로
두 스크립트의 정렬 결과가 어긋나지 않는다.

사용:
  python3 realign_readme_table.py --readme README.md --section "하네스 관리 · 유틸리티"

--section 은 표 바로 위의 제목 텍스트(레벨 무관).
"""
import argparse
import importlib.util
import sys
from pathlib import Path

ALIGNER = Path(__file__).resolve().parent / "align_readme_table.py"


def load_aligner():
    if not ALIGNER.exists():
        raise SystemExit(f"[에러] 같은 폴더에서 {ALIGNER.name} 를 찾지 못했습니다.")
    spec = importlib.util.spec_from_file_location("align_readme_table", ALIGNER)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["align_readme_table"] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", required=True)
    ap.add_argument("--section", required=True, help="표 위 제목 텍스트")
    ap.add_argument("--amb", type=int, default=1, help="ambiguous 폭(기본 1)")
    args = ap.parse_args()

    a = load_aligner()

    lines = open(args.readme, encoding="utf-8").read().split("\n")
    h = a.find_heading(lines, args.section)
    header_idx, sep_idx, data_idx = a.find_table(lines, h)
    if not data_idx:
        raise SystemExit(f"[에러] '{args.section}' 표에 데이터 행이 없습니다.")

    header = a.split_cells(lines[header_idx])
    ncol = len(header)
    rows = [a.split_cells(lines[d]) for d in data_idx]

    colw = [
        max(a.width(header[c], args.amb), max(a.width(r[c], args.amb) for r in rows))
        for c in range(ncol)
    ]

    def emit(cells):
        return "| " + " | ".join(a.pad(cells[c], colw[c]) for c in range(ncol)) + " |"

    block = [emit(header), "| " + " | ".join("-" * colw[c] for c in range(ncol)) + " |"]
    block += [emit(r) for r in rows]

    wset = {a.width(b, args.amb) for b in block}
    if len(wset) != 1:
        raise SystemExit(f"[에러] 정렬 검증 실패: 줄 폭이 제각각 {sorted(wset)}")

    new_lines = lines[:header_idx] + block + lines[data_idx[-1] + 1:]
    open(args.readme, "w", encoding="utf-8").write("\n".join(new_lines))

    print(f"[OK] '{args.section}' 표 재정렬 완료 (열 폭 {colw}, 줄 폭 {wset.pop()})")


if __name__ == "__main__":
    main()
