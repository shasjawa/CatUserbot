from telethon import events
from userbot.utils import admin_cmd
import random
import re
import asyncio
from userbot import CMD_HELP
from collections import deque
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

@borg.on(admin_cmd(pattern="lul$", outgoing=True))
@borg.on(sudo_cmd(pattern="lul$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event , "lul")
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=r"nothappy$"))
@borg.on(sudo_cmd(pattern="noathappy$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event ,"nathappy")
	deq = deque(list("😁☹️😁☹️😁☹️😁"))
	for _ in range(48):
		await asyncio.sleep(0.4)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(outgoing=True, pattern="clock$"))
@borg.on(sudo_cmd(pattern="clock$",allow_sudo = True))
async def _(event):
	    event = await edit_or_reply(event , "clock")
	    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	    for _ in range(48):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)
        
@borg.on(admin_cmd(pattern=r"muah$"))
@borg.on(sudo_cmd(pattern="muah$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event ,"muah")
	deq = deque(list("😗😙😚😚😘"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)	
    
@borg.on(admin_cmd(pattern="heart$"))
@borg.on(sudo_cmd(pattern="heart$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event ,"heart")
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)        
        
		
@borg.on(admin_cmd(pattern="gym$", outgoing=True))
@borg.on(sudo_cmd(pattern="gym$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event ,"gym")
	deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=f"earth$", outgoing=True))
@borg.on(sudo_cmd(pattern="earth$",allow_sudo = True))
async def _(event):
	event = await edit_or_reply(event ,"earth")
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(outgoing=True, pattern="moon$"))
@borg.on(sudo_cmd(pattern="moon$",allow_sudo = True))
async def _(event):
	    event = await edit_or_reply(event ,"moon")
	    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	    for _ in range(48):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)
        
@borg.on(admin_cmd(pattern=f"smoon$", outgoing=True))
@borg.on(sudo_cmd(pattern="smoon$",allow_sudo = True))
async def _(event):
    event = await edit_or_reply(event ,"smoon")
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    await event.edit("smoon..")
    animation_chars = [

            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",    
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])
            
@borg.on(admin_cmd(pattern=f"tmoon$", outgoing=True))
@borg.on(sudo_cmd(pattern="tmoon$",allow_sudo = True))
async def _(event):
    event = await edit_or_reply(event ,"tmoon")
    animation_interval = 0.1
    animation_ttl = range(0, 117)
    await event.edit("tmoon")
    animation_chars = [

            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 32])

@borg.on(admin_cmd(pattern=f"clown$", outgoing=True))
@borg.on(sudo_cmd(pattern="clown$",allow_sudo = True))
async def _(event):
    event = await edit_or_reply(event ,"clown")
    animation_interval = 0.50
    animation_ttl = range(0, 16)
    animation_chars = [
        

            "COMMAND CREATE BY @Sur_vivor",
            "🤡️",
            "🤡🤡",
            "🤡🤡🤡",
            "🤡🤡🤡🤡",
            "🤡🤡🤡🤡🤡",
            "🤡🤡🤡🤡🤡🤡",    
            "🤡🤡🤡🤡🤡",
            "🤡🤡🤡🤡",
            "🤡🤡🤡",
            "🤡🤡",
            "🤡",
            "You",
            "You Are",
            "You Are A",
            "You Are A Clown 🤡"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 16])
