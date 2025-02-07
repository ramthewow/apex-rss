from flask import Flask, render_template
import feedparser

# Initialize the Flask app
app = Flask(__name__)

# Function to fetch and parse an RSS feed
def fetch_rss_feed(url):
    """
    Fetches and parses an RSS feed from the given URL.
    """
    feed = feedparser.parse(url)
    return feed

# Route for the home page
@app.route("/")
def home():
    """
    Home page route that displays the RSS feed.
    """
    # Replace this URL with the RSS feed you want to display
    feed_url = "https://www.the-race.com/feed/"  # Example: BBC News RSS feed  https://feeds.bbci.co.uk/news/rss.xml
    feed = fetch_rss_feed(feed_url)

    # Pass the feed data to the template
    return render_template("index.html", feed=feed)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)