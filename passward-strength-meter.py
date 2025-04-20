import streamlit as st
import re
import random
import string

# --- PAGE CONFIG ---
st.set_page_config("VaultLock 🔒", layout="wide", page_icon="🔒")

# --- HEADER ---
st.markdown("""
    <style>
    .app-header {
        text-align: center;
        font-size: 2.5em;
        font-weight: 800;
        color: #2c3e50;
    }
    .subtext {
        text-align: center;
        font-size: 1.1em;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-header'>🔒 VaultLock</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Check the strength of your password and get secure suggestions</div>", unsafe_allow_html=True)
st.divider()

# --- FUNCTIONS ---
def assess(password):
    rules = {
        "has_len": len(password) >= 8,
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_digit": bool(re.search(r"[0-9]", password)),
        "has_symbol": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    total = sum(rules.values())
    if total == 5:
        return "🟢 Excellent", "green", 100
    elif total >= 3:
        return "🟠 Average", "orange", 60
    else:
        return "🔴 Poor", "red", 30

def suggest_password():
    mix = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choices(mix, k=14))

# --- LAYOUT ---
left, right = st.columns([2, 1])

with left:
    st.markdown("### 🔑 Enter your password below:")
    user_password = st.text_input("Password Input", type="password", placeholder="Enter your password here")

    go = st.button("Check 🔍")

    if go:
        if not user_password:
            st.error("🚫 You need to type a password!")
        else:
            label, color, bar = assess(user_password)
            st.markdown(f"**Security Level:** <span style='color:{color}; font-size: 1.3em;'>{label}</span>", unsafe_allow_html=True)
            st.progress(bar)

            if label == "🔴 Poor":
                st.info("🛡️ Use a mix of uppercase, lowercase, numbers, and symbols.")
                st.code(suggest_password(), language="text")

with right:
    st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=180)

st.divider()
st.caption("Made with Streamlit ❤️ | VaultLock - Your password safety checker.")
