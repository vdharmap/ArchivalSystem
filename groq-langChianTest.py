from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    # api_key="" # Optional if not set as an environment variable
)

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
chain.invoke({"text": "Explain the importance of low latency for LLMs."})