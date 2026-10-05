# System Handoff Instruction for Antigravity AI

## 🎯 Project Overview

**Role:** You are an Expert Frontend Developer and Data Visualization Specialist.
**Task:** Build a modern, interactive, and responsive web-based dashboard to analyze the global AI, Data Science, and Statistics job market.
**Target Audience:** Students, job seekers, and recruiters analyzing career trends.

## 🛠 Tech Stack Requirements

* **Framework:** React (Next.js or Vite)
* **Styling:** Tailwind CSS for a clean, modern, dark/light mode toggleable UI.
* **Icons:** Lucide React or Heroicons.
* **Data Visualization:** Recharts, Chart.js, or Nivo (for interactive charts).
* **State Management:** React Hooks (`useState`, `useMemo` for filtering).

## 📊 Data Context & Real Open Data Sources

The dashboard is designed to visualize insights from the following real-world Open Data sources. **Please structure your application to accommodate these data models.**

1. **Education Data (Stanford AI Index):**
   * *Description:* Global and US data on AI, CS, and Statistics graduates.
   * *Source Link:* [Stanford AI Index GitHub Repo](https://github.com/stanford-hai/ai-index)
2. **Demographic & Salary Data (Kaggle ML & DS Survey):**
   * *Description:* Global survey data covering minimum degrees, salary bands, and countries.
   * *Source Link:* [Kaggle ML & DS Survey](https://www.kaggle.com/datasets/kaggle/kaggle-survey-2022)
3. **Company & Job Postings Data (Glassdoor Dataset):**
   * *Description:* Real job postings detailing hiring companies, industries, and ratings.
   * *Source Link:* [Data Science Job Postings on Kaggle](https://www.kaggle.com/datasets/slamin/data-science-job-postings-on-glassdoor)
4. **Skills Data (O*NET Database):**
   * *Description:* US Dept. of Labor data on highly demanded tech skills (Python, SQL, etc.) for Data Scientists (Code 15-2051.00).
   * *Source Link:* [O*NET Resource Center](https://www.onetcenter.org/database.html)
5. **Seniority Levels (Levels.fyi STEM Salaries):**
   * *Description:* Career level mapping (Entry, Mid, Senior) correlated with years of experience and compensation.
   * *Source Link:* [STEM Salaries on Kaggle](https://www.kaggle.com/datasets/jackogozaly/data-science-and-stem-salaries)

## 🏗 Mock Data Requirements (For Initial Render)

Since you cannot load these external CSVs directly on the first render, please **generate robust mock data** natively within the application based on the sources above so the dashboard is fully functional upon loading.

### 1. Filters Schema
* `roles`: ["Data Scientist", "AI Engineer", "Statistician", "Data Analyst"]
* `levels`: ["Entry-Level", "Mid-Level", "Senior", "Expert"]
* `regions`: ["Global", "North America", "Europe", "Asia-Pacific"]

### 2. Required Visualizations & Mock Models
* **Education vs. Demand (Line Chart):** Years 2018-2024. Show two lines: "Graduates" (Stanford AI Index) vs "Open Roles".
* **Top Skills (Horizontal Bar Chart):** Python, SQL, R, TensorFlow, AWS, Spark, NLP, PyTorch, Tableau (O*NET). Values should be percentage of job postings.
* **Salary by Region & Level (Grouped Bar or Map):** Compare starting salaries (Entry) vs (Senior) across regions (Kaggle & Levels.fyi).
* **Top Hiring Companies (Data Table):** Company Name, Industry, Open Roles, Average Rating (Glassdoor).

## 💻 UI/UX Layout & Features

### 1. Sidebar / Top Control Panel
* **Header:** "AI & Data Science Market Explorer"
* **Global Filters:** Dropdowns or toggle buttons for `Role`, `Region`, and `Career Level`.
* **Behavior:** Changing these filters MUST dynamically update all charts and tables on the page.

### 2. Main Dashboard Area (Grid Layout)
* **Top Row (Key Metrics Cards):** Total Open Roles, Average Global Starting Salary, Most Demanded Skill.
* **Middle Row (Charts):** *Left:* Line Chart (Education vs Demand). *Right:* Horizontal Bar Chart (Top Skills).
* **Bottom Row (Salary & Companies):** *Left:* Salary Distribution (Bar Chart). *Right:* Scrollable Data Table of Top Hiring Companies.

## ⚙️ Execution Instructions for Antigravity

1. **Single-File Mandate:** Output all React components, logic, and styling in a single file to ensure compatibility.
2. **Interactive First:** Ensure tooltips appear on hover for all charts and tables are sortable.
3. **Seamless Migration:** Hardcode the mock data as distinct constants or objects. Structure the components so that replacing these mock objects with real CSV parsed data (e.g., via `papaparse`) in the future is trivial.
4. **Aesthetics:** Use a professional color palette suitable for a data analytics tool (e.g., Slate/Indigo or Dark Blue/Teal).

**Please generate the code for this dashboard now.**