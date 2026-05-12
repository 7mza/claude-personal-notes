# [Claude 101](https://anthropic.skilljar.com/claude-101)

## good prompt

1. set stage: your role, objectives, context (upload files, web search, connectors), ...
2. define task: action for claude to take: write, analyse, build, ...
3. rules: style, tones, examples for claude to look at, ...

## supported models

- opus: most powerfull, reasoning, for complex problems
- sonnet: balanced, everyday use
- haiku: smallest, fast responses, simple tasks

## modes

- extended thinking: complexe problems, planning, tech problems, coding
- research: conduct multi angle investigation, exploring external sources

## common challenges

| challenge                     | why                                                | fix                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| response too generic          | not enough context in prompt                       | add details about your specific situation: audience, role, constraints, ... : <br> - ~~write an email about project delay~~ <br> - write an email to our enterprise client explaining that the software integration will be delayed by two weeks. they've been patient so far but this is the second delay. Keep it professional but apologetic. |
| response too long/short       | model guessing length                              | be explicit : <br> - give me a 2 paragraph summary <br> - keep this under 100 words <br> - length isn't a concern                                                                                                                                                                                                                                |
| response didn't follow format | model understood what not how you wanted presented | whow dont just tell, provide example of format, descibe structure explicitly : <br> - use bullet points with bold headers for each section                                                                                                                                                                                                       |
| confident but wrong reponse   | models can hallucinate                             | verify facts, ask for sources, ask for confidence level, enable websearch                                                                                                                                                                                                                                                                        |
| tone not right                | model defaults to a tone not matching your case    | describe tone in details, provide example of writing style : <br> - make this more conversational <br> - This should sound authoritative and formal                                                                                                                                                                                              |

## interation

first propmpt rarely produces perfect result, it's start of process not one shot request

- treat it as starting point : review, identify what's working/not, refine
- give specific and detailed feedback
- know when to start fresh : context pollution is a thing, new clear and refined prompt is sometimes better

## evaluation

testing how well a model performes on a specific type of task will help :

- understand where model add most value in a workflow
- indentify tasks where more context and examples are needed
- build confidence in model output

### simple approach

1. gather example of tasks: written emails, reports created, analyses done
2. create test prompts: write prompts to generate similar output, include context you do naturally when doing this work
3. compare outputs: run prompts and compare model response to your examples and eval
   - does model capture key information
   - tone/style appropriate
   - whats missing/could be improved
4. refine: adjust prompts, add examples, identify where human review is necessary

## projects

self contained workspace, dedicated env for specific work/team, with its own memory, chat history, knowledge base and custom instructions

- knwoledge base : enhance model understanding by uploading relevant documents for model to reference across all chat in project. scale through RAG when context limit is aproached
- custom instructions : guide model behavior, specify tone/style/epertise level, apply to every chat withing project
- collaboration : share context, instructions and accumulated knwoledge with team

### when to use ?

valuable when working on ongoing problems not just one-off questions, use when you have a workflow with:

- reference meterials used repeatedly: notes, results, reports, data
- consitent input requirements
- team collaboration

### instructions

programming model behavior for a project

good project isntructions

- context about what you are working on (this project is for creating marketing content for our B2B software produc)
- process instructions (first consider a blog structure that will entice this audience, then write the draft)
- tone and style preferences (use a professional but conversational tone. avoid jargon when possible)
- specific requirements (always include a call-to-action at the end of marketing copy)

can also be used to automate a workflow (when I upload a meeting transcript, create a structured summary using this template.)

### knowledge base

- Reference documents (brand guidelines, style guides, templates)
- Background materials (research reports, meeting notes, requirements docs)
- Examples of work you want Claude to emulate
- Technical documentation or specifications

name your files descriptively, model uses file names to understand and find right informations, never use "document1.pdf" but "Q4-2024-Brand-Guidelines.pdf"

### collaboration

permission levels

- view: readonly
- edit: read/write project and components
- owner: \*, members, visibility

### best practices

- start focused and expand: beging with a specific use case and enrich
- keep knowledge base current: outdated documents = outdated reponses
- clear instuctions: vague instructions = inconsistent results
- name documents descriptievly and group related files together: model uses filenames and proximity to understand relationships between docs
- reference docs by name when asking questions to help model focus its search: based on our Q3 report, what were the ...?

## artifacts

standalone (interactive) output model can create automatically or by asking explicitly (create me this artifact, description), alongside a conversation :

- Create a flowchart showing our customer onboarding process
- Build an interactive dashboard that lets me input monthly expenses and see a breakdown
- Design a landing page for a productivity app with a hero section and feature list
- Write a project brief template I can reuse for new initiatives

types :

- documents you can export or edit
- code snippet
- html pages
- images
- diagrams
- ...

