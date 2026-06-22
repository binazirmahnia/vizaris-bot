from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Pro $9.99", callback_data="pro")],
        [InlineKeyboardButton("Premium $49.99", callback_data="premium")],
        [InlineKeyboardButton("AI Chat", callback_data="ai")]
    ]

    await update.message.reply_text(
        "Welcome to Vizaris Bot",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "pro":
        await q.edit_message_text("Pro selected")
    elif q.data == "premium":
        await q.edit_message_text("Premium selected")
    else:
        await q.edit_message_text("AI mode active")


def build_application():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handler))
