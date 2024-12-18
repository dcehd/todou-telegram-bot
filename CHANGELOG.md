# Changelog

---

All notable changes to this project will be documented in this file.

## [1.0.0] - Initial Release - 2024-12-15

---
- Added basic functionality for a task management bot:
  - `/start` command to display a welcome message and show tasks.
  - Tasks displayed with "Done" buttons for marking completion.
  - Basic feedback provided in the console for debugging.

## [1.1.0] - Enhanced Task Handling - 2024-12-15

---
- Improved `/start` command to handle existing tasks dynamically:
  - Prevents re-sending tasks if already in progress.
  - Displays only the first 3 tasks in a batch.
- Introduced "Set Complete" message when a batch is completed.

## [1.2.0] - Expanded Task List - 2024-12-16

---
- Added more tasks to the `task_list`.
- Introduced congratulatory message when all tasks are completed.

## [1.3.0] - Persistent Task Storage - 2024-12-16

---
- Implemented persistence for completed tasks using `completed_tasks.json`.
- Ensured tasks marked as complete are not displayed again.
- Added dynamic filtering of tasks based on completed status.

## [1.4.0] - Custom Task Batch Size - 2024-12-17

---
- Introduced user input to customize the number of tasks displayed per batch.
  - Allowed inputs: numbers (1-10) and "all".
- Added input validation for the task limit feature.
- Refactored task handling logic to integrate batch size functionality.

