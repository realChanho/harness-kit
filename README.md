# harness-kit

자주 쓰는 **Claude Code 하네스 엔지니어링 자산**(skills · agents · hooks · CLAUDE.md 설정)을 한곳에 모아둔 개인 모음집입니다.
새 프로젝트를 시작할 때 필요한 자산만 골라 받아서 바로 쓰기 위한 저장소입니다.

## 📦 구조

```
harness-kit/
├─ skills/      # 재사용 skill (각 폴더 = 하나의 skill, SKILL.md 포함)
├─ agents/      # subagent 정의 (*.md)
├─ hooks/       # 훅 스크립트 + 설정 스니펫
├─ claude-md/   # CLAUDE.md 템플릿 / 스니펫 모음
└─ README.md
```

## 🧩 수록 자산

### Skills

| 이름          | 설명 | 다운로드 |
| ------------- | ---- | -------- |
| _(아직 없음)_ |      |          |

> skill 다운로드 명령: `npx skills@latest add <your-id>/harness-kit/<skill-name>`

### Agents

| 이름          | 설명 | 다운로드 |
| ------------- | ---- | -------- |
| _(아직 없음)_ |      |          |

### Hooks

| 이름          | 트리거 | 다운로드 |
| ------------- | ------ | -------- |
| _(아직 없음)_ |        |          |

### CLAUDE.md 스니펫

| 이름                  | 용도                                                                              | 다운로드                                                  |
| --------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `karpathy-guidelines` | LLM 코딩 실수를 줄이는 행동 가이드라인(Andrej Karpathy 기반). [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) 플러그인이 추가하는 CLAUDE.md 원문 | 1. `/plugin marketplace add forrestchang/andrej-karpathy-skills`<br>2. `/plugin install andrej-karpathy-skills@karpathy-skills` |

