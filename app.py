import streamlit as st

st.set_page_config(page_title="VidyaMitra", page_icon="📘")

# Your lessons: a keyword and its explanation.
# Later, write these in YOUR OWN words and add more topics.
lessons = {
    "photosynthesis": "Plants make food using sunlight, water and air. A leaf is like a kitchen that cooks with sunlight.",
    "gravity": "Gravity pulls things down to the Earth. That is why a mango falls down from the tree.",
    "fraction": "A fraction is a part of a whole. If you cut a roti into 4 equal pieces and eat 1, you ate 1/4 of it.",
    "water cycle": "The sun heats water and it rises as vapour. High up it cools and makes clouds. Then it falls as rain.",
    "noun": "A noun is the name of a person, place or thing. In 'Ravi has a book', Ravi and book are nouns.",
}


def get_answer(question):
    for word, explanation in lessons.items():
        if word in question.lower():
            return explanation
    return "I do not know this topic yet. Try another one."


with st.sidebar:
    st.title("📘 VidyaMitra")
    st.caption("Your study friend | SDG 4: Quality Education")
    name = st.text_input("Your name")
    cls = st.selectbox("Class", [6, 7, 8, 9, 10])
    subject = st.selectbox("Subject", ["Maths", "Science", "English"])

st.header(f"Hello {name or 'Student'}! 👋")
tab1, tab2, tab3 = st.tabs(["Ask the Tutor", "Adaptive Quiz", "My Progress"])

with tab1:
    st.write(f"Ask any Class {cls} {subject} doubt.")
    question = st.chat_input("Type your doubt here...")
    if question:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            st.write(get_answer(question))

with tab2:
    st.write("The quiz is coming soon.")

with tab3:
    st.write("Your progress will appear here.")