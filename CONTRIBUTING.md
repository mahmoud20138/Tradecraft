# Contributing to Skills Collection

Thank you for your interest in contributing!

## Adding a New Skill

1. **Find the right category** — place your `.md` file in the appropriate subdirectory under `classified/`
2. **Follow the naming convention** — use lowercase, hyphen-separated names (e.g., `my-new-skill.md`)
3. **Include metadata** — add an entry to `skills_index.json` with name, path, kind, category, status, tags, related_skills, lines, and has_code
4. **Update the catalog** — add an entry to `SKILLS_CATALOG.md` in the appropriate category section
5. **Test your skill** — verify it works with your AI assistant before submitting

## Skill File Guidelines

- Start with a clear title and description
- Include usage instructions and trigger keywords
- Add executable code blocks where applicable (mark with language identifier)
- Reference related skills using their exact names
- Keep skills self-contained and focused

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-new-skill`)
3. Make your changes
4. Ensure `skills_index.json` and `SKILLS_CATALOG.md` are updated
5. Submit a pull request with a clear description

## Reporting Issues

Use GitHub Issues to report:
- Broken or outdated skills
- Incorrect categorization
- Missing related skill references
- Suggestions for new skills
