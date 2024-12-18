from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from decouple import config

task_list = [
    "Task 1: This is a sample task.",
    "Task 2: Another sample task.",
    "Task 3: Yet another sample task.",
    "Task 4: Mock task to test the bot.",
    "Task 5: Testing the task list feature."
]

not_completed = task_list[:]
completed = []
current_batch = []


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_batch
    await update.message.reply_text("Insert welcome message from TODOU")

    await send_tasks(update)


# send tasks
async def send_tasks(update: Update):
    global current_batch
    current_batch = not_completed[:3]

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

    if task in current_batch:
        current_batch.remove(task)
    if task in not_completed:
        not_completed.remove(task)
        completed.append(task)

    await query.edit_message_text("Completed ✅")

    # this is for my feedback, so I can see the effect in real time
    print("--------------------------------------------")
    print(f" First batch - {current_batch[:3]}")
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
