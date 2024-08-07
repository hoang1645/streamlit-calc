import streamlit as st

# Initialize session state for the calculator
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'result_displayed' not in st.session_state:
    st.session_state.result_displayed = False

# Title of the app
st.title("Pocket Calculator")

# Display for input and result
current_input = st.text_input("Display", value=st.session_state.display, key="display", disabled=True)

# CSS to style buttons uniformly
st.markdown("""
    <style>
    .calc-button {
        background-color: #f0f0f0;
        border: none;
        border-radius: 5px;
        color: black;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 24px;
        margin: 4px 2px;
        cursor: pointer;
        width: 100%;
    }
    .calc-button:hover {
        background-color: #d4d4d4;
    }
    .stButton>button {
        width: 100%;
        margin: 0;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def update_display(value):
    if st.session_state.result_displayed:
        st.session_state.display = str(value)
        st.session_state.result_displayed = False
    else:
        if value == '＊': value = "*"
        if value == '−': value = '-'
        if value == '＋': value = '+'    
        print(value)
        if value in ['+', '-', '*', '/']:
            if st.session_state.display and st.session_state.display[-1] in ['+', '-', '*', '/']:
                st.session_state.display = st.session_state.display[:-1] + value
            else:
                evaluate_display(press_equal=False)
                st.session_state.display += str(value)
        else:
            st.session_state.display += str(value))



# Function to clear the display
def clear_display():
    st.session_state.display = ""

# Function to evaluate the expression
def evaluate_display(press_equal=False):
    try:
        st.session_state.display = str(eval(st.session_state.display))
    except:
        st.session_state.display = "Error"
    if press_equal: st.session_state.result_displayed = True

# Layout for calculator buttons
button_config = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '＊'],
    ['1', '2', '3', '−'],
    ['C', '0', '.', '＋']
]

# Display the buttons
for row in button_config:
    cols = st.columns(4)  # Create 4 columns for each row
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == 'C':
                st.button(btn, on_click=clear_display)
            else:
                st.button(btn, on_click=update_display, args=(btn,))

# Separate evaluate button
cols = st.columns(4)
with cols[0]:
    st.button("=", on_click=evaluate_display, key='equals', help="Evaluate the expression")
