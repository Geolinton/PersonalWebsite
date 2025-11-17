import streamlit as st

page_title = "Praise's Home Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")

def homePage():
    st.title(page_title + " :house_with_garden:")
    st.markdown("""
        Welcome to Praise's Home Page! This application is designed to help you train machine learning models and view detailed results of your experiments.

        ### Features:
        - **Train Model**: Navigate to the training page to build and train your machine learning models.
        - **Detailed Results**: View comprehensive results and analyses of your model training experiments.
        - **About**: Learn more about this application and its purpose.
        - **Contact**: Get in touch for support or inquiries.

        Use the sidebar to navigate through different sections of the application.
    """)

def main():
    # st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Products", "Presentations", "Story", "Contact"])

    if page == "Home":
        homePage()
    elif page == "Products":
        st.switch_page("pages/Products.py")
    elif page == "Presentations":
        st.switch_page("pages/Presentations.py")
    elif page == "Story":
        # st.title("About Page")
        st.switch_page("pages/Story.py")
    elif page == "Contact":
        # st.title("Contact Page")
        st.switch_page("pages/Contact.py")
            

main()