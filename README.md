# 🐍 Phase 1 — Python Fundamentals + AI Engineering

> **Learning Path:** AI Engineer → Agentic AI Engineer
> **Approach:** 20% Concepts · 80% Implementation

This repository contains my **Phase 1 Python learning journey**, focused on building strong Python fundamentals through practical, AI-engineering-oriented projects.

The goal of this phase was not to memorize Python syntax, but to learn how to **use Python to solve problems, model data, build applications, and structure code properly**.

---

## 🎯 Phase 1 Objectives

By the end of this phase, I aimed to be able to:

- Work confidently with Python's core data types
- Choose appropriate data structures
- Work with nested data
- Write conditions and loops
- Validate user input
- Build CLI applications
- Use functions to separate responsibilities
- Organize Python projects into modules
- Apply Git and `uv` workflows
- Build an AI-related project from scratch

---

# 🧱 Phase 0 Foundation

Before starting Phase 1, I completed the developer workflow foundation.

### Tools & Practices

- Python project structure
- `uv`
- Virtual environments
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore`
- `.env`
- `.env.example`
- Git
- GitHub
- VS Code
- Terminal workflows
- README documentation

### Core `uv` Workflow

```bash
uv init
uv add <package>
uv sync
uv run python <file>
```

### Git Workflow

```bash
git status
git add .
git commit -m "meaningful message"
git push
```

These practices were carried forward into the Phase 1 project.

---

# 🐍 Python Fundamentals Covered

## 1. Variables & Data Types

Covered:

- Variables
- `int`
- `float`
- `str`
- `bool`
- `None`
- `type()`
- `isinstance()`
- Type conversion
- Mutable vs immutable objects
- Boolean conversion pitfalls

Example:

```python
prompt_name = "code_reviewer"
prompt_category = "coding"
version = 1
is_active = True
```

---

## 2. Strings

Covered:

- Indexing
- Slicing
- `split()`
- `join()`
- `strip()`
- `replace()`
- `find()`
- `startswith()`
- `endswith()`
- f-strings
- Multiline strings
- Input normalization

### Important Lesson

User input such as identifiers can be normalized:

```python
name = input().strip().lower()
```

But actual AI prompt content should generally preserve its original capitalization and formatting.

---

## 3. Collections

### Lists

Covered:

- Creating lists
- Indexing
- Slicing
- `append()`
- `extend()`
- `insert()`
- `pop()`
- `remove()`
- Searching
- List comprehensions

### Tuples

Covered:

- Immutable sequences
- Tuple unpacking
- Tuples returned from dictionary `.items()`

### Sets

Covered:

- Unique values
- Membership checking
- Extracting unique categories

### Dictionaries

Covered in depth:

- Keys
- Values
- Items
- `.get()`
- `.keys()`
- `.values()`
- `.items()`
- Adding values
- Updating values
- Deleting values
- Nested dictionaries
- Dictionary iteration
- Dictionary comprehensions
- Dictionary-based data modeling

Important understanding:

```python
for key in dictionary:
    print(key)
```

iterates over keys.

```python
for key, value in dictionary.items():
    print(key, value)
```

iterates over key/value pairs.

Also practiced:

```python
enumerate(dictionary)
enumerate(dictionary.items(), start=1)
```

---

## 4. Nested Data Structures

I learned how to represent AI-related configuration using nested dictionaries.

Example:

```python
prompt_dictionary = {
    "coder_python": {
        "name": "coder_python",
        "category": "coding",
        "system_prompt": "You are a senior Python engineer.",
        "version": "1.2.0",
        "is_active": True,
    }
}
```

Mental model:

```text
Dictionary
    ↓
key → value

Nested Dictionary
    ↓
key → dictionary → fields
```

This became the foundation for the Prompt Manager project.

---

## 5. Control Flow

Covered:

- `if`
- `elif`
- `else`
- `for`
- `while`
- `break`
- `continue`
- `range()`
- `enumerate()`
- `zip()`

These concepts were applied directly to the CLI application.

---

## 6. Comprehensions

Practiced:

- List comprehensions
- Dictionary comprehensions

Example:

```python
matches = [
    name
    for name in prompt_dictionary
    if user_input in name
]
```

Dictionary comprehension:

```python
category_wise_prompts = {
    category: []
    for category in categories
}
```

---

## 7. Functions

Although functions were initially planned for a later stage, I introduced and used them during Phase 1.

Covered:

- Defining functions
- Parameters
- Arguments
- Return values
- `None`
- Type hints
- Separating responsibilities
- Calling functions from a main controller

The project uses functions to keep application control separate from business logic.

---

# 🤖 Main Project — Prompt Manager CLI

## Problem

AI engineering workflows often involve reusable system prompts.

Instead of keeping prompts scattered across files, I built a CLI application that allows prompts to be managed from one place.

The application stores prompt metadata and provides CRUD-style operations.

---

# ✨ Features

The Prompt Manager supports:

```text
1. Create Prompt
2. List Prompts
3. Search Prompt
4. Filter by Category
5. Update Prompt
6. Delete Prompt
7. Exit
```

---

## 📦 Prompt Data Model

Each prompt follows this structure:

```python
{
    "name": "coder_python",
    "category": "coding",
    "system_prompt": "You are a senior Python engineer.",
    "version": "1.2.0",
    "is_active": True,
}
```

The complete collection is represented using nested dictionaries.

---

# 🔨 Features Implemented

## Create Prompt

Implemented:

- User input
- Input cleaning
- Duplicate-name validation
- Category validation
- Empty-value validation
- Version validation
- Boolean conversion
- Dictionary insertion

---

## List Prompts

Implemented:

- Dictionary iteration
- `enumerate()`
- Prompt information display
- Active/inactive status
- Prompt counting

---

## Search Prompts

Implemented:

- Exact searching
- Partial/substring searching
- List comprehensions
- Zero-match handling
- Multiple-match handling
- User selection from multiple matches

Example:

```text
Input:
coder

