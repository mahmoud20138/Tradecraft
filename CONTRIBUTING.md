# Contributing to Claude Skills Collection

Thank you for your interest in contributing!

## Adding a New Skill

1. **Create the skill directory** at `plugins/claude-skills-collection/skills/<skill-name>/` using lowercase, hyphen-separated names (e.g., `my-new-skill`).
2. **Create `SKILL.md`** inside that directory with YAML frontmatter:
   ```markdown
   ---
   name: my-new-skill
   description: One-line description that Claude uses to decide when to auto-invoke this skill.
   ---

   # My New Skill

   Skill content...
   ```
3. **Write the content** — include usage instructions, trigger keywords, and executable code blocks (marked with a language identifier) where applicable.
4. **Keep skills focused** — one skill, one topic. Cross-reference related skills by their exact name.
5. **Test locally**:
   ```shell
   claude --plugin-dir ./plugins/claude-skills-collection
   # inside Claude:
   /claude-skills-collection:my-new-skill
   ```

## Skill File Guidelines

- Start with a clear title and purpose statement
- The `description` frontmatter field should be a single line; Claude uses it to decide when to invoke the skill model-side
- Add executable code blocks with language identifiers (e.g., ` ```python `)
- Reference related skills using their exact names
- Keep skills self-contained — avoid cross-file imports

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-new-skill`)
3. Make your changes
4. Validate the marketplace (`claude plugin validate .`)
5. Submit a pull request with a clear description

## Reporting Issues

Use GitHub Issues to report:
- Broken or outdated skills
- Incorrect frontmatter or missing descriptions
- Suggestions for new skills
