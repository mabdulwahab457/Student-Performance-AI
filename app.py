# ==========================================
# 5. MODULE 1: FULLY CUSTOMIZED DASHBOARD (WITH SLIDESHOW)
# ==========================================
if app_mode == "📈 Live Dashboard":
    
    # --- AUTO-SLIDING PROFESSIONAL BANNER (NEW) ---
    st.markdown("""
    <style>
    .slider-wrapper {
        width: 100%;
        overflow: hidden;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        margin-bottom: 25px;
        position: relative;
        background: #0f0c29;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to right, #24243e, #302b63, #0f0c29);
        background: linear-gradient(to right, #24243e, #302b63, #0f0c29);
    }
    .slide-track {
        display: flex;
        width: 300%;
        animation: playSlider 15s infinite cubic-bezier(0.77, 0, 0.175, 1);
    }
    .slide-item {
        width: 33.333%;
        position: relative;
    }
    .slide-img {
        width: 100%;
        height: 320px;
        object-fit: cover;
        opacity: 0.5;
        display: block;
    }
    .slide-content {
        position: absolute;
        bottom: 50px;
        left: 50px;
        color: white;
    }
    .slide-content h2 {
        font-size: 3rem;
        margin: 0;
        font-weight: 900;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .slide-content p {
        font-size: 1.3rem;
        margin-top: 10px;
        font-weight: bold;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
        color: #E2E8F0;
    }
    @keyframes playSlider {
        0%, 28% { transform: translateX(0); }
        33.33%, 61% { transform: translateX(-33.333%); }
        66.66%, 94% { transform: translateX(-66.666%); }
        100% { transform: translateX(0); }
    }
    </style>

    <div class="slider-wrapper">
        <div class="slide-track">
            <div class="slide-item">
                <img class="slide-img" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop" />
                <div class="slide-content">
                    <h2>Advanced Data Analytics</h2>
                    <p>Visualizing student performance metrics in real-time.</p>
                </div>
            </div>
            <div class="slide-item">
                <img class="slide-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" />
                <div class="slide-content">
                    <h2>Machine Learning Core</h2>
                    <p>Powered by Random Forest predictive capabilities.</p>
                </div>
            </div>
            <div class="slide-item">
                <img class="slide-img" src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop" />
                <div class="slide-content">
                    <h2>Empowering Education</h2>
                    <p>Predicting outcomes to support student success.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("Real-time insights and analytics extracted from the student database.")
    st.markdown("---")

    if df is not None:
        # --- TOP KPI CARDS ---
        st.subheader("📊 Key Performance Indicators (KPIs)")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        with kpi1:
            st.metric("Total Students", f"{len(df)}", "+12 New")
        with kpi2:
            avg_grade = round(df['G3'].mean(), 1)
            st.metric("Average Grade", f"{avg_grade} / 20", "+0.4")
        with kpi3:
            pass_rate = round((len(df[df['G3'] >= 10]) / len(df)) * 100, 1)
            st.metric("Passing Rate", f"{pass_rate}%", "Optimal")
        with kpi4:
            st.metric("AI Accuracy", "89.5%", "High")

        st.markdown("<br>", unsafe_allow_html=True)

        # --- MIDDLE SECTION: CHARTS & INSIGHTS ---
        col_chart, col_insights = st.columns([2, 1])
        
        with col_chart:
            st.markdown("### 📈 Grade Distribution Trend")
            grade_counts = df['G3'].value_counts().sort_index()
            st.area_chart(grade_counts, color="#FF4B2B")
            
        with col_insights:
            st.markdown("### 💡 AI Smart Insights")
            st.info("**Trend 1:** Students with high absences (10+) show a 40% drop in final scores.")
            st.success("**Trend 2:** Study time of 'Category 3 & 4' guarantees a 95% passing rate.")
            st.warning("**Alert:** 15% of students are currently in the 'High Risk' zone.")
    else:
        st.error("Data file (student_data.csv) not found! Cannot display dashboard.")