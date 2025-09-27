import streamlit as st

st.set_page_config(page_title="AI Engineer Portal", layout="centered")

# --- In-memory user store (demo) ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": {"password": "1234", "fname": "AI", "lname": "Admin", "age": 25, "class": "Masters"}}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# --- Custom CSS for colors & cards ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .stTabs [role="tab"] {
        background: #1f4068;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    .stTabs [role="tab"]:hover {
        background: #162447;
        color: #e43f5a;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, select {
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #0072ff;
    }
    .stButton>button {
        border-radius: 8px;
        background: linear-gradient(90deg, #ff512f, #dd2476);
        color: white;
        font-weight: bold;
        padding: 8px 20px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #dd2476, #ff512f);
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 Title (Blue like old "Login to Continue")
st.markdown("<h2 style='text-align:center; color:#00c6ff;'>🤖 AI Engineer Authentication Portal</h2>", unsafe_allow_html=True)

# --- Tabs for Login & Sign Up ---
tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])

# --- LOGIN TAB ---
with tab1:
    st.markdown("<h3 style='color:#FFD700;'>Login to Continue</h3>", unsafe_allow_html=True)  # Dark Yellow
    with st.form("login_form"):
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if username in st.session_state.users and st.session_state.users[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                user_data = st.session_state.users[username]
                st.success(f"✅ Welcome back, {user_data['fname']} {user_data['lname']} ({user_data['age']} yrs, {user_data['class']})")
            else:
                st.error("❌ Invalid username or password")

# --- SIGN UP TAB ---
with tab2:
    st.markdown("<h3 style='color:#ff512f;'>Create a New Account</h3>", unsafe_allow_html=True)
    with st.form("signup_form"):
        fname = st.text_input("📝 First Name")
        lname = st.text_input("📝 Last Name")
        age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1)
        edu_class = st.selectbox("🎓 Class / Education Level", ["Intermediate", "BS", "Masters"])
        new_user = st.text_input("👤 Choose Username")
        new_pass = st.text_input("🔑 Choose Password", type="password")
        confirm_pass = st.text_input("🔑 Confirm Password", type="password")
        signup_btn = st.form_submit_button("Sign Up")

        if signup_btn:
            if new_user in st.session_state.users:
                st.warning("⚠ Username already exists. Please choose another.")
            elif new_pass != confirm_pass:
                st.error("❌ Passwords do not match.")
            elif not fname or not lname or not new_user.strip():
                st.error("❌ Please fill all required fields.")
            else:
                st.session_state.users[new_user] = {
                    "password": new_pass,
                    "fname": fname,
                    "lname": lname,
                    "age": age,
                    "class": edu_class
                }
                st.success(f"✅ Account created successfully! You can now login as {new_user}")

# --- AFTER LOGIN ---
if st.session_state.logged_in:
    user_data = st.session_state.users[st.session_state.current_user]
    st.info(f"🎉 Logged in as {user_data['fname']} {user_data['lname']} "
            f"(Age: {user_data['age']}, Class: {user_data['class']})")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.success("✅ Logged out successfully.")