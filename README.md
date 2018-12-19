# sentiment-analyze
# Program For Cultural Heritage
Final Presentation: Sentiment Analysis of “#gene_editing” tweets 
# My Github Repo: https://github.com/WANYIWANG/sentiment-analyze

# Project Description:
The final project of Programming for Culture Heritage is an integrity project with API request, data scraping and cleaning, semantical analyze, save data into csv file, and data visualization by python and tableau. 
RRecently, A Chinese researcher used CRISPR - Cas9 technology that created the first gene-edited twin babies.
CRISPR is easier to use and more precise than previous methods, but it is not a perfect technology. It can lead to unintended consequences, such as affecting other genes (“off-target” effects) or making multiple modifications of the gene we are aiming to modify (“on-target” effects). There is an ongoing discussion as to how widespread “off target” and “on-targets” modifications are, and what the unintended consequences of these effects may be.
This technology Is not allowed in US and many other country. 
My topic is about the movement of #gene_editing on Twitter. I want to analysis US people’s opinions (positive or negative) about this issue by the distribution of region. 

# Procedure of data collection:

1.Apply for the Twitter API key (Twurl is access token app specifically for the Twitter API.)
Install twurl : gem install twurl
twurl authorize --consumer-key key / --consumer-secret secret

2.Make request 
twurl /1.1/search/tweets.json?"q=gene editing
&count=100&geocode=40.730610,-73.935242,50mi&result_type=popular"
(in this step, I requested area within 50miles of 15 main regions of U.S., each region requested twice.)

3.Parse json data
Find the json structure by browse it into json reader online. Specify the path I want to request, Key: "Statues"

4.Load data
Load tweets from downloaded files. First, create an empty list to store parsed tweets, and store all tweets into a list that each tweet is represented by a dict, e.g., read all files under current directory.

5.Clean data
In this step, I cleaned tweets data by separate text by blank using TweetTokenizer, "ascii" to convert it to unicode, and "strip & reduce len" to delete space. I skipped the test of url, @ sign, and length short than 3 characters text from follower analysis. only keep useful fields, like "text", "location", "post_time" and "user_name"

6.Semantical analysis by Google Cloud API
In Google NLP API, Quickstart: Using Client Libraries. I set up a project and download API key json file.
from google.cloud import language, enums, and types.Do the semantical analysis based on Google instruction that to get two more dimensions data: sentiment score and sentiment magnitude.

7.import csv
I wrote data and sentiment score into csv file with six dimensions.
   fieldnames = ['user_name', 'location', 'post_time', 'sentiment_score', "magnitude", "text"]


# Result Analysis
From Nov 26 - Dec 1
1350 tweets from 15 country have been loaded in. 
703 out of 1350 tweets show negative attitude for #china gene editing 
EXP: JUST BECAUSE WE CAN DOES NOT MEAN WE SHOULD-Chinese Scientist Claims to Use Crispr to Make First Genetically Edited
375 out of 1350 tweets show neutral attitude for #china gene editing
EXP: the gene-edited embryo is meant to be born and could potentially suffer unknown consequences from it
272 out of 1350 tweets show positive attitude for #china gene editing
EXP: China baby gene-editing scientist defends his research , raises possibility of thirdembryo
However ' Proud '(sarcasm)appearance for many times in positive sentiment score result which means irony and sarcasm can not be tested by computer. 
Within five days, 400 people in two major cities in California posted or forwarded tweets of #gene_editing. New York and Boston also paid close attention to this topic, with tweets of 200. On the contrary, Las Vegas, Penn and some other cities have only a few tweets about this news.

# Python first layer map (with 15 country icon)
file:///Users/wanyiwang/Desktop/wanyi-tweet-analysis/map.html

# Python second layer map (choropleth map)
In this step, I stocked by error 
"raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 7 column 1 (char 6)"

# Tableau map
In the folder foward. Please check.
<img width="923" alt="screen shot 2018-12-19 at 6 08 13 am" src="https://user-images.githubusercontent.com/31804095/50219557-9e0ced80-035d-11e9-8404-50c5bf1af730.png">

<img width="1137" alt="screen shot 2018-12-19 at 6 08 52 am" src="https://user-images.githubusercontent.com/31804095/50219575-ae24cd00-035d-11e9-9a69-e82b3abf2cde.png">

# Future: 
Keep play on the python visualizaiton. Practice regular expression and data scraping, and find a interesting topic.

# Resources:
Twitter Tweets Guide: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html

Twurl get API: https://developer.twitter.com/en/docs/tutorials/using-twurl.html
https://github.com/twitter/twurl

Google NLP API: https://cloud.google.com/natural-language/docs/quickstart-client-libraries?authuser=1

Python Parsing Twitter: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

Read Jason files: https://jsoneditoronline.org/

Github Instruction: https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/

Leaflet: https://leafletjs.com/

NLTK.tokenize : https://www.nltk.org/api/nltk.tokenize.html

Python Map Creation: https://www.youtube.com/watch?v=4RnU5qKTfYY



