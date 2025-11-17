import streamlit as st

page_title = "Praise's Contact Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")


def contactPage():
    st.title(page_title + " :house_with_garden:")
    st.markdown(f"""
        Welcome to {page_title}! You can reach out to me here!
    """)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Contact", "Home", "Products", "Presentations", "Story"])

    if page == "Contact":
        contactPage()
    elif page == "Projects":
        st.switch_page("pages/Products.py")
    elif page == "Presentations":
        st.switch_page("pages/Presentations.py")
    elif page == "Home":
        st.switch_page("homePage.py")
    elif page == "Story":
        st.write("pages/Story.py")
            

main()