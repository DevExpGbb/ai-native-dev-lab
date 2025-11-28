# 🎯 Hands-On Lab Structure: From Vibe Coding to Vibe Engineering

## Executive Summary

This hands-on lab guides participants from simple instruction files to fully orchestrated agent workflows using VS Code Copilot's native customization primitives. The lab follows a **dual-track approach** where participants choose between documentation generation or test generation workflows.

---

## 🏗️ Lab Timeline (60 minutes)

```mermaid
gantt
    title Lab Timeline
    dateFormat X
    axisFormat %M min
    
    section Setup
    Phase 0 - Setup & Context     :0, 5
    
    section Foundation
    Phase 1 - Custom Instructions :5, 15
    
    section Automation
    Phase 2 - Prompt Files        :20, 15
    
    section Orchestration
    Phase 3 - Agents & Handoffs   :35, 20
    
    section Wrap-up
    Phase 4 - Exploration & Q&A   :55, 5
```

---

## 📚 The Three Primitives

```mermaid
graph TB
    subgraph "VS Code Copilot Customization Hierarchy"
        I[".instructions.md<br/>📋 Rules & Guidelines"]
        P[".prompt.md<br/>📝 Reusable Tasks"]
        A[".agent.md<br/>🤖 AI Personas + Handoffs"]
    end
    
    I -->|"Referenced by"| P
    P -->|"Can specify"| A
    A -->|"Can chain to"| A
    
    style I fill:#e1f5fe,stroke:#01579b
    style P fill:#fff3e0,stroke:#e65100
    style A fill:#f3e5f5,stroke:#7b1fa2
```

| Primitive | Purpose | Trigger | Complexity |
|-----------|---------|---------|------------|
| `.instructions.md` | Define rules/guidelines | Auto-applied or manual | ⭐ Simple |
| `.prompt.md` | Reusable task workflows | `/command` in chat | ⭐⭐ Moderate |
| `.agent.md` | AI personas with handoffs | Agent dropdown | ⭐⭐⭐ Advanced |

---

## 🎓 Two Tracks

Participants choose one track based on their interest:

```mermaid
graph LR
    subgraph "Choose Your Track"
        DOC["📖 Documentation Track<br/>Auto-generate docs"]
        TEST["🧪 Testing Track<br/>Auto-generate tests"]
    end
    
    START((Start)) --> DOC
    START --> TEST
    
    DOC --> SAME["Same Core Concepts<br/>Different Content"]
    TEST --> SAME
    
    style DOC fill:#c8e6c9,stroke:#2e7d32
    style TEST fill:#bbdefb,stroke:#1565c0
```

| Track | Focus | Deliverable |
|-------|-------|-------------|
| **📖 Documentation** | Auto-generate documentation | Instructions → Doc Prompt → Analyzer + Writer Agents |
| **🧪 Testing** | Auto-generate unit tests | Instructions → Test Prompt → Analyzer + Tester Agents |

---

## 📖 Phase Details

### Phase 0: Setup & Context (5 min)

**Objectives:**
- Verify VS Code settings are enabled
- Orient participants to the three primitives
- Choose a track (documentation or testing)

**Checklist:**
- [ ] VS Code with GitHub Copilot extension
- [ ] Settings enabled: `chat.promptFiles`, `github.copilot.chat.codeGeneration.useInstructionFiles`
- [ ] Lab repository cloned or project folder ready

---

### Phase 1: Foundation - Custom Instructions (15 min)

**Objectives:**
- Create a `.instructions.md` file with frontmatter
- Define team/project standards
- Test auto-application in Copilot Chat

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant VSC as VS Code
    participant CP as Copilot Chat
    
    Dev->>VSC: Create .instructions.md
    Dev->>VSC: Add YAML frontmatter (applyTo)
    Dev->>VSC: Write coding standards
    Dev->>VSC: Open matching file type
    VSC->>CP: Auto-applies instructions
    Dev->>CP: Ask coding question
    CP-->>Dev: Response follows your standards!
```

**Deliverable:** A working instruction file that automatically applies when editing matching files.

---

### Phase 2: Task Automation - Prompt Files (15 min)

**Objectives:**
- Create a `.prompt.md` file
- Reference the instruction file
- Use variables and specify tools
- Invoke via `/command`

```mermaid
flowchart LR
    subgraph "Prompt File Structure"
        FM["YAML Frontmatter<br/>name, tools, agent"]
        BODY["Markdown Body<br/>Task description"]
        VARS["Variables<br/>${file}, ${input:}"]
        REFS["References<br/>[instructions](...)"]
    end
    
    FM --> BODY
    BODY --> VARS
    BODY --> REFS
