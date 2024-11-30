import requests
import json
import telebot


with open('api_key', 'r') as file:
    PROXY_API_KEY = file.readline().strip()
with open('tg_token', 'r') as file:
    TG_TOKEN = file.readline().strip()

bot = telebot.TeleBot(TG_TOKEN)

# URL для запроса
url = "https://api.proxyapi.ru/openai/v1/chat/completions"

# Заголовки запроса
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {PROXY_API_KEY}"
}


def quest(question):
    with open('db.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    data = {
        "model": "gpt-4-turbo",
        "messages": [{f"role": "user", "content": f"Привет. Ты чат-помощник компании GitPro. Вот типовые вопросы с ответами: {text}. Отвечай на вопросы пользователя по этому справочнику. На вопросы, которых нет в справочнике отвечай сам, либо отказывай в ответе, если вопрос не по теме компании. Вопрос пользователя: {question}"}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        bot_response = response.json()['choices'][0]['message']['content']
        return bot_response
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.text)


@bot.message_handler()
def Bot_Start(msg):
    text = quest(msg.text)
    bot.reply_to(msg, text)


bot.infinity_polling()
