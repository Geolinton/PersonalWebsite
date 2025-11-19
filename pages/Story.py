import streamlit as st

page_title = "Praise's Story Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")


def storyPage():
    st.title(page_title + " :house_with_garden:")
    st.markdown(f"""
        Welcome to {page_title}! You can learn a lot about me here!
    """)

def main():
    # st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Story", "Home", "Products", "Presentations", "Contact"])
    # page = "Story"

    if page == "Story":
        storyPage()
    elif page == "Projects":
        st.switch_page("pages/Products.py")
    elif page == "Presentations":
        st.switch_page("pages/Presentations.py")
    elif page == "Home":
        st.switch_page("homePage.py")
    elif page == "Contact":
        st.switch_page("pages/Contact.py")
            

main()