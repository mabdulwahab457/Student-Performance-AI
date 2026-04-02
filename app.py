import streamlit as st
import pandas as pd
import pickle

# Set up the page configuration
st.set_page_config(page_title="Student AI Predictor", page_icon="🎓", layout="wide")

# Load the trained AI Model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: 'model.pkl' not found. Please run train.py first.")

# Create a Sidebar for Navigation
st.sidebar.title("Navigation Panel")
# Added 'About the Project' to the menu
app_mode = st.sidebar.selectbox("Choose a Module:", ["Dashboard", "Data Analytics", "Prediction Center", "About the Project"])

# Module 1: Dashboard
if app_mode == "Dashboard":
    st.title("🎓 Student Performance Prediction AI")
    st.markdown("---")
    st.write("Welcome to the advanced Student Performance Predictor.")
    st.write("Use the **Navigation Panel** on the left to explore the analytics or generate predictions.")
    st.info("System Status: AI Model Loaded Successfully and Ready for Predictions.")

# Module 2: Data Analytics
elif app_mode == "Data Analytics":
    st.title("📈 Dataset Analytics")
    st.write("Explore the relationships between student behaviors and their final grades.")
    st.markdown("---")
    
    df = pd.read_csv('student_data.csv')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Impact of Study Time")
        st.write("Average Final Grade based on Study Time category.")
        study_chart_data = df.groupby('studytime')['G3'].mean()
        st.bar_chart(study_chart_data)
        
    with col2:
        st.subheader("Impact of Absences")
        st.write("Distribution of Final Grades against Total Absences.")
        st.scatter_chart(df, x="absences", y="G3")
        
    st.markdown("---")
    st.write("### Raw Dataset Overview")
    st.dataframe(df.head(10))

# Module 3: Prediction Center
elif app_mode == "Prediction Center":
    st.title("📊 Prediction Center")
    st.write("Enter the student's metrics below to predict their Final Grade (G3).")
    st.markdown("---")

    col1, col2 = st.columns(2)
    
    with col1:
        studytime = st.number_input("Study Time Category (1 to 4)", min_value=1, max_value=4, value=2)
        absences = st.number_input("Number of Absences", min_value=0, max_value=93, value=5)
        
    with col2:
        G1 = st.number_input("First Period Grade (G1)", min_value=0, max_value=20, value=12)
        G2 = st.number_input("Second Period Grade (G2)", min_value=0, max_value=20, value=12)

    st.markdown("---")
    
    if st.button("Generate AI Prediction", type="primary"):
        input_data = pd.DataFrame({
            'studytime': [studytime],       
            'absences': [absences],         
            'G1': [G1],
            'G2': [G2]
        })

        try:
            prediction = model.predict(input_data)
            st.success(f"🎯 AI Prediction Result: The expected Final Grade is **{prediction[0]}** out of 20.")
        except Exception as e:
            st.error(f"Prediction Error: {e}")

# --- NEW Module 4: About the Project ---
elif app_mode == "About the Project":
    st.title("👨‍💻 About the Project")
    st.markdown("---")
    st.subheader("Artificial Intelligence Project")
    st.write("This Machine Learning application is designed to predict student academic outcomes based on their study habits, attendance, and previous scores using a Random Forest Classifier algorithm.")
    
    st.markdown("---")
    st.subheader("Developer Profile")
    st.write("**Developed by:** M. Abdulwahab (Wahab)")
    st.write("**Program:** Bachelor of Science in Computer Science (BSCS)")
    st.write("**Semester:** 4th Semester")
    st.write("**Institution:** COMSATS University, Sahiwal Campus")
    
    st.markdown("---")
    st.write("Built entirely using Python, Pandas, Scikit-Learn, and Streamlit.")