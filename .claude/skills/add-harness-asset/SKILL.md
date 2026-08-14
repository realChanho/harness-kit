---
name: add-harness-asset
description: harness-kit 레포에 새 자산(skill·agent·hook·CLAUDE.md 스니펫)을 추가하거나 기존 자산을 변경할 때 쓴다. 자산 종류를 판별해 올바른 위치에 파일을 만들고, README "수록 자산" 표에 이름·설명 행을 추가하며, 표의 CJK(한글 전각) 폭 정렬까지 맞춘다. harness-kit에서 "자산/스킬/에이전트/훅/스니펫 추가", "카탈로그에 등록", "수록 자산 표 갱신" 같은 요청이 나오면 명시적으로 이 스킬을 부르지 않아도 반드시 사용한다.
---

# add-harness-asset

harness-kit에 자산을 추가/변경하는 절차를 한 번에 끝내기 위한 스킬이다. 정본 규칙은
이 레포의 `CLAUDE.md`("자산 추가 절차")에 있고, 이 스킬은 그 절차를 실행 가능한 형태로
풀어 놓은 것이다. 규칙이 바뀌면 `CLAUDE.md`가 우선이다 — 충돌하면 `CLAUDE.md`를 따른다.

핵심은 두 가지다. ① 자산을 **올바른 위치**에 두는 것(그래야 이 레포에서 자동 로드·테스트된다),
② README "수록 자산" 표를 **정렬을 깨지 않고** 갱신하는 것. 표는 한글이 섞여 단순 글자 수로는
정렬되지 않으므로 번들 스크립트로 처리한다.

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
맞는 게 없으면 `####` 소제목과 2열 표(`이름 | 설명`)를 신설한다.

표에 설치 명령 칸은 두지 않는다. 설치는 필요할 때 각자 출처에서 찾는다 — 대신 설명 끝에
출처 링크(예: `([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))`)를
넣어 어디서 온 자산인지 추적 가능하게 한다.

### 2. 파일 스캐폴딩

위 표의 위치에 파일을 만든다.
- **skill**: `SKILL.md`에 `name`(폴더명과 일치)·`description` frontmatter 필수. 부속 파일이
  필요하면 같은 폴더에 `scripts/`·`references/`·`assets/`를 둔다.
- **agent**: `.claude/agents/<name>.md`에 subagent 정의.
- **hook**: `.claude/hooks/<name>.*` 스크립트를 만들고 `.claude/settings.json`의 hooks에 등록한다.
- **스니펫**: `claude-md/<name>.md`. 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둔다.

외부 플러그인·빌트인을 **참조만** 하는 경우(예: `superpowers`, `btw`)는 이 레포에 파일을
만들지 않는다 — README 표에 카탈로그 행만 추가한다.

### 3. README 표 갱신 (정렬 스크립트 사용)

번들 스크립트로 행을 추가하면 placeholder 제거·CJK 폭 재정렬·중복 검사가 한 번에 된다.
레포 루트에서 실행한다:

```bash
python3 .claude/skills/add-harness-asset/scripts/align_readme_table.py \
  --readme README.md --section "프론트엔드" \
  --cells '`<name>`' '<설명/트리거/용도 한 줄 + 출처 링크>'
```

- `--section`: 표 바로 위 제목 텍스트(레벨 무관). skill은 카테고리 소제목(`프론트엔드` /
  `배포 · 인프라` / `워크플로 · 방법론` / `하네스 관리 · 유틸리티` 등), 그 외 종류는
  `Agents` / `Hooks` / `CLAUDE.md 스니펫`.
- `--cells`: 표 컬럼 순서대로 2개(개수가 헤더 열 수와 다르면 에러). 둘째 칸 헤더는 표마다
  다르다(Skills·Agents=설명, Hooks=트리거, 스니펫=용도) — 의미만 맞춰 넣는다.
