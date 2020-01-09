# noinspection PyUnresolvedReferences

import discord
import asyncio

token = "NjQwNTEyNDY5MTAxNzA3MjY1.Xg2lfQ.jODSoLs7FAMnjZiIWuF75YoEMAo"

client=discord.Client()

@client.event
async def on_ready() :
    print(client.user.id)
    print("ready")
    game = discord.game("베타 테스트")
    await client.charge_presence(status=discord.status.online, activity=game)
    client.event

async def on_message(message):
        if message.content.startswith("닉몬봇 안녕하살법"):
            await message.channel.send("안녕하살법 받아치기!")

if message.content.startswith("닉몬봇 100"):
        for acount in range(100):
            await client.send_message(message.channel, acount+1)
            await client.send_message(message.channel, "100까지 다 셌어요! ~~이 명령어 왜 하는거야~~")

if message.content.startswith("닉몬봇 계산"):
        global calcResult
        if message.content[7:].startswith("닉몬봇 더하기"):
            calcResult = int(message.content[11:12])+int(message.content[13:14])
            await client.send_message(message.channel, "결과는? "+str(calcResult))
        if message.content[7:].startswith("닉몬봇 빼기"):
            calcResult = int(message.content[10:11])-int(message.content[12:13])
            await client.send_message(message.channel, "결과는? "+str(calcResult))
        if message.content[7:].startswith("닉몬봇 곱하기"):
            calcResult = int(message.content[11:12])*int(message.content[13:14])
            while client.send_message(message.channel, "결과는? "+str(calcResult))


client.run(token)
