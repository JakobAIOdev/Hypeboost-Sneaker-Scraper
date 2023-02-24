# Hypeboost-Sneaker-Scraper
A web Scraper for Sneaker Prices on Hypeboost with discord message.
The Scraper will Scrape Price informations for all listed Sizes on Hypeboost and return
you a list of them in your discord server.
The message also includes the Hypeboost Product URL, StockX Product URL and Restocks Product URL for the Scraped Product.
A Product Photo is also added to the return message.




# How to use:

1. Check or install following libraries:

+ requests (pip install requests)
+ json (pip install json)
+ BeautifulSoup (pip install beautifulsoup4)
+ Discord (pip install discord.py)


2. Open "discord_embed" file and input your Discord Bot Token in the "TOKEN" variable.

3. Run the "discord_embed" file.

4. write the keyword ($scrape) + SKU in your discord server.
   format: $scrape SKU --> (example: $scrape CW1590-100)



The Scraper will now send you all listed sizes and their prices in the discord server.
Also the Hypeboost Product URL is in the blue title.
At the bottom of the discord message you can also find the StockX and Restocks Product URL to the Scraped Product.




# Notes
This is my first Github Project and the code might not be the best or the simplest,
if you have any questions just ask them and i will try to help.



# Return Message Example:
The return message looks like this:


![Discord-embed-pic2](https://user-images.githubusercontent.com/103487648/221241049-eb73f4b7-4582-4e05-b028-e1f7fcac9627.png)
