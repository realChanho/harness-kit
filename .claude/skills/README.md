# skills

각 skill은 **폴더 하나**로 구성됩니다. 폴더 안에는 최소한 `SKILL.md`(YAML frontmatter + 본문)가 있어야 하며, 필요 시 스크립트·템플릿·참고 파일을 같이 둘 수 있습니다.

```
.claude/skills/
└─ <skill-name>/
   ├─ SKILL.md          # 필수: name, description frontmatter + 사용 지침
   └─ (선택) scripts/, templates/, reference.md ...
```

`SKILL.md` frontmatter 예시:

```markdown
---
name: my-skill
description: 이 skill이 무엇이며 언제 자동으로 트리거되어야 하는지 한 줄 설명
---

# my-skill

(여기에 실제 동작 지침을 작성)
```

설치 방법은 루트 [README](../../README.md) 참고.
