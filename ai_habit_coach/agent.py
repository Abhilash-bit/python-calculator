"""
agent.py
Simple LangGraph wrapper & decomposition function for MVP.
Replace the placeholder logic with actual LangGraph calls later.
"""

from typing import List, Dict, Optional

def decompose_goal(goal: str, user_info: Optional[str] = None) -> List[Dict]:
    """
    Return a list of 2-3 S.M.A.R.T. task dicts for the given goal.
    Each dict: {"id": int, "task": str, "details": str, "completed": False}
    This is an MVP placeholder. Replace with LangGraph-based reasoning later.
    """
    g = goal.lower() if goal else ""
    info = user_info.lower() if user_info else ""

    tasks = []
    if "sleep" in g or "energy" in g:
        tasks = [
            {"id": 1, "task": "Reduce screen time by 30 minutes before bed", "details": "No screens 30 mins before bed", "completed": False},
            {"id": 2, "task": "Go to bed 15 minutes earlier each night", "details": "Adjust bedtime by 15 minutes nightly", "completed": False},
            {"id": 3, "task": "Avoid caffeine after 2 PM", "details": "No caffeinated drinks after 2 PM", "completed": False},
        ]
        if "night owl" in info:
            # prioritize bedtime routine
            tasks[0]["task"] = "Establish a consistent bedtime routine"
            tasks[0]["details"] = "Choose wind-down activities for 30 minutes before bed"
    else:
        tasks = [
            {"id": 1, "task": "Walk 20 minutes daily", "details": "Walk at a comfortable pace each day", "completed": False},
            {"id": 2, "task": "Drink 8 cups water daily", "details": "Track water consumption", "completed": False},
            {"id": 3, "task": "Get 7-8 hours of sleep", "details": "Aim for consistent sleep schedule", "completed": False},
        ]
    return tasks

def update_goal_state(goal_state: dict, completed_task_id: int) -> dict:
    """
    Minimal state update: mark the task as completed in the goal_state dict.
    In a full implementation, this should update LangGraph's nodes/state.
    """
    for t in goal_state.get("tasks", []):
        if t["id"] == completed_task_id:
            t["completed"] = True
    return goal_state
