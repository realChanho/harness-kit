# harness-kit

Claude Code 하네스 엔지니어링 자산(skills · agents · hooks · CLAUDE.md 스니펫)을 모아 배포하는 레포. 빌드 산출물이 아니라 **자산 모음집**이다.

## 구조

- `skills/<name>/SKILL.md` — 재사용 skill (폴더 = skill 1개)
- `agents/<name>.md` — subagent 정의
- `hooks/<name>.*` — 훅 스크립트 + 설정 스니펫
- `claude-md/<name>.md` — CLAUDE.md 붙여넣기 스니펫
- `README.md` — "수록 자산" 표가 자산 카탈로그 겸 설치 안내

## 핵심 규칙

- 새 자산을 추가할 때는 **`add-asset` 스킬**(`skills/add-asset/`)의 절차를 따른다. 파일 스캐폴딩 + README "수록 자산" 표 갱신을 한 번에 처리한다.
- 자산을 추가/변경하면 **README의 수록 자산 표를 반드시 같이 갱신**한다(이름·설명·위치·다운로드).
- 이름은 **kebab-case**.
- skill의 `SKILL.md`에는 `name`·`description` frontmatter가 **필수**다. `skills` CLI가 이 둘로 자산을 인식한다.

## 배포 / 설치 메커니즘

- skill은 [`skills` CLI](https://skills.sh)로 설치한다: `npx skills@latest add <your-id>/harness-kit[/<skill-name>]`.
- `skills` CLI는 **skill만** 설치한다. agent·hook·CLAUDE.md 스니펫은 수동 복사/붙여넣기 대상이다.
- 레포 자체를 플러그인화하지 않는다.

## 문서 언어

README·SKILL.md 등 레포 문서는 한국어로 작성한다.
