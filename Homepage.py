import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Overthinking Out Loud",
    layout="wide",
    page_icon="📜",
)

# Load the CSS file
with open("main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("index.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

st.markdown("---")
st.subheader("About the Blog")
st.write("""
Hey, I’m Kyla, a 20-year-old caffeine-dependent, sleep-deprived overthinker who’s trying to figure out life just like you. 
Whether it’s navigating career pressure, unlearning toxic hustle culture, or debating if pineapple belongs on pizza, 
this is a safe space where we keep it real, laugh at our struggles, and grow together.
""")

# Latest Post Section
st.markdown("---")
st.subheader("Latest Post: 'Am I Doing Enough, or Is Capitalism Gaslighting Me?'")
st.markdown("**November 24, 2024**")
st.write("""
Raise your hand if you’ve ever been personally victimized by your own ambition.

One minute, you’re scrolling TikTok for a “quick break,” and the next, you’re knee-deep in videos of 19-year-olds starting multi-million dollar businesses 
while you’re still trying to decide what to have for dinner. Sound familiar?

Here’s the thing Gen Z struggles with most: the constant pressure to do it all. Social media makes everyone look like they’ve got life figured out, 
and we feel like failures for needing a break. But here’s the tea: rest is productive. Hustle culture is a trap. And comparison is the thief of joy.

In this post, I’m sharing:

1. Why your worth isn’t tied to productivity
2. How to set boundaries with work and social media
3. Why saying “no” to some goals is saying “yes” to mental health

You’re doing enough. You are enough. Let’s stop letting the grind define us.
""")

# Reader Comments Section
st.markdown("---")
st.subheader("Reader Comments:")

# List of comments with names and dates
comments = [
    ("Lila", "Nov 24, 2024", "This hit me so hard today. I needed to hear that rest is okay. Thanks, Kai!"),
    ("Sammy", "Nov 24, 2024", "Why do I feel attacked but also seen? Time to log off and take a walk."),
    ("Jordan", "Nov 24, 2024", "Can you write a follow-up about how to actually stop overthinking? Asking for a friend.")
]

# Display comments
for name, date, comment in comments:
    st.write(f"**{name}** ({date}): {comment}")

# Sidebar for navigation (future pages can be added here)
st.sidebar.success("Select pages above")
