# System Handoff Instruction for Dashboard Development

## 🎯 Project Overview
**Role:** You are an Expert Python Data Application Developer (using Dash by Plotly or Streamlit + Plotly).
**Task:** Build an interactive, multi-tab dashboard to analyze the supply of graduates (Tab 1), job market demand (Tab 2), and Skill Mismatch (Tab 3) in AI, Data Science, and Statistics fields. 
**Core Requirements:**
- **Backend/Framework:** Python (Dash or Streamlit).
- **Visualization:** Plotly for all charts.
- **Interactivity:** All charts within the same tab MUST be interconnected (cross-filtering). Clicking a data point on one chart must update the others.

---

## 🗄️ Relational Database (RDB) Schema
Please structure the backend data processing around this relational model. Generate mock data for these tables to ensure the dashboard works on the first render.

### Tab 1 Data (Supply / University Side)
*   **Table 1: `programs`** (หลักสูตร)
    *   `program_id` (PK)
    *   `program_name` (e.g., B.S. Data Science, M.S. AI)
    *   `university`
    *   `tuition_fee_per_year` (Numeric)
*   **Table 2: `program_stats`** (สถิติบัณฑิตรายปี)
    *   `stat_id` (PK)
    *   `program_id` (FK)
    *   `year` (YYYY)
    *   `graduates_count` (Number of grads)
    *   `emp_rate_yr1` (Employment rate 1st year %)
    *   `emp_rate_yr2` (Employment rate 2nd year %)
    *   `emp_rate_yr3` (Employment rate 3rd year %)
*   **Table 3: `program_courses`** (วิชาบังคับ)
    *   `course_id` (PK)
    *   `program_id` (FK)
    *   `course_name`
*   **Table 4: `learned_skills`** (ทักษะที่สอน)
    *   `id` (PK)
    *   `program_id` (FK)
    *   `skill_name` (Standardized skill name, e.g., Python, SQL, NLP)

### Tab 2 Data (Demand / Job Market Side)
*   **Table 5: `companies`** (บริษัท)
    *   `company_id` (PK)
    *   `company_name`
    *   `industry`
*   **Table 6: `job_postings`** (ตำแหน่งงาน)
    *   `job_id` (PK)
    *   `company_id` (FK)
    *   `job_role` (AI Engineer, Data Scientist, Statistician)
    *   `experience_level` (Entry, Mid, Senior)
    *   `open_positions_count` (Number of vacancies)
    *   `salary_avg` (Numeric)
*   **Table 7: `required_skills`** (ทักษะที่ต้องการ)
    *   `id` (PK)
    *   `job_id` (FK)
    *   `skill_name` (Standardized skill name - MUST match mapping with `learned_skills`)

---

## 💻 Dashboard Layout & Visualization Requirements

### 📑 Tab 1: Graduate Supply & Learned Skills (ปริมาณคนที่จบและทักษะ)
**Interactive Logic:** Selecting a `program_name` or `year` in any chart filters the rest.
*   **Chart 1.1 (Bar/Line Chart):** Number of graduates per program by year (`program_stats.graduates_count` over time).
*   **Chart 1.2 (Data Table or Horizontal Bar):** Mandatory courses for the selected programs (`program_courses.course_name`).
*   **Chart 1.3 (Grouped Bar Chart):** Employment rates after 1st, 2nd, and 3rd years (`emp_rate_yr1`, `emp_rate_yr2`, `emp_rate_yr3`).
*   **Chart 1.4 (KPI / Gauge Chart):** Average or specific Tuition Fee for the selected program (`programs.tuition_fee_per_year`).

### 📑 Tab 2: Job Demand & Required Skills (ปริมาณงานที่จ้างและทักษะที่ต้องการ)
**Interactive Logic:** Selecting an `experience_level`, `job_role`, or `company_name` filters the rest.
*   **Chart 2.1 (Bar/Pie Chart):** Number of open positions by job role (`open_positions_count`).
*   **Chart 2.2 (Word Cloud or Horizontal Bar):** Top demanded skills (`required_skills.skill_name`) frequency.
*   **Chart 2.3 (Treemap or Table):** Top hiring companies and their open roles (`companies.company_name` vs `open_positions_count`).
*   **Chart 2.4 (Box Plot or Bar Chart):** Salary distributions across different experience levels (`salary_avg` by `experience_level`).

### 📑 Tab 3: Skill Mismatch Analysis (วิเคราะห์ความเหลื่อมล้ำของทักษะ)
**Interactive Logic:** Combine data from `learned_skills` and `required_skills`.
*   **Chart 3.1 (Diverging Bar Chart or Radar Chart):** 
    *   *X-axis / Axis:* Standardized Skill Name (e.g., Python, Cloud, ML).
    *   *Y-axis 1 (Supply):* Frequency of skill taught in `learned_skills`.
    *   *Y-axis 2 (Demand):* Frequency of skill required in `required_skills`.
    *   *Goal:* Visually highlight gaps (e.g., High demand for AWS, but low presence in university curricula).
*   **Chart 3.2 (Scatter Plot):** Mismatch Matrix. X-axis: Demand Score, Y-axis: Supply Score. Highlight quadrants (e.g., "High Demand, Low Supply" = Urgent Gap).

## ⚙️ Execution Instructions
1. Initialize the Python environment with Dash or Streamlit and Plotly Express/Graph Objects.
2. Build the Pandas DataFrames using the RDB schema provided (generate mock data for about 5 universities and 50 job postings).
3. Implement callbacks (Dash `@callback`) or state management (Streamlit `st.session_state`) to ensure cross-filtering within Tab 1 and Tab 2 works seamlessly.
4. Provide the complete executable Python script.