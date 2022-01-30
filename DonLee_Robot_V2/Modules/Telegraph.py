# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import os
from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2 import Import
from telegraph import upload_file

@DonLee_Robot_V2.on_message(filters.command(["tgmedia", "tgraph", "telegraph"]))
async def telegraph(client, message: Import.Msg):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply_photo(
            photo=f"https://telegra.ph{response[0]}",
            caption=f"<b>𝗅𝗂𝗇𝗄:-</b> <code>https://telegra.ph{response[0]}</code>\n\n𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @Mo_Tech_YT",
            quote=True,
            reply_markup=Import.Markup([[
               Import.Button(text="𝗈𝗉𝖾𝗇 𝗅𝗂𝗇𝗄", url=f"https://telegra.ph{response[0]}"),
               Import.Button(text="𝗌𝗁𝖺𝗋𝖾 𝗅𝗂𝗇𝗄", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
               ],[
               Import.Button(text="𝖢𝗅𝗈𝗌𝖾 🗑️", callback_data="close")
               ]]
        )
    )
    finally:
        os.remove(download_location)
