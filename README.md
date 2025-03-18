# Hyperbolic Task Automation Script  

## Overview  
This script automates daily AI-generated tasks, including text, image, and audio generation. It interacts with the **Groq API** (for generating prompts) and the **Hyperbolic API** (for AI-generated content). Users can customize the number of tasks per day and duration.  

## Features  
- **Text Generation**: Generates random questions or phrases and sends them to Hyperbolic Chat API.  
- **Image Generation**: Requests AI-generated image prompts and sends them to Hyperbolic Image API.  
- **Audio Generation**: Generates short AI voice sentences using Hyperbolic Audio API.  
- **Scheduling**: Runs tasks daily for a user-defined number of days.  

## Requirements  
- Python 3.x  
- `requests` module (`pip install requests`)  

## 🔐 How to Get an API Key

### 1. **Groq API Key (TEXT, IMAGE, AUDIO prompt)**
- Visit: [https://console.groq.com/keys](https://console.groq.com/keys)
- Click `+ New Key`, and copy API Key
  

### 2. **Hyperbolic API Key **
- visit: [https://hyperbolic.xyz](https://hyperbolic.xyz)
- Login, go to settings and get api key
- 
## Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/thund3rbreath/hyperbolic-labs
cd hyperbolic-labs
python main.py