- 셀 안에 백틱·`<br>`·마크다운 링크를 그대로 써도 된다. 셸 인용 때문에 작은따옴표로 감싸고,
  값에 작은따옴표가 있으면 적절히 이스케이프한다.
- `_(아직 없음)_` placeholder 행은 자동 삭제된다. 같은 이름 행이 이미 있으면 에러로 멈추니,
  수정은 README에서 직접 한다.

스크립트가 표를 통째로 다시 정렬하므로, 새 행이 기존보다 길면 열을 넓혀 모든 행을 다시 패딩한다.
즉 기존 행이 충분히 짧으면(열 폭 안에 들어오면) diff는 새 행 한 줄만 깔끔하게 추가된다.

#### 이름이 길어 렌더링에서 쪼개질 때

Markdown 표에는 열 너비 문법이 없다. 소스의 패딩은 파일을 읽을 때만 의미가 있고, 렌더링된
열 너비는 브라우저·프리뷰가 내용 길이를 보고 정한다. 그래서 이름이 길면(대략 25자 이상)
설명 칸에 밀려 하이픈마다 줄이 잘린다. 이럴 때는 이름 칸을 백틱 대신 `<code>` 태그로 쓰고
하이픈을 `&#8209;`(non-breaking hyphen, U+2011)로 바꿔 줄바꿈을 막는다. 백틱 안에서는 HTML
엔티티가 해석되지 않아 `&#8209;` 가 글자 그대로 보이므로 `<code>` 태그가 필요하다.

```
<code>supabase&#8209;postgres&#8209;best&#8209;practices</code>
```

대가가 하나 있다 — 표에서 이름을 복사하면 하이픈이 ASCII `-` 가 아니라 U+2011로 딸려온다.
이름이 짧아 문제가 없으면 그냥 백틱을 쓴다.

#### 이미 있는 행을 고친 뒤 폭만 다시 맞출 때

`align_readme_table.py` 는 행 추가 전용이고, 같은 이름 행이 있으면 에러로 멈춘다. 기존 셀을
직접 고쳤다면 같은 폴더의 `realign_readme_table.py` 로 폭만 다시 맞춘다. 폭 계산 함수를
`align_readme_table.py` 에서 그대로 가져오므로 두 스크립트의 정렬 결과가 어긋나지 않는다.

```bash
python3 .claude/skills/add-harness-asset/scripts/realign_readme_table.py \
  --readme README.md --section "하네스 관리 · 유틸리티"
```

### 4. 마무리 점검

- 표 행과 실제 파일 위치가 일치하는가. 참조 전용 자산이면 파일이 없는 게 의도된 상태인가.
- skill이면 `name` frontmatter가 폴더명과 같은가.
- 표의 모든 줄 시각 폭이 같은가(스크립트가 `[OK] … 줄 폭 N`으로 출력해 준다).
- hook이면 `.claude/settings.json` 등록까지 됐는가.
- 문서 언어는 한국어인가(README·SKILL.md 등 레포 문서 규칙).
<!-- mirror:verbatim -->
- 이 스킬 자체나 `CLAUDE.md` 를 고쳤다면 `python3 .claude/skills/add-harness-asset/scripts/sync_agents_mirror.py` 로 Codex용 `.agents/` 미러를 다시 만들었는가(`--check` 로 확인만 할 수도 있다).
<!-- /mirror:verbatim -->

## 정렬은 왜 스크립트로 하나

README 표는 한글(전각 2칸)과 영문(1칸)이 섞여 있어 글자 수로 칸을 맞추면 에디터에서 어긋난다.
정렬 기준은 East Asian Width(전각 W/F=2, 그 외 1)이고, ambiguous 문자(`—`, `·` 등)는 이 레포
기존 정렬과 동일하게 **1칸**으로 센다(역검증으로 확인된 값, 스크립트 기본값 `--amb 1`).
손으로 맞추면 거의 틀리므로 스크립트를 쓴다.
