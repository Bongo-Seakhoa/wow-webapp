import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    You can find more information by using the following links:

    Web App URL: <Here>

    GitHub repository: <https://github.com/DarkSpace56831>
    """
)

st.title("Wow web-app")

st.markdown(
    """
    This multi-page web app demonstrates was created to easily give stakeholders an overview of maker conditions in relation to the camping and caravaning sector in Australia, Predictive modeling has also been used to facilitate the user
    guaging further into the future and enhance descision making.
    """
)

st.info("Click on the left sidebar menu to navigate to the different pages.")

st.subheader("Page overview")
st.markdown(""" This section is intended to give you a brief overview of the different pages in this dashboard. There are also additional notebooks you can look at to see how the data was sourced and cleaned to create these visualizations they are the following:""")
st.markdown("""

        Notebooks for each page:

            Client Demographics :   [Click here](http://localhost:8501/Client_Demographics)

            Climate :               [Click here](http://localhost:8501/Climate)

            Sentiment :             [Click here](http://localhost:8501/Sentiment)
        """)

row1_col1, row1_col2, row1_col3 = st.columns(3)
with row1_col1:
    st.subheader("Client Demographics")
    st.markdown(""" These are our client demographics across the camping and caravaning sector, we are most focused on longer stays of 30 days or more. 
    [Go to page](http://localhost:8501/Client_Demographics#client-demographics)""")

with row1_col2:
    st.subheader("Climate")
    st.markdown("""This dashboard contains weather and climate related data visualized so that the user can easily understand it. [Go to page](http://localhost:8501/Climate#climate-and-weather)""")

with row1_col3:
    st.subheader("Sentiment")
    st.markdown("""This dashboard contains sentiments and social media trend data. [Go to page]()""")

