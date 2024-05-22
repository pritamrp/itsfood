import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the LangChain components
prompt = PromptTemplate(
    input_variables=["prompt"],
    template="You are a helpful assistant. Answer the following question: {prompt}"
)

llm = OpenAI(engine="text-davinci-003", temperature=0.7, max_tokens=150)

chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit app
st.title("LLM Web App")
st.write("Enter your prompt below to get a response from the language model.")

prompt_input = st.text_input("Prompt")

if st.button("Generate Response"):
    if prompt_input:
        response = chain.run({"prompt": prompt_input})
        st.write("Response:")
        st.write(response)
    else:
        st.write("Please enter a prompt.")
