import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


SYSTEM_MESSAGE_TEMPLATE = "You're a helpful assistant"
system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_MESSAGE_TEMPLATE)
HUMAN_MESSAGE_TEMPLATE = "What is the capital of India?"
human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_MESSAGE_TEMPLATE)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])


if __name__ == '__main__':
    load_dotenv()

    os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    response = llm(chat_prompt.format_prompt().to_messages())
    print(response)
