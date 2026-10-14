<#
.SYNOPSIS
    Safe Git review, commit, and push helper script for the 'dev' branch.
.DESCRIPTION
    Ensures safe review before committing and pushing changes to GitHub.
    Prevents accidental pushes to 'main'.
.PARAMETER Message
    Commit message. If omitted, prompts interactively.
#>
param (
    [string]$Message
)

$ErrorActionPreference = "Stop"

Write-Host "`n==========================================" -ForegroundColor Cyan
Write-Host "       Git Safe Sync Helper (dev)         " -ForegroundColor Cyan
Write-Host "==========================================`n" -ForegroundColor Cyan

# 1. Check current branch
$currentBranch = (git branch --show-current).Trim()
Write-Host "[1/5] Current branch: $currentBranch" -ForegroundColor Yellow

if ($currentBranch -ne "dev") {
    Write-Host "[WARNING] You are currently on branch '$currentBranch', NOT 'dev'!" -ForegroundColor Red
    Write-Host "Switching to 'dev' branch to protect '$currentBranch'..." -ForegroundColor Yellow
    git checkout dev
    $currentBranch = (git branch --show-current).Trim()
    if ($currentBranch -ne "dev") {
        Write-Error "Failed to switch to 'dev' branch. Aborting."
        exit 1
    }
}

# 2. Review changed files
Write-Host "`n[2/5] Inspecting pending changes..." -ForegroundColor Yellow
$status = git status --short
if (-not $status) {
    Write-Host "Working tree is clean. No changes detected to commit." -ForegroundColor Green
    Write-Host "Sync status with remote:"
    git status
    exit 0
}

Write-Host "The following files have changes:" -ForegroundColor Cyan
git status --short
Write-Host ""

# 3. Prompt for commit message if not provided
if (-not $Message -or $Message.Trim() -eq "") {
    $Message = Read-Host "Enter commit message (or press Ctrl+C to abort)"
    if (-not $Message -or $Message.Trim() -eq "") {
        Write-Host "No commit message provided. Aborted without making changes." -ForegroundColor Red
        exit 1
    }
}

# 4. Stage and commit
Write-Host "`n[3/5] Staging files..." -ForegroundColor Yellow
git add .

Write-Host "[4/5] Committing changes with message: '$Message'..." -ForegroundColor Yellow
git commit -m "$Message"

# 5. Push to GitHub origin dev
Write-Host "`n[5/5] Pushing to origin dev..." -ForegroundColor Yellow
git push origin dev

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[SUCCESS] Successfully pushed changes to GitHub!" -ForegroundColor Green
    Write-Host "View your branch online at: https://github.com/1mayurchaudhary9/AI-ML-/tree/dev`n" -ForegroundColor Cyan
} else {
    Write-Host "`n[ERROR] Failed to push changes. Please check network/credentials.`n" -ForegroundColor Red
    exit $LASTEXITCODE
}
