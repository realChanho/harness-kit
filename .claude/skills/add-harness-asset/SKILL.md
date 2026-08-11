---
name: add-harness-asset
description: harness-kit 레포에 새 자산(skill·agent·hook·CLAUDE.md 스니펫)을 추가하거나 기존 자산을 변경할 때 쓴다. 자산 종류를 판별해 올바른 위치에 파일을 만들고, 출처 유형에 맞는 정식 설치 경로로 README "수록 자산" 표에 행을 추가하며, 표의 CJK(한글 전각) 폭 정렬까지 맞춘다. harness-kit에서 "자산/스킬/에이전트/훅/스니펫 추가", "카탈로그에 등록", "수록 자산 표 갱신" 같은 요청이 나오면 명시적으로 이 스킬을 부르지 않아도 반드시 사용한다.
---

# add-harness-asset

harness-kit에 자산을 추가/변경하는 절차를 한 번에 끝내기 위한 스킬이다. 정본 규칙은
이 레포의 `CLAUDE.md`("자산 추가 절차")에 있고, 이 스킬은 그 절차를 실행 가능한 형태로
풀어 놓은 것이다. 규칙이 바뀌면 `CLAUDE.md`가 우선이다 — 충돌하면 `CLAUDE.md`를 따른다.

핵심은 두 가지다. ① 자산을 **올바른 위치**에 두는 것(그래야 이 레포에서 자동 로드·테스트된다),
② README "수록 자산" 표를 **정식 설치 경로**로, **정렬을 깨지 않고** 갱신하는 것. 표는 한글이
섞여 단순 글자 수로는 정렬되지 않으므로 번들 스크립트로 처리한다.

## 절차

### 1. 자산 종류 판별 → 위치·README 표

| 종류             | 생성 위치                                                 | README 표                                       |
| ---------------- | --------------------------------------------------------- | ----------------------------------------------- |
| skill            | `.claude/skills/<name>/SKILL.md`                          | `### Skills · Commands` 아래 카테고리 `####` 표 |
| agent            | `.claude/agents/<name>.md`                                | `### Agents`                                    |
| hook             | `.claude/hooks/<name>.*` (+ `.claude/settings.json` 등록) | `### Hooks`                                     |
| CLAUDE.md 스니펫 | `claude-md/<name>.md` (루트)                              | `### CLAUDE.md 스니펫`                          |

이름은 **kebab-case**. skill이면 폴더명 = `SKILL.md`의 `name` frontmatter여야 한다(`skills`
CLI가 이걸로 자산을 인식한다).

skill 표는 `### Skills · Commands` 아래 **카테고리별 `####` 소제목**(프론트엔드, 배포 · 인프라,
워크플로 · 방법론, 하네스 관리 · 유틸리티 등)으로 나뉘어 있다. 자산 성격에 맞는 카테고리 표를 고르고,
맞는 게 없으면 `####` 소제목과 3열 표(`이름 | 설명 | 다운로드`)를 신설한다.

### 2. 출처 유형 판별 → "다운로드" 칸

표의 "다운로드" 칸은 "로컬 파일을 붙여넣어라"가 아니라 **정식 설치 경로**를 가리킨다.
출처에 따라 셋 중 하나다. "동기화가 안 된다"는 식의 부연은 README에 넣지 않는다.

| 출처 유형                          | 다운로드 칸 예시                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------- |
| 이 레포에서 작성한 skill           | `npx skills@latest add <your-id>/harness-kit/<name>`                              |
| 외부 플러그인(마켓플레이스)        | `/plugin install <plugin>@<marketplace>` (필요시 `/plugin marketplace add …` 먼저) |
| Claude Code 빌트인(번들 skill 등)  | `Claude Code 내장 — 설치 불필요.` + 공식 docs 링크                                |

