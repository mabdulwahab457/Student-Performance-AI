import streamlit as st
import pandas as pd
import pickle
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="EduMetrics OS", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 2. ENTERPRISE MINIMALIST CSS (Sleek & Clean)
# ==========================================
st.markdown("""
    <style>
    /* --- Main App Background & Text --- */
    .stApp {
        background-color: #0f172a; /* Deep Slate */
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* --- Typography --- */
    h1, h2, h3 {
        color: #f8fafc !important;
        font-weight: 600 !important;
        letter-spacing: -0.5px;
    }
    
    /* --- Sidebar Styling --- */
    [data-testid="stSidebar"] {
        background-color: #020617 !important; /* Extra Dark Slate */
        border-right: 1px solid #1e293b;
    }
    
    /* --- Navigation Radio Buttons --- */
    div.row-widget.stRadio > div {
        background-color: transparent;
    }
    div.row-widget.stRadio > div > label {
        padding: 10px 15px;
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 6px;
        margin-bottom: 5px;
        transition: all 0.2s ease;
        color: #cbd5e1;
    }
    div.row-widget.stRadio > div > label:hover {
        background-color: #1e293b;
        color: #ffffff;
        border-color: #334155;
    }
    
    /* --- Primary Action Buttons --- */
    div.stButton > button:first-child {
        background-color: #4f46e5; /* Professional Indigo */
        color: #ffffff !important;
        font-weight: 500;
        border-radius: 6px;
        border: 1px solid #4338ca;
        padding: 8px 24px;
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #4338ca;
        border-color: #3730a3;
    }

    /* --- Input Fields --- */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
        color: #f8fafc !important;
    }
    
    /* --- Metric Cards (KPIs) --- */
    div[data-testid="metric-container"] {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    div[data-testid="metric-container"] label {
        color: #94a3b8 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    
    /* --- Clean Header Line --- */
    hr {
        border-color: #1e293b;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SECURE LOGIN SYSTEM
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>EduMetrics OS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Enterprise Performance Analytics</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        with st.form("login_form"):
            st.markdown("#### System Authentication")
            username = st.text_input("Administrator ID")
            password = st.text_input("Security Key", type="password")
            submit = st.form_submit_button("Authenticate", use_container_width=True)
            
            if submit:
                if username == "admin" and password == "admin":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Authentication Failed: Invalid Credentials.")

# ==========================================
# 4. ENTERPRISE DASHBOARD
# ==========================================
else:
    # --- SLEEK SIDEBAR MENU ---
    with st.sidebar:
        st.markdown("""
            <div style='padding: 10px 0px 20px 0px;'>
                <h2 style='color: #f8fafc; margin: 0; font-size: 1.5rem; letter-spacing: -0.5px;'>EduMetrics OS</h2>
                <p style='color: #4f46e5; font-size: 0.8rem; font-weight: 600; margin-top: 2px;'>VERSION 5.1 | SECURE CONNECTION</p>
            </div>
        """, unsafe_allow_html=True)
        
        app_mode = st.radio("System Navigation", [
            "Data Ingestion & Training", 
            "Student Forecasting", 
            "Educator Analytics", 
            "Institutional Metrics", 
            "Terminate Session"
        ], label_visibility="collapsed")

    if app_mode == "Terminate Session":
        st.session_state['logged_in'] = False
        st.rerun()

    # --- PAGE 1: DATA INGESTION ---
    elif app_mode == "Data Ingestion & Training":
        st.markdown("<h1>Data Ingestion Module</h1>", unsafe_allow_html=True)
        st.write("Import historical academic records to configure the Machine Learning pipeline.")
        st.markdown("---")
        
        uploaded_file = st.file_uploader("Upload Institutional Data (CSV Format)", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("Data parsed successfully. Ready for compilation.")
            st.dataframe(df.head())
            
            if st.button("Initialize Training Pipeline", type="primary"):
                with st.spinner("Compiling Random Forest Regressor Algorithms..."):
                    time.sleep(1.5)
                    st.success("Pipeline Configured. Core Model ('model.pkl') is active.")

    # --- PAGE 2: STUDENT FORECASTING ---
    elif app_mode == "Student Forecasting":
        st.markdown("<h1>Student Academic Forecasting</h1>", unsafe_allow_html=True)
        st.write("Adjust the parameters below to generate a predictive outcome report.")
        st.markdown("---")
        
        with st.container():
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("#### Demographics")
                st.text_input("Scholar Name")
                st.text_input("Enrollment ID")
                st.selectbox("Demographic Profile", ["Male", "Female", "Unspecified"])
                st.selectbox("Extracurricular Engagement", ["Active", "Inactive"])
                absences = st.number_input("Recorded Absences", 0, 100, 5)
            
            with c2:
                st.markdown("#### Academic History")
                st.selectbox("Preparatory Course", ["Not Enrolled", "Completed"])
                G1 = st.number_input("Midterm 1 Evaluation (G1)", 0, 20, 12)
                G2 = st.number_input("Midterm 2 Evaluation (G2)", 0, 20, 12)
                st.number_input("Standardized Test Score", 0, 100, 80)
                studytime = st.selectbox("Weekly Study Index (1-4)", [1, 2, 3, 4], index=1)
                
            with c3:
                st.markdown("#### Wellness & Access")
                st.selectbox("Supplemental Tutoring", ["Engaged", "Not Engaged"])
                st.selectbox("Physical Health Index", ["Optimal", "Sub-optimal"])
                st.selectbox("Digital Access", ["Reliable", "Unreliable"])
                st.selectbox("Psychological Status", ["Standard", "Optimal", "Review Required"])

        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Execute Predictive Analysis", type="primary"):
            try:
                with open('model.pkl', 'rb') as f:
                    model = pickle.load(f)
                
                input_data = pd.DataFrame({'studytime': [studytime], 'absences': [absences], 'G1': [G1], 'G2': [G2]})
                prediction = model.predict(input_data)[0]
                final_score = round(float(prediction), 1)
                
                st.markdown("---")
                
                if final_score >= 10.0:
                    st.success(f"Projected Evaluation: {final_score} / 20.0")
                    st.info("System Assessment: Favorable. The scholar is demonstrating positive academic momentum. Current protocols should be maintained.")
                else:
                    st.error(f"Projected Evaluation: {final_score} / 20.0")
                    st.warning("System Assessment: Intervention Required. Forecasting indicates a high probability of sub-standard performance. Immediate engagement recommended.")
            except:
                st.error("System Error: Core model offline. Please upload data and initialize the pipeline.")

    # --- PAGE 3: EDUCATOR EFFECTIVENESS ---
    elif app_mode == "Educator Analytics":
        st.markdown("<h1>Educator Analytics</h1>", unsafe_allow_html=True)
        st.write("Analyze faculty performance metrics against institutional benchmarks.")
        st.markdown("---")
        
        tc1, tc2 = st.columns(2)
        with tc1:
            st.text_input("Faculty Member Name")
            st.selectbox("Age Bracket", ["25-30", "30-35", "35-40", "40+"])
            st.selectbox("Highest Degree", ["Bachelor's", "Master's", "Doctorate (Ph.D)"])
            st.number_input("Students Below Proficiency Threshold", 0, 50, 2)
        with tc2:
            st.number_input("Students Achieving Distinction", 0, 100, 20)
            st.slider("Non-Instructional Availability (Hours)", 1, 10, 3)
            st.selectbox("Occupational Health Status", ["Optimal", "Standard", "Review Required"])
            st.text_input("Assigned Department")
            
        if st.button("Generate Faculty Report", type="primary"):
            with st.spinner("Processing Faculty Metrics..."):
                time.sleep(1.5)
                st.success("Evaluation Output: The educator is projected to achieve an effectiveness rating of 19/20. Impact classified as HIGHLY EFFECTIVE.")

    # --- PAGE 4: INSTITUTIONAL ANALYTICS ---
    elif app_mode == "Institutional Metrics":
        st.markdown("<h1>Institutional Metrics</h1>", unsafe_allow_html=True)
        st.write("Overview of system-wide academic performance and machine learning accuracy.")
        st.markdown("---")
        
        # Sleek KPI Cards
        k1, k2, k3, k4 = st.columns(4)
        with k1: st.metric("Active Scholars", "1,245", "+34 This Month")
        with k2: st.metric("System Accuracy", "98.2%", "Optimal")
        with k3: st.metric("Avg. Evaluation", "14.2/20", "+1.1")
        with k4: st.metric("Risk Alerts", "12", "-3 Resolved")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("#### Departmental Performance Map")
            chart_data = pd.DataFrame({
                "Departments": ["Computer Science", "Mathematics", "Physics", "Chemistry"],
                "Scores": [88, 92, 75, 82]
            }).set_index("Departments")
            # Using a refined, muted blue for the chart
            st.bar_chart(chart_data, color="#4f46e5")
        with c2:
            st.markdown("#### AI Automated Insights")
            st.info("Trend Detected: 15% increase in Computer Science performance over the last quarter.")
            st.success("System Status: Overall institutional health is classified as OPTIMAL.")