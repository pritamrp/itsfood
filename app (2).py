
# Define the LangChain components
prompt = PromptTemplate(
    input_variables=["prompt"],
    template="You are the master of Nutrition and Great Health. Help others by suggesting food: {prompt}"
)

llm = OpenAI(openai_api_key=key,engine="gpt-3.5-turbo-instruct", temperature=0.7, max_tokens=150)

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
