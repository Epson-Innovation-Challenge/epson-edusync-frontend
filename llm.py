from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompts import load_generation_prompt

def generate_question(question):
    """
    Question generation chain.
    """
    prompt = load_generation_prompt()
    llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.1, max_tokens=2048)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": question})

    return response
