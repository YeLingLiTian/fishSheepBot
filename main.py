from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain

import asyncio
import util

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host=util.config["host"],  # 填入 httpapi 服务运行的地址
        authKey=util.config["authkey"],  # 填入 authKey
        account=util.config["account"],  # 你的机器人的 qq 号
        websocket=util.config["websocket"]  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)


@bcc.receiver("FriendMessage")
async def friend_message_listener(bot_app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain("我是于洋嘎嘎嘎")
    ]))


app.launch_blocking()
