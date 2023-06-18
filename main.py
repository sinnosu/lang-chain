from os import getenv
from openai_gateway import OpenaiGateway
from dotenv import load_dotenv

def conversation(ai):
    print("\nconversaton start!")
    print("ex: Once upon a time, in a land far, far away, there was a princess who...")
    while 1:
        question = input("\nquestion (q:quit)> ")
        if question == "q":
            print("bye")
            break
        res = ai.generate_response(question)
        print("<answer>", res)

def conversation_by_langchain(ai):
    print("\nconversaton start by lang chain!")
    print("ex: Once upon a time, in a land far, far away, there was a princess who...")
    while 1:
        question = input("\nquestion (q:quit)> ")
        if question == "q":
            print("bye")
            break
        res = ai.generate_langchanin(question)
        print("<answer>", res)

def main():
    # .envファイルの内容を読み込見込む
    load_dotenv()
    ai = OpenaiGateway()
    # conversation()
    conversation_by_langchain(ai)


if __name__ == "__main__":
    main()