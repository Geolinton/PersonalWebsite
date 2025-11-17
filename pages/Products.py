import streamlit as st

page_title = "Praise's Products Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")

productsList = []

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
            with st.container():
                # input("Add a new project (name, description, link):")
                if st.button("Add Project"):
                    newProdInfo = st.text_input("Add a new project. Use this format: name, description, link:")
                    info = newProdInfo.split(",")
                    if len(info) <= 3 and len(info) > 0:
                        name = info[0].strip()
                        desc = info[1].strip() if len(info) > 1 else ""
                        link = info[2].strip() if len(info) > 2 else ""
                        Product.addProduct(name, desc, link)
                        st.success(f"Project '{name}' added!")
                    else:    
                        name = info[0].strip() if len(info) > 0 else ""
                        desc = info[1].strip() if len(info) > 1 else ""
                        link = info[2].strip() if len(info) > 2 else ""
                        allElse = [f"{w}," if w == info[-1] else f"{w}" for w in info[3:]] if len(info) > 3 else ""
                        Product.addProduct(name, desc, link)
                        st.error(f"Project '{name}' not added!\nWrong inputS:\n{allElse}")

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


class Product:
    def __init__(self, name, description, link):
        self.name = name
        self.description = description
        self.link = link
    
    def displayProduct(self):
        st.subheader(self.name)
        st.write(self.description)
        st.markdown(f"[Learn more]({self.link})")

    def addProduct(name, desc, link):
        newProdcut = Product(name, desc, link)
        productsList.append(newProdcut)
    
    def removeProduct(name):
        global productsList
        productsList = [product for product in productsList if product.name != name]

main()
