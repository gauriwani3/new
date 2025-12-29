import streamlit as st

st.set_page_config(
    page_title="Gauri Wani | Data Engineer Intern",
    page_icon="📊",
    layout="wide"
)

st.sidebar.image("assets/profile.png", width=120)
st.sidebar.title("Gauri Wani")
st.sidebar.markdown("**Data Engineer Intern**")
st.sidebar.markdown("📍 Mumbai, Maharashtra")

page = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Experience", "Technical Skills", "Contact"]
)

# ---------- ABOUT ME ----------
if page == "About Me":
    st.title("👋 Hi, I'm Gauri Wani")

    st.write("""
    Data Engineer Intern at **Aditya Birla Group - Hindalco Industries**.  
    Passionate about leveraging data to generate business insights and build predictive models.  
    Skilled in **Python**, **Data Cleaning**, **Data Analysis**, **ML** and **Data Visualization**.
    """)

    st.subheader("🎓 Education")
    st.markdown("""
    - **Bachelor of Engineering in Electronics and Telecommunication**  
    **Pune Institute of Computer Technology**  
    **CGPA**: 8.16 | **Jul 2019 – Jul 2023**  
    - Relevant Coursework:
      - Python, C, C++
      - Data Visualization, Machine Learning Fundamentals
      - Exploratory Data Analysis, Database Management System
    """)

    with open("assets/resume.pdf", "rb") as file:
        st.download_button(
            "📄 Download Resume",
            file,
            "Gauri_Wani_Resume.pdf"
        )

# ---------- PROJECTS ----------

# ---------- EXPERIENCE ----------
elif page == "Experience":
    st.title("🏢 Experience")

    st.subheader("Aditya Birla Group - Hindalco Industries Ltd. — Data Engineer Intern")
    st.markdown("""
    **Oct 2025 – Present | Mumbai, Maharashtra**  
    - Cleaned, preprocessed, and performed feature engineering on large-scale manufacturing and process datasets.
    - Automated EDA pipelines (missing values, outliers, datetime parsing) using Python, Pandas, and Numpy, reducing manual analysis time.
    - Collaborated with senior analysts to deliver business-aligned insights for operational decision-making.
    """)

# ---------- TECHNICAL SKILLS ----------
elif page == "Technical Skills":
    st.title("🛠 Technical Skills")

    st.subheader("Languages")
    st.markdown("""
    - **Python**, **C**, **C++**
    """)

    st.subheader("Data Analysis & Machine Learning")
    st.markdown("""
    - **Pandas**, **NumPy**, **Scikit-learn**
    - **Exploratory Data Analysis** (EDA), **Feature Engineering**
    """)

    st.subheader("Data Visualization")
    st.markdown("""
    - **Matplotlib**, **Plotly**, **Streamlit**
    """)

    st.subheader("Tools & Platforms")
    st.markdown("""
    - **Streamlit Community Cloud**, **Databricks**, **Jupyter Notebook**
    - **VS Code**, **GitHub**
    """)

# ---------- CONTACT ----------
else:
    st.title("📬 Contact")

    st.markdown("""
    - **LinkedIn:** [gauri-wani-083025212](https://linkedin.com/in/gauri-wani-083025212)
    - **GitHub:** [GauriWani](https://github.com/GauriWani)
    - **Email:** gauriwan1212@gmail.com
    """)

