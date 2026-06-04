import streamlit as st
import pandas as pd
import joblib

model = joblib.load("linear_regression_model.pkl")

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

def classify_grade(score):
    if score >= 70:
        return "A", "Excellent performance"
    elif score >= 60:
        return "B", "Very good performance"
    elif score >= 50:
        return "C", "Good performance"
    elif score >= 45:
        return "D", "Fair performance"
    elif score >= 40:
        return "E", "Pass performance"
    else:
        return "F", "Poor performance"

st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.app-header {
    background-color: #0f172a;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    color: white;
}

.app-header h1 {
    margin-bottom: 0.3rem;
    font-size: 2.3rem;
}

.app-header p {
    font-size: 1rem;
    color: #cbd5e1;
}

.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-top: 1rem;
    margin-bottom: 0.7rem;
    color: #111827;
}

.result-box {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    border-left: 6px solid #2563eb;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 1.5rem;
}

.metric-score {
    font-size: 2.5rem;
    font-weight: 800;
    color: #2563eb;
}

.grade-badge {
    display: inline-block;
    padding: 0.4rem 0.9rem;
    border-radius: 6px;
    background-color: #dbeafe;
    color: #1e40af;
    font-weight: 700;
    margin-top: 0.5rem;
}

.small-note {
    color: #64748b;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="app-header">
    <h1>Student Performance Predictor</h1>
    <p>Predict a student's expected exam score using academic, personal, and school-related factors.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Academic Information</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    hours_studied = st.number_input(
        "Hours Studied",
        min_value=0,
        max_value=50,
        value=10
    )

with col2:
    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

with col3:
    previous_scores = st.number_input(
        "Previous Scores",
        min_value=0,
        max_value=100,
        value=70
    )

col4, col5, col6 = st.columns(3)

with col4:
    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0,
        max_value=24,
        value=7
    )

with col5:
    tutoring_sessions = st.number_input(
        "Tutoring Sessions",
        min_value=0,
        max_value=10,
        value=1
    )

with col6:
    physical_activity = st.number_input(
        "Physical Activity",
        min_value=0,
        max_value=10,
        value=3
    )

st.markdown('<div class="section-title">Student Support And Environment</div>', unsafe_allow_html=True)

col7, col8, col9 = st.columns(3)

with col7:
    parental_involvement = st.selectbox(
        "Parental Involvement",
        ["Low", "Medium", "High"]
    )

with col8:
    access_to_resources = st.selectbox(
        "Access to Resources",
        ["Low", "Medium", "High"]
    )

with col9:
    motivation_level = st.selectbox(
        "Motivation Level",
        ["Low", "Medium", "High"]
    )

col10, col11, col12 = st.columns(3)

with col10:
    family_income = st.selectbox(
        "Family Income",
        ["Low", "Medium", "High"]
    )

with col11:
    teacher_quality = st.selectbox(
        "Teacher Quality",
        ["Low", "Medium", "High"]
    )

with col12:
    peer_influence = st.selectbox(
        "Peer Influence",
        ["Negative", "Neutral", "Positive"]
    )

st.markdown('<div class="section-title">School And Personal Information</div>', unsafe_allow_html=True)

col13, col14, col15 = st.columns(3)

with col13:
    extracurricular_activities = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

with col14:
    internet_access = st.selectbox(
        "Internet Access",
        ["No", "Yes"]
    )

with col15:
    school_type = st.selectbox(
        "School Type",
        ["Public", "Private"]
    )

col16, col17, col18 = st.columns(3)

with col16:
    learning_disabilities = st.selectbox(
        "Learning Disabilities",
        ["No", "Yes"]
    )

with col17:
    parental_education_level = st.selectbox(
        "Parental Education Level",
        ["High School", "College", "Postgraduate"]
    )

with col18:
    distance_from_home = st.selectbox(
        "Distance from Home",
        ["Near", "Moderate", "Far"]
    )

col19, col20, col21 = st.columns(3)

with col19:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col20:
    st.write("")

with col21:
    st.write("")

st.markdown("---")

predict_button = st.button("Predict Exam Score", use_container_width=True)

if predict_button:
    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Tutoring_Sessions": [tutoring_sessions],
        "Physical_Activity": [physical_activity],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Extracurricular_Activities": [extracurricular_activities],
        "Motivation_Level": [motivation_level],
        "Internet_Access": [internet_access],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "School_Type": [school_type],
        "Peer_Influence": [peer_influence],
        "Learning_Disabilities": [learning_disabilities],
        "Parental_Education_Level": [parental_education_level],
        "Distance_from_Home": [distance_from_home],
        "Gender": [gender]
    })

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    grade, performance = classify_grade(prediction)

    st.markdown(f"""
    <div class="result-box">
        <p class="small-note">Prediction Result</p>
        <div class="metric-score">{prediction:.2f}%</div>
        <div class="grade-badge">Grade {grade}</div>
        <h3>{performance}</h3>
        <p class="small-note">
            A = 70 and above, B = 60-69, C = 50-59, D = 45-49, E = 40-44, F = 39 and below.
        </p>
    </div>
    """, unsafe_allow_html=True)