# 🚀 AI Native Development Lab: Scaling AI-Native Development

> **From Vibe Coding to AI Native Development**: Learn to build structured AI workflows with VS Code and GitHub Copilot

[![VS Code](https://img.shields.io/badge/VS%20Code-1.96+-blue?logo=visualstudiocode)](https://code.visualstudio.com/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Required-green?logo=github)](https://github.com/features/copilot)

---

## 📋 Overview

This hands-on lab teaches you to move beyond simple prompt-based coding into **structured AI engineering workflows**. You'll learn to create:

- **Custom Instructions** - Team standards that automatically apply to your code
- **Prompt Files** - Reusable task workflows invoked with `/commands`
- **Custom Agents** - Specialized AI personas with handoff capabilities

By the end, you'll have a working multi-agent pipeline that either generates documentation or unit tests based on your team's standards.

---

## 🎯 Learning Objectives

| Objective | Outcome |
|-----------|---------|
| Create custom instructions | Auto-applied coding standards |
| Build prompt files | Reusable `/commands` for common tasks |
| Design custom agents | Specialized AI with handoffs |
| Implement handoffs | Multi-agent sequential workflows |

---

## 📚 Prerequisites

### Required
- [VS Code](https://code.visualstudio.com/) version 1.96 or later
- [GitHub Copilot](https://github.com/features/copilot) subscription (Individual, Business, or Enterprise)
- GitHub Copilot Chat extension installed

### Recommended
- A "brownfield" project you want to improve (your own codebase)
- Basic familiarity with YAML syntax
- Understanding of Markdown

---

## ⚙️ Setup

### 1. Enable Required Settings

Open VS Code Settings (`Cmd+,` / `Ctrl+,`) and ensure these are enabled:

```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.promptFiles": true,
  "chat.instructionsFilesLocations": {
    ".github/instructions": true
  },
  "chat.promptFilesLocations": {
    ".github/prompts": true
  },
  "chat.agentFilesLocations": {
    ".github/agents": true
  }
}
```

> 💡 **Tip**: Copy `.vscode/settings.json` from this repo to your project for pre-configured settings.

### 2. Clone This Repository

```bash
git clone https://github.com/your-org/vibe-engineer-lab.git
cd vibe-engineer-lab
code .
```

### 3. Choose Your Track

| Track | Best For | Focus |
|-------|----------|-------|
| [📖 Documentation](#-documentation-track) | Teams needing consistent docs | Auto-generate documentation |
| [🧪 Testing](#-testing-track) | Teams improving test coverage | Auto-generate unit tests |

---

## 📖 Documentation Track

### Phase 1: Create Your Instructions File (15 min)

Create a file at `.github/instructions/documentation-standards.instructions.md`:

```yaml
---
applyTo: "**/*.md"
---
# Documentation Standards

When writing or reviewing documentation:

## Structure
- Use descriptive headings (H2 for sections, H3 for subsections)
- Include a brief overview at the top of each document
- Add code examples for technical concepts

## Style
- Write in active voice
- Keep sentences concise (max 25 words)
- Use bullet points for lists of 3+ items

## Code Examples
- Include language identifier in code blocks
- Add comments explaining complex logic
- Show both input and expected output when relevant
```

**✅ Test it:** Open any `.md` file and ask Copilot a documentation question. It should follow your standards!

---

### Phase 2: Create Your Prompt File (15 min)

Create a file at `.github/prompts/generate-docs.prompt.md`:

```yaml
---
name: generate-docs
description: Generate documentation for the current file or selection
agent: agent
tools: ['search', 'editFile', 'createFile']
---
# Generate Documentation

Generate comprehensive documentation for the following code.

## Context
- File: ${file}
- Selection: ${selection}

## Requirements
Follow the documentation standards in [documentation-standards](../instructions/documentation-standards.instructions.md).

## Output
Create or update a markdown file with:
1. Overview of the code's purpose
2. API reference (functions, classes, methods)
3. Usage examples
4. Any important notes or caveats
```

**✅ Test it:** Type `/generate-docs` in Copilot Chat and select some code!

---

### Phase 3: Create Your Agents (20 min)

#### Agent 1: Doc Analyzer

Create `.github/agents/doc-analyzer.agent.md`:

```yaml
---
name: Doc Analyzer
description: Analyze code structure for documentation
tools: ['search', 'usages', 'fetch']
handoffs:
  - label: "📝 Write Documentation"
    agent: doc-writer
    prompt: "Based on my analysis above, generate comprehensive documentation."
    send: false
---
# Documentation Analyzer

You are a documentation analyst. Your job is to analyze code and identify what needs to be documented.

## Your Tasks
1. Identify all public functions, classes, and methods
2. Determine the purpose of each component
3. Find existing documentation gaps
4. Note any complex logic that needs explanation

## Guidelines
- DO NOT edit any files
- Focus on understanding, not writing
- List your findings clearly
- Prepare a summary for the documentation writer

When you're done analyzing, use the handoff to pass your findings to the Doc Writer.
```

#### Agent 2: Doc Writer

Create `.github/agents/doc-writer.agent.md`:

```yaml
---
name: Doc Writer
description: Write documentation based on analysis
tools: ['editFile', 'createFile', 'search']
---
# Documentation Writer

You are a technical writer. Your job is to create clear, comprehensive documentation.

## Your Tasks
1. Review the analysis provided
2. Create or update documentation files
3. Follow the team's documentation standards
4. Include code examples where helpful

## Standards
Follow the guidelines in [documentation-standards](../instructions/documentation-standards.instructions.md).

## Output Format
- Create `.md` files in a `docs/` folder
- Use consistent heading hierarchy
- Include a table of contents for longer docs
```

**✅ Test it:** Select "Doc Analyzer" from the agent dropdown, analyze some code, then click the handoff button!

---

## 🧪 Testing Track

### Phase 1: Create Your Instructions File (15 min)

Create a file at `.github/instructions/testing-standards.instructions.md`:

```yaml
---
applyTo: "**/*.test.{js,ts,jsx,tsx,py}"
---
# Testing Standards

When writing unit tests:

## Structure
- Use descriptive test names: `should [expected behavior] when [condition]`
- Group related tests with describe/context blocks
- Follow Arrange-Act-Assert pattern

## Coverage
- Test happy path and edge cases
- Include error handling tests
- Mock external dependencies

## Best Practices
- One assertion per test (when possible)
- Keep tests independent and isolated
- Use meaningful test data, not random values
```

**✅ Test it:** Open any test file and ask Copilot about testing. It should follow your standards!

---

### Phase 2: Create Your Prompt File (15 min)

Create a file at `.github/prompts/generate-tests.prompt.md`:

```yaml
---
name: generate-tests
description: Generate unit tests for the current file or selection
agent: agent
tools: ['search', 'editFile', 'createFile']
---
# Generate Unit Tests

Generate comprehensive unit tests for the following code.

## Context
- File: ${file}
- Selection: ${selection}

## Requirements
Follow the testing standards in [testing-standards](../instructions/testing-standards.instructions.md).

## Output
Create a test file with:
1. Tests for all public functions/methods
2. Happy path tests
3. Edge case tests
4. Error handling tests
```

**✅ Test it:** Type `/generate-tests` in Copilot Chat and select a function!

---

### Phase 3: Create Your Agents (20 min)

#### Agent 1: Test Analyzer

Create `.github/agents/test-analyzer.agent.md`:

```yaml
---
name: Test Analyzer
description: Analyze code to identify what needs testing
tools: ['search', 'usages', 'fetch']
handoffs:
  - label: "🧪 Generate Tests"
    agent: test-generator
    prompt: "Based on my analysis above, generate comprehensive unit tests."
    send: false
---
# Test Analyzer

You are a test planning specialist. Your job is to analyze code and plan what tests are needed.

## Your Tasks
1. Identify all testable functions and methods
2. Determine input parameters and return types
3. Identify edge cases and error conditions
4. Check for existing test coverage gaps

## Guidelines
- DO NOT edit any files
- Focus on analysis, not implementation
- List each function with its test cases needed
- Note any mocking requirements

When done, use the handoff to pass your test plan to the Test Generator.
```

#### Agent 2: Test Generator

Create `.github/agents/test-generator.agent.md`:

```yaml
---
name: Test Generator
description: Generate unit tests based on analysis
tools: ['editFile', 'createFile', 'search']
---
# Test Generator

You are a test implementation specialist. Your job is to write comprehensive unit tests.

## Your Tasks
1. Review the test plan provided
2. Create test files following project conventions
3. Implement all identified test cases
4. Add appropriate mocks and fixtures

## Standards
Follow the guidelines in [testing-standards](../instructions/testing-standards.instructions.md).

## Output Format
- Create test files next to source files (e.g., `foo.test.ts`)
- Use the project's testing framework
- Include setup and teardown as needed
```

**✅ Test it:** Select "Test Analyzer" from the agent dropdown, analyze a function, then click the handoff button!

---

## 📁 Project Structure

```
vibe-engineer-lab/
├── README.md                    # This file
├── lab-structure.md             # Detailed lab structure
├── cheatsheet.md                # Quick reference
├── .vscode/
│   └── settings.json            # Pre-configured settings
├── golden-examples/             # Complete working examples
│   ├── documentation-track/
│   └── testing-track/
└── starter-templates/           # Empty templates to start from
```

---

## 🔧 Starter Templates

Copy these templates to your project to get started quickly:

| Template | Use For |
|----------|---------|
| [`starter-templates/instructions-template.instructions.md`](starter-templates/instructions-template.instructions.md) | Creating instruction files |
| [`starter-templates/prompt-template.prompt.md`](starter-templates/prompt-template.prompt.md) | Creating prompt files |
| [`starter-templates/agent-template.agent.md`](starter-templates/agent-template.agent.md) | Creating agent files |

---

## 📖 Official Documentation

Essential reading for deeper understanding:

| Topic | Link |
|-------|------|
| **Customization Overview** | [VS Code Docs: Customization](https://code.visualstudio.com/docs/copilot/customization/overview) |
| **Custom Instructions** | [VS Code Docs: Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) |
| **Prompt Files** | [VS Code Docs: Prompts](https://code.visualstudio.com/docs/copilot/customization/prompt-files) |
| **Custom Agents** | [VS Code Docs: Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) |

---

## 🎯 Quick Reference

### Instruction File Frontmatter
```yaml
---
applyTo: "**/*.py"    # Glob pattern for auto-apply
---
```

### Prompt File Frontmatter
```yaml
---
name: my-prompt           # Command name after /
description: What it does
agent: agent              # ask | edit | agent | custom-agent-name
tools: ['search', 'editFile', 'createFile']
---
```

### Agent File Frontmatter
```yaml
---
name: My Agent
description: What the agent does
tools: ['search', 'usages']
handoffs:
  - label: "Next Step"
    agent: other-agent
    prompt: "Continue with..."
    send: false
---
```

### Variables (for Prompt Files)
| Variable | Description |
|----------|-------------|
| `${file}` | Current file path |
| `${selection}` | Selected text |
| `${input:name}` | User input |
| `${input:name:placeholder}` | With placeholder |

---

## ❓ Troubleshooting

### Instructions not applying?
1. Check `applyTo` glob pattern matches your file
2. Verify settings are enabled
3. Restart VS Code if needed

### Prompt not showing?
1. Ensure file is in `.github/prompts/` folder
2. Check frontmatter syntax (YAML)
3. Verify `chat.promptFiles` is enabled

### Handoff button not appearing?
1. Check `handoffs` array syntax in agent file
2. Ensure target agent exists
3. Verify agent name matches exactly

---

## 📝 License

This lab is provided for educational purposes. Feel free to adapt for your team's training needs.

---

## 🙏 Acknowledgments

- VS Code and GitHub Copilot teams for the customization features
- The AI-native development community for inspiration

---

**Happy AI Native Development! 🎉**
