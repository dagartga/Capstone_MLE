# streamlit_app.property

import streamlit as st


# Custom imports
from multipage import MultiPage
from pages import project_description, prediction # import your pages here

# Create an instance of the app
app = MultiPage()

st.title("Bitcoin Next Day Price Prediction")

# Add all your application here
app.add_page("Prediction Page", prediction.app)
app.add_page("Project Description", project_description.app)

# run the main app
app.run()
