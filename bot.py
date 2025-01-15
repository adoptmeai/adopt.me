import tweepy
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Twitter API keys
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# AI Image Generator API key
AI_IMAGE_API_KEY = os.getenv("AI_IMAGE_API_KEY")

# Initialize Twitter API client
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitter_api = tweepy.API(auth)

# Function to generate a dog image
def generate_dog_image():
    response = requests.post(
        "https://api.example.com/generate",  # Replace with actual API URL
        headers={"Authorization": f"Bearer {AI_IMAGE_API_KEY}"}
    )
    if response.status_code == 200:
        return response.json()["image_url"]
    return None

# Function to respond to tweets
def respond_to_tweets():
    mentions = twitter_api.mentions_timeline()
    for mention in mentions:
        if "i'd like to adopt a dog" in mention.text.lower():
            dog_image = generate_dog_image()
            if dog_image:
                message = f"Meet your new dog! 🐶 Personality: Playful\nSupport real dogs: https://www.dogsforbetterlives.org/donate"
                twitter_api.update_status_with_media(
                    status=message, 
                    filename="dog_image.jpg", 
                    file=requests.get(dog_image).content, 
                    in_reply_to_status_id=mention.id
                )

# Run the bot
if __name__ == "__main__":
    respond_to_tweets()
