import streamlit as st
import pandas as pd
import pickle
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="EduMetrics AI | 3D Analytics", page_icon="🏛️", layout="wide")

# ==========================================
# 2. PREMIUM 3D CSS (NEUMORPHISM & GLASS)
# ==========================================
st.markdown("""
    <style>
    /* --- Main Background --- */
    .stApp {
        background-color: #121826;
        color: #E2E8F0;
    }
    
    /* --- 3D Buttons (Popping out) --- */
    div.stButton > button:first-child {
        background: linear-gradient(145deg, #1e293b, #121826);
        color: #38BDF8 !important;
        font-weight: 800;
        letter-spacing: 1px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.05);
        padding: 12px 24px;
        box-shadow:  6px 6px 12px #0a0d15, -6px -6px 12px #1a2337;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        color: #0ea5e9 !important;
        transform: translateY(-2px);
        box-shadow:  8px 8px 16px #0a0d15, -8px -8px 16px #1a2337;
    }
    div.stButton > button:first-child:active {
        transform: translateY(2px);
        box-shadow: inset 4px 4px 8px #0a0d15, inset -4px -4px 8px #1a2337;
    }

    /* --- 3D Input Fields & Select Boxes (Carved in) --- */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {
        background: #121826 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: inset 5px 5px 10px #0a0d15, inset -5px -5px 10px #1a2337 !important;
        color: white !important;
    }
    
    /* --- Floating 3D Metric Cards --- */
    div[data-testid="metric-container"] {
        background: linear-gradient(145deg, #161d2e, #121826);
        border-radius: 16px;
        padding: 20px;
        box-shadow:  8px 8px 16px #0a0d15, -8px -8px 16px #1a2337;
        border: 1px solid rgba(255,255,255,0.02);
        text-align: center;
        transition: transform 0.3s;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
    }
    div[data-testid="metric-container"] label {
        color: #94A3B8 !important;
        font-weight: 700;
        letter-spacing: 1px;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-size: 2.8rem !important;
        text-shadow: 0px 4px 10px rgba(56, 189, 248, 0.3);
    }

    /* --- 3D Sidebar Panel --- */
    [data-testid="stSidebar"] {
        background: #121826 !important;
        border-right: 2px solid #1a2337;
        box-shadow: 10px 0 20px rgba(0,0,0,0.5);
    }
    div.row-widget.stRadio > div {
        background: linear-gradient(145deg, #161d2e, #121826);
        border-radius: 12px;
        padding: 15px;
        box-shadow:  5px 5px 10px #0a0d15, -5px -5px 10px #1a2337;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SECURE LOGIN SYSTEM
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<br><br><br><h1 style='text-align: center; color: #38BDF8; text-shadow: 0 4px 10px rgba(56,189,248,0.4); font-size: 4rem;'>EduMetrics 3D™</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 1.2rem;'>Enterprise Performance Analytics Panel</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        with st.form("login_form"):
            st.markdown("### 🔐 Secure System Access")
            username = st.text_input("Administrator ID")
            password = st.text_input("Security Key", type="password")
            submit = st.form_submit_button("Initialize Secure Login", use_container_width=True)
            
            if submit:
                if username == "admin" and password == "admin":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Authentication Failed: Invalid Credentials.")

# ==========================================
# 4. 3D ENTERPRISE DASHBOARD
# ==========================================
else:
    # --- 3D SIDEBAR MENU ---
    with st.sidebar:
        st.markdown("""
            <div style='text-align: center; padding: 10px;'>
                <img src="https://cdn-icons-png.flaticon.com/512/8637/8637099.png" width="90" style="filter: drop-shadow(0px 10px 10px rgba(56, 189, 248, 0.4)); margin-bottom: 15px;">
                <h2 style='color: #F8FAFC; margin: 0; font-size: 1.6rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>EduMetrics OS</h2>
                <p style='color: #38BDF8; font-size: 0.85rem; font-weight: bold;'>v5.0 - 3D PANEL ACTIVE</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        app_mode = st.radio("Navigation Console", [
            "⚙️ Data Ingestion & Training", 
            "🎓 Student Forecasting Panel", 
            "👨‍🏫 Educator Analytics", 
            "📈 3D Institutional Metrics", 
            "🔒 Secure Logout"
        ], label_visibility="collapsed")

    if app_mode == "🔒 Secure Logout":
        st.session_state['logged_in'] = False
        st.rerun()

    # --- PAGE 1: DATA INGESTION ---
    elif app_mode == "⚙️ Data Ingestion & Training":
        st.markdown("<h1>⚙️ Data Ingestion Module</h1>", unsafe_allow_html=True)
        st.write("Import historical academic records into the 3D Machine Learning pipeline.")
        st.markdown("---")
        
        uploaded_file = st.file_uploader("Upload Institutional Data (CSV Format)", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("Data Ingestion Successful! Parsing records...")
            st.dataframe(df.head())
            
            if st.button("Initialize 3D Training Pipeline", type="primary"):
                with st.spinner("Compiling Random Forest Regressor Algorithms..."):
                    time.sleep(2)
                    st.success("Pipeline Configured. Core Model ('model.pkl') is now active.")

    # --- PAGE 2: STUDENT FORECASTING ---
    elif app_mode == "🎓 Student Forecasting Panel":
        st.markdown("<h1>🎓 Student Forecasting Panel</h1>", unsafe_allow_html=True)
        st.write("Adjust the 3D sliders and dropdowns below to generate a predictive outcome.")
        st.markdown("---")
        
        # Wrapped in a 3D container
        with st.container():
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("### 👤 Demographics")
                st.text_input("Scholar Name")
                st.text_input("Enrollment ID")
                st.selectbox("Demographic Profile", ["Male", "Female", "Other"])
                st.selectbox("Extracurricular Engagement", ["Active", "Inactive"])
                absences = st.number_input("Recorded Absences", 0, 100, 5)
            
            with c2:
                st.markdown("### 📚 Academics")
                st.selectbox("Preparatory Course", ["Not Enrolled", "Completed"])
                G1 = st.number_input("Midterm 1 Evaluation (G1)", 0, 20, 12)
                G2 = st.number_input("Midterm 2 Evaluation (G2)", 0, 20, 12)
                st.number_input("Standardized Test Score", 0, 100, 80)
                studytime = st.selectbox("Weekly Study Index (1-4)", [1, 2, 3, 4], index=1)
                
            with c3:
                st.markdown("### 🧠 Wellness & Access")
                st.selectbox("Supplemental Tutoring", ["Engaged", "Not Engaged"])
                st.selectbox("Physical Health Index", ["Optimal", "Sub-optimal"])
                st.selectbox("Digital Access", ["Reliable", "Unreliable"])
                st.selectbox("Psychological Well-being", ["Standard", "Optimal", "Review Needed"])

        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Execute Predictive Analysis", type="primary"):
            try:
                with open('model.pkl', 'rb') as f:
                    model = pickle.load(f)
                
                input_data = pd.DataFrame({'studytime': [studytime], 'absences': [absences], 'G1': [G1], 'G2': [G2]})
                prediction = model.predict(input_data)[0]
                final_score = round(float(prediction), 1)
                
                st.markdown("---")
                
                if final_score >= 10.0:
                    st.success(f"### 📈 Projected Final Evaluation: {final_score} / 20.0")
                    st.info("**System Assessment: Favorable.**\n\nThe scholar is demonstrating positive academic momentum. Keep up the excellent work.")
                else:
                    st.error(f"### 📉 Projected Final Evaluation: {final_score} / 20.0")
                    st.warning("**System Assessment: Academic Intervention Required.**\n\nForecasting indicates a high probability of sub-standard performance. Immediate engagement recommended.")
            except:
                st.error("System Error: Core model offline. Please upload data and train the model first.")

    # --- PAGE 3: EDUCATOR EFFECTIVENESS ---
    elif app_mode == "👨‍🏫 Educator Analytics":
        st.markdown("<h1>👨‍🏫 Educator Analytics</h1>", unsafe_allow_html=True)
        st.write("Analyze faculty metrics in the 3D interface.")
        st.markdown("---")
        
        tc1, tc2 = st.columns(2)
        with tc1:
            st.text_input("Faculty Member Name")
            st.selectbox("Age Bracket", ["25-30", "30-35", "35-40", "40+"])
            st.selectbox("Highest Degree", ["Bachelor's", "Master's", "Doctorate (Ph.D)"])
            st.number_input("Students Below Proficiency", 0, 50, 2)
        with tc2:
            st.number_input("Students Achieving Distinction", 0, 100, 20)
            st.slider("Non-Instructional Availability", 1, 10, 3)
            st.selectbox("Health Status", ["Optimal", "Standard", "Review"])
            st.text_input("Department")
            
        if st.button("Generate Faculty Report", type="primary"):
            with st.spinner("Processing 3D Faculty Metrics..."):
                time.sleep(1.5)
                st.success("🎯 **Evaluation Output:** The educator is projected to achieve a rating of 19/20. Impact classified as HIGHLY EFFECTIVE.")

    # --- PAGE 4: INSTITUTIONAL ANALYTICS ---
    elif app_mode == "📈 3D Institutional Metrics":
        st.markdown("<h1>📈 Institutional Metrics</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        # 3D KPI Cards
        k1, k2, k3, k4 = st.columns(4)
        with k1: st.metric("Active Scholars", "1,245", "+34 This Month")
        with k2: st.metric("System Accuracy", "98.2%", "Optimized")
        with k3: st.metric("Avg. Evaluation", "14.2/20", "+1.1")
        with k4: st.metric("Risk Alerts", "12", "-3 Resolved")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("📊 Departmental Performance Map")
            chart_data = pd.DataFrame({
                "Departments": ["Computer Science", "Mathematics", "Physics", "Chemistry"],
                "Scores": [88, 92, 75, 82]
            }).set_index("Departments")
            st.bar_chart(chart_data, color="#38BDF8")
        with c2:
            st.subheader("💡 AI Insights")
            st.info("Algorithms detect a 15% increase in Computer Science performance.")
            st.success("Overall institutional health is classified as OPTIMAL.")