import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")
st.caption("Check how strong your password is in real-time.")


def check_strength(password):
    score = 0
    suggestions = []

    
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$ etc.).")

    return score, suggestions


password = st.text_input("Enter your password:", type="password")

if password:
    score, tips = check_strength(password)
    
    st.subheader("Strength Rating:")
    if score <= 2:
        st.error("❌ Weak Password")
    elif score == 3:
        st.warning("⚠️ Moderate Password")
    elif score == 4:
        st.info("✅ Strong Password")
    elif score == 5:
        st.success("💪 Very Strong Password")

    st.progress(score / 5)

    if tips:
        st.subheader("Suggestions to improve:")
        for tip in tips:
            st.markdown(f"- {tip}")
