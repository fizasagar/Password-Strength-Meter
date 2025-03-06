# Project : Password Strength Meter By Sir Zia

import re
import streamlit as st 


# Page Styling 
st.set_page_config(page_title="Password Strength Checker By Fiza Asif", page_icon="🔑", layout="centered")

# Custom Css
st.markdown("""
<style>
    .main {text-align: center; }
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #ba88f7; color: white; font-size: 18px; }
    .stButton button:hover {background-color: #5cbbfa; color: #fafafa;}
</style>
""", unsafe_allow_html=True)

# Page Title & Description
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long**. ")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**. ")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **atleast one number (8-9) **. ")

# special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **atleast one special character (!@#$%^&*)**.")
    
    # Display password strength result 
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features")
    else:
        st.error("**Week Password** - Follow the suggestion below to strength it.")

    # Feedback
    if feedback:
        with st.expander("🔎 ** Improve Your Password**"):
            for item in feedback:
                st.write(item)
password= st.text_input("Enter Your Password:", type="password", help="Ensure your password must be strong💪")

# Button Working 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!") #showing warning if password is empty