```

**Deliverable:** A reusable prompt invocable via `/command` in Copilot Chat.

---

### Phase 3: Orchestration - Agents with Handoffs (20 min)

**Objectives:**
- Create two `.agent.md` files
- Define specialized AI personas
- Implement handoff between agents
- Test the sequential workflow

```mermaid
stateDiagram-v2
    [*] --> Analyzer: User selects agent
    
    state "🔍 Analyzer Agent" as Analyzer {
        [*] --> Analyze
        Analyze: Read-only tools
        Analyze: Understands code structure
        Analyze --> [*]: Analysis complete
    }
    
    Analyzer --> Handoff: Click "Generate" button
    
    state "📝 Generator Agent" as Generator {
        [*] --> Generate
        Generate: Edit tools enabled
        Generate: Creates files
        Generate --> [*]: Files created
    }
    
    Handoff --> Generator
    Generator --> [*]: Workflow complete
```

**Deliverable:** Two agents with a working handoff button.

---

### Phase 4: Wrap-Up (5 min)

**Objectives:**
- Share patterns discovered
- Q&A and advanced scenarios
- Resources for continued learning

---

## 🔄 Workflow Diagrams by Track

### 📖 Documentation Track

```mermaid
flowchart TB
    subgraph Instructions["📋 Instructions Layer"]
        DI[documentation-standards.instructions.md<br/>applyTo: **/*.md]
    end
    
    subgraph Prompt["📝 Prompt Layer"]
        DP[generate-docs.prompt.md<br/>Invoked with /generate-docs]
    end
    
    subgraph Agents["🤖 Agent Layer"]
        DA[doc-analyzer.agent.md<br/>Tools: search, usages]
        DW[doc-writer.agent.md<br/>Tools: createFile, editFile]
    end
    
    DI -.->|"Referenced by"| DP
    DP -->|"Uses agent"| DA
    DA -->|"Handoff: Write Documentation"| DW
    
    style DI fill:#e3f2fd,stroke:#1565c0
    style DP fill:#fff8e1,stroke:#f9a825
    style DA fill:#fce4ec,stroke:#c2185b
    style DW fill:#e8f5e9,stroke:#2e7d32
```

### 🧪 Testing Track

```mermaid
flowchart TB
    subgraph Instructions["📋 Instructions Layer"]
        TI[testing-standards.instructions.md<br/>applyTo: **/*.test.*]
    end
    
    subgraph Prompt["📝 Prompt Layer"]
        TP[generate-tests.prompt.md<br/>Invoked with /generate-tests]
    end
    
    subgraph Agents["🤖 Agent Layer"]
        TA[test-analyzer.agent.md<br/>Tools: search, usages]
        TG[test-generator.agent.md<br/>Tools: createFile, editFile]
    end
    
    TI -.->|"Referenced by"| TP
    TP -->|"Uses agent"| TA
    TA -->|"Handoff: Generate Tests"| TG
    
    style TI fill:#e3f2fd,stroke:#1565c0
    style TP fill:#fff8e1,stroke:#f9a825
    style TA fill:#fce4ec,stroke:#c2185b
    style TG fill:#e8f5e9,stroke:#2e7d32
```

---

## 📁 Repository Structure

```
vibe-engineer-lab/
├── README.md                          # Step-by-step lab guide
├── lab-structure.md                   # This file
├── cheatsheet.md                      # Quick reference
├── .vscode/
│   └── settings.json                  # Pre-configured settings
│
├── golden-examples/                   # Reference implementations
│   ├── documentation-track/
│   │   ├── .github/
│   │   │   ├── instructions/
│   │   │   │   └── documentation-standards.instructions.md
│   │   │   ├── prompts/
│   │   │   │   └── generate-docs.prompt.md
│   │   │   └── agents/
│   │   │       ├── doc-analyzer.agent.md
│   │   │       └── doc-writer.agent.md
│   │   └── sample-code/
│   │
│   └── testing-track/
│       ├── .github/
│       │   ├── instructions/
│       │   │   └── testing-standards.instructions.md
│       │   ├── prompts/
│       │   │   └── generate-tests.prompt.md
│       │   └── agents/
│       │       ├── test-analyzer.agent.md
│       │       └── test-generator.agent.md
│       └── sample-code/
│
└── starter-templates/                 # Scaffolds for participants
    ├── instructions-template.instructions.md
    ├── prompt-template.prompt.md
    └── agent-template.agent.md
```

---

## ✅ Success Criteria

By the end of the lab, each participant should have:

| Deliverable | Validation |
|-------------|------------|
| ✅ 1 Custom Instruction file | Applied automatically when editing matching files |
| ✅ 1 Prompt file | Invocable via `/command` in Copilot Chat |
| ✅ 2 Agent files with handoff | Visible handoff button after first agent completes |
| ✅ Working workflow | Successfully generates docs OR tests for their code |

---

## 🎯 Key Pedagogical Decisions

1. **Native VS Code Format Over APM** - Keep it simple with `.instructions.md`, `.prompt.md`, `.agent.md`
2. **"Bring Your Own Project" with Fallback** - Participants use their code; golden examples provide backup
3. **Progressive Disclosure** - Instructions → Prompts → Agents (simple to complex)
4. **Analyzer → Generator Pattern** - Read-only analysis, then handoff to editing agent

---

## 📖 Related Documentation

- [VS Code Copilot Customization Overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
