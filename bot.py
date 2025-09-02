import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes


BOT_TOKEN = os.environ["7559095836:AAG50xgGTiAG3hGLYS8tYJtxxqoPqjHPXpA"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("MLBB Normal Server Dia", url="https://t.me/yourshoplink")],
        [InlineKeyboardButton("PUBG UC", url="https://t.me/yourshoplink")],
        [InlineKeyboardButton("Free Fire Dia", url="https://t.me/yourshoplink")],
        [InlineKeyboardButton("Honor of Kings Token", url="https://t.me/yourshoplink")],
        [InlineKeyboardButton("BIGO Live Dia", url="https://t.me/yourshoplink")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎮 Game Top-up Menu:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
