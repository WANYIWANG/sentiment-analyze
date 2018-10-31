import json

# read sample tweets from twurl command
with open('tweets.txt') as f:
  tweets = json.loads(f.read().strip().replace('[\n\r]', ' '))
  for t in tweets['statuses']:
    content, user_location = t['text'], t['user']['location']
    print('##########################')
    print(content)
    print(user_location)
 
  
