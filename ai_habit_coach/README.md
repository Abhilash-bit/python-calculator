\# Iteration 1 – AI Habit / Wellness Coach



\## Overview

The \*\*AI Habit / Wellness Coach\*\* is a Streamlit application that helps users turn high-level wellness goals into small, actionable weekly habits.  

It uses \*\*LangGraph-style reasoning\*\* for goal decomposition (`agent.py`) and \*\*Streamlit\*\* for the interactive user interface (`app.py`).



---



\## Completed User Stories



\###  US1: Initial Goal Decomposition

\- Users can enter a high-level goal (e.g., “Improve my sleep”).

\- The system generates 2–3 S.M.A.R.T. tasks (e.g., reduce screen time, go to bed earlier).

\- Implemented in `agent.py`.



\###  US2: Task Completion and Progress

\- Users can mark habits as complete in the Streamlit interface.

\- The app tracks how many tasks are finished and updates a progress bar.

\- Implemented in `app.py`.



---



\## Deferred to Iteration 2

\- \*\*US3:\*\* Task Sequencing (AI suggests the next habit automatically)

\- Additional features like motivational feedback or saving progress



---



\## How to Run

Make sure you have Streamlit installed:

```bash

pip install streamlit



