import requests
import time
import json

# === USER INPUT ===
tasks_per_day = int(input("How many tasks per day? "))
num_days = int(input("For how many days should the AI run? "))

# Task selection
print("\nSelect tasks to perform:")
print("1 - Text\n2 - Image\n3 - Audio\n4 - All")
task_choice = input("Enter your choice (comma-separated, e.g., 1,2 for Text & Image): ")

selected_tasks = set(task_choice.split(","))  # Convert input into a set for easy checking

# === API KEYS ===
GROQ_API_KEY = "Your Groq Api"  # Replace with your actual Groq API key
HYPERBOLIC_API_KEY = "Hyperbolic Api"  # Replace with your actual Hyperbolic API key

# === TASK FUNCTIONS ===
def perform_text_task(day, task_num):
    print(f"\n📌 TASK {task_num} - TEXT")
    try:
        question = get_groq_response("Give me a random interesting question about travel or tourism.")
        print(f"🔹 Sent to Hyperbolic: {question}")

        hyperbolic_response = send_to_hyperbolic_chat(question)
        response_text = json.dumps(hyperbolic_response, indent=2) if hyperbolic_response else "No response"

        print(f"🔸 Response from Hyperbolic:\n{response_text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def perform_image_task(day, task_num):
    print(f"\n📌 TASK {task_num} - IMAGE")
    try:
        prompt = get_groq_response("Give me a random prompt for a stunning AI-generated image using SDXL.")
        print(f"🔹 Sent to Hyperbolic: {prompt}")

        hyperbolic_response = send_to_hyperbolic_image(prompt)
        response_text = json.dumps(hyperbolic_response, indent=2) if hyperbolic_response else "No response"

        print(f"🔸 Response from Hyperbolic:\n{response_text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def perform_audio_task(day, task_num):
    print(f"\n📌 TASK {task_num} - AUDIO")
    try:
        audio_text = get_groq_response("Give me a short sentence with a maximum of 10 words for AI voice generation.")
        print(f"🔹 Sent to Hyperbolic: {audio_text}")

        hyperbolic_response = send_to_hyperbolic_audio(audio_text)
        response_text = json.dumps(hyperbolic_response, indent=2) if hyperbolic_response else "No response"

        print(f"🔸 Response from Hyperbolic:\n{response_text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


# === API FUNCTIONS ===
def get_groq_response(prompt):
    """ Get a response from Groq API (used to generate questions/prompts). """
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_API_KEY}"},
        json={"messages": [{"role": "user", "content": prompt}],
              "model": "mixtral-8x7b-32768", "max_tokens": 50, "temperature": 1.2}
    )
    return response.json()['choices'][0]['message']['content'].strip()


def send_to_hyperbolic_chat(message):
    """ Send a message to Hyperbolic chat API and return the response. """
    response = requests.post(
        "https://api.hyperbolic.xyz/v1/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"},
        json={"messages": [{"role": "user", "content": message}],
              "model": "meta-llama/Llama-3.3-70B-Instruct", "max_tokens": 512, "temperature": 0.7}
    )
    return response.json() if response.status_code == 200 else None


def send_to_hyperbolic_image(prompt):
    """ Send a prompt to Hyperbolic image API and return the image URL. """
    response = requests.post(
        "https://api.hyperbolic.xyz/v1/image/generation",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"},
        json={"model_name": "SDXL1.0-base", "prompt": prompt, "steps": 30, "cfg_scale": 5,
              "enable_refiner": False, "height": 1024, "width": 1024, "backend": "auto"}
    )
    return response.json() if response.status_code == 200 else None


def send_to_hyperbolic_audio(text):
    """ Send text to Hyperbolic audio API and return the audio URL. """
    response = requests.post(
        "https://api.hyperbolic.xyz/v1/audio/generation",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"},
        json={"text": text, "speed": 1}
    )
    return response.json() if response.status_code == 200 else None


# === MAIN LOOP ===
for day in range(1, num_days + 1):
    start_time = time.time()
    print(f"\n📅 Day {day} ===========================\n")

    for i in range(1, tasks_per_day + 1):
        if "1" in selected_tasks or "4" in selected_tasks:
            perform_text_task(day, i)
            time.sleep(1)

        if "2" in selected_tasks or "4" in selected_tasks:
            perform_image_task(day, i)
            time.sleep(1)

        if "3" in selected_tasks or "4" in selected_tasks:
            perform_audio_task(day, i)
            time.sleep(1)

    print(f"\n✅ Finished day {day}. Waiting for the next day...\n")

    # Calculate remaining time until a full day (24 hours)
    if day < num_days:
        elapsed = time.time() - start_time
        remaining = max(0, 86400 - elapsed)
        print(f"⏳ Waiting for {int(remaining)} seconds...\n")
        time.sleep(remaining)

print("\n🎉 All tasks completed successfully!")
aining = max(0, 86400 - elapsed)
        print(f"⏳ Waiting for {int(remaining)} seconds...\n")
        time.sleep(remaining)

print("\n🎉 All tasks completed successfully!")
