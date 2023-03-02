""" 
CC Checker & Generator for ZThon™ @ZedThon
Write file by Zelzal @ZlZZ7 
hhh o ya beby

"""

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from zthon import zedub

from ..core.managers import edit_or_reply


@zedub.zed_cmd(pattern="ch(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@BesTIRCbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ فحص البطـاقـه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("B_B_CBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="بين(?:\s|$)([\s\S]*)")
async def song2(event):
    chat = "@BesTIRCbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ فحص بن 𝚅𝙸𝚂𝙴💲...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/bin")
        except YouBlockedUserError:
            await zedub(unblock("B_B_CBot"))
            await conv.send_message("/bin")
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await zed.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="توليد(?:\s|$)([\s\S]*)")
async def song2(event):
    been = event.pattern_match.group(1)
    chat = "@BesTIRCbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, f"**- جـارِ توليـد 10 بطاقـات ع الـ Bin {been}  💳...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message("/gen")
            await asyncio.sleep(2)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("BesTIRCbot"))
            gool = "/gen {}".format(been)
            await conv.send_message("/gen")
            await asyncio.sleep(2)
            await conv.send_message(gool)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="chk(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@BesTIRCbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ فحص البطـاقـه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/chk")
        except YouBlockedUserError:
            await zedub(unblock("BesTIRCbot"))
            await conv.send_message("/chk")
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await zed.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="ck(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@BesTIRCbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ فحص البطـاقـه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/ck")
        except YouBlockedUserError:
            await zedub(unblock("BesTIRCbot"))
            await conv.send_message("/ck")
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await zed.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()