# Contributing to Shownamer
Thank you for considering contributing to **Shownamer**.  
Contributions are welcome, whether it is fixing a bug, adding a feature, or improving documentation.  

This document explains the rules and workflow so that contributions stay consistent.  

---

### Getting Started
1. Fork the repository.  
2. Create a new branch for your work:  
   ```bash
   git checkout -b feat/newfeature
   ```
3. Make your changes.  
4. Commit using **Conventional Commits** (see below).  
5. Push your branch and open a Pull Request (PR).  

---

### Commit Message Rules (Conventional Commits)

We use [Conventional Commits](https://www.conventionalcommits.org/) to keep history readable and changelogs easy to generate.  

#### Format
```
<type>(optional scope): <brief summary (lowercase)>
```

#### Common Types
- **feat:** a new feature  
- **fix:** a bug fix  
- **docs:** documentation changes only  
- **refactor:** code change that does not add features or fix bugs  
- **test:** adding or fixing tests  
- **chore:** maintenance (build, dependencies, etc.) 
- **init:** add new file(s)

### Examples
```
feat: add optional year field to distinguish shows with same name
fix: handle titles with '0' correctly
docs: update README with installation instructions
init(docs): add header image
```

### Avoid
- `wip: working on something`  
- `update: fixed stuff`  
- Redundant prefixes (e.g., `feat: new feature added`)  

Commit messages should be clear, concise, and meaningful.  

## Code and Project Guidelines
- Use proper & brief comments while coding (lowercase)
- Test your changes before submitting a PR.  
- Keep commits focused; one logical change per commit.  
- Do not modify unrelated parts of the repo (eg, The header image, badges, or README style)  

## Pull Request Guidelines
- Reference related issues in your PR description, e.g., `Fixes #1`.  
- Explain what your change does and why.  
- Keep PRs small and focused so they are easier to review and merge.  
- Be respectful and collaborative in discussions.  

>[!TIP]
>If in doubt about something, open an issue first to discuss before coding. Happy Coding!
