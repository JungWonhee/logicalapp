#Scripts\activate.bat
#streamlit run app.py

import openai
import streamlit as st

messages = []
content = ""
chat_response = ""


openai.api_key = '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'

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        st.sidebar.title("추론 프로그램")
        st.sidebar.subheader("어떤 방법으로 추론하시겠습니까?")
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])
    
        app['function']()

def g():
    global content
    st.title("귀납법 프로그램 실행합니다.")
    Ginfer1 = st.text_input("개별적 사실 (여러 문장 입력시 ,로 구분해서 쓰시오.)", value = "(ex. A새는 난다, B새는 난다, C새는 난다)")
    Ginfer2 = st.text_input("소전제", value = "(ex. A새, B새, C새는 모두 새다)")
    if st.button("입력"):
        content = f"귀납법으로 추론, 개별적 사실은 {Ginfer1}, 소전제는 {Ginfer2}, 결론만 출력"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a philosopher"},
                {"role": "user", "content": content}
            ]
        )

    # 응답 결과 표시
        chat_response = completion.choices[0].message.content
        st.text(chat_response)

def y():
    global content
    st.title("연역법 프로그램 실행합니다.")
    Yinfer1 = st.text_input("대전제", value = "(ex. 모든 사람은 죽는다)")
    Yinfer2 = st.text_input("소전제", value = "(ex. 소크라테스는 사람이다)")
    if st.button("입력"):
        content = f"연역법으로 추론, 대전제는 {Yinfer1} 소전제는 {Yinfer2}, 결론만 출력"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a philosopher"},
                {"role": "user", "content": content}
            ]
        )

    # 응답 결과 표시
        chat_response = completion.choices[0].message.content
        st.text(chat_response)
        
infer = MultiApp()
infer.add_app("귀납법 입력", g)
infer.add_app("연역법 입력", y)
infer.run()
