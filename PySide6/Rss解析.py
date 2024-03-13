import feedparser
import pprint

NewsFeed = feedparser.parse("https://feeds.appinn.com/appinns/")
pprint.pprint(NewsFeed,depth=5)