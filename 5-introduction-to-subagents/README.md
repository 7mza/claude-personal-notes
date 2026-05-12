# [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)

subagent = break work into focused pieces, delegate a task to specialized system prompt + new context + tools, return summary/output to calling context

`/agents` to create/list

same general principles as [skills](../4-introduction-to-agent-skills/README.md)

main will use sub desc to write an input sys prompt when launching it (to tell it what to do), use this information in desc `You (main) must tell the sub which input X, where to do Y` (for example forward `git diff` result from main to sub) (think if sub need input and pass it directly from main ?)

use `proactively use this agent when you need to TASK` in desc

add examples of converstation in md file to help model better decide when to use sub

define output format in md for sub to decide when a task should be considered done

tell sub to pass back obstacles/errors/exceptions in output format so main context can access it (**whatever is important to main context should be passed back**)

use subs if intermediate work is not important to context and only output/summary is needed (ex research)

use subs if you need fresh eyes (context separation)

don't use subs for `you are an expert in X` it's useless

`if(intermediate work matters) main else sub`
