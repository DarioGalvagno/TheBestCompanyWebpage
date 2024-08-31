import streamlit as st
import pandas


with st.container():
    st.title("The Best Company")
    content = """
Welcome to The Best Company, where excellence isn't just a goal—it's our identity. 
Founded with a passion for innovation and a commitment to quality, we strive to set new standards in everything we do. 
Whether you're looking for cutting-edge technology, unparalleled service, or industry-leading expertise, 
The Best Company delivers solutions that exceed expectations.

Our team is a diverse group of talented professionals who share a common belief in the power of collaboration and 
the drive to achieve greatness. We are dedicated to building lasting relationships with our clients, partners, 
and communities, ensuring that every interaction reflects our core values of integrity, creativity, and excellence.

At The Best Company, we don’t just aim to be the best—we aim to be better every day. 
Join us on our journey as we continue to push boundaries, inspire change, and lead the way in our industry.
 Welcome to a world where the best is yet to come.
    """
    st.write(content)
    st.header("Our Team")

col1, empty1, col2, empty2, col3,empty3 = st.columns([1, 0.2, 1, 0.2, 1,0.2])
df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index,row in df[:4].iterrows():
        st.header(row["first name"].title())
        st.header(row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])



with col2:
    for index,row in df[4:8].iterrows():
        st.header(row["first name"].title())
        st.header(row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])



with col3:
    for index,row in df[8:12].iterrows():
        st.header(row["first name"].title())
        st.header(row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])




