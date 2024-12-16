import discord
import os
import random
import requests
from discord.ext import commands
from bot_token import token
from detect_class import detect_pvp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def minecraft_nasil_bitirilir(ctx):
    await ctx.send(f'önce odun kaz sonra taş kaz demir bul kazma ve kova yap lav bul suyu 3.2lik biryapıdan akıt(iki blok aşağı kaz)çakmakla yak fortles bul blaze kes mavi biyomda enderman kes ender gözü yap fırlat end portalını bul gözleri koy ende git ejderhayı kes ve bitti(oyunu sadece bir kez bitiren birinden yardım aldın)')

        
@bot.command()
async def mem1(ctx):
    with open('image/mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('image/mem2.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('image/mem3.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def vip(ctx):
    with open('image/vip.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def I_love_minecraft(ctx):
    with open('image/minecraft.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kedi1(ctx):
    with open('m2l1/images/mc_cat.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kopek1(ctx):
    with open('m2l1/hayvan/rusty_wolf.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kopek2(ctx):
    with open('m2l1/hayvan/chesnut-wolf.webp', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()

async def mem(ctx):
    meme_list=os.listdir('m2l1/images')
    meme=random.choice(meme_list)
    with open(f'm2l1/images/{meme}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


async def hayvan(ctx):
    hayvan_list=os.listdir('m2l1/hayvan')
    hayvan=random.choice(hayvan_list)
    with open(f'm2l1/hayvan/{hayvan}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def detect(ctx):
    
    if ctx.message.attachments:
        await ctx.send(f'Algılama başladı!')
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            await ctx.send(f'Dosya kaydedildi!')
            classname,score=detect_pvp(file_path,"converted_keras (4)\keras_model.h5","converted_keras (4)\labels.txt")
            await ctx.send(f'Bu bir {classname.strip()} bundan % {int(100*score)}')
            if classname.strip() =="kilic":
                await ctx.send(f"bu kılıç minecraftın bedrock versiyonunda pvpnin asıl silahıdır javada kullanılır ama kullanılma sebebi çok vurduğu için değil savurduğunuz için.")
            elif classname.strip() =="balta":
                await ctx.send(f"bu minecraftın bedrock versiyonunda genelde ağaç kesmek için kullanılır ama java da pvpde de kullanılır çünkü daha çok vurul")
            elif classname.strip() =="yay":
                await ctx.send(f"bu uzak menzilli bir silah daha uzun basılı tutar san ve bırakırsan daha uzağa gider ve daha fazla hasar verir")
            elif classname.strip() =="arbalet":
                await ctx.send(f"bu uzak menzilli bir silah önce basılı tutarak içine ya ok ya da roket girer sonra bir daha basarsan ateş eder")
    else:
        await ctx.send(f'Bu komutla birlikte bir fotoğraf da yüklemelisiniz!')

bot.run(token)