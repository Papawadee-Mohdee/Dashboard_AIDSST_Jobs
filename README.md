# AI, Data Science, and Statistics Job Market Dashboard

## 🎯 Project Overview
This project is an interactive, multi-tab dashboard designed to analyze the global AI, Data Science, and Statistics job market. It provides insights for students, job seekers, and recruiters by visualizing the supply of university graduates, job market demand, and identifying skill mismatches.

## 🛠 Tech Stack
Based on the project specifications, the dashboard is being built using:
- **Backend/Framework:** Python (Streamlit)
- **Data Manipulation:** Pandas
- **Visualization:** Plotly
*(Note: An earlier specification considered a React/Next.js stack, but the current implementation focuses on Python/Streamlit for robust data handling and rapid dashboard development).*

## 📊 Key Features
1. **Graduate Supply & Learned Skills (Tab 1):** Analyzes the number of graduates, mandatory courses, employment rates, and tuition fees across various programs.
2. **Job Demand & Required Skills (Tab 2):** Visualizes open positions by role, top demanded skills, top hiring companies, and salary distributions.
3. **Skill Mismatch Analysis (Tab 3):** Compares the supply of learned skills from universities against the demand for required skills in the job market to highlight critical gaps.

## 🗄️ Data Model
The application uses a relational data structure with the following key entities:
- **Supply:** `programs`, `program_stats`, `program_courses`, `learned_skills`
- **Demand:** `companies`, `job_postings`, `required_skills`

Mock data is generated natively within the application to ensure the dashboard is fully functional upon loading, based on real-world contexts like the Stanford AI Index and Kaggle ML & DS Surveys.
