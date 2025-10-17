import os

from langchain_openai import ChatOpenAI
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

models = {
    "gpt": "openai/gpt-oss-20b:free",
    "deepseek": "deepseek/deepseek-chat-v3.1:free",
}


def get_llm(model):
    if model == "giga":
        return GigaChat(
            credentials=os.getenv("GIGACHAT_KEY"),
            verify_ssl_certs=False,
        )
    else:
        return ChatOpenAI(
            model=models[model],
            api_key=os.getenv("OPENROUTER_KEY"),
            base_url="https://openrouter.ai/api/v1",
            temperature=0.0,
        )


def prepare_messages(character,input):
    person = {
        'giga': 'Александр Друзь',
        'gpt': 'Бенджамин Франклин',
        'deepseek': 'Конфуций'
    }
    messages = [
        SystemMessage(
            content=f"Ты – {person[character]}, один из мудрейших людей в мире. Твя задача - ответить на вопрос в максимально схожем с исторической персоной стиле."
        ),
        HumanMessage(
            content=f"{input}"
        ),
    ]
    return messages
