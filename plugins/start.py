from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("📌️ KOT BOTS 🔎", url="https://t.me/KOT_BOTS")],
        [InlineKeyboardButton("📌️ support 🔎", url="https://t.me/KOT_REPORS")]

    ])
    thumbnail_url = "https://telegra.ph/file/fe4379cb5ebf812e3379e.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**</b>\n\n<br>__😇 I Can Download YT Videos For You ✨️__</br>\n\n<b>• **🗂️ Instructions for use...🚨**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
