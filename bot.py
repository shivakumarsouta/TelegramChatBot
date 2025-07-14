import os
import requests
import telebot
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-3.3-70b-versatile') 

bot = telebot.TeleBot(BOT_TOKEN)

# Function to get response from Groq API
def get_chatbot_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        message = data['choices'][0]['message']['content'].strip()
        return message
    except Exception as e:
        print(f"Error fetching Groq response: {e}")
        return "Sorry, I couldn't process your request right now. Please try again later."


@bot.message_handler(commands=['start', 'hello', 'hi'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hey there! I’m your Groq-powered chatbot. Just type your question or message!")


@bot.message_handler(func=lambda msg: True)
def chatbot_handler(message):
    user_text = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    response = get_chatbot_response(user_text)
    bot.reply_to(message, response)


if __name__ == "__main__":
    while True:
        try:
            print("Bot is running...")
            bot.infinity_polling()
        except Exception as e:
            print(f"Bot crashed. Restarting... Error: {e}")
            time.sleep(5)
