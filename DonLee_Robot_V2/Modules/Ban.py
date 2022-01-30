# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2 import Config 
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
from DonLee_Robot_V2.Admins import admin_check, extract_user, extract_time

@DonLee_Robot_V2.on_message(filters.command("ban", COMMAND_HAND_LER))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting off..! "
                f"{user_first_name}"
                " Is forbidden."
            )
        else:
            await message.reply_text(
                "Someone else is dusting off..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Is forbidden."
            )


@DonLee_Robot_V2.on_message(filters.command("tban", COMMAND_HAND_LER))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if len(message.command) <= 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalidbtime type specified. "
                "Expected m, h, or d, Got it: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.kick_member(
            user_id=user_id,
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting off..! "
                f"{user_first_name}"
                f" banned for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Someone else is dusting off..! "
                f"<a href='tg://user?id={user_id}'>"
                "Lavane"
                "</a>"
                f" banned for {message.command[1]}!"
            )



@DonLee_Robot_V2.on_message(filters.command(["unban", "unmute"], COMMAND_HAND_LER))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Congratulations "
                f"{user_first_name} "
                " You can join the group!"
            )
        else:ശരി
            await message.reply_text(
                ",Okay, changed ... now"
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> ക്ക് "
                "ഗ്രൂപ്പിൽ ചേരാൻ കഴിയും!"
            )
