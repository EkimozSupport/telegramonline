from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, an open-source bot that lets you play music in your Telegram groups.For Support Join our group @abhinasroy.\n\n The Assistant must be in your group to play music in the voice chat of your group.\n\n /help to know my commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πππππππβ‘οΈ", url="https://t.me/Smailesi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πππΌπππβ‘οΈ", url="https://t.me/ellycarlmusicplayer"
                    ),
                    InlineKeyboardButton(
                        "KΔ°NGβ‘οΈ", url="https://t.me/kizilsancaksahibi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ππππBA EKLEME β‘οΈ", url="https://t.me/Ellycarlmusicbot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
