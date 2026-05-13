# [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

without coding assistant

```
user                                                  LLM
  |                                                    |
  |-------------- whats in file x ? ------------------>|
  |                          |                         |
  |<------ i don't have ability to read file ----------|
  |                                                    |
  |--------- whats in file x + content of file x ----->|
  |                          |                         |
  |<-------- here's resume of file --------------------|
  |                          |                         |

```

with coding assistant

```
user                       CA                                LLM
|                          |                                  |
|------------------- whats in file x ? ---------------------->|
|                          |                                  |
|                          |<-------- `readFile: X`-----------|
|                          |                                  |
|                          |---                               |
|                          |  | execute (tool use)            |
|                          |<--                               |
|                          |                                  |
|                          |------------ content  ----------->|
|                          |                                  |
|<-------------------- LLM response --------------------------|
|                          |                                  |
```

claude code built-in tools:

| name         | purpose                 |
| ------------ | ----------------------- |
| Agent        | launch subagent         |
| Bash         | `sh command`            |
| Edit         | mod file                |
| Glob         | find files by pattern   |
| Grep         | search in files         |
| LS           | list files and dirs     |
| MultiEdit    | multi edit at same time |
| NotebookEdit | edit cell in jupyter nb |
| NotebookRead | read cell               |
| Read         | read file               |
| TodoRead     | read from todo list     |
| TodoWrite    | update todo             |
| WebFetch     | fetch from url          |
| WebSearch    | search web              |
| Write        | write to a file         |

memory mode:

- `/memory`
- use `# prompt` to tell model to memorize something (in CLAUDE.md)

can copy screenshot to prompt to help model, or use browser integration

Ctrl+O to expand reasoning steps

`/effort` to adjust how model reasons through a problem

- plan mode = width, broad understanding, multi step implementation, multi input
- effort / extended thinking = depth, complexe single problem
- both consume more usage

to clean context polution: `esc esc` to enter rewind mode, go back in conv (remove/summarize at point)

custom commands:

- for simple cmds you can use [md file](../.claude/toto.md) to desc a command, use `$ARGUMENTS` placeholder to pass args

browser automation mcp:

- `claude mcp add playwright npx @playwright/mcp@latest` outside claude
- [give it perm](../.claude/settings.json)
- prompt `open browser at google.fr` or `open librewolf at` (if default chrome not found)

[github integration](https://anthropic.skilljar.com/claude-code-in-action/303240)

`// FIXME : do a simple gh issue/mention/ playwritght example`
