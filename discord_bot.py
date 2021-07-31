import discord
from discord.ext import commands,tasks
import random
from itertools import cycle
from twitter import TwitterBot
import os

PREFIX = '!!' #คำนำหน้า


bot = commands.Bot(command_prefix=PREFIX)

channel = bot.get_channel('channel id')


    # print(f'{bot.user.id} ')
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # if 'happy birthday' in message.content.lower():
    #     await message.channel.send('Happy Birthday! 🎈🎉')
    if message.content.lower().startswith('!hello'):
        choice = ['Morning','Evening','After-noon']
        response = random.choice(choice)
        await message.channel.send(f'Hello {response} {message.author.name} ! ')
            # await  message.channel.send(f'Hello {bot.user} {c} ')
        print('User sent Message')
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    # twitter_to_discord.start()

    print('User send Ping')

    await ctx.send('Pong!!')

@bot.command()
async def echo(ctx,*args):
    output =''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)



file_name = 'test.pkl'

status = cycle(['Status Wait','Status Do'])
@tasks.loop(minutes=60)
async def twitter_to_discord(): ### pancake swaps
    global  file_name
    global status
    channel= bot.get_channel(870604414442950676) ### ID CHanale
    tw = TwitterBot('pancakeswap') ###
    cond,tweet=tw.fetch_twitter_post(file_name) ## True Flase , tweet
    # data_pickle= tw.data_pickle
    # print(cond,tweet)
    if cond == True :

        date_update = tweet['created_at']
        print(tweet)
        e = discord.Embed(title=f"Twitter News Update {tw.name}",
                        description=f"อัพเดตล่าลุดเมื่อ {date_update}",
                        color=12530335)  #)
                    # e.set_image(url=tw.profile_url)


        e.set_thumbnail(url=tw.profile_url)
        e.add_field(name=':book: TEXT', value=f"{tweet['text']}")
        e.add_field(name=':love_letter: Love', value=f"{tweet['retweet']}")
        e.add_field(name=':thumbsup: Like', value=f"{tweet['like']}")
        id =tweet['id']
        e.url = f'http://twitter.com/{tw.name}/status/{id}'
        # await bot.get_channel('870604414442950676').send('test')
        await channel.send(embed=e)
        await bot.change_presence(activity=discord.Game(next(status)))

        # await discord.send(embed=e)

    if cond == False :
        print(f'Condition is {cond}')
        # await channel.send(embed=e)
        # await channel.send('Test Discord')
    # await bot.get_channel('870604414442950676').send('test')
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_ready():
    # channel =
    twitter_to_discord.start()

    print(f'{bot.user} has connected to Discord!')


TOKEN = os.environ['TOKEN']

bot.run(TOKEN)

