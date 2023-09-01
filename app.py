import streamlit as st
import subprocess
import os

# Function to run Model 1 (People Counting)
def run_model1():
    try:
        model1_path = os.path.join("models", "model1", "submain.py")
        subprocess.Popen(["python", model1_path], cwd="D:/tink")
    except Exception as e:
        st.error(f"Error running Model 1: {str(e)}")

# Function to run Model 2 (Sign Detection)
def run_model2():
    try:
        model2_path = os.path.join("models", "model2", "submain.py")
        subprocess.Popen(["python", model2_path], cwd="D:/tink")
    except Exception as e:
        st.error(f"Error running Model 2: {str(e)}")

# Function to run Model 3 (Face Detection)
def run_model3():
    try:
        model3_path = os.path.join("models", "model3", "main.py")
        subprocess.Popen(["python", model3_path], cwd="D:/tink")
    except Exception as e:
        st.error(f"Error running Model 3: {str(e)}")

def main():
    st.title("Tinker Streamlit App")

    st.write("Click the buttons to run the models:")

    if st.button("People Count"):
        run_model1()

    if st.button("Sign Detection"):
        run_model2()

    if st.button("Face Detection"):
        run_model3()

if __name__ == "__main__":
    main()
