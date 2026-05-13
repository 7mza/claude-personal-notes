# [Claude Code 101](https://anthropic.skilljar.com/claude-code-101)

```
prompt --> gather context --> take action --> verify result --> output
                 ^                                   |
                 |_____________ agentic loop ________|
                                   ^
                                   |
                        iterrupt, steer, add context
```

`shift tab` to toggle between permission modes

`plan mode` readonly, research, thinking return detailed plan of actions to tackle a task

```
explore : explore subagent, plan mode, interviews, spec drilling, ...
    |
    v
plan : plan mode, course correction, ...
    |
    v
code : test suits, hooks (format, lint, ...), tools (browser automation, ...)
    |
    v
commit : code review subagent, security audit, commiter subagent, ...
```

## context

`/context`

`/compact`

`/clear`

efficient context = be specific / limit searching

## CLAUDE.md

`CLAUDE.md` = persistant memory (onboarding script for model), read auto at session start, can ref other docs using `@docs/example.md`, start with short desc, stacks, prefs, commands, then build on (but keep it concise)

scopes:

- `project/.CLAUDE.md` = project only
- `~/.CLAUDE.md` = picked for all projects, personal prefs

## agents

agent = software, backed by an LLM, that can interract with its env through tools and perform actions to complete a goal

[subagent](../5-introduction-to-subagents/README.md) = delegate a task to specialized system prompt + new context + tools, return summary/output to calling context

built-in `/agents`

```
claude · inherit
claude-code-guide · haiku
Explore · haiku
general-purpose · inherit
Plan · inherit
statusline-setup · sonnet
```

## [skills](../4-introduction-to-agent-skills/README.md)

skill = teach model how to do something once, picked up automatically by agents based on context and skill name/desc

scopes:

- `project/.claude/skills` = project only, team standards
- `~/.claude/skills` = picked for all projects, personal prefs

## MCP

Model Context Protocol = standard protocol to make models discover and understand an external service capabilites + to bring external knwoledge to current context (standard wrapper that exposes your existing logic)

types:

- http (network)
- stdio (local)

scopes:

- local: installed by you in current project, no conf files, not checkout in repo
- user: `~/.claude.json`, available every session
- project: `project/.mcp.json`, project only, checked in repo

**mcp servers pollute context (load eveything), cli > mcp, teach model a CLI through skill**

[useful mcp](https://github.com/upstash/context7)

## hooks

hooks = deterministic based on condition (event/matcher), LLMs are not, if you need something to happen 100% (format, block dangerous op, ...etc) use a hook

scopes:

- `project/.claude/settings.json`

event that trigger a hook:

- UserPromptSubmit
- PreToolUse (hard rules, block here)
- PostToolUse
- Notification
- Stop

matcher = tool (available to claude, Edit|SearchWeb, ...etc)

use `$CLAUDE_PROJECT_DIR` envar + scripts checked in repo, when designing hook commands

## misc

`/commit-push-pr` skill handles commit push and PR creation in 1 step

when Claude creates a PR through `gh pr create`, session gets linked to PR automatically, to come back to it later (address review comments, fix a failing build, ...) : `claude --from-pr <PR_NUMBER>`
