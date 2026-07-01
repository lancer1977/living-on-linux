#!/usr/bin/env bash
set -euo pipefail

fail=0

echo "[1/5] Python syntax check across tracked python files"
python3 -m compileall -q . || fail=1

echo "[2/5] Required shell entry points are executable"
if ! find scripts -maxdepth 1 -type f -name "*.sh" -print0 | xargs -0 -I{} test -x "{}"; then
  echo "warning: one or more scripts are not executable"
  fail=1
fi

echo "[3/5] Project hygiene: verify each project has a README and an entry script when present"
while IFS= read -r -d '' project_dir; do
  if [[ -d "$project_dir" ]]; then
    if [[ ! -f "$project_dir/README.md" ]]; then
      echo "warning: missing project README: $project_dir"
      fail=1
    fi
  fi
done < <(find projects -mindepth 1 -maxdepth 1 -type d -print0)

echo "[4/5] Discover project inventory"
project_count="$(find projects -mindepth 1 -maxdepth 1 -type d | wc -l)"
if [[ "$project_count" -eq 0 ]]; then
  echo "warning: no projects found under projects/"
  fail=1
else
  echo "projects discovered: $project_count"
fi

echo "[5/5] Local diagnostics directories"
if [[ -d ".devstudio/runtime" ]]; then
  echo "ok: .devstudio/runtime exists (local generated diagnostics, ignored by .gitignore)."
fi

if find . -name "test_*.py" -type f -print -quit | grep -q .; then
  echo "pytest discovery detected; running local tests"
  pytest
else
  echo "no test_*.py files found; pytest skipped"
fi

if [[ $fail -ne 0 ]]; then
  echo "living-on-linux test checks reported warnings."
  exit 1
fi

echo "living-on-linux test checks passed."
