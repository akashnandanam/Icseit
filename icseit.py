import streamlit as st

st.set_page_config(page_title="ICSEit - Class 10 Math AI", layout="wide")

st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 10px;
    }
    .user {
        background-color: #DCF8C6;
        text-align: right;
    }
    .bot {
        background-color: #F1F0F0;
        text-align: left;
    }
    .chat-box {
        max-height: 70vh;
        overflow-y: auto;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 ICSEit – Quadratic Equations Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_response(user_input):
    user_input = user_input.lower()
    if "quadratic equation" in user_input:
        return "A quadratic equation is an equation of the form ax² + bx + c = 0, where a ≠ 0."
    elif "solve" in user_input:
        return "To solve a quadratic equation, you can use factorisation, completing the square, or the quadratic formula."
    elif "roots" in user_input:
        return "The roots of a quadratic equation are the values of x that satisfy ax² + bx + c = 0. Use the quadratic formula: x = (-b ± √(b² - 4ac)) / 2a."
    elif "discriminant" in user_input:
        return "The discriminant is D = b² - 4ac. It tells us the nature of the roots. If D > 0, roots are real and distinct; D = 0, real and equal; D < 0, roots are complex."
    elif "real" in user_input and "imaginary" in user_input:
        return "A quadratic equation has real roots when the discriminant is ≥ 0. If it's negative, the roots are imaginary (complex)."
    else:
        return "I'm still learning! Try asking about solving, roots, or the discriminant of quadratic equations."

# Input box
user_input = st.text_input("Ask ICSEit anything about Quadratic Equations...")

# Generate and display response
if user_input:
    st.session_state.chat_history.append((user_input, "user"))
    response = generate_response(user_input)
    st.session_state.chat_history.append((response, "bot"))

# Display chat
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for msg, sender in st.session_state.chat_history:
    cls = "user" if sender == "user" else "bot"
    st.markdown(f"<div class='chat-message {cls}'>{msg}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

