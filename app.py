import streamlit as st

from llm import get_llm, prepare_messages


st.title("Задай вопрос ИИ!")

llm_choice = st.radio("Кто будет отвечать на вопрос:", ['Александр Друзь (GigaChat)', 'Бенджамин Франклин (ChatGpt)', 'Конфуций (DeepSeek)'])

text = st.text_input("Напишите ваш вопрос:", "")

if st.button("Получить ответ"):
    try:
        if llm_choice == 'Александр Друзь (GigaChat)':
            person = 'giga'         
        elif llm_choice == 'Бенджамин Франклин (ChatGpt)':
            person = 'gpt'
        else:
            person = 'giga'

        llm = get_llm(person) 
        text_message = prepare_messages(person,text)

        result = llm.invoke(text_message)

        st.success(result.content)
    except Exception as e:
        print(e)
        st.error("Что-то пошло не так....")
    
