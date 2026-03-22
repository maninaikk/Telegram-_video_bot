
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import yt_dlp
import os

BOT_TOKEN = os.environ.get("8378656167:AAGn-rIAinArZB0ZcfYhax8poPkCjzf6yH0)

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    ydl_opts = {
        "format": "best",
        "outtmpl": "video.%(ext)s"
    }

    try:
        await update.message.reply_text("Downloading... ⏳")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, "rb") as video:
            await update.message.reply_video(video=video)

        os.remove(filename)

    except Exception as e:
        await update.message.reply_text("Error 😔")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

app.run_polling()
