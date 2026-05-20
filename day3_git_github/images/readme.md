# Coastal Git Practice

This repository demonstrates a complete Git and GitHub workflow including:

- Initializing a repository
- Adding and committing files
- Connecting to GitHub
- Creating branches
- Pushing branches
- Pulling changes
- Merging branches
- Resolving merge conflicts

---

# Step 1: Initialize Git Repository

```bash
git init
```

---

# Step 2: Add Files

```bash
git add .
```

Check repository status:

```bash
git status
```

---

# Step 3: Commit Files

```bash
git commit -m "first file"
```

---

# Step 4: Rename Default Branch to Main

```bash
git branch -M main
```

---

# Step 5: Connect Local Repository to GitHub

```bash
git remote add origin https://github.com/tarun-coastal/coastalgitpractice.git
```

Verify remote:

```bash
git remote -v
```

---

# Step 6: Push Main Branch to GitHub

```bash
git push -u origin main
```

---

# Branch Workflow

## Create Branch1

```bash
git checkout -b branch1
```

---

## Add Files in Branch1

```bash
git add .
```

Commit changes:

```bash
git commit -m "added example2"
```

Push branch:

```bash
git push --set-upstream origin branch1
```

---

# Create Branch2

```bash
git checkout -b branch2
```

---

## Add Files in Branch2

```bash
git add .
```

Commit changes:

```bash
git commit -m "added example3"
```

Push branch:

```bash
git push --set-upstream origin branch2
```

---

# Switching Between Branches

Switch to main branch:

```bash
git checkout main
```

Switch to branch1:

```bash
git checkout branch1
```

Switch to branch2:

```bash
git checkout branch2
```

---

# Pull Latest Changes from Main

```bash
git pull origin main
```

---

# Merge Main Branch into Branch1

```bash
git checkout branch1
git merge origin/main
```

---

# Resolve Merge Conflicts

Check status:

```bash
git status
```

After manually resolving conflicts:

```bash
git add .
git commit -m "resolved merge conflict"
```

Push updated branch:

```bash
git push
```

---

# Useful Git Commands

## View All Branches

```bash
git branch
```

## Check Repository Status

```bash
git status
```

## View Commit History

```bash
git log
```

## Abort Merge Process

```bash
git merge --abort
```

## Remove Staged File

```bash
git rm --cached <file-name>
```

---

# Common Errors and Fixes

## Error

```bash
fatal: pathspec 'README.md' did not match any files
```

### Fix

Create the file first or use:

```bash
git add .
```

---

## Error

```bash
error: remote origin already exists.
```

### Fix

Remove existing remote and add again:

```bash
git remote remove origin
git remote add origin <repository-url>
```

---

## Error

```bash
fatal: The current branch has no upstream branch
```

### Fix

```bash
git push --set-upstream origin <branch-name>
```

---

# Repository Link

Repository URL:

```bash
https://github.com/tarun-coastal/coastalgitpractice.git
```
