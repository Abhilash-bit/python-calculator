# app.py
import streamlit as st
from agent import decompose_goal, update_goal_state

st.set_page_config(page_title="AI Habit/Wellness Coach - MVP")

st.title("AI Habit/Wellness Coach (MVP)")

# Input form
with st.form(key="goal_form"):
    goal_text = st.text_input("Enter a high-level wellness goal:", placeholder="e.g., Improve my sleep and energy")
    user_info = st.text_input("Optional: tell us about your routine (e.g., 'I am a night owl')", "")
    submit = st.form_submit_button("Generate Plan")

if submit and goal_text.strip():
    tasks = decompose_goal(goal_text, user_info)
    # store goal state
    st.session_state["goal_state"] = {"goal": goal_text, "tasks": tasks}
    st.success("Plan generated — see tasks below.")

if "goal_state" in st.session_state:
    st.subheader("Your Weekly Tasks")
    tasks = st.session_state["goal_state"]["tasks"]
    for t in tasks:
        # Using key with task id to keep unique widget keys
        checked = st.checkbox(label=t["task"], value=t.get("completed", False), key=f"task_{t['id']}")
        # update session state immediately
        for idx, _t in enumerate(st.session_state["goal_state"]["tasks"]):
            if _t["id"] == t["id"]:
                st.session_state["goal_state"]["tasks"][idx]["completed"] = checked

    # Simple progress display
    completed = sum(1 for x in st.session_state["goal_state"]["tasks"] if x["completed"])
    total = len(st.session_state["goal_state"]["tasks"])
    st.progress(completed / total if total > 0 else 0)
    st.write(f"{completed} of {total} tasks completed")

    # Optional: call update_goal_state (placeholder for LangGraph update)
    if st.button("Save progress/update agent"):
        # call a function to sync/update agent state
        st.session_state["goal_state"] = update_goal_state(st.session_state["goal_state"], completed_task_id=None)  # placeholder
        st.info("Progress saved (MVP).")
