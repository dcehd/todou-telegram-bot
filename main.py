from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from decouple import config
import json
import os

task_list = [
    "Task 1: This is a sample task.",
    "Task 2: Another sample task.",
    "Task 3: Yet another sample task.",
    "Task 4: Mock task to test the bot.",
    "Task 5: Testing the task list feature.",
    "Task 6: Another sample task.",
    "Task 7: A task you have to do today!",
]

# Load completed items (persistent storage)
if os.path.exists("completed_tasks.json"):
    with open("completed_tasks.json", 'r') as file:
        completed = json.load(file)
else:
    completed = []

# Filter `not_completed` to exclude completed tasks
not_completed = [task for task in task_list if task not in completed]
current_batch = []


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_batch
    # If not_completed has tasks, load... if not congratulate me :)
    if not_completed:
        if not current_batch:
            await update.message.reply_text("Insert welcome message from TODOU")

            current_batch = not_completed[:3]

            await send_tasks(update)
        else:
            # send tasks
            await send_tasks(update)
    else:
        await update.message.reply_text("Finished ALL tasks!!! 🎉")
        return


# send tasks
async def send_tasks(update: Update):
    global current_batch

    # cue the task with a "Done" button
    for task in current_batch:
        keyboard = [[InlineKeyboardButton("Done", callback_data=f"done_{task}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(task, reply_markup=reply_markup)


# What happens when you click the button
async def click_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_batch, not_completed, completed
    query = update.callback_query
    await query.answer()

    task = query.data.split("_", 1)[1]

    if task:
        # Remove the task from current_batch
        if task in current_batch:
            current_batch.remove(task)
        # Remove the task from not_completed
        if task in not_completed:
            not_completed.remove(task)
        # Add it to the completed list
        completed.append(task)

        # Save the completed list
        with open("completed_tasks.json", "w") as f:
            json.dump(completed, f, indent=4)

    # show this once a task is done
    await query.edit_message_text("Completed ✅")

    # show this once that set is complete
    if not current_batch:
        await query.message.reply_text("All done with this set 🎉")

    # this is for my feedback, so I can see the effect in real time
    print("--------------------------------------------")
    print(f" Current batch - {current_batch[:3]}")
    print("--------------------------------------------")
    print(f" Not completed - {not_completed[:3]}")
    print("--------------------------------------------")
    print(f" Completed - {completed[:3]}")
    print("--------------------------------------------")


# start and run the bot
def main():
    token = config("TOKEN")
    application = Application.builder().token(token).build()

    # add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(click_button, pattern="^done_"))

    #  Run the bot
    application.run_polling()


if __name__ == "__main__":
    main()
