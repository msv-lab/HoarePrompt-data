# Check if a commit message is provided
if [ -z "$1" ]; then
  echo "Usage: $0 \"commit message\""
  exit 1
fi

# Add changes (modify '.' if you want to limit to specific files or directories)
git add .

# Commit changes with the provided message
git commit -m "$1"

# Push to the current branch (assuming origin remote and current branch)
current_branch=$(git branch --show-current)
echo "Pushing changes to branch: $current_branch"
git push origin "$current_branch"
