# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Claude personal notes

these are my personal notes from the different courses provided by anthropic skilljar plateform

## structure

each numbered folder corresponds to one skilljar course, with notes in its `README.md`:

- `./1-claude-101/` — Claude 101
- `./2-ai-fluency/` — AI Fluency Framework
- `./3-claude-code-101/` — Claude Code 101
- `./4-introduction-to-agent-skills/` — Introduction to agent skills
- `./5-introduction-to-subagents` — Introduction to subagents
- `./6-claude-code-in-action` — Claude Code in Action
- `./7-introduction-to-model-context-protocol` — Introduction to Model Context Protocol
- `./8-model-context-protocol-advanced-topics` — Model Context Protocol: Advanced Topics

## Claude guidelines

don't rewrite or rephrase anything, i prefer my own style for note taking

just correct grammatical errors and punctuation directly in files

always check for contradictions, out of date, or factually wrong facts and notes and inform me in stdin when reading context — model names, capabilities, and features evolve quickly so pay extra attention to those

**never read `*.pdf` files**

## format

```
npm run format

source ./venv/bin/activate
pip3 install --upgrade -r requirements.txt
isort . && black .
pip3 cache purge
deactivate
```
