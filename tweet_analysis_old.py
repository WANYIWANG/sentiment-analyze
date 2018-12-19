import csv
import json
import os
from nltk.tokenize import TweetTokenizer
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# load tweets from downloaded files
def load_tweets(dir):
    # store all tweets into a list, each tweet is represented by a dict, e.g.,
    # {"created_at": "Dec 01 2018", "text": "China AIDS group really regrets in gene-editing"}
    all_tweets = []
    # read all files under current directory
    for filename in os.listdir(dir):
        if filename.endswith('.txt'):
            with open(dir + filename, 'r') as f:
                tweets_dict = json.loads(f.read())
                print("read file {}, total {} tweets".format(filename, len(tweets_dict["statuses"])))
                for tweet in tweets_dict["statuses"]:
                    all_tweets.append(tweet)
    print("\n **** Total {} tweets ****".format(len(all_tweets)))
    return all_tweets


# clean unused fields in tweets
def clean_fields(all_tweets):
    new_tweets = []
    tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)
    for tweet in all_tweets:
        # only keep useful fields, like "text", "location", "post_time" and "user_name"
        tweet_text = tweet["text"].encode('ascii', errors='ignore')
        tokens = tokenizer.tokenize(tweet_text)
        tokens = [t for t in tokens if not t.startswith("@") and not t.startswith("http")]
        if len(tokens) <= 3:
            continue
        new_tweet = {"text": " ".join(tokens),
                     "location": tweet["user"]["location"],
                     "post_time": tweet["created_at"],
                     "user_name": tweet["user"]["name"]
                     }
        new_tweets.append(new_tweet)
    return new_tweets


# compute sentiment score using Google Cloud NLP API for each tweet
def compute_sentiment_score(client, all_tweets):
    # The text to analyze
    for tweet in all_tweets:
        document = types.Document(
            content=tweet["text"],
            type=enums.Document.Type.PLAIN_TEXT
        )

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        tweet["sentiment_score"], tweet["magnitude"] = "%.2f" % sentiment.score, "%.2f" % sentiment.magnitude
        print('Text: {}'.format(tweet["text"]))
        print('Sentiment: {}, {}'.format(tweet["sentiment_score"], tweet["magnitude"]))


# save tweets to a CSV file
def save_tweets(filename, all_tweets):
    fieldnames = ['user_name', 'location', 'post_time', 'sentiment_score', "magnitude", "text"]
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tweet in all_tweets:
            writer.writerow(tweet)
    print('write processed tweets to {}'.format(filename))


all_tweets = load_tweets("data/")
all_tweets = clean_fields(all_tweets)
# Instantiates a Google NLP client
client = language.LanguageServiceClient()
# compute Google sentiment scores
compute_sentiment_score(client, all_tweets)
save_tweets('tweets_output.txt', all_tweets)
