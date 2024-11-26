import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Overthinking Out Loud",
    page_icon="📜",
)

img=Image.open('./assets/ad.png')

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(img, width=230)

with col2:
    st.title('Kyla Cubelo', anchor=False)
    st.write('Surigao State University, Bachelor of Science in Computer Engineering, a 2nd Year Student')


st.write("\n\n")
st.subheader("Short Discription About me:")
st.write(
    """
    Hi! I’m Kyla, a 20-year-old who’s equal parts dreamer and doer. I’m the friend who’s always down for spontaneous road trips, long coffee dates, and deep late-night conversations. I love journaling, exploring cute bookstores, and baking cookies (even if they don’t always turn out perfect!). Life’s a mix of chasing big goals and appreciating the little joys, and I’m all about finding the magic in everyday moments. 💕
    """
)

st.sidebar.success("Select pages above")