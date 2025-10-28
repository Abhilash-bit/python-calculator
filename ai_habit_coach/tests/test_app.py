from agent import decompose_goal
# test session-like behavior via dict manipulation

def test_mark_task_completed_updates_state():
    tasks = decompose_goal("Improve my sleep")
    goal_state = {"goal": "Improve my sleep", "tasks": tasks}
    # simulate marking task id 1 as completed
    for t in goal_state["tasks"]:
        if t["id"] == 1:
            t["completed"] = True
    assert any(t["completed"] for t in goal_state["tasks"])
