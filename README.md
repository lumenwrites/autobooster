# AutoBooster bot for Mastodon

This bot automatically boosts all the posts made by a user.

It can be useful if you have moved your account to a different instance, and want to automatically share all your posts with your old followers.

# Usage

Clone this repo and cd into it:

```
git clone https://github.com/raymestalez/autobooster.git
cd autobooster
```

Install Mastodon API wrapper:

```
pip3 install Mastodon.py
```

Rename `config.json.sample` into `config.json`, and enter email/password/instance of the account that should automatically boost the posts.

Now to automatically boost all the recent posts made by a `SourceUsername@instance.social` you can run:

```
python3 ./autobooster.py SourceUsername@instance.social
```

If you need to run more than one bot, instead of modifying config.json you can specify the autobooster account credentials as arguments:

```
python3 ./autobooster.py SourceUsername@instance.social autobooster@gmail.com autobooster_password https://autoboosters-instance.social
```

# Run it regularly

You can use cron to run the bot regularly.

Run the command:

```
crontab -e
```

And at the end of the file add the line:

```
0,30 * * * * cd /path/to/autobooster/ && python3 autobooster.py SourceUsername@instance.social
```

(this will execute every 30 minutes)

