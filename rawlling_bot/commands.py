from telegram import Bot, Update, ParseMode
from random import randint


def start(bot: Bot, update: Update):
    """Send Start / Help message to client.

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
    """
    reply = """*Rawlling Bot* 
     
[@rawlling_bot](https://t.me/rawlling_bot) | [GitHub](https://github.com/Nachtalb/rawlling_bot) 
 
*How to use me* 
Just use the `/rawl` command, also working in groups.

*Commands* 
- /help, /start: show this help message with information about the bot and it's usage. 
- /rawl: I rawl numbers from 0 to 10000 so you can get your sexy dubs, trips and quads. 
 
*My other bots*  
Please share this bot with your friends so that I ([the magician](https://github.com/Nachtalb/) behind this project)  
have enough motivation to continue and maintain this bot. 
 
Check out my other project\[s\]: 
- [@insta_looter_bot](https://t.me/insta_looter_bot) - Download images and videos from Instagram via 
Telegram
- [@reverse_image_search_bot](https://t.me/reverse_image_search_bot) - Reverse image search directly in  
Telegram
- [@yet_another_urban_dictionary_bot](https://t.me/yet_another_urban_dictionary_bot) - Urban Dictionary lookup directly in Telegram

*Contributions* 
_Bug report / Feature request_ 
If you have found a bug or want a new feature, please make an issue here: [Nachtalb/rawlling_bot](https://github.com/Nachtalb/rawlling_bot) 
 
_Code Contribution / Pull Requests_ 
Please use a line length of 120 characters and [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).  
 
Thank you for using [@rawlling_bot](https://t.me/rawlling_bot).
"""
    update.message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def rawl(bot: Bot, update: Update, args: list = None):
    """Rawl a number between 0 and 10000

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
        args (:obj:`list`): List of sent arguments
    """
    update.message.reply_text('{rawl:0>5}'.format(rawl=randint(0, 10000)))


def unknown(bot: Bot, update: Update):
    """Send a error message to the client if the entered command did not work.

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
    """
    update.message.reply_text('Sorry, I didn\'t understand that command. Use /help for more information.')
