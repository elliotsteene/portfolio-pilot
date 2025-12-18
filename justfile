check:
    @. ./.claude/scripts/run_silent.sh && run_silent "Ruff check passed" "uv run ruff check --force-exclude --fix"
    @. ./.claude/scripts/run_silent.sh && run_silent "Ruff format passed" "uv run ruff format --force-exclude"
    @. ./.claude/scripts/run_silent.sh && run_silent "Pyrefly check passed" "uv run pyrefly check"

tests:
    @. ./.claude/scripts/run_silent.sh && run_silent_with_test_count "Pytests passed successfully" "uv run pytest -x"

check-test: check tests
    @echo "✓ Check Test complete"

run:
    @ PYTHONASYNCIODEBUG=1 && uv run src/main.py

hl-sync:
    @. ./.claude/scripts/run_silent.sh && run_silent "Thought sync successful" "humanlayer thoughts sync"

hl-status:
    @ humanlayer thoughts status
