import discord
import Scraper_Main
from discord.ext import commands
from Scraper_Main import product_url
from Scraper_Main import product_title
from Scraper_Main import product_picture
from Scraper_Main import stockx_url
from Scraper_Main import restocks_url


TOKEN = 'MTA3MjIyODk0Nzg4ODE5MzU0Ng.GqOJPA.sv9j3_GxUS2RFWvKRnlik7KRT7Dy0fv9t7mYkY'

hypeboost_preise = Scraper_Main.product_search
product_url = Scraper_Main.product_url
product_title = Scraper_Main.product_title
product_picture = Scraper_Main.product_picture
stockx_url = Scraper_Main.stockx_url
restocks_url = Scraper_Main.restocks_url

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping!'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.content.startswith(f'$scrape'): #(Prefix "§") keyword for scraping
    #await message.channel.send('''Scraping still in development. By JakobAIO \n---------------------------------------------''')

    if f'$scrape' in message_content:
        SKU = message_content.replace('$scrape ', '') # everything after prefix is the search (SKU)
        #await message.channel.send("test")
        text = hypeboost_preise(SKU) #SKU used for scraping
        product_url_output = product_url(SKU)
        product_title_output = product_title(product_url_output)
        product_picture_output = product_picture(product_url_output)
        stockx_url_output = stockx_url(SKU)
        restocks_url_output = restocks_url(SKU)
        #text = product_search(str(SKU))
        embed = discord.Embed(
          title=product_title_output,
          url=product_url_output,
          color=0x1abc9c
        )
        embed.set_author(
          name="HypeBoost Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://consumersiteimages.trustpilot.net/business-units/610a587f2b259a001d8d9b5f-198x149-1x.jpg"
          )
        embed.set_thumbnail(
          url=product_picture_output
        )
        embed.add_field(
          name="Prices:",
          value=text
        )
        embed.add_field(
          name='StockX',
          value=stockx_url_output,
          inline=False
        )
        embed.add_field(
          name='Restocks',
          value=restocks_url_output,
          inline=False
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )


        await message.channel.send(embed=embed) #sends sizes in discord chat
        #await message.channel.send("Product URL: comming soon!\nProduct Title: comming soon!\n---------------------------------------------\nScraping finished!")
        print('Scraping Successful!')


bot.run(TOKEN)