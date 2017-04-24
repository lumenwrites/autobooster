# Autobooster bot for Mastodon

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

Now to automatically boost all the recent posts made by a `username@instance.social` you can run:

```
python3 ./autobooster.py username@instance.social
```


# Run it regularly

You can use cron to run the bot regularly.

Run the command:

```
crontab -e
```

And at the end of the file add the line:

```
0,30 * * * * python3 /path/to/the/script/autobooster.py username@instance.social
```

(this will execute every 30 minutes)
