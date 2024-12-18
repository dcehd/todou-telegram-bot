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