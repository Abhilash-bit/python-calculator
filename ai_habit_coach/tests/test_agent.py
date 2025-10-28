from agent import decompose_goal

def test_sleep_goal_generates_three_tasks():
    tasks = decompose_goal("Improve my sleep")
    assert isinstance(tasks, list)
    assert len(tasks) == 3

def test_night_owl_personalization():
    tasks = decompose_goal("Improve my sleep", "I am a night owl")
    assert any("bedtime" in t["task"].lower() or "bedtime" in t["details"].lower() or "routine" in t["task"].lower() for t in tasks)
