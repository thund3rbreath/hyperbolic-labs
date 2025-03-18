Hyperbolic Task Automation Script

Overview

This script automates daily AI-generated tasks, including text, image, and audio generation. It interacts with the Groq API (for generating prompts) and the Hyperbolic API (for AI-generated content). Users can customize the number of tasks per day and duration.

Features

Text Generation: Generates random questions or phrases and sends them to Hyperbolic Chat API.

Image Generation: Requests AI-generated image prompts and sends them to Hyperbolic Image API.

Audio Generation: Generates short AI voice sentences using Hyperbolic Audio API.

Scheduling: Runs tasks daily for a user-defined number of days.


Requirements

Python 3.x

requests module (pip install requests)


Setup

1. Clone the Repository

git clone https://github.com/yourusername/ai-task-automation.git
cd ai-task-automation


2. Install Dependencies

pip install requests


3. Set API Keys
Replace GROQ_API_KEY and HYPERBOLIC_API_KEY in the script with your actual API keys.


4. Run the Script

python main.py


5. Follow the Prompts

Enter the number of tasks per day.

Enter the number of days to run the AI.

Select task types (text, image, audio, or all).




Example Output

📅 Day 1 ===========================
📌 TASK 1 - TEXT
🔹 Sent to Hyperbolic: "What is the most underrated travel destination?"
🔸 Response from Hyperbolic: "Bhutan offers breathtaking scenery with limited tourist crowds."

📌 TASK 2 - IMAGE
🔹 Sent to Hyperbolic: "A futuristic city floating in the clouds at sunset."
🔸 Response from Hyperbolic: {"image_url": "https://generated-image-url.com"}

✅ Finished day 1. Waiting for the next day...

Notes

The script will wait 24 hours before starting the next day's tasks (unless modified).

API rate limits may apply depending on your subscription.

Ensure your API keys are kept secure.


License

This project is open-source under the MIT License.


