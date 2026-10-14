# Semester 7 AI & ML Practicals

This repository contains practical implementations and assignments for Semester 7 **Artificial Intelligence** and **Machine Learning** courses.

## Project Structure

```
sem-7_practica_backup/
├── AI/                     # Artificial Intelligence Practicals
│   ├── pr1/ - pr6/        # Python implementations (Tic-Tac-Toe, Search Algorithms, etc.)
│   ├── pr7/ - pr11/       # Prolog implementations (Knowledge representation, rules, etc.)
│   └── pr12/ - pr13/      # NLP and text processing practicals (Python / NLTK)
└── ML/                     # Machine Learning Practicals
    ├── pr1/ - pr12/       # Python implementations (Statistics, Supervised & Unsupervised learning)
```

## Branch Strategy

- **`main`**: Original base branch.
- **`dev`**: Active working and development branch.

## Safe Git Workflow

To ensure changes are reviewed before pushing and to protect `main`:

### Option 1: Using VS Code Tasks
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and type **Tasks: Run Task**.
2. Select **Git: Review Changes (Status & Diff)** to review what changed.
3. Select **Git: Safe Commit & Push to dev** and enter your commit message when prompted.

### Option 2: Using the Git Helper Script
Run the PowerShell helper script from the terminal:
```powershell
.\git-sync.ps1
```
Or with a message directly:
```powershell
.\git-sync.ps1 -Message "Your commit message"
```

### Option 3: Manual Git Commands
```bash
# Verify you are on branch dev
git checkout dev

# Check status
git status

# Stage intended changes
git add .

# Commit with a meaningful message
git commit -m "Your descriptive commit message"

# Push to dev branch on GitHub
git push origin dev
```
