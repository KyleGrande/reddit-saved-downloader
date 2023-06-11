import praw
import csv
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

# Create a Reddit instance
reddit = praw.Reddit(client_id=client_id,  
                     client_secret=client_secret,
                     user_agent='my_user_agent', 
                     username=username,  
                     password=password) 

def save_posts():
    with open('saved_posts.csv', 'w', newline='') as f:
        fieldnames = ['Title', 'URL', 'Body', 'Reddit_Link']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for post in reddit.user.me().saved(limit=None):
            if isinstance(post, praw.models.Submission):
                writer.writerow({'Title': post.title, 'URL': post.url, 'Body': post.selftext, 'Reddit_Link': 'https://reddit.com' + post.permalink})

def save_comments():
    with open('saved_comments.csv', 'w', newline='') as f:
        fieldnames = ['Comment']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for comment in reddit.user.me().saved(limit=None):
            if isinstance(comment, praw.models.Comment):
                writer.writerow({'Comment': comment.body})

def main():
    save_posts()
    save_comments()

if __name__ == "__main__":
    main()