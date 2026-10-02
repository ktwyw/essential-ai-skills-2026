# Git and GitHub

## Why it matters

Git gives you version control: a full history of every change, with the ability to compare versions and undo mistakes. GitHub hosts that history online for sharing and collaboration. In the AI era this matters even more, because AI agents edit files directly, and you need a way to review and reverse what they did.

## Learn first

```bash
git init                      # start tracking a folder
git status                    # see what changed
git add notes.md              # stage a change
git commit -m "Add notes"     # save a snapshot with a message
git log --oneline             # see history
git diff                      # see exact changes
git clone <url>               # copy a repository from GitHub
git push                      # send commits to GitHub
git pull                      # get the latest changes
```

Then learn **branches** (`git switch -c new-idea`) and **pull requests** on GitHub.

## Tips for becoming proficient

- **Put your own notes under version control from day one**, even if no one else will see them.
- **Commit small, focused changes** with messages that explain *why*, not just *what*.
- **Practice the recovery moves on purpose:** undo a change, restore an old version, and resolve a simple merge conflict.
- **Commit before letting an AI agent edit your files**, so you can review its changes with `git diff` and roll back if needed.
- **Never commit secrets.** Use a `.gitignore` file (this repo has one) and keep API keys out of your code.

## Practice

1. Fork this repository on GitHub and clone it to your computer.
2. Create a file `my-notes.md`, commit it, and push it to your fork.
3. Make a change, then undo it with `git restore`.
4. Create a branch, edit a file, and open a pull request against your own fork.

## Resources

- Pro Git book (free): https://git-scm.com/book
- GitHub documentation: https://docs.github.com
