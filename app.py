import streamlit as st
import pandas as pd
import pickle
import time

# 1. Set up the page configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Student AI Predictor", page_icon="🎓", layout="wide")

# 2. Custom CSS for Advanced UI (Gradients, Hover Effects, and Fonts)
st.markdown("""
    <style>
    /* Gradient text for the main dashboard title */
    .main-title {
        font-size: 3.5rem;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-text {
        text-align: center;
        font-size: 1.2rem;
        color: #A0AEC0;
        margin-bottom: 30px;
    }
    /* Glowing, animated prediction button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: #0E1117;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 800;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 15px rgba(0, 201, 255, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0px 6px 20px rgba(0, 201, 255, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load the trained AI Model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: 'model.pkl' not found. Please run train.py first.")

# 4. Beautiful Sidebar Navigation
# Adding a cool AI icon and custom branding for your channel/portfolio
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/8637/8637099.png", width=80) 
st.sidebar.markdown("## **Tech With Wahab**")
st.sidebar.caption("AI Solutions & Analytics Dashboard")
st.sidebar.markdown("---")

# Changed from a dropdown menu to a cleaner Radio button menu
app_mode = st.sidebar.radio("Navigate the System", ["Dashboard", "Data Analytics", "Prediction Center", "About the Project"])

# --- Module 1: Dashboard ---
if app_mode == "Dashboard":
    st.markdown('<p class="main-title">Student AI Predictor</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Empowering education with Machine Learning and Data Analytics</p>', unsafe_allow_html=True)
    
    # Adding a high-quality aesthetic banner image from Unsplash
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
    
    st.markdown("---")
    st.info("🟢 System Status: Neural Network 'model.pkl' is loaded and online.")

# --- Module 2: Data Analytics ---
elif app_mode == "Data Analytics":
    st.title("📈 Dataset Analytics")
    st.write("Visualizing the relationship between student habits and academic success.")
    st.markdown("---")
    
    df = pd.read_csv('student_data.csv')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Time vs. Grades")
        study_chart_data = df.groupby('studytime')['G3'].mean()
        st.bar_chart(study_chart_data, color="#00C9FF") 
        
    with col2:
        st.subheader("Absences vs. Grades")
        st.scatter_chart(df, x="absences", y="G3", color="#92FE9D") 
        
    st.markdown("---")
    st.write("### Raw Data Explorer")
    st.dataframe(df.head(10), use_container_width=True)

# --- Module 3: Prediction Center ---
elif app_mode == "Prediction Center":
    st.title("📊 Prediction Center")
    st.write("Adjust the parameters below to generate a real-time AI prediction.")
    st.markdown("---")

    # Added a nice layout container with emojis
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            studytime = st.number_input("📚 Study Time Category (1 to 4)", min_value=1, max_value=4, value=2)
            absences = st.number_input("🚶‍♂️ Number of Absences", min_value=0, max_value=93, value=5)
        with col2:
            G1 = st.number_input("📝 First Period Grade (G1)", min_value=0, max_value=20, value=12)
            G2 = st.number_input("📝 Second Period Grade (G2)", min_value=0, max_value=20, value=12)

    st.markdown("---")
    
    if st.button("Generate AI Prediction", use_container_width=True):
        with st.spinner("🧠 Analyzing patterns with Random Forest..."):
            time.sleep(1.2) # Dramatic pause animation
            
            input_data = pd.DataFrame({
                'studytime': [studytime],       
                'absences': [absences],         
                'G1': [G1],
                'G2': [G2]
            })

            try:
                prediction = model.predict(input_data)
                final_score = prediction[0]
                
                st.markdown("### 🎯 AI Conclusion")
                col_res1, col_res2 = st.columns(2)
                
                with col_res1:
                    if final_score >= 10:
                        st.metric(label="Predicted Final Grade", value=f"{final_score} / 20", delta="Passing")
                        st.balloons()
                    else:
                        st.metric(label="Predicted Final Grade", value=f"{final_score} / 20", delta="Failing", delta_color="inverse")
                
                with col_res2:
                    st.write("**🤖 Automated Insights:**")
                    if final_score >= 15:
                        st.success("Exceptional! The student is demonstrating strong academic potential.")
                    elif final_score >= 10:
                        st.info("Satisfactory performance. Consistent study time will improve these results.")
                    else:
                        st.error("Action Required: High risk of failure. Immediate academic intervention recommended.")

            except Exception as e:
                st.error(f"Prediction Error: {e}")

# --- Module 4: About the Project ---
elif app_mode == "About the Project":
    st.title("👨‍💻 About the Project")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("System Architecture")
        st.write("This application leverages a **Random Forest Classifier** to analyze educational datasets. The model evaluates features like historical grades and attendance to forecast final academic performance.")
        st.write("Built with: **Python, Streamlit, Pandas, and Scikit-Learn.**")
        
    with col2:
        st.info("""
        **Developer Profile**
        - **Name:** M. Abdulwahab (Wahab)
        - **Degree:** BS Computer Science
        - **Semester:** 4th
        - **University:** COMSATS Sahiwal
        """)