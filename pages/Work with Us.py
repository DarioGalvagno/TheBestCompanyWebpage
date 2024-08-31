import streamlit as st
import pandas



st.title("Work with Us")
st.header("Join Our Team and Make a Difference")
content="""
At The Best Company, we're more than just a workplace—we're a community of passionate, innovative,
and driven individuals who are committed to making a positive impact in the world.
Whether you're a seasoned professional or just starting your career, we offer a dynamic environment where you can grow, 
learn, and contribute to exciting projects that matter.
"""
st.write(content)

st.header("Why Work With Us?")
st.subheader("1. Purposeful Work:")
content="""
Our projects are designed to solve real-world problems. 
You'll be working on meaningful initiatives that have a tangible impact on our clients, customers,
 and the world at large.
"""
st.write(content)
st.subheader("2. Growth Opportunities:")
content="""
We believe in continuous learning and development. With access to a variety of training programs, workshops, 
and mentorship, you'll have the resources you need to advance your career.
"""
st.write(content)

st.subheader("3. Inclusive Culture:")
content="""
Diversity and inclusion are at the core of our values. We celebrate different perspectives 
and strive to create a workplace where everyone feels welcome, respected, and empowered to contribute.
"""
st.write(content)

st.subheader("4. Flexible Work Environment:")
content="""
We understand that life happens outside of work. That's why we offer flexible working hours, remote work options, 
and a healthy work-life balance.
"""
st.write(content)

st.subheader("5. Competitive Benefits:")
content="""
We offer a comprehensive benefits package that includes health insurance, retirement plans, paid time off, 
and more, ensuring that you and your family are well taken care of.
"""
st.write(content)

st.header("Current Opportunities")
content="""
We're always looking for talented people to join our team. Check out our current job openings below:
"""
st.write(content)




df= pandas.read_csv("Job_Roles_Responsibilities_Skills.csv")

for index, row in df.iterrows():
    st.header(row["Role"].title())  # Use row["role"] to access the role in the current row
    st.write(f"**Summary:** {row['Summary']}")
    st.write(f"**Responsibilities:** {row['Responsibilities']}")
    st.write(f"**Required Skills and Experience:** {row['Required Skills and Experience']}")


    st.write("**Note:** If you want to apply, please go to the [Contact Us](http://localhost:8502/Contact_Us) page and select 'Job Enquiry'.Please mention the role you are applying for in the body of your email.")