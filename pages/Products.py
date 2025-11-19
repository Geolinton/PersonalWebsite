import streamlit as st
import time

page_title = "Praise's Products Page"
st.set_page_config(page_title=page_title, page_icon=":house_with_garden:",layout="wide", initial_sidebar_state="auto")


done = True
newProductInfo = ""


class Product:
    def __init__(self, name, description, link):
        self.name = name
        self.description = description
        self.link = link
    
    def displayProduct(self):
        with st.container(height = 150, border=False):
            st.info(f"""
                {self.name}\n
                {self.description}\n
                [Learn more]({self.link})
                    """)
            # st.subheader(self.name)
            # st.write(self.description)
            # st.markdown(f"[Learn more]({self.link})")

    def addProduct(name, desc, link):
        newProduct = Product(name, desc, link)
        st.session_state.productsList.append(newProduct)
    
    def removeProduct(name):
        global productsList
        productsList = [product for product in productsList if product.name != name]

productsList = [
    Product("Fisher", "A digital fish finding system", "www.fisherman.com"),
    Product("Pricer", "A digital price finding system", "www.Pricerman.com"),
    Product("Vaulter", "A digital vault finding system", "www.Vaulterman.com")
]

if "productsList" not in st.session_state:
    st.session_state.productsList = productsList

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
            # show current projects
            with st.container():
                st.subheader("Current Projects:")
                with st.container(border=True, height=325):
                    if len(productsList) == 0:
                        st.write("No projects added yet.")
                    else:
                        for product in st.session_state.productsList:
                            product.displayProduct()

            # add new project
            with st.container():
                st.subheader("Add New Project:")
                with st.form(key="add_product_form"):
                    name = st.text_input("Project Name")
                    desc = st.text_area("Project Description")
                    link = st.text_input("Project Link")
                    submit_button = st.form_submit_button(label="Add Project")

                    if submit_button:
                        if name and desc and link:
                            Product.addProduct(name, desc, link)
                            st.success(f"Project '{name}' added successfully!")
                        else:
                            st.error("Please fill in all fields to add a project.")
            

        with pubs:
            st.header("Publications")
            st.markdown("""
            - **Publication 1**: Description of publication 1.
            - **Publication 2**: Description of publication 2.
            - **Publication 3**: Description of publication 3.
            """)

def main():
    # st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Products", "Home", "Presentations", "Story", "Contact"])
    # page = "Products"

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
