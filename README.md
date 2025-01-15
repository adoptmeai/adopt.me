# adopt.me
Welcome to **adopt.me**, a Twitter AI bot that lets users adopt their own digital dog! This project combines AI-generated art and a cause-driven mission to support the **Dogs for Better Lives** foundation.

## How It Works

1. **Interaction with the Bot**:
   - Users interact with the bot by replying to any of its tweets or mentions with the following message:
     ```
     I'd like to adopt a dog @adoptdotme
     ```
   - The bot will process the request and reply with a unique AI-generated image of a digital dog.

2. **Donation Integration**:
   - Users who adopt a digital dog will also have the opportunity to donate to the **Dogs for Better Lives** foundation. A donation link will be included in the bot’s reply.

3. **Personalized Experience**:
   - Each user receives a one-of-a-kind digital dog, ready to be their online best friend.

---

## Features

- **AI-Generated Dog Images**:
  - The bot uses advanced AI to create custom images of digital dogs, ensuring that no two dogs are alike.

- **Donation Support**:
  - A clear, user-friendly link to support the Dogs for Better Lives foundation.

- **Automatic Replies**:
  - The bot processes replies and generates responses automatically using the Twitter API.

- **Scalable and Reliable**:
  - Built with robust architecture to handle high levels of engagement.

---

## Tech Stack

- **Backend**: Python (Flask)
- **AI Generation**: OpenAI API for image generation
- **Twitter Integration**: Tweepy (Python library for Twitter API)
- **Hosting**: AWS Lambda or similar cloud service

---

## Getting Started

### Prerequisites

1. Python 3.9 or later
2. Twitter Developer Account with API access
3. OpenAI API key
4. Hosting account (e.g., AWS, Azure, Heroku)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/adopt.me.git
   cd adopt.me
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the root directory and add the following:
     ```env
     TWITTER_API_KEY=your_twitter_api_key
     TWITTER_API_SECRET_KEY=your_twitter_secret_key
     TWITTER_ACCESS_TOKEN=your_twitter_access_token
     TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
     OPENAI_API_KEY=your_openai_api_key
     DONATION_URL=https://www.dogsforbetterlives.org/donate
     ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

1. **Trigger the Bot**:
   - Reply to any tweet with the specified adoption message format.

2. **Monitor Logs**:
   - Use the logging system to monitor requests and bot activity:
     ```bash
     tail -f logs/adoptme.log
     ```

3. **Deploy**:
   - Deploy the application using your preferred hosting service.

---

## Code Overview

### Main Files

- `app.py`: Main application logic for handling Twitter interactions and AI image generation.
- `dog_generator.py`: Logic for generating unique AI images and descriptions for the digital dogs.
- `twitter_bot.py`: Handles Twitter API interactions, including reading replies and posting responses.
- `requirements.txt`: List of Python dependencies.

### API Workflow

1. The bot checks for mentions containing the adoption phrase.
2. It processes the request and sends the user’s input to the AI API to generate a digital dog image.
3. The bot replies to the user with the generated image and a donation link.
4. Logs the interaction for auditing and monitoring purposes.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your branch and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- A big shoutout to the Dogs for Better Lives foundation for their amazing work.

---

## Social Media

Follow us on Twitter for updates and announcements: [https://x.com/adoptdotme](https://x.com/adoptdotme)
