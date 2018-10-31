# sentiment-analyze
# Programming for Cultural Heritage Final Project Proposal
# My Github Repo: https://github.com/WANYIWANG/sentiment-analyze

# Project Description:
The final project of Programming for Culture Heritage is an integrity project with API request, data scraping, semantical analyze, and data visualization. My topic is about the movement of #MeToo on Twitter. The #MeToo movement, with many local and international alternatives, is a movement against sexual harassment and sexual assault. #MeToo spread virally in October 2017 as a hashtag used on social media in an attempt to demonstrate the widespread prevalence of sexual assault and harassment, especially in the workplace. I want to display a geo-semantical map that shows attitudes of people from different countries of the world about #MeToo movement.  

# Which Page I Am:
Right Now, I finished Twitter API key request, used Twurl get 100 tweets about #MeToo and saved it into a text file. I also scripted main information, above user location and tweets content inside of Jason file.
I need more tweets with locations that apply Google NLP API to do the semantic analysis. Eventually, I want to get corresponding user address and tweets and get longitude and latitude by Google Map API.  I will use location information and semantic analysis results(attitude number) to make a map that illustrates how this movement influence people all over the world. The map will be made by Leaflet or D3.JS. 

# Problem: 
Right now, I can only get 100 #MeToo tweets per query, also my second query gets the same result with the first one. 
I right now keep searching for more resources. But preparing for the worst, I may only analysis 100 tweets. I find CSV file of #MeToo tweets in 2017, but without location information: https://data.world/balexturner/390-000-metoo-tweets


# Resources:
Twitter Tweets Guide: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html

Twurl get API: https://developer.twitter.com/en/docs/tutorials/using-twurl.html
https://github.com/twitter/twurl

Google NLP API: https://cloud.google.com/natural-language/docs/quickstart-client-libraries?authuser=1

Python Parsing Twitter: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

Read Jason files: https://jsoneditoronline.org/

Github Instruction: https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/

Leaflet: https://leafletjs.com/



