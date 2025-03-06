from flask import Flask, render_template
import feedparser

app = Flask(__name__)

#Function to fetch and parse an RSS feed
def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed

# Home page route to display the feed
@app.route("/")
def home():
    feed_url = "https://www.the-race.com/feed/"  
    feed = fetch_rss_feed(feed_url)

    # Passing the feed data to the template
    return render_template("index.html", feed=feed)

if __name__ == "__main__":
    app.run(debug=True)