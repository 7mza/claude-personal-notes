# [ai fluency framework](https://anthropic.skilljar.com/ai-fluency-framework-foundations)

[AI Fluency vocabulary guide](./AI_Fluency_vocabulary_cheat_sheet.pdf)

## introduction

ai fluency involves developing practical skills, knowledge, insights, and values that help you interact with AI systems in ways that are effective, efficient, ethical, and safe

maximising what you get from ai interactions without wasting time, energy and in an honest and responsible way that protects the privacy and security of yourself and others

3 ways to engage with AI:

- automation:
  - AI completes specific tasks based on your instructions
  - examples
    - summerize doc
    - draft email
    - create image
    - plan trip
    - ...
  - works well when you have a clear outcome in mind
  - challenging when you are not sure what you are looking for
- augmentation:
  - you and AI collaborate as creative thinking and problem solving partners
  - explore problems
  - bounce ideas off each other
  - use AI to augments creativity and thinking
  - ai doesnt do work of you, but help you do your work better
  - works best when solutions arent straight forward and you need to explore and experiment
- agency:
  - you configure AI to work independently on your behalf establishing its knowledge and behavior patterns rather than just giving it specific tasks
  - rather than defining specific actions, you establish ai knowledge and behavior patterns
  - you become less than a script writer giving exact directions, but like a director setting a vision

each approache serve a different purpose and excel in different situations, you might use all in same project

augmentation and agency > automation for taking advantage of ai capabilites and often lead to the most creative and effective solutions

ai is not just a tool, it's also a partner and co creator

### 4D framework

4 competencies for AI fluency

- delegation :
  - big picture
  - what are you trying to acomplish ?
  - what kinds of work are involved
  - what should you handle yourself
  - know what ai system can and can't do well
  - where might ai be helpful
- description :
  - clear communication with ai
    - ~~make me a logo~~
    - describing company values, target audience, prefered colors, syles references, ...
  - goes beyond writing prompts
    - detailed context rich conversations:
      - what are you trying to achieve
      - format of the output
      - how the ai should approach the task
      - tone and style of interactions
- discernment :
  - evaluationg AI output:
    - are the facts accurate
    - does reasoning make sense
    - do recomenations align with input
    - does output help me move forward
  - draws on you own expertise in a domain
  - require insight and judgement to separate what's usefull from what's not
- diligence :
  - safety and ethics
  - personal responsibility and accountability
  - how to ensure fairness and control bias
  - sensitive data protection

## gen ai

[overview](./DD1_Handout__Overview_of_Generative_AI.pdf)

limitations:

- knowledge cutoff date
- incorrect informations / hallucinations
- window memory/context limitation
- non deterministic output

human provides :

- critical thinking
- judgement
- creativity
- ethical oversight

ai provides :

- speed
- scale
- pattern recongnition
- processing abilities

## delegation competency

**augmentation can help eveywhere, just ask the model**

how to work effectively and efficiently with ai ?

- breaking down complex work into smaller parts
- making decision about who does what
- choosing right mode of interaction : automation, augmentation or agency

corner stone of delegation = your own expertise not ai:

### problem awareness

- what is success :
  - objective, vision
  - what are you trying to solve
  - key project goals

- what kind of thinking and work is needed to get to success :
  - are there areas that are simple but time consuming
  - areas of uncertainty where you could use a thinking partner
  - areas of ignorance where you need more data
  - areas of precision and critical judgement where you need human intervention

**most effective ai collaborator = expert in their fields first then ai delagators second**

### platform awarness

hands on experimentation with different plateform
develop insight:

- which plateform, or model do what best
- limitations of each

### task delegation

dividing work between human and ai

- what could be usefully automated ?
- where augmentation would create more value than working alone ?
- what should be exclusively human ?
- what routine interactions can ai agent handle for you ? (agency)

## description competency

ability to transform ai tool from a generic assitant to a fine tuned thinking partner that meet your current need

how to communicate with ai, build a bridge between your intentions and ai capabilities

- far beyond prompts
- explain tasks, ask questions, provide context and guide interactions
- build a shared thinking env where both human and ai can each do best their work

### product description

ability to clearly define characteristics of desired ouput

quality of ai output depends on how you clearly describe what you want with every relevant detail:

- context
- format
- audience
- style
- other constraints

### process description

ability to guide model thought process

specifying how ai should tackle a job is as important as specifying end goal :

- general guidance
- step by step instructions
- demonstration through examples

models already have extensive knowledge, u should give additional context to your specific situation

- specific data to draw on
- specific issues to adress in a prefered order

### performance description

ability to define behavioral aspects of an ai interaction

models are non deterministic interactive systems that will behave differently in different context :

- explain how should model behave to get best results
- ask your self what kind of thinking partner do i need right now
  - narrowing down or exploring multiple possibilities
  - should model challenge your assumptions or follow your lead
  - provide details or concise final answer

## effective prompting

**probably outdated, just ask model to conduct a small interview for the problem to solve and to craft a prompt at the end, andor extended thinking**

### foundations

#### 1. provide context

be specific about

- what you want
- why you anti it
- who you are

#### 2. offer examples

showing is better than telling when it's hard to explain

give some examples for input and desired output in your prompt

#### 3. specify output constraints

**model can't read your mind**, tell it exacly what's required for output

#### 4. break down complex tasks

chain of toughts prompting

give steps on how to approach solving

#### 5. give ai space to think

plan mode/extended thinking mode, do it automatially

for older or local models, steer it in prompt

```
before answering, think through this problem carefully.
considere different factors involved, potential constraints, and various approaches before reccomending the best solution.
```

#### 6. define roles

who do you want model to act/think as

who's the output for

### iterative process

```
                              ___________________
                              |                 |
                                                v
create initial prompt -> model reponse -> refine prompt -> output
                              ^
                              |_________________|
```

### usefull techniques

| technique                | example                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ |
| ask for variations       | can u give me 3 different version of this ?                                    |
| request different format | instead of paragraph, can you present this as bullet points ?                  |
| check model confidence   | how confident are you about this answer and why ?                              |
| reset context            | context polution will harm outputs, try with fresh context after honing prompt |

## discernment competency

ability to evaluate ai output and how it got there

domain expertise and common sense

### product discernment

ability to judge quality of output:

- factually accurate
- appropriate audience and purpose
- coherent and well structured
- meet requirements
- add any value / solve problem

### process discernment

ability to judge quality of problem solving approach:

- ass pulling
- context switching
- logical inconsistency
- lapses in attention
- inapropriate steps
- stuck in small details
- circular reasoning

### performance discernment

ability to judge ai behavior

- appropriate communications style
- information at right level
- response to feedback
- efficient interaction

### feedback and correction

`description <-> discernment`

- specify problem
- explain why is it a problem
- provide concrete suggestion for improvement
- revising input that led to problem

## diligence competency

### creation diligence

nothing new, usual common sense, anything you participate in
creating can come back to bite you

- ethical standards and values
- org policies
- laws
- what are the implication of working with this input
- who own the input
- how did we get this input
- privacy and security protection
- ...

### transparency diligence

ability to be open about ai interaction with relevant audience

- who have the right to know when ai played a part in creation
- what they need to know
- how it should be communicated

### deployement diligence

creators are responsible for shared output, not models or plateforms

- verify facts
- check biases
- ensure accuracy
- usage right
- ...

### ethical frameworks

- personal guidelines
- orgs policies
- professional sandards
- industry code of conducrs
- law and regulations
- staying informed
