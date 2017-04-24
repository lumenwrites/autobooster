import os, datetime, sys
from mastodon import Mastodon
import json

def mastodon_bot(botname, email, password, instance_url='https://mastodon.social'):
    # This will be used to generate unique names for files containing your credentials
    # So that you could run several bots with different accounts
    account_name = email+"_"+instance_url.replace("https://","")+"_"

    # Create app if doesn't exist
    if not os.path.isfile(account_name + "clientcred.txt"):
        print("Creating app")
        mastodon = Mastodon.create_app(
            botname,
            to_file = account_name + 'clientcred.txt',
            api_base_url=instance_url
        )
    
    # Fetch access token if I didn't already
    if not os.path.isfile(account_name + "usercred.txt"):
        print("Logging in")
        mastodon = Mastodon(
            client_id = account_name + 'clientcred.txt',
            api_base_url=instance_url        
        )
        mastodon.log_in(email, password, to_file = account_name + 'usercred.txt')
    
    # Login using generated auth
    mastodon = Mastodon(
        client_id = account_name + 'clientcred.txt',
        access_token = account_name + 'usercred.txt',
        api_base_url=instance_url    
    )
    print(botname + " logged in as " + email + " at " + instance_url)

    return mastodon



def repost_recent_statuses(mastodon, source_username):
    # Follow the account by username@instance.social,
    # returns the account I can grab recent toots from.
    source_account = mastodon._Mastodon__api_request('POST',
                                                     '/api/v1/follows',
                                                     params={"uri":source_username})
    print("source_account " + str(source_account))
    recent_statuses = mastodon.account_statuses(source_account["id"])
    print("Fetched recent statuses from " + source_username)
    # print(recent_statuses)
    
    for status in recent_statuses[:10]:
        try:
            mastodon.status_reblog(status["id"])
            print("Reblogged status " + str(status["id"]))
        except:
            print("Error reblogging status " + str(status["id"]))        
    

with open('config.json', 'r') as f:
    config = json.load(f)
    


try:
    # Can also pass the rebooster account credentials as arguments
    botname = "AutoboosterBot"
    email =  sys.argv[2]
    password =  sys.argv[3]
    instance_url =  sys.argv[4]
except:
    botname = config["botname"]
    email = config["email"]
    password = config["password"]
    instance_url = config["instance_url"]

# Log into mastodon
mastodon = mastodon_bot(botname, email, password, instance_url)

# Boost recent posts made by user
source_username = sys.argv[1]
repost_recent_statuses(mastodon, source_username)
