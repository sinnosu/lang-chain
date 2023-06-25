from os import getenv
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)

class OpenaiGateway:
    def __init__(self):
        API_KEY = getenv("OPENAI_SECRET_KEY", "-")
        self.model_engine = "text-davinci-003"
        self.llm = OpenAI(temperature=0.7, openai_api_key=API_KEY)
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=API_KEY)
        openai.api_key = API_KEY

    def langchain_chat_model(self,sys_msg, human_msg):
        # llm = OpenAI(self.model_engine)
        response = self.llm(text)
        return response

    def generate_langchanin(self, text):
        # llm = OpenAI(self.model_engine)
        response = self.llm(text)
        return response

    def generate_response(self, text):
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=text,
            max_tokens=1024, # Temperature: ランダムさ。創造的にするには0.9、答えがある場合は0推奨。top_pと同時変更は非推奨
            n=1,
            stop=None,
            temperature=0.9,
        )
        response = completion.choices[0].text
        return response
