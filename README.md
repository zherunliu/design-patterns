add file `.git/hooks/post-commit` to auto-format

```bash
#!/bin/sh
echo "[post-commit] Running black formatter..."
black .

if [ $? -eq 0 ]; then
  echo "[post-commit] Black finished successfully."
else
  echo "[post-commit] Black failed!"
  exit 1
fi

git add -u
if ! git diff --cached --quiet; then
    git commit --amend --no-edit
    echo "[post-commit] Commit amended with black changes."
else
    echo "[post-commit] No changes after black."
fi
```

add and view permission

```bash
chmod +x .git/hooks/post-commit
ls -l .git/hooks/post-commit
```
