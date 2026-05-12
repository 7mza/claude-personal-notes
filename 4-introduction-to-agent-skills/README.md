# [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)

[agentskills.io](https://agentskills.io/home)

skill = add specific knowledge to current context

repeating an explanation to model = skill

skill structure :

```
skill-name/
    |_SKILL.md # max 500 lines
    |_references/ # additional doc
    |_scripts/ # executable code
    |_assets/ # image, data, ...
```

format:

```md
# title

---

name(req): skill-name
description(req): summary of what skill do and when to use it
allowed-tools: Read, Grep, Glob, Bash (REMEMBER LLMs are not deterministic, HOOKS when danger)
model: sonnet

---

detailed system prompt

progressive disclosure: **only load when user request about toto**[toto](./references/TOTO.md)
```

skills name/desc are loaded auto on session start from (highest precedence wins when conflict)

- `managed-settings.json` (entreprise settings ?)
- `~/.claude/skills` (personal)
- `project/.claude/skills` (project)
- `project/.claude-plugin/plugin.json` (plugins)

sys prompt is picked by model on demand (from context) based on name/desc (semantic matching)

use specific name/desc to avoid conflicts

only scripts output should consume tokens (because model need to read it), **tell models to execute a script not read it**

**[subagents](../5-introduction-to-subagents/README.md) can't access skills unless specified in AGENT.md**

troubleshooting :

- [skills verifier](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- on new session ask claude what skills are loaded
- `claude --debug` to see errors
- `rm -rf ~/.claude/plugins/cache/`
- if skill uses external packaged that need install, explain it in SKILL.md
