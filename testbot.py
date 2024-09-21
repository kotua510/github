import os
import discord
from discord.ext import commands

# インテントを有効化する
intents = discord.Intents.default()
intents.message_content = True  # メッセージ関連のイベントを有効にする

# Botのコマンドプレフィックスを設定
bot = commands.Bot(command_prefix="!", intents=intents)


# Botが準備完了したときの処理
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# メッセージが送信されたときの処理
@bot.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author == bot.user:
        return

    # ユーザーが「あいうえお」と送信した場合
    if message.content == "あいうえお":
        await message.channel.send("かきくけこ")

# Botのトークンを入れる
bot.run('DISTOKEN')
