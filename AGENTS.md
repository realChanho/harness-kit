# harness-kit

Codex 하네스 엔지니어링 자산(skills · agents · hooks · AGENTS.md 스니펫)을 모아 배포하는 레포. 빌드 산출물이 아니라 **자산 모음집**이다.

## 구조

- `.agents/skills/<name>/SKILL.md` — 재사용 skill (폴더 = skill 1개)
- `.agents/agents/<name>.md` — subagent 정의
- `.agents/hooks/<name>.*` — 훅 스크립트 (+ `.agents/settings.json` 등록)
- `agents-md/<name>.md` — AGENTS.md 붙여넣기 스니펫 (루트)
- `README.md` — "수록 자산" 표가 자산 카탈로그 겸 설치 안내

<!-- mirror:verbatim -->
- `.agents/`·`AGENTS.md` — 위 자산의 **Codex용 미러**. 정본은 `.claude/`·`CLAUDE.md`이고, 미러는 손으로 고치지 않는다. 정본을 고쳤으면 레포 루트에서 `python3 .claude/skills/add-harness-asset/scripts/sync_agents_mirror.py` 를 실행해 다시 만든다(`--check` 는 쓰지 않고 어긋난 파일만 보고). 미러는 경로(`.claude/`→`.agents/`, `claude-md/`→`agents-md/`)와 문서명(`CLAUDE.md`→`AGENTS.md`), 루트 문서의 에이전트 이름(`Claude Code`→`Codex`)만 치환한 것이다. 이 문단처럼 치환하면 안 되는 구간은 `mirror:verbatim` 주석으로 감싼다.
<!-- /mirror:verbatim -->

자산을 `.agents/` 아래 두는 이유: Codex가 이 경로에서 프로젝트 skill·agent·hook을 자동 로드하므로 **이 레포 자체에서 자산을 바로 켜고 테스트**할 수 있다. `agents-md/` 스니펫은 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둔다.

## 핵심 규칙

- 자산을 추가/변경하면 **README의 "수록 자산" 표를 반드시 같이 갱신**한다(이름·설명). 단계는 아래 [자산 추가 절차](#자산-추가-절차) 참고.
  - 예외: `.agents/skills/add-harness-asset/`는 이 절차 자체를 돕는 **레포 내부 도구 스킬**이다. 레포에 커밋해 공유하지만 배포용 자산이 아니므로 카탈로그(README 표)에는 등재하지 않는다.
- 이름은 **kebab-case**.
- skill의 `SKILL.md`에는 `name`·`description` frontmatter가 **필수**다. `skills` CLI가 이 둘로 자산을 인식한다.
- 레포의 자산 파일(`.agents/skills/`·`.agents/agents/`·`.agents/hooks/`, `agents-md/`)은 이 프로젝트에서 **로드·테스트하는 동시에 배포용 카탈로그**다. README 표는 **이름·설명 2열**이고 설치 명령 칸은 두지 않는다 — 설치는 필요할 때 각자 출처에서 찾는다. 대신 설명 끝에 **출처 링크**를 달아 어디서 온 자산인지 추적 가능하게 한다.

## 자산 추가 절차

1. **종류 확인 → 생성 위치 결정**

   | 종류             | 생성 위치                                                 | README 표                                       |
   | ---------------- | --------------------------------------------------------- | ----------------------------------------------- |
   | skill            | `.agents/skills/<name>/SKILL.md`                          | `### Skills · Commands` 아래 카테고리 `####` 표 |
   | agent            | `.agents/agents/<name>.md`                                | `### Agents`                                    |
   | hook             | `.agents/hooks/<name>.*` (+ `.agents/settings.json` 등록) | `### Hooks`                                     |
   | AGENTS.md 스니펫 | `agents-md/<name>.md` (루트)                              | `### AGENTS.md 스니펫`                          |

2. **파일 스캐폴딩** — 위 위치에 파일을 만든다. skill이면 `SKILL.md` frontmatter의 `name`(폴더명과 일치)·`description`이 필수. 필요 시 같은 폴더에 `scripts/`·`templates/`·`reference.md` 등 부속 파일을 둔다.

3. **README 표 갱신** — 해당 종류 표에서 `_(아직 없음)_` placeholder 행이 있으면 지우고 `이름 | 설명` 행을 추가한다. skill은 `### Skills · Commands` 아래 **카테고리별 `####` 소제목**(프론트엔드, 배포 · 인프라, 워크플로 · 방법론, 하네스 관리 · 유틸리티 등)마다 표가 따로 있으므로, 맞는 카테고리 표에 행을 추가하고 맞는 카테고리가 없으면 `####` 소제목과 표를 신설한다. 설명 끝에는 출처 링크(업스트림 레포·플러그인)를 단다.

4. **마무리** — 표 행과 실제 파일 위치가 일치하는지, skill이면 `name` frontmatter가 폴더명과 같은지 확인한다.

## 배포 / 설치 메커니즘

- skill은 [`skills` CLI](https://skills.sh)로 설치한다: `npx skills@latest add <your-id>/harness-kit[/<skill-name>]`.
- `skills` CLI는 **skill만** 설치한다. agent·hook·AGENTS.md 스니펫은 설명에 달린 출처 링크를 따라가 원본에서 받는다.
- 레포 자체를 플러그인화하지 않는다.

## 문서 언어

README·SKILL.md 등 레포 문서는 한국어로 작성한다.