판단이 안 서면 출처를 먼저 확인한다: 플러그인 마켓플레이스 캐시
(`~/.claude/plugins/marketplaces/`)에 있으면 외부 플러그인, 없고 본체에 내장이면 빌트인,
이 레포가 직접 작성하는 것이면 첫 번째다.

### 3. 파일 스캐폴딩

위 표의 위치에 파일을 만든다.
- **skill**: `SKILL.md`에 `name`(폴더명과 일치)·`description` frontmatter 필수. 부속 파일이
  필요하면 같은 폴더에 `scripts/`·`references/`·`assets/`를 둔다.
- **agent**: `.claude/agents/<name>.md`에 subagent 정의.
- **hook**: `.claude/hooks/<name>.*` 스크립트를 만들고 `.claude/settings.json`의 hooks에 등록한다.
- **스니펫**: `claude-md/<name>.md`. 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둔다.

외부 플러그인·빌트인을 **참조만** 하는 경우(예: `superpowers`, `btw`)는 이 레포에 파일을
만들지 않는다 — README 표에 카탈로그 행만 추가한다.

### 4. README 표 갱신 (정렬 스크립트 사용)

번들 스크립트로 행을 추가하면 placeholder 제거·CJK 폭 재정렬·중복 검사가 한 번에 된다.
레포 루트에서 실행한다:

```bash
python3 .claude/skills/add-harness-asset/scripts/align_readme_table.py \
  --readme README.md --section "프론트엔드" \
  --cells '`<name>`' '<설명/트리거/용도 한 줄>' '<다운로드 — 정식 설치 경로>'
```

- `--section`: 표 바로 위 제목 텍스트(레벨 무관). skill은 카테고리 소제목(`프론트엔드` /
  `배포 · 인프라` / `워크플로 · 방법론` / `하네스 관리 · 유틸리티` 등), 그 외 종류는
  `Agents` / `Hooks` / `CLAUDE.md 스니펫`.
- `--cells`: 표 컬럼 순서대로 3개. 중간 칸 헤더는 표마다 다르다(Skills·Agents=설명, Hooks=트리거,
  스니펫=용도) — 의미만 맞춰 넣는다.
- 셀 안에 백틱·`<br>`·마크다운 링크를 그대로 써도 된다. 셸 인용 때문에 작은따옴표로 감싸고,
  값에 작은따옴표가 있으면 적절히 이스케이프한다.
- `_(아직 없음)_` placeholder 행은 자동 삭제된다. 같은 이름 행이 이미 있으면 에러로 멈추니,
  수정은 README에서 직접 한다.

스크립트가 표를 통째로 다시 정렬하므로, 새 행이 기존보다 길면 열을 넓혀 모든 행을 다시 패딩한다.
즉 기존 행이 충분히 짧으면(열 폭 안에 들어오면) diff는 새 행 한 줄만 깔끔하게 추가된다.

### 5. 마무리 점검

- 표 행과 실제 파일 위치가 일치하는가. 참조 전용 자산이면 파일이 없는 게 의도된 상태인가.
- skill이면 `name` frontmatter가 폴더명과 같은가.
- 표의 모든 줄 시각 폭이 같은가(스크립트가 `[OK] … 줄 폭 N`으로 출력해 준다).
- hook이면 `.claude/settings.json` 등록까지 됐는가.
- 문서 언어는 한국어인가(README·SKILL.md 등 레포 문서 규칙).

## 정렬은 왜 스크립트로 하나

README 표는 한글(전각 2칸)과 영문(1칸)이 섞여 있어 글자 수로 칸을 맞추면 에디터에서 어긋난다.
정렬 기준은 East Asian Width(전각 W/F=2, 그 외 1)이고, ambiguous 문자(`—`, `·` 등)는 이 레포
기존 정렬과 동일하게 **1칸**으로 센다(역검증으로 확인된 값, 스크립트 기본값 `--amb 1`).
손으로 맞추면 거의 틀리므로 스크립트를 쓴다.
