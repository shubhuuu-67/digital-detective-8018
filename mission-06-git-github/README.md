# Mission 6 - Git and GitHub

## 1. Task / objective
Practice the core Git workflow, create a separate branch to update the root README, open a Pull Request on GitHub, and write a glossary of common Git commands.

## 2. Work completed

**Task 6.1 - Understand the basic Git workflow**

| Git operation | What it does in your own words |
| :--- | :--- |
| Check repository status (`git status`) | Shows which branch I am on and lists any modified, new, or staged files in my working folder. |
| Stage selected changes (`git add`) | Selects specific modified or new files and places them in the staging area so they are ready for the next commit. |
| Create a commit (`git commit`) | Saves a permanent snapshot of everything currently in the staging area along with a descriptive message. |
| View commit history (`git log`) | Displays the list of past commits in order, showing each commit ID, author, date, and message. |

**Difference between staging and committing:** Staging (`git add`) is like packing items into a box before sealing it. It lets you choose which file changes belong together without including unfinished edits. Committing (`git commit`) seals that box and records it permanently in the repository's history.

**Task 6.2 - Create and use a branch**
Created a new branch named `update-about`, added a **My Learning** section to the root `README.md` describing three things learned so far, staged and committed the update, and pushed the `update-about` branch to GitHub.

**Task 6.3 - Create a Pull Request**
Opened a Pull Request on GitHub from `update-about` into `main` with a short summary of the README update, reviewed the diff, merged it into `main`, and pulled the updated `main` branch back down to my local computer.

- **Pull Request status:** Merged into `main` (visible in the repository's Pull Requests tab on GitHub).
- **What a branch and Pull Request are and why they are useful:** A branch is an independent line of development where you can make edits or test features without affecting the main working code. A Pull Request is a formal request to review and merge changes from one branch into another. Together, they let multiple people work on different parts of the same project at the same time, discuss code changes, and catch mistakes before updating the main project.

**Task 6.4 - Build your Git command glossary**

- **Initialise a repository (`git init`):** Turns a normal local folder into a new Git repository so version tracking can begin.
- **Check status (`git status`):** Lists which files have been changed, staged, or left untracked on the current branch.
- **Stage changes (`git add`):** Adds file changes to the staging area to prepare them for the next commit.
- **Commit changes (`git commit`):** Records a saved snapshot of staged changes in the local repository history with a message.
- **View history (`git log`):** Shows a chronological log of previous commits made in the repository.
- **Create or list branches (`git branch`):** Lists existing local branches or creates a new branch name.
- **Switch branches (`git checkout` / `git switch`):** Moves your working directory from one branch to another.
- **Publish changes (`git push`):** Uploads local commits and branches to a remote repository like GitHub.
- **Retrieve remote changes (`git pull`):** Downloads and merges the latest commits from GitHub into your current local branch.

## 3. Commands / tools used
- `git checkout -b update-about` to create and switch to the new branch.
- `git status`, `git add`, `git commit`, and `git push` to stage, commit, and publish both the branch and mission files.
- `git checkout main` and `git pull` to return to `main` and bring the merged Pull Request changes onto my computer.
- `git log --oneline -n 6` to inspect recent commit history.
- GitHub web interface to open, review, and merge the Pull Request.

## 4. My understanding
Git and GitHub separate local version tracking from online collaboration. Using branches keeps `main` clean while new edits are being written, and Pull Requests provide a clear checkpoint to review changes before merging them in. Checking `git status` before staging and committing also prevents accidentally uploading the wrong files.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-06-git-github/README.md` (Git workflow table, branch and PR notes, and command glossary)
- Root `README.md` (updated with the `My Learning` section via the `update-about` branch and Pull Request)

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Status: Committed and pushed to the `main` branch on GitHub.