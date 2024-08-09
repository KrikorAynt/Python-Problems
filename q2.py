############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############
import urllib.request
import xml.etree.ElementTree as ET

google_news_url="https://news.google.com/news/rss"

def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    headlines=[]


    # urllib to open and read rss feed
    url_response = urllib.request.urlopen(rss_url)
    content = url_response.read()
    
    # xml library to parse the data
    parsed_content = ET.fromstring(content)

    for obj in parsed_content.findall('.//item'):
        title = obj.find('title').text
        headlines.append(title)

    return headlines

print(get_headlines(google_news_url))