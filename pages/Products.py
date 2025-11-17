import streamlit as st

page_title = "Praise's Products Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")


def productsPage():
    st.title(page_title + " :house_with_garden:")
    st.markdown(f"""
        Welcome to {page_title}! You can view my projects, publications, and the likes here!
    """)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Products", "Home", "Presentations", "Story", "Contact"])

    if page == "Products":
        productsPage()
    elif page == "Contact":
        st.switch_page("pages/Contact.py")
    elif page == "Presentations":
        st.switch_page("pages/Presentations.py")
    elif page == "Home":
        st.switch_page("homePage.py")
    elif page == "Story":
        st.switch_page("pages/Story.py")
            

main()