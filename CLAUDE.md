# harness-kit

Claude Code 하네스 엔지니어링 자산(skills · agents · hooks · CLAUDE.md 스니펫)을 모아 배포하는 레포. 빌드 산출물이 아니라 **자산 모음집**이다.

## 구조

- `.claude/skills/<name>/SKILL.md` — 재사용 skill (폴더 = skill 1개)
- `.claude/agents/<name>.md` — subagent 정의
- `.claude/hooks/<name>.*` — 훅 스크립트 (+ `.claude/settings.json` 등록)
- `claude-md/<name>.md` — CLAUDE.md 붙여넣기 스니펫 (루트)
- `README.md` — "수록 자산" 표가 자산 카탈로그 겸 설치 안내

자산을 `.claude/` 아래 두는 이유: Claude Code가 이 경로에서 프로젝트 skill·agent·hook을 자동 로드하므로 **이 레포 자체에서 자산을 바로 켜고 테스트**할 수 있다. `claude-md/` 스니펫은 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둔다.

## 핵심 규칙

- 자산을 추가/변경하면 **README의 "수록 자산" 표를 반드시 같이 갱신**한다(이름·설명·다운로드). 단계는 아래 [자산 추가 절차](#자산-추가-절차) 참고.
  - 예외: `.claude/skills/add-harness-asset/`는 이 절차 자체를 돕는 **레포 내부 도구 스킬**이다. 레포에 커밋해 공유하지만 배포용 자산이 아니므로 카탈로그(README 표)에는 등재하지 않는다.
- 이름은 **kebab-case**.
- skill의 `SKILL.md`에는 `name`·`description` frontmatter가 **필수**다. `skills` CLI가 이 둘로 자산을 인식한다.
- 레포의 자산 파일(`.claude/skills/`·`.claude/agents/`·`.claude/hooks/`, `claude-md/`)은 이 프로젝트에서 **로드·테스트하는 동시에 배포용 카탈로그**다. README 다운로드 칸은 "로컬 파일 붙여넣기"가 아니라 **정식 설치 경로**(`skills` CLI `npx skills@latest add …`, 외부 출처는 원본 플러그인 `/plugin install …`)를 가리킨다. "동기화 안 된다"는 식의 부연 설명은 README에 넣지 않는다.

## 자산 추가 절차

1. **종류 확인 → 생성 위치 결정**

   | 종류             | 생성 위치                                                 | README 표               |
   | ---------------- | --------------------------------------------------------- | ----------------------- |
   | skill            | `.claude/skills/<name>/SKILL.md`                          | `### Skills · Commands` |
   | agent            | `.claude/agents/<name>.md`                                | `### Agents`            |
   | hook             | `.claude/hooks/<name>.*` (+ `.claude/settings.json` 등록) | `### Hooks`             |
   | CLAUDE.md 스니펫 | `claude-md/<name>.md` (루트)                              | `### CLAUDE.md 스니펫`  |

2. **파일 스캐폴딩** — 위 위치에 파일을 만든다. skill이면 `SKILL.md` frontmatter의 `name`(폴더명과 일치)·`description`이 필수. 필요 시 같은 폴더에 `scripts/`·`templates/`·`reference.md` 등 부속 파일을 둔다.

3. **README 표 갱신** — 해당 종류 표에서 `_(아직 없음)_` placeholder 행이 있으면 지우고 `이름 | 설명 | 다운로드` 행을 추가한다. 다운로드 칸은 정식 설치 경로로 채운다:
   - skill → `npx skills@latest add <your-id>/harness-kit/<name>` (`skills` CLI가 이 레포에서 설치)
   - 그 외 → 원본(업스트림)의 정식 설치 명령(예: 플러그인 `/plugin install …`). 로컬 파일을 그대로 붙여넣으라는 안내로 쓰지 않는다.

4. **마무리** — 표 행과 실제 파일 위치가 일치하는지, skill이면 `name` frontmatter가 폴더명과 같은지 확인한다.

## 배포 / 설치 메커니즘

- skill은 [`skills` CLI](https://skills.sh)로 설치한다: `npx skills@latest add <your-id>/harness-kit[/<skill-name>]`.
- `skills` CLI는 **skill만** 설치한다. agent·hook·CLAUDE.md 스니펫은 README 다운로드 칸의 정식 설치 경로(원본 플러그인 등)로 받는다.
- 레포 자체를 플러그인화하지 않는다.

## 문서 언어

README·SKILL.md 등 레포 문서는 한국어로 작성한다.
