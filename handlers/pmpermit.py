from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hello This Is My Music Assistance Id Dont Spam 𝗚𝗿𝗼𝘂𝗽 𝗺𝗲 𝗮𝗱𝗱 𝗸𝗿𝗼 𝗮𝘂𝗿 𝗵𝗾 𝗺𝘂𝘀𝗶𝗰 𝗲𝗻𝗷𝗼𝘆 𝗸𝗿𝗼  😑")
  return                        
