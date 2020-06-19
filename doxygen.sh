#!/bin/bash

git remote set-url origin https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/TE-/${GITHUB_REPOSITORY}.git

cd docs/html

git log -1
last_commit_message="$(git log -1 | tail -1)"
echo $last_commit_message

if [ -z "$(echo $last_commit_message | grep updater)" ]; then
    git log -1 | head -1 > last_commit.txt
    cat last_commit.txt
    git add .
    git commit -m '[updater] update last commit'
    git push origin gh-page
else
    echo "nothing updated"
fi
