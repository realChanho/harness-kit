# harness-kit

자주 쓰는 **Claude Code 하네스 엔지니어링 자산**(skills · agents · hooks · CLAUDE.md 설정)과 **에이전트 페르소나 키트**를 한곳에 모아둔 개인 모음집입니다.
새 프로젝트를 시작할 때 필요한 자산만 골라 받아서 바로 쓰기 위한 저장소입니다.

## 구조

```
harness-kit/
├─ .claude/
│  ├─ skills/   # 재사용 skill (각 폴더 = 하나의 skill, SKILL.md 포함)
│  ├─ agents/   # subagent 정의 (*.md)
│  └─ hooks/    # 훅 스크립트 (+ .claude/settings.json 등록)
├─ claude-md/       # CLAUDE.md 붙여넣기 스니펫 (루트)
├─ hermes-persona/  # 개인 에이전트 페르소나 키트 (SOUL·AGENTS·USER)
└─ README.md
```

> 자산을 `.claude/` 아래 두어 **이 레포에서 바로 로드·테스트**할 수 있게 했습니다. `claude-md/` 스니펫은 자동 로드 대상이 아니라 붙여넣기/`@import`용이라 루트에 둡니다.

## 수록 자산

### Skills · Commands

#### 프론트엔드

| 이름                            | 설명                                                                                                                                                                                                                                                             | 다운로드                                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `vercel-react-best-practices`   | Vercel 공식 React/Next.js 베스트 프랙티스 skill. 8개 카테고리 70개 우선순위 규칙으로 useEffect 데이터 페칭·불필요한 useState·과도한 메모이제이션 같은 안티패턴을 차단([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))                   | `npx skills@latest add vercel-labs/agent-skills --skill vercel-react-best-practices`                                  |
| `next-best-practices`           | Next.js App Router 베스트 프랙티스 — 파일 컨벤션·RSC(서버/클라이언트) 경계·데이터 페칭 패턴·async API·메타데이터 규칙. 별도 skill에서 프레임워크 내장으로 이관되어 버전 불일치 없이 제공([vercel/next.js](https://github.com/vercel/next.js/tree/canary/skills)) | Next.js 16.3+ 내장 — `next dev`가 `AGENTS.md`/`CLAUDE.md` 자동 생성. 이전 버전은 `npx @next/codemod@canary agents-md` |
| `vercel-composition-patterns`   | 확장 가능한 React 컴포지션 패턴 가이드. boolean prop 증식 리팩토링, 컴파운드 컴포넌트·render props·Context 프로바이더 등 재사용 컴포넌트 API 설계에 사용하며 React 19 API 변경을 반영([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))   | `npx skills@latest add vercel-labs/agent-skills --skill vercel-composition-patterns`                                  |
| `vercel-react-view-transitions` | React View Transition API(`<ViewTransition>`·`addTransitionType`)로 서드파티 라이브러리 없이 페이지 전환·공유 요소·리스트 재정렬 애니메이션을 구현하는 가이드. Next.js 연동 포함([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))        | `npx skills@latest add vercel-labs/agent-skills --skill vercel-react-view-transitions`                                |
| `vercel-react-native-skills`    | React Native·Expo 베스트 프랙티스. 리스트 성능 최적화·애니메이션·네이티브 모듈 등 모바일 앱 성능 작업에 사용([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))                                                                            | `npx skills@latest add vercel-labs/agent-skills --skill vercel-react-native-skills`                                   |

#### 배포 · 인프라

| 이름                     | 설명                                                                                                                                                                                                                                             | 다운로드                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| `deploy-to-vercel`       | 앱·웹사이트를 Vercel에 배포. 기본은 프리뷰 배포이고 명시적으로 요청할 때만 프로덕션 배포([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))                                                                                | `npx skills@latest add vercel-labs/agent-skills --skill deploy-to-vercel`       |
| `vercel-cli-with-tokens` | 대화형 `vercel login` 없이 액세스 토큰 인증으로 Vercel CLI 배포·프로젝트 관리(환경 변수 설정 등) — CI·에이전트 환경에 적합([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills))                                              | `npx skills@latest add vercel-labs/agent-skills --skill vercel-cli-with-tokens` |
| `vercel-optimize`        | 배포된 프로젝트의 Vercel 비용·성능 최적화 감사. 메트릭·사용량·프로젝트 설정을 먼저 수집하고 근거 있는 후보만 조사해 순위화된 권고안을 생성(Next.js·SvelteKit·Nuxt 지원)([vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)) | `npx skills@latest add vercel-labs/agent-skills --skill vercel-optimize`        |

#### 워크플로 · 방법론

| 이름          | 설명                                                                                                                                                                                         | 다운로드                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `superpowers` | 제대로 작동하는 에이전트 스킬 프레임워크이자 소프트웨어 개발 방법론 — TDD·디버깅·협업 등 검증된 워크플로 라이브러리(Jesse Vincent / [obra/superpowers](https://github.com/obra/superpowers)) | `/plugin install superpowers@claude-plugins-official` |

#### 하네스 관리 · 유틸리티

| 이름                                        | 설명                                                                                                                                                                                                                                                                                                               | 다운로드                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `claude-md-improver`,<br>`revise-claude-md` | CLAUDE.md 관리 플러그인. `claude-md-improver`(skill)는 레포의 모든 CLAUDE.md를 스캔·품질 평가 후 승인받아 타깃 개선하고, `revise-claude-md`(command)는 이번 세션의 학습을 CLAUDE.md에 반영함([claude-md-management](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management)) | `/plugin install claude-md-management@claude-plugins-official`                              |
| `btw`                                       | 작업을 멈추지 않고 곁가지 질문을 던지는 Claude Code 내장 명령. 도구 없는 임시 오버레이 에이전트가 현재 대화 맥락만으로 한 번 답하고, 그 질의응답은 메인 히스토리에 남지 않아 토큰을 아낌                                                                                                                           | Claude Code 내장 — 설치 불필요. [커맨드 레퍼런스](https://code.claude.com/docs/en/commands) |

#### 보안 · 검증

| 이름           | 설명                                                                                                                                                                                                                                                                                                                                                                                                                            | 다운로드                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `skillspector` | skill·MCP 서버를 **설치 전에** 보안 스캔하는 NVIDIA 오픈소스 CLI. 정적 패턴 매칭 + 선택적 LLM 시맨틱 평가 2단계로 17개 카테고리 68개 취약 패턴(프롬프트 인젝션·데이터 유출·권한 상승·공급망·MCP 툴 포이즈닝 등)을 잡아 0~100 위험 점수와 터미널/JSON/Markdown/SARIF 리포트를 냄. Claude Code·Codex·Gemini CLI skill 대상, MCP 서버로 등록해 설치 게이트로도 사용([NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)) | `uv tool install git+https://github.com/NVIDIA/skillspector.git` 후 `skillspector scan ./my-skill/` |

### Agents

| 이름          | 설명 | 다운로드 |
| ------------- | ---- | -------- |
| _(아직 없음)_ |      |          |

### Hooks

| 이름          | 트리거 | 다운로드 |
| ------------- | ------ | -------- |
| _(아직 없음)_ |        |          |

### CLAUDE.md 스니펫

| 이름          | 용도 | 다운로드 |
| ------------- | ---- | -------- |
| _(아직 없음)_ |      |          |

### Agent Personas

| 이름             | 설명                                                                                                                                                                                                         | 다운로드                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| `hermes-persona` | AGENTS.md 기반 개인 에이전트 페르소나 키트. `SOUL.md`(정체성·성격·금지 특성)·`AGENTS.md`(운영 규칙·보고·멀티에이전트)·`USER.md`(사용자 프로필·목표·선호) 3개 파일로 에이전트의 정체성·행동·맥락을 부트스트랩 | `hermes-persona/` 폴더를 복사해 각 파일을 본인 값으로 교체 |
