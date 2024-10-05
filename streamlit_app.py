def main():
    load_dotenv()
    
    # Load the OpenAI API key from the environment variable
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY") == "":
        print("GOOGLE_API_KEY is not set")
        exit(1)
    else:
        print("GOOGLE_API_KEY is set")
    df = pd.read_csv("LegalPioneer Data - legalpioneer_profiles.csv")
    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")
    st.write(df.head())
    st.html("Example Prompts: <br> Which County raised the greatest amount of money? <br> Who in the Area of Automation has the most raised money? <br> Which Name has raised the most money in Ireland?")

   


    #csv_file = convert_df(df)
    #csv_file = st.file_uploader("Upload a CSV file", type="csv")
    
    agent = create_csv_agent(
        GoogleGenerativeAI(temperature=.5, model="gemini-pro"), "LegalPioneer Data - legalpioneer_profiles.csv", verbose=True, allow_dangerous_code=True)

    user_question = st.text_input("Ask a question about your CSV: ")

    if user_question is not None and user_question != "":
        with st.spinner(text="In progress..."):
            st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
