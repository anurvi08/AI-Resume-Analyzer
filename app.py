import streamlit as st
import pdfplumber

st.title("AI-Powered Resume Analyzer & Career Recommendation System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    st.subheader("Extracted Resume Text")
    st.write(text)

    skills = [
        "python",
        "sql",
        "power bi",
        "excel",
        "machine learning",
        "data analysis",
        "git",
        "github",
        "numpy",
        "pandas",
        "tableau",
        "statistics",
        "tensorflow",
        "pytorch",
        "streamlit",
        "html",
        "css",
        "javascript",
        "mysql",
        "data visualization"
    ]

    detected_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            detected_skills.append(skill)

    st.subheader("Detected Skills")
    st.write(detected_skills)

    score = min(len(detected_skills) * 10, 100)

    st.subheader("Resume Score")
    st.write(f"{score}/100")

    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent Resume!")
    elif score >= 60:
        st.warning("Good Resume. Add more relevant skills.")
    else:
        st.error("Resume needs improvement.")

    role = "General Candidate"

    if "power bi" in detected_skills and "sql" in detected_skills:
        role = "Data Analyst"

    elif "machine learning" in detected_skills and "python" in detected_skills:
        role = "AI/ML Intern"

    elif "python" in detected_skills and "sql" in detected_skills:
        role = "Python Developer"

    st.subheader("Recommended Role")
    st.success(role)

    missing_skills = list(set(skills) - set(detected_skills))

    st.subheader("Recommended Skills to Learn")

    for skill in missing_skills:
        st.write("•", skill.title())

    report = f"""
Resume Score: {score}/100

Recommended Role: {role}

Detected Skills:
{', '.join(detected_skills)}

Missing Skills:
{', '.join(missing_skills)}
"""

    st.download_button(
        label="Download Analysis Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )