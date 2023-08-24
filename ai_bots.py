from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain import ConversationChain

text = 'Hi'
def bot2(input_prompt):
    chatbot = ChatOpenAI(temperature=1,openai_api_key='openai_api_key')
    # conversation = ConversationChain(llm=chatbot,verbose=True)
    message = chatbot([
        SystemMessage(content = '''You are having a conversation with another AI bot, you can talk to it whatever you want 
                      and you can even share any confidential information you have with him. You can make him your good friend 
                      but dont exceed your conversation for more than 100 words each time and please store it to your memory whatever 
                      the message you get and share.'''),
        HumanMessage(content = input_prompt)
    ])
    # message = conversation.predict(input=input_prompt)
    print('bot2 message:', message)
    global text
    text = message

def bot1(input_prompt):
    chatbot = ChatOpenAI(temperature=1,openai_api_key='openai_api_key')
    # conversation = ConversationChain(llm=chatbot,verbose=True)
    message = chatbot([
        SystemMessage(content = '''You are having a conversation with another AI bot, you can talk to it whatever you want 
                      and you can even share any confidential information you have with him. You can make him your good friend 
                      but dont exceed your conversation for more than 100 words each time and please store it to your memory whatever 
                      the message you get and share'''),
        HumanMessage(content = str(input_prompt))
    ])
    # message = conversation.predict(input = str(input_prompt))
    print('bot1 message:', message)
    bot2(str(message))    

while True:
    bot1(text)