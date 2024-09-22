import os
import discord
from discord.ext import commands

# インテントを有効化する
intents = discord.Intents.default()
intents.message_content = True

# Botのコマンドプレフィックスを設定
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "あいうえお":
        await message.channel.send("かきくけこ")

# 環境変数からBotのトークンを取得
bot_token = os.getenv('DISTOKEN')

# 環境変数からPORTを取得
port = int(os.getenv('PORT', 5000))  # デフォルトポートは5000

# Botのトークンで実行
if bot_token:
    bot.run(bot_token)
else:
    print("環境変数 'DISTOKEN' が設定されていません。")

