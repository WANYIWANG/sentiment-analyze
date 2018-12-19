import csv
import json
import os
from nltk.tokenize import TweetTokenizer
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

latlog = {
    "atlanta": {"lat": 33.753746, "long": -84.386330},
    "boston": {"lat": 42.361145, "long": -71.057083},
    "chicago": {"lat": 41.881832, "long": -87.623177},
    "dallas": {"lat": 32.897480, "long": -97.040443},
    "denver": {"lat": 39.742043, "long": -104.991531},
    "detroit": {"lat": 42.331429, "long": -83.045753},
    "las_vegas": {"lat": 36.114647, "long": -115.172813},
    "los_angeles": {"lat": 34.052235, "long": -118.243683},
    "miami": {"lat": 25.761681, "long": -80.191788},
    "new_york": {"lat": 40.730610, "long": -73.935242},
    "penn": {"lat": 41.203323, "long": -77.194527},
    "phoenix": {"lat": 33.448376, "long": -112.074036},
    "san_francisco": {"lat": 37.773972, "long": -122.431297},
    "seattle": {"lat": 47.608013, "long": -122.335167},
    "washington_dc": {"lat": 38.889931, "long": -77.009003}
}

# load tweets from downloaded files
def load_tweets(dir):
    # store all tweets into a list, each tweet is represented by a dict, e.g.,
    # {"created_at": "Dec 01 2018", "text": "China AIDS group really regrets in gene-editing"}
    all_tweets = []
    # read all files under current directory
    for filename in os.listdir(dir):
        if filename.endswith('.txt'):
            with open(dir + filename, 'r') as f:
                city = filename.split("-")[1]
                tweets_dict = json.loads(f.read())
                print("read file {}, total {} tweets".format(filename, len(tweets_dict["statuses"])))
                for tweet in tweets_dict["statuses"]:
                    # add latitude longitude information
                    tweet["city"] = city
                    tweet["latitude"] = latlog[city]["lat"]
                    tweet["longitude"] = latlog[city]["long"]
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
                     "post_city": tweet["city"],
                     "latitude": tweet["latitude"],
                     "longitude": tweet["longitude"],
                     "user_location": tweet["user"]["location"],
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
    fieldnames = ['user_name', 'user_location', 'post_city', 'latitude', 'longitude',
                  'post_time', 'sentiment_score', "magnitude", "text"]
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
save_tweets('tweets_output.csv', all_tweets)