can be published publicly (readonly via public link) or shared with org (require team auth)

### tips

- be specific:
  - ~~Build a budget tracker~~
  - Build a monthly budget tracker where I can input expenses by category, see a pie chart breakdown, and get a warning when I'm over budge
- describe end user to help model make appropriate design choice:
  - "This flowchart is for new employees" != "This flowchart is for the engineering team"
- iterate incrementally: one feature and change at a time to identify whats working and catch issues early
- request artifact when needed if model is not it creating automatically "create that as an artifact"

## [skills](../4-introduction-to-agent-skills/README.md)

- folder of instructions, scripts and resource that model loads dynamically to improve perf on specialized tasks
- expertise packages
- teach model how to complete specific task in repeateable manner
- codify repeatable workflow so model follow same steps every time
- model use them automatically based on request

### how to create

if no technical knowledge, create using model itself

1. i want to create a skill for ...
2. model will conduct interview about your workflow
3. upload reference materials
4. save new skill

### skills vs projects

projects: store knwoledge (what)

- knowledge hub
- how model understand work

skills: perform tasks (how)

- how model execute task
- specific steps
- order of operations

|             | projects                                             | skills                                                                                                         |
| ----------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| purpose     | store knwoledge model can reference                  | define processes models can execute                                                                            |
| best for    | long term context, referencing material, team collab | repeatable workflow, multi step tasks, consistent methodology                                                  |
| example     | customer hub, research buddy, feedback generator     | process guidelines (brand, legal), blog drafting, pdf creation                                                 |
| persistence | knwoledge available across all chats in project      | instructions applied when the skill is picked by model (automatically depending on chat and skill description) |

## connectors

give model access to external services (instead of manual knowledge upload):

- web connectors: access to cloud services (gmail, jira, slack, ...)
- desktop extensions: run locally through claude desktop app, give acess to local files, native apps (browser automation, ...) and OS features (terminal, ...)

Model Context Protocol is the universal standard (like usb for AI)

check [claude.ai/directory](https://claude.ai/directory) for available connectors

once connected, model use them when responding to requests:

- jira: whats is my highest priority task today
- gmail: find the email where we ...
- confluence: search our documentation for ...
- stripe: show me last x transactions over 100€
- ...

## entreprise search

- `Ask {Your Org Name}` option
- designed to find and synthesize knowledge across company tools and data sources (sharepoint, slack, gmail threads, gdrive, ...etc)
- prebuild project for entire org, with company knowledge base already loded

### common use cases

Getting up to speed

- "What happened yesterday while I was out?"
- "Summarize key updates across the business from the last week"
- "What are the current blockers on the Platform project?"

Policy and process questions

- "What is our company's remote work policy?"
- "How do I submit an expense report?"
- "What's the process for requesting time off?"

Research and analysis

- "What are the main reasons customers cite for choosing competitors?"
- "Summarize discussions about the Q4 product roadmap"
- "Find information about our customer onboarding process"
  Onboarding new team members

- "How does our authentication system work?"
- "Who should I talk to about learning the billing system?"
- "What tools does the engineering team use for deployment?"

Performance and project tracking

- "Find discussions and documents related to the marketing campaign"
- "What were the key decisions from last week's leadership meetings?"
- "Summarize team contributions to the Infrastructure initiative"

## reasearch mode

(research assitant skill) transfrom model from a conversational assistant into a systematic investigator:

- don't just answer question but explore it from multiple angles (from web and connected integrations)
- compare different perspective
- cross reference sources
- synthesize information and findings
- provide citations

consider simple `web search` instead, if speed matter and you only need quick specific fact that require low number of sources

consider `extended thinking` instead, fom complexe problemes that doesnt require external information (math, code) and where answer comes from reasoning rather than gathering information

consider `entreprise search` instead, when you need to draw from org knowledge not public web

`research mode` automatically enable `extended thinking` and `plan mode`

### tips

it's a very long runing process

- be specific about the goals :
  - ~~Tell me about the EV market~~
  - Analyze the electric vehicle battery market—identify key players technology trends, and supply chain challenges that might affect investment decision
- specify sections or structure you want :
  - Compare venue options for a team offsite including: location and accessibility, meeting space and amenities, catering options, and pricing considerations
- include relevant constraints will help model focus its search on relevant options
- ask model to help refine the prompt before enabling feature
- model can pull context from connectors :
  - Review my calendar commitments for next week and research each company I'm meeting with
  - Find all internal documents about our pricing strategy and compare to how competitors are positioning themselves
- you can steer model to use integrations by saying things like :
  - pull relevent context from my gdrive/emails
- you can turn off websearch to do internal only research across connectors

## [use cases examples](https://claude.com/resources/use-cases/)

##
