# Autobooster bot for Mastodon

Automatically boosts all the posts made by a user.

# Setup

Clone this repo and cd into it:

```
git clone https://github.com/raymestalez/autobooster.git
cd autobooster
```

Install Mastodon API wrapper:

```
pip3 install Mastodon.py
```

Rename `config.json.sample` into `config.json`, and enter your email/password/instance.

Now to automatically boost all the recent posts made by a `username@instance.social` you can run:

```
python3 ./autobooster.py username@instance.social
```


