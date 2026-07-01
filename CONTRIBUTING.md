# Contributing to Living on Linux

Thank you for considering contributing to Living on Linux! This document provides guidelines for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Guidelines](#development-guidelines)
- [Project Structure](#project-structure)
- [Documentation Standards](#documentation-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Adding New Projects](#adding-new-projects)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful in all interactions and follow professional standards of conduct.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- System information (OS, Python version, dependencies)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

- Use a clear and descriptive title
- Describe the proposed feature and its benefits
- Explain why this enhancement would be useful
- Include examples if applicable

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make your changes following our guidelines
4. Test your changes thoroughly
5. Update documentation if needed
6. Submit the pull request

## Development Guidelines

### Code Style

- **Python**: Follow PEP 8 style guidelines
- **Indentation**: 4 spaces (no tabs)
- **Line length**: Maximum 88 characters (Black formatter default)
- **Naming**: Use descriptive variable and function names
- **Comments**: Add clear comments for complex logic

### Code Quality

- **Minimal dependencies**: Prefer built-in libraries over external packages
- **Error handling**: Implement comprehensive error checking
- **User feedback**: Provide clear status messages and progress indicators
- **Security**: Handle user input safely and avoid command injection
- **Performance**: Optimize for minimal resource usage

### Git Workflow

- Use descriptive commit messages
- Follow conventional commit format when possible:
  - `feat: add new feature`
  - `fix: resolve bug`
  - `docs: update documentation`
  - `refactor: improve code structure`
- Keep commits atomic and focused
- Rebase your branch before submitting PRs

## Project Structure

```
living-on-linux/
├── README.md              # Main project documentation
├── CONTRIBUTING.md        # This file
├── LICENSE               # Project license
├── .github/              # GitHub workflows and templates
│   ├── workflows/        # CI/CD workflows
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                 # Project documentation
│   ├── setup.md         # Setup instructions
│   ├── development.md   # Development guidelines
│   └── best-practices.md # Best practices
├── scripts/             # Utility scripts
│   ├── setup.sh         # Project setup script
│   └── lint.sh          # Code linting script
└── projects/            # Individual microprojects
    ├── project-name/
    │   ├── README.md     # Project-specific documentation
    │   ├── setup.sh      # Installation/setup script
    │   ├── main.py       # Main application/script
    │   ├── requirements.txt # Python dependencies
    │   ├── tests/        # Unit tests
    │   ├── docs/         # Additional documentation
    │   └── assets/       # Project assets
    └── another-project/
```

## Documentation Standards

### README Files

Each project must include a comprehensive README with:

- **Project description**: What it does and why it's useful
- **Installation**: Step-by-step setup instructions
- **Usage**: Clear examples and command-line options
- **Configuration**: How to customize the project
- **Troubleshooting**: Common issues and solutions
- **Contributing**: How others can contribute to the project

### Code Documentation

- **Module docstrings**: Describe what the module does
- **Function docstrings**: Explain parameters, return values, and behavior
- **Inline comments**: Explain complex logic or non-obvious code
- **Type hints**: Use Python type hints where helpful

### Documentation Format

- Use Markdown format
- Include code examples with syntax highlighting
- Use clear, descriptive headings
- Include screenshots or diagrams when helpful

## Testing

Run the repo-native verification command:

```bash
./scripts/test.sh
```

### Test Structure

```
projects/project-name/
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_utils.py
│   └── fixtures/
│       └── sample_data.json
└── requirements-dev.txt
```

### Test Guidelines

- Write tests for all new functionality
- Use pytest framework
- Include both unit tests and integration tests
- Test edge cases and error conditions
- Mock external dependencies when appropriate
- Ensure tests run quickly and reliably

### Test Requirements

- Tests must pass before submitting PRs
- Maintain good test coverage
- Tests should be independent and repeatable
- Use descriptive test names

## Repo Health Notes

- The current repo-native validation command is `./scripts/test.sh`.
- Generated local diagnostics are written to `.devstudio/runtime/` and are intentionally ignored from source control.
- CI is not currently wired yet; add a workflow here when it is introduced so validation commands can be documented and replaced as appropriate.

## Repo Lifecycle Notes

- This repository is currently **active and retained** in the operating-systems wrapper.
- No consolidation, archival, or migration is planned yet.
- If a future phase requires changing this posture, raise a follow-up issue with:
  - decision owner
  - target destination or target archive location
  - migration or deprecation checklist
  - exact date for completion


## Submitting Changes

### Before Submitting

1. Run the linting and formatting tools
2. Run the test suite
3. Update documentation if needed
4. Ensure your branch is up to date with main

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code is completed
- [ ] Code is commented, particularly in hard-to-understand areas
- [ ] Corresponding changes to documentation have been made
- [ ] Changes generate no new warnings
- [ ] New and existing unit tests pass locally

### Pull Request Description

Include in your PR description:

- Summary of changes made
- Related issue number (if applicable)
- Screenshots for visual changes
- Testing instructions

## Adding New Projects

### Project Requirements

Before adding a new project, ensure it:

- Solves a specific, well-defined problem
- Follows the microproject philosophy (focused, lightweight)
- Includes comprehensive documentation
- Has minimal dependencies
- Is tested and working

### Project Setup Checklist

- [ ] Create project directory under `projects/`
- [ ] Add comprehensive README.md
- [ ] Include setup/installation script
- [ ] Add main application code
- [ ] Create requirements.txt if needed
- [ ] Add unit tests
- [ ] Include documentation in docs/
- [ ] Add assets in assets/ if needed
- [ ] Update main README with project entry
- [ ] Test on clean system if possible

### Project Naming

- Use lowercase with hyphens for project names
- Choose descriptive names that clearly indicate the project's purpose
- Avoid generic names that could be confused with existing tools

## Getting Help

- Check existing issues and discussions
- Search the documentation
- Ask questions in issues (use "question" label)
- Be specific about your problem and what you've tried

## Recognition

Contributors will be recognized in:

- Project README files
- Changelog entries
- Special contributor sections

Thank you for contributing to Living on Linux!
