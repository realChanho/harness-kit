---
name: add-asset
description: harness-kit 레포에 새 자산(skill·agent·hook·CLAUDE.md 스니펫)을 추가할 때 사용. 자산 파일을 알맞은 위치에 스캐폴딩하고 README의 "수록 자산" 표에 행을 추가/갱신한다.
---

# add-asset

harness-kit에 새 자산을 추가하는 작업을 표준화한다. 자산을 만들면 **반드시 README의 수록 자산 표도 같이 갱신**해 "무엇이 있고 어떻게 받는지"를 최신으로 유지한다.

## 1. 자산 종류 확인

사용자에게(또는 맥락에서) 무엇을 추가하는지 파악한다.

| 종류        | 생성 위치                       | README 표           |
| ----------- | ------------------------------- | ------------------- |
| skill       | `skills/<kebab-name>/SKILL.md`  | `### Skills`        |
| agent       | `agents/<name>.md`              | `### Agents`        |
| hook        | `hooks/<name>.*` (+ 설정 스니펫) | `### Hooks`         |
| CLAUDE.md 스니펫 | `claude-md/<name>.md`       | `### CLAUDE.md 스니펫` |

이름은 **kebab-case**로 통일한다.

## 2. 자산 파일 스캐폴딩

### skill

- `skills/<name>/SKILL.md` 생성. frontmatter에 `name`·`description` **필수** (`skills` CLI가 이 둘로 자산을 인식한다).
- 카탈로그로 묶고 싶으면 `skills/<category>/<name>/SKILL.md`도 허용된다(둘 다 CLI가 인식).
- 필요 시 같은 폴더에 `scripts/`, `templates/`, `reference.md` 등 부속 파일을 둔다.

```markdown
---
name: <name>
description: 이 skill이 무엇이며 언제 자동으로 트리거되어야 하는지 한 줄 설명
---

# <name>

(실제 동작 지침)
```

### agent

- `agents/<name>.md` 생성. subagent 정의 형식(frontmatter + 시스템 프롬프트)을 따른다.

### hook

- `hooks/<name>.*` (스크립트) 생성 + 등록용 `settings.json` 스니펫을 같이 둔다.

### CLAUDE.md 스니펫

- `claude-md/<name>.md`에 붙여넣기용 스니펫을 둔다.

## 3. README 수록 자산 표 갱신

해당 종류의 표에서 `_(아직 없음)_` placeholder 행이 있으면 지우고, 새 행을 추가한다.
컬럼은 `이름 | 설명(또는 용도/트리거) | 위치 | 다운로드`.

**다운로드 컬럼** 값:

| 종류        | 다운로드 값                                              |
| ----------- | -------------------------------------------------------- |
| skill       | `npx skills@latest add <your-id>/harness-kit/<name>`     |
| agent       | `cp agents/<name>.md ~/.claude/agents/`                  |
| hook        | `cp hooks/<name>.* ~/.claude/hooks/` (+ settings.json 등록) |
| CLAUDE.md 스니펫 | `claude-md/<name>.md` 내용을 CLAUDE.md에 붙여넣기      |

`<your-id>`는 실제 GitHub 사용자명/조직명으로 둔다(레포에서 placeholder를 쓰고 있으면 그대로 둔다).

## 4. 마무리

- 표 행과 실제 파일 위치가 일치하는지 확인한다.
- skill을 추가했으면 `SKILL.md` frontmatter의 `name`이 폴더명과 일치하는지 확인한다.
