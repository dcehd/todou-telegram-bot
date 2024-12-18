# TODOU - A Task Management Telegram Bot

---
TODOU is an effective task management bot for Telegram. It helps users organize and complete their tasks in an engaging way by offering batch task display and completion tracking.

## Features

---
- **Batch Task Display:** View tasks in customizable batch sizes (1-10 tasks or all tasks at once).
- **Completion Tracking:** Mark tasks as completed and prevent them from being displayed again.
- **Persistent Storage:** Save and load completed tasks using `completed_tasks.json`.
- **Interactive Buttons:** Use inline "Done" buttons to mark tasks as completed.
- **Dynamic Updates:** Displays congratulatory messages when all tasks are completed.

## Setup

---

1. Clone this repository
2. Install dependencies:
    ```
    pip install python-telegram-bot python-decouple

3. Add your bot token:

   - Create a .env file in the project directory. 
   - Add the following line:
     ```
     TOKEN=your-telegram-bot-token
  
4. Run the bot:
    ```
    main.py

## Usage

---
1. Start the bot with /start. 
2. Enter the number of tasks you'd like to view (1-10) or type "all" to see all remaining tasks. 
3. Mark tasks as completed using the "Done" button.

## Customization

---
- Task List: Edit the task_list variable in the code to include your tasks. 
- Persistent Storage: The bot uses completed_tasks.json to save completed tasks. Delete this file to reset the progress.