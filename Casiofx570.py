import streamlit as st
import math

st.set_page_config(page_title="Casio Fx-570 Calculator")

# Constants
NUM_BUTTON_COLS = 5
NUM_BUTTON_ROWS = 5
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 75

# State variables
current_value = ""
stored_value = None
current_operator = None

# Define the buttons
buttons = [
    "7", "8", "9", "/", "sqrt",
    "4", "5", "6", "*", "%",
    "1", "2", "3", "-", "1/x",
    "0", ".", "Ans", "+", "=",
    "(", ")", "AC", "M+", "M-",
]

# Helper functions
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def handle_number_button(button):
    global current_value
    if is_number(button):
        current_value += button
        st.write(current_value)

def handle_operator_button(button):
    global stored_value, current_value, current_operator
    if current_value:
        if stored_value is None:
            stored_value = float(current_value)
        else:
            if current_operator == "+":
                stored_value += float(current_value)
            elif current_operator == "-":
                stored_value -= float(current_value)
            elif current_operator == "*":
                stored_value *= float(current_value)
            elif current_operator == "/":
                stored_value /= float(current_value)
        current_operator = button
        current_value = ""
        st.write(stored_value)

def handle_other_button(button):
    global stored_value, current_value, current_operator
    if button == "AC":
        stored_value = None
        current_value = ""
        current_operator = None
        st.write("")
    elif button == "sqrt":
        current_value = str(math.sqrt(float(current_value)))
        st.write(current_value)
    elif button == "%":
        current_value = str(float(current_value) / 100)
        st.write(current_value)
    elif button == "1/x":
        current_value = str(1 / float(current_value))
        st.write(current_value)
    elif button == ".":
        if "." not in current_value:
            current_value += "."
            st.write(current_value)
    elif button == "=":
        handle_operator_button("=")
        current_value = str(stored_value)
        stored_value = None
        current_operator = None
        st.write(current_value)
    elif button == "Ans":
        if stored_value is not None:
            current_value = str(stored_value)
            st.write(current_value)
    elif button == "M+":
        if stored_value is not None:
            stored_value += float(current_value)
            st.write(stored_value)
    elif button == "M-":
        if stored_value is not None:
            stored_value -= float(current_value)
            st.write(stored_value)
# Helper functions
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def handle_number_button(button):
    global current_value
    if is_number(button):
        current_value += button
        st.write(current_value)

def handle_operator_button(button):
    global stored_value, current_value, current_operator
    if current_value:
        if stored_value is None:
            stored_value = float(current_value)
        else:
            if current_operator == "+":
                stored_value += float(current_value)
            elif current_operator == "-":
                stored_value -= float(current_value)
            elif current_operator == "*":
                stored_value *= float(current_value)
            elif current_operator == "/":
                stored_value /= float(current_value)
        current_operator = button
        current_value = ""
        st.write(stored_value)

def handle_other_button(button):
    global stored_value, current_value, current_operator
    if button == "AC":
        stored_value = None
        current_value = ""
        current_operator = None
        st.write("")
    elif button == "sqrt":
        current_value = str(math.sqrt(float(current_value)))
        st.write(current_value)
    elif button == "%":
        current_value = str(float(current_value) / 100)
        st.write(current_value)
    elif button == "1/x":
        current_value = str(1 / float(current_value))
        st.write(current_value)
    elif button == ".":
        if "." not in current_value:
            current_value += "."
            st.write(current_value)
    elif button == "=":
        handle_operator_button("=")
        current_value = str(stored_value)
        stored_value = None
        current_operator = None
        st.write(current_value)
    elif button == "Ans":
        if stored_value is not None:
            current_value = str(stored_value)
            st.write(current_value)
    elif button == "M+":
        if stored_value is not None:
            stored_value += float(current_value)
            st.write(stored_value)
    elif button == "M-":
        if stored_value is not None:
            stored_value -= float(current_value)
            st.write(stored_value)
def main():
    pass

if __name__ == '__main__':
    main()
