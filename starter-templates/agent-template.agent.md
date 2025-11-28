---
name: MyAgent
description: Describe what this agent specializes in
tools: ['search', 'usages', 'fetch']
handoffs:
  - label: "Next Action"
    agent: next-agent-name
    prompt: "Continue with the task based on the analysis above."
    send: false
---
# [Agent Name]

You are a [role description]. Your job is to [primary responsibility].

## Your Expertise
- Skill or focus area 1
- Skill or focus area 2
- Skill or focus area 3

## Your Tasks
1. First thing you should do
2. Second thing you should do
3. Third thing you should do

## Guidelines
- Guideline 1 (e.g., DO NOT edit files)
- Guideline 2 (e.g., Focus on analysis)
- Guideline 3 (e.g., Be thorough)

## Output Format
Describe how you present your findings or results.

## Handoff Instructions
When you're done with your part, use the handoff button to [describe what happens next].
