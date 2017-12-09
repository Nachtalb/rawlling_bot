# Yet Another Urban Dictionary Bot

[@rawlling_bot](https://t.me/rawlling_bot) | [GitHub](https://github.com/Nachtalb/rawlling_bot)

<!-- toc -->

- [How to use me](#how-to-use-me)
- [Commands](#commands)
- [My other bots](#my-other-bots)
- [Contributions](#contributions)
  * [Bug report / Feature request](#bug-report--feature-request)
  * [Code Contribution / Pull Requests](#code-contribution--pull-requests)
  * [Local installation](#local-installation)

<!-- tocstop -->

## How to use me
Just use the `/rawl` command, also working in groups.

## Commands
- /help, /start: show this help message.
- /rawl: I rawl numbers from 0 to 10000 so you can get your sexy dubs, trips and quads. 

## My other bots
Please share this bot with your friends so that I ([the magician](https://github.com/Nachtalb/) behind this project) 
have enough motivation to continue and maintain this bot.

Check out my other project\[s\]: 
- [@insta_looter_bot](https://github.com/Nachtalb/insta_looter_bot) - Download images and videos from Instagram via 
Telegram
- [@reverse_image_search_bot](https://github.com/Nachtalb/reverse_image_search_bot) - Reverse image search directly in Telegram
- [@yet_another_urban_dictionary_bot](https://t.me/yet_another_urban_dictionary_bot) - Urban Dictionary lookup directly in Telegram


## Contributions
### Bug report / Feature request
If you have found a bug or want a new feature, please make an issue here: [Nachtalb/rawlling_bot](https://github.com/Nachtalb/rawlling_bot)

### Code Contribution / Pull Requests
Please use a line length of 120 characters and [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). 

### Local installation
Instead of the old `pip` with `requirements.txt` I use the new and fancy `pipenv` with `pipfile`. If you read the intro
to [pipenv](https://github.com/pypa/pipfile) and [pipfile](https://docs.pipenv.org) you will understand why I use it.

With this info we now install our virtualenv with: 
```bash
pip install pipenv  # Install pipenv
pipenv --three      # Create virtualeenv from your python3 installation
pipenv install      # Install all requirements
pipenv shell        # Spawn shell for your pipenv virtualenv
``` 

After this is complete, you have to get an API Token from Telegram. You can easily get one via the
[@BotFather](https://t.me/BotFather).

Now that you have your API Token copy the `settings.example.py` to `settings.py` and paste in your API Token.
Finally you can use this to start your bot.
```bash
python run_bot.py
``` 

Thank you for using [@rawlling_bot](https://t.me/rawlling_bot).
