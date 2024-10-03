import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aptitude_"]
collection = db["questions"]


st.title("Quantitative Aptitude Test")

# Fetch questions from MongoDB
questions = list(collection.find())

for question in questions:
    st.subheader(question["question_text"])

    if question["type"] == "MCQ":
        options = [opt["option_text"] for opt in question["options"]]
        selected_option = st.radio("Choose an option:", options)

        if st.button("Submit"):
            if selected_option == question["correct_answer"]:
                st.success("Correct!")
            else:
                st.error("Incorrect! The correct answer is: " + question["correct_answer"])
    elif question["type"] == "Short Answer":
        user_answer = st.text_input("Your answer:")

        if st.button("Submit"):
            if user_answer == question["correct_answer"]:
                st.success("Correct!")
            else:
                st.error("Incorrect! The correct answer is: " + question["correct_answer"])

