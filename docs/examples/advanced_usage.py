# Multi-step code refactoring
reasoning_engine = ReasoningEngine(agent)
plan = reasoning_engine.plan_code_changes(
    "Refactor this class to use dependency injection",
    codebase_context
)

results = reasoning_engine.execute_plan(plan, file_manager, editor)
