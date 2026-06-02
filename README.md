# harness-kit

자주 쓰는 **Claude Code 하네스 엔지니어링 자산**(skills · agents · hooks · CLAUDE.md 설정)을 한곳에 모아둔 개인 모음집입니다.
새 프로젝트를 시작할 때 필요한 자산만 골라 받아서 바로 쓰기 위한 저장소입니다.

## 구조

```
harness-kit/
├─ .claude/
│  ├─ skills/   # 재사용 skill (각 폴더 = 하나의 skill, SKILL.md 포함)
│  ├─ agents/   # subagent 정의 (*.md)
│  └─ hooks/    # 훅 스크립트 (+ .claude/settings.json 등록)
├─ claude-md/   # CLAUDE.md 붙여넣기 스니펫 (루트)
└─ README.md
```

> 자산을 `.claude/` 아래 두어 **이 레포에서 바로 로드·테스트**할 수 있게 했습니다. `claude-md/` 스니펫은 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둡니다.

## 수록 자산

### Skills

| 이름                  | 설명                                                                                                                                                                                         | 다운로드                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `superpowers`         | 제대로 작동하는 에이전트 스킬 프레임워크이자 소프트웨어 개발 방법론 — TDD·디버깅·협업 등 검증된 워크플로 라이브러리(Jesse Vincent / [obra/superpowers](https://github.com/obra/superpowers)) | `/plugin install superpowers@claude-plugins-official`                                                |
| `understand-anything` | 코드를 처음 볼 때의 막막함 해결 — 코드베이스·지식베이스·문서를 대화형 지식 그래프로 변환해 탐색·검색·질문([Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything))     | 1. `/plugin marketplace add Lum1104/Understand-Anything`<br>2. `/plugin install understand-anything` |
| `code-review`         | 현재 diff를 리뷰해 **정확성 버그 + 재사용·단순화·효율 정리거리**를 찾는 Claude Code 번들 skill. effort `low`~`max`, `ultra`(클라우드 멀티에이전트 심층 리뷰), `--comment`/`--fix` 지원       | Claude Code 내장 — 설치 불필요. [커맨드 레퍼런스](https://code.claude.com/docs/en/commands)          |

### Agents

| 이름          | 설명 | 다운로드 |
| ------------- | ---- | -------- |
| _(아직 없음)_ |      |          |

### Hooks

| 이름          | 트리거 | 다운로드 |
| ------------- | ------ | -------- |
| _(아직 없음)_ |        |          |

### CLAUDE.md 스니펫

| 이름                  | 용도                                                                                                                                                                              | 다운로드                                                                                                                        |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `karpathy-guidelines` | LLM 코딩 실수를 줄이는 행동 가이드라인(Andrej Karpathy 기반). [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) 플러그인이 추가하는 CLAUDE.md 원문 | 1. `/plugin marketplace add forrestchang/andrej-karpathy-skills`<br>2. `/plugin install andrej-karpathy-skills@karpathy-skills` |
