import streamlit as st

page_title = "Praise's Products Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")


def productsPage():
    st.title(page_title + " :house_with_garden:")
    st.markdown(f"""
        Welcome to {page_title}! You can view my projects, publications, and the likes here!
    """)

    # whole page
    with st.container():
        prjs, pubs = st.columns(2)

        with prjs:
            st.header("Projects")
            st.markdown("""
            - **Project 1**: Description of project 1.
            - **Project 2**: Description of project 2.
            - **Project 3**: Description of project 3.
            """)

        with pubs:
            st.header("Publications")
            st.markdown("""
            - **Publication 1**: Description of publication 1.
            - **Publication 2**: Description of publication 2.
            - **Publication 3**: Description of publication 3.
            """)

def main():
    # st.sidebar.title("Navigation")
    # page = st.sidebar.selectbox("Go to", ["Products", "Home", "Presentations", "Story", "Contact"])
    page = "Products"

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