Possible result:
coder_python
```

---

## Filter by Category

Implemented:

- Unique category extraction using sets
- Category-based dictionary structures
- Nested dictionary filtering
- Displaying matching prompts

Example:

```text
coding
research
support
utility
general
```

---

## Update Prompt

Implemented:

- Prompt selection
- Field selection
- Updating multiple fields
- Dictionary-based update tracking
- Original vs updated data comparison
- Temporary working data

---

## Delete Prompt

Implemented:

- Prompt selection
- Deletion confirmation
- Dictionary deletion
- Invalid prompt handling

---

# 🏗️ Project Architecture

The project was separated into multiple modules rather than keeping everything inside one file.

```text
prompt_manager/
│
├── src/
│   └── prompt_manager/
│       ├── __init__.py
│       │
│       └── prompt_cli/
│           ├── main.py
│           ├── core_logic.py
│           └── shared_data.py
│
├── tests/
│
├── README.md
├── .gitignore
├── pyproject.toml
├── uv.lock
└── .python-version
```

### Responsibility

```text
main.py
    │
    └── Application / menu control
            │
            ▼
core_logic.py
    │
    └── CRUD / business logic
            │
            ▼
shared_data.py
    │
    └── Shared prompt data
```

---

# 🧠 What I Learned From the Project

The main learning objective was to move from:

```text
Learning Python syntax
```

to:

```text
Understanding a problem
        ↓
Choosing data structures
        ↓
Writing Python logic
        ↓
Validating input
        ↓
Handling user interaction
        ↓
Separating responsibilities
        ↓
Building a working application
```

This project helped me understand that Python fundamentals become much more useful when combined into an actual application.

---

# 🛠️ Engineering Practices

The project continues the engineering practices learned during Phase 0.

### Development

- `uv`
- Virtual environments
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- Terminal
- VS Code

### Version Control

- Git
- GitHub
- Meaningful commits
- `.gitignore`

### Project Organization

- `src/` layout
- Python modules
- Separation of application and business logic
- README documentation

---

# ⚠️ Known Technical Debt

The project is **functionally complete**, but it is not being treated as perfectly production-ready.

Known cleanup areas include:

- Improving type hints
- Reducing unnecessary complexity
- Improving validation consistency
- Handling additional edge cases
- Reducing duplicated logic
- Improving shared-state/data ownership
- Removing unnecessary imports and variables
- Improving search/update logic
- Improving overall readability

These are intentionally treated as **technical debt and future refactoring opportunities**.

The purpose of Phase 1 was primarily to demonstrate understanding and practical application of Python fundamentals.

---

# 📚 Phase 1 Knowledge Checklist

| Topic                     | Status |
| ------------------------- | ------ |
| Variables                 | ✅      |
| Python Data Types         | ✅      |
| Type Conversion           | ✅      |
| Strings                   | ✅      |
| Lists                     | ✅      |
| Tuples                    | ✅      |
| Sets                      | ✅      |
| Dictionaries              | ✅      |
| Nested Data               | ✅      |
| Conditions                | ✅      |
| Loops                     | ✅      |
| `range()`                 | ✅      |
| `enumerate()`             | ✅      |
| `zip()`                   | ✅      |
| List Comprehensions       | ✅      |
| Dictionary Comprehensions | ✅      |
| Functions                 | ✅      |
| Modules                   | ✅      |
| CLI Application           | ✅      |
| Input Validation          | ✅      |
| CRUD Logic                | ✅      |
| `uv` Workflow             | ✅      |
| Git/GitHub                | ✅      |
| Project Structure         | ✅      |

---

# 🚀 What's Next?

After completing the Phase 1 evaluation, the next stage is:

## Phase 2 — Functions + JSON + Files + Error Handling

The next phase will build on the existing Python foundation and introduce:

- Deeper function design
- Parameters
- Return values
- Scope
- Reusable functions
- JSON
- Reading and writing files
- Data persistence
- Exception handling
- `try/except`
- `finally`
- Custom errors where appropriate
- Better project architecture

The same learning philosophy will continue:

> **20% Concepts → 80% Implementation**

The projects will continue to evolve toward real **AI Engineering → Agentic AI Engineering** workflows.

---

# 🎯 Long-Term Roadmap

```text
Python Fundamentals
        ↓
Functions + Files + Error Handling
        ↓
HTTP / APIs
        ↓
Pydantic
        ↓
LLM APIs
        ↓
Async + Streaming
        ↓
FastAPI
        ↓
PostgreSQL
        ↓
AI Assistant + Memory
        ↓
RAG
        ↓
Tool Calling
        ↓
Agents
        ↓
LangChain
        ↓
LangGraph
        ↓
Production AI Systems
```

---

## 👨‍💻 Learning Philosophy

This repository is not intended to be a collection of copied tutorials.

It represents my progression from:

> **Python learner → Python developer → AI Engineer → Agentic AI Engineer**

The focus is on **understanding, implementing, debugging, and building**.