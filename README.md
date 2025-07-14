# 🤖 Groq Chatbot Telegram Bot

A simple, conversational Telegram bot powered by the Groq API and Telebot (pyTelegramBotAPI). This bot responds to user messages using a large language model via Groq’s chat completions API.

---

## ✨ Features

* Natural language conversation using Groq LLMs
* Supports custom models via environment variable
* Automatic error handling with auto-restart
* Lightweight, easy-to-deploy Python script

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shivkumars005/GroqTelegramBot.git
cd GroqTelegramBot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file in the root directory:

```
BOT_TOKEN=your-telegram-bot-token
GROQ_API_KEY=your-groq-api-key
GROQ_MODEL=llama-3.3-70b-versatile  # Optional: defaults to this model
```

✅ Make sure `.env` is added to `.gitignore` to keep your credentials secure.

### 4️⃣ Run the Bot

```bash
python bot.py
```

---

## 🛠️ Project Structure

```
├── bot.py                # Main bot script
├── .env                  # Environment variables (not pushed to repo)
├── .gitignore            # Files to ignore in git
├── requirements.txt      # Python dependencies
└── README.md             # Project README
```

---

## 📋 Bot Commands

* `/start`, `/hello`, or `/hi` – Sends a greeting and instructions.
* Any text message – The bot replies using Groq LLM responses.

---

## 📎 Dependencies

* Python 3.8+
* `pyTelegramBotAPI`
* `requests`
* `python-dotenv`

Install everything with:

```bash
pip install -r requirements.txt
```

---

## ✅ Example Usage

* User sends `/hello`.
* Bot replies: `"👋 Hey there! I’m your Groq-powered chatbot. Just type your question or message!"`
* User types: `"Tell me a joke."`
* Bot sends back a Groq LLM-generated response.

---

## ⚠️ Notes

* Ensure your Telegram bot token and Groq API key are valid.
* Default model: `llama-3.3-70b-versatile` (configurable via `.env`).
* Be mindful of your API quota and rate limits from Groq.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙏 Credits

* Groq API
* Python Telegram Bot Community

---