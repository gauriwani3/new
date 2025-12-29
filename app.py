import streamlit as st

st.set_page_config(
    page_title="Gauri Wani | Data Analyst",
    layout="wide"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "",
    ["About Me", "Projects", "Experience", "Contact"]
)

# ---------- ABOUT ----------
if page == "About Me":
    st.title("👋 Hi, I'm Gauri")

    st.write("""
    Data Analyst with professional experience at **Aditya Birla Group**.
    Skilled in Python, data analysis, visualization, and machine learning fundamentals.
    Passionate about building data-driven solutions and interactive dashboards.
    """)

    st.subheader("🛠 Skills")
    st.markdown("""
    - Python (Pandas, NumPy)
    - Data Visualization (Plotly, Matplotlib)
    - Machine Learning (Scikit-learn)
    - Streamlit
    """)

# ---------- PROJECTS ----------
elif page == "Projects":
    st.title("📊 Projects")

    with st.expander("📈 Sales Performance Analytics Dashboard"):
        st.write("""
        **Tools:** Python, Pandas, Plotly, Streamlit  
        **Description:** Interactive dashboard to analyze sales KPIs,
        trends, and regional performance.
        """)
        st.markdown("[🔗 View Project](projects/sales_dashboard/app.py)")

    with st.expander("🤖 Customer Churn Prediction"):
        st.write("""
        **Tools:** Python, Scikit-learn, Streamlit  
        **Description:** End-to-end ML project to predict customer churn.
        """)

# ---------- EXPERIENCE ----------
elif page == "Experience":
    st.title("🏢 Experience")

    st.subheader("Aditya Birla Group — Data Analyst")
    st.markdown("""
    - Automated data analysis using Python
    - Built dashboards for business stakeholders
    - Performed trend, variance, and KPI analysis
    """)

# ---------- CONTACT ----------
else:
    st.title("📬 Contact")
    st.markdown("""
    - **LinkedIn:** your-link  
    - **GitHub:** github/GauriWani
    - **Email:** gauriwani1212@gmail.com@email.com
    """)
