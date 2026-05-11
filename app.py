from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",   # fast + free model
    temperature=0.7
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a helpful AI assistant. Answer the question: {question}"
)

# Create chain
chain = prompt | llm

# Chat loop
print("AI Assistant Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break
        
    response = chain.invoke({"question": user_input})
    print("AI:", response.content)
