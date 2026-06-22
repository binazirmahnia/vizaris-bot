from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ Starter $9", callback_data="starter")],
        [InlineKeyboardButton("💎 Pro $49", callback_data="pro")],
        [InlineKeyboardButton("🚀 Enterprise $99", callback_data="enterprise")],
        [InlineKeyboardButton("🤖 AI Chat", callback_data="ai")]
    ]

    await update.message.reply_text(
        "👑 Welcome to Vizaris PRO SaaS\nChoose your plan:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# BUTTONS
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "starter":
        await q.edit_message_text("⚡ Starter activated")
    elif q.data == "pro":
        await q.edit_message_text("💎 Pro activated")
    elif q.data == "enterprise":
        await q.edit_message_text("🚀 Enterprise activated")
    else:
        await q.edit_message_text("🤖 AI mode started")


# BUILD APP
def build_application():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handler))

    return app
