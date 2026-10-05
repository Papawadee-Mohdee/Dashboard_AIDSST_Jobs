import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI & Data Science Market Explorer", layout="wide")

# --- MOCK DATA GENERATION ---
@st.cache_data
def load_mock_data():
    # 1. Supply Data (Universities)
    programs = pd.DataFrame({
        'program_id': [1, 2, 3, 4, 5],
        'program_name': ['B.S. Data Science', 'M.S. Artificial Intelligence', 'B.S. Statistics', 'M.S. Data Analytics', 'B.S. Computer Science'],
        'university': ['Stanford', 'MIT', 'Berkeley', 'CMU', 'UW'],
        'tuition_fee_per_year': [55000, 60000, 45000, 58000, 42000]
    })

    # Stats over years 2019-2024
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    stats_data = []
    stat_id = 1
    for pid in programs['program_id']:
        base_grads = np.random.randint(50, 200)
        for y in years:
            grads = int(base_grads * (1 + (y - 2019)*np.random.uniform(0.05, 0.15)))
            emp1 = np.random.uniform(70, 90)
            emp2 = np.random.uniform(85, 95)
            emp3 = np.random.uniform(90, 98)
            stats_data.append([stat_id, pid, y, grads, emp1, emp2, emp3])
            stat_id += 1
            
    program_stats = pd.DataFrame(stats_data, columns=['stat_id', 'program_id', 'year', 'graduates_count', 'emp_rate_yr1', 'emp_rate_yr2', 'emp_rate_yr3'])

    courses_data = [
        [1, 1, 'Intro to Data Science'], [2, 1, 'Machine Learning'], [3, 1, 'Database Systems'],
        [4, 2, 'Deep Learning'], [5, 2, 'Computer Vision'], [6, 2, 'Advanced ML'],
        [7, 3, 'Probability Theory'], [8, 3, 'Statistical Inference'], [9, 3, 'Regression Analysis'],
        [10, 4, 'Data Mining'], [11, 4, 'Big Data Analytics'], [12, 4, 'Business Intelligence'],
        [13, 5, 'Algorithms'], [14, 5, 'Data Structures'], [15, 5, 'AI Principles']
    ]
    program_courses = pd.DataFrame(courses_data, columns=['course_id', 'program_id', 'course_name'])

    learned_skills_data = [
        [1, 1, 'Python'], [2, 1, 'SQL'], [3, 1, 'ML'], [4, 1, 'Statistics'],
        [5, 2, 'Python'], [6, 2, 'Deep Learning'], [7, 2, 'PyTorch'], [8, 2, 'AWS'],
        [9, 3, 'R'], [10, 3, 'Statistics'], [11, 3, 'Python'],
        [12, 4, 'SQL'], [13, 4, 'Tableau'], [14, 4, 'Python'], [15, 4, 'Cloud'],
        [16, 5, 'Python'], [17, 5, 'Java'], [18, 5, 'Algorithms'], [19, 5, 'C++']
    ]
    learned_skills = pd.DataFrame(learned_skills_data, columns=['id', 'program_id', 'skill_name'])

    # 2. Demand Data (Job Market)
    companies = pd.DataFrame({
        'company_id': [1, 2, 3, 4, 5],
        'company_name': ['Google', 'Meta', 'Amazon', 'OpenAI', 'Microsoft'],
        'industry': ['Tech', 'Tech', 'E-commerce/Cloud', 'AI', 'Tech']
    })

    roles = ['AI Engineer', 'Data Scientist', 'Statistician', 'Data Analyst']
    levels = ['Entry', 'Mid', 'Senior']
    job_postings_data = []
    job_id = 1
    for cid in companies['company_id']:
        for _ in range(10): # 10 postings per company
            role = np.random.choice(roles)
            level = np.random.choice(levels)
            open_pos = np.random.randint(1, 15)
            
            base_sal = 90000 if level == 'Entry' else (130000 if level == 'Mid' else 180000)
            if role == 'AI Engineer': base_sal += 20000
            elif role == 'Data Scientist': base_sal += 10000
            
            salary_avg = base_sal + np.random.randint(-15000, 15000)
            
            job_postings_data.append([job_id, cid, role, level, open_pos, salary_avg])
            job_id += 1
            
    job_postings = pd.DataFrame(job_postings_data, columns=['job_id', 'company_id', 'job_role', 'experience_level', 'open_positions_count', 'salary_avg'])

    all_skills = ['Python', 'SQL', 'ML', 'Statistics', 'Deep Learning', 'PyTorch', 'AWS', 'R', 'Tableau', 'Cloud', 'Java', 'Algorithms', 'C++', 'NLP', 'TensorFlow']
    required_skills_data = []
    req_id = 1
    for jid in job_postings['job_id']:
        # Assign 3-5 random skills to each job
        job_skills = np.random.choice(all_skills, size=np.random.randint(3, 6), replace=False)
        for s in job_skills:
            required_skills_data.append([req_id, jid, s])
            req_id += 1
            
    required_skills = pd.DataFrame(required_skills_data, columns=['id', 'job_id', 'skill_name'])

    return programs, program_stats, program_courses, learned_skills, companies, job_postings, required_skills

# Load data
programs, program_stats, program_courses, learned_skills, companies, job_postings, required_skills = load_mock_data()

st.title("📊 AI, Data Science & Statistics Job Market Dashboard")
st.markdown("Analyze the gap between university graduate supply and job market demand.")

tab1, tab2, tab3 = st.tabs(["🎓 Graduate Supply (Tab 1)", "💼 Job Demand (Tab 2)", "⚖️ Skill Mismatch (Tab 3)"])

# --- TAB 1: SUPPLY ---
with tab1:
    st.header("Graduate Supply & Learned Skills")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("Filters")
        selected_program = st.selectbox("Select Program", ["All"] + list(programs['program_name'].unique()))
        selected_year = st.selectbox("Select Year", ["All"] + sorted(list(program_stats['year'].unique())))
    
    # Filter Logic
    filt_stats = program_stats.copy()
    filt_progs = programs.copy()
    
    if selected_program != "All":
        prog_id = programs[programs['program_name'] == selected_program]['program_id'].values[0]
        filt_stats = filt_stats[filt_stats['program_id'] == prog_id]
        filt_progs = filt_progs[filt_progs['program_id'] == prog_id]
        
    if selected_year != "All":
        filt_stats = filt_stats[filt_stats['year'] == selected_year]
        
    # Merge for viz
    stats_viz = pd.merge(filt_stats, programs[['program_id', 'program_name']], on='program_id')
    
    with col2:
        # Chart 1.1: Graduates per program over time
        if not stats_viz.empty:
            fig1 = px.line(stats_viz.sort_values('year'), x='year', y='graduates_count', color='program_name', markers=True, title="Number of Graduates per Program by Year")
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.warning("No data for Chart 1.1")
            
    col3, col4 = st.columns(2)
    with col3:
        # Chart 1.3: Employment rates
        if not stats_viz.empty:
            avg_emp = stats_viz[['emp_rate_yr1', 'emp_rate_yr2', 'emp_rate_yr3']].mean().reset_index()
            avg_emp.columns = ['Year after Grad', 'Employment Rate (%)']
            fig3 = px.bar(avg_emp, x='Year after Grad', y='Employment Rate (%)', title="Average Employment Rates (1-3 Yrs)", range_y=[0, 100])
            st.plotly_chart(fig3, use_container_width=True)
            
    with col4:
        # Chart 1.4: Tuition KPI
        if not filt_progs.empty:
            avg_tuition = filt_progs['tuition_fee_per_year'].mean()
            fig4 = go.Figure(go.Indicator(
                mode = "number",
                value = avg_tuition,
                number = {'prefix': "$"},
                title = {"text": "Average Tuition Fee per Year"}
            ))
            st.plotly_chart(fig4, use_container_width=True)
            
    st.subheader("Mandatory Courses")
    # Chart 1.2: Courses Table
    filt_courses = program_courses[program_courses['program_id'].isin(filt_progs['program_id'])]
    st.dataframe(pd.merge(filt_courses, programs[['program_id', 'program_name']], on='program_id')[['program_name', 'course_name']], use_container_width=True)


# --- TAB 2: DEMAND ---
with tab2:
    st.header("Job Demand & Required Skills")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("Filters")
        selected_level = st.selectbox("Experience Level", ["All"] + list(job_postings['experience_level'].unique()))
        selected_role = st.selectbox("Job Role", ["All"] + list(job_postings['job_role'].unique()))
        selected_company = st.selectbox("Company", ["All"] + list(companies['company_name'].unique()))
        
    # Filter Logic
    filt_jobs = pd.merge(job_postings, companies[['company_id', 'company_name']], on='company_id')
    if selected_level != "All":
        filt_jobs = filt_jobs[filt_jobs['experience_level'] == selected_level]
    if selected_role != "All":
        filt_jobs = filt_jobs[filt_jobs['job_role'] == selected_role]
    if selected_company != "All":
        filt_jobs = filt_jobs[filt_jobs['company_name'] == selected_company]

    with col2:
        # Chart 2.1: Open positions by job role
        if not filt_jobs.empty:
            roles_agg = filt_jobs.groupby('job_role')['open_positions_count'].sum().reset_index()
            fig21 = px.pie(roles_agg, values='open_positions_count', names='job_role', title="Open Positions by Job Role")
            st.plotly_chart(fig21, use_container_width=True)
            
    col3, col4 = st.columns(2)
    with col3:
        # Chart 2.4: Salary distribution
        if not filt_jobs.empty:
            fig24 = px.box(filt_jobs, x='experience_level', y='salary_avg', title="Salary Distributions by Experience Level")
            st.plotly_chart(fig24, use_container_width=True)
            
    with col4:
        # Chart 2.3: Top hiring companies
        if not filt_jobs.empty:
            comp_agg = filt_jobs.groupby('company_name')['open_positions_count'].sum().reset_index().sort_values('open_positions_count', ascending=False)
            fig23 = px.bar(comp_agg, x='open_positions_count', y='company_name', orientation='h', title="Top Hiring Companies")
            st.plotly_chart(fig23, use_container_width=True)
            
    st.subheader("Top Demanded Skills")
    # Chart 2.2: Top skills
    filt_req_skills = required_skills[required_skills['job_id'].isin(filt_jobs['job_id'])]
    if not filt_req_skills.empty:
        skill_counts = filt_req_skills['skill_name'].value_counts().reset_index()
        skill_counts.columns = ['Skill', 'Frequency']
        fig22 = px.bar(skill_counts.head(10), x='Frequency', y='Skill', orientation='h', title="Top 10 Demanded Skills")
        st.plotly_chart(fig22, use_container_width=True)


# --- TAB 3: MISMATCH ---
with tab3:
    st.header("Skill Mismatch Analysis")
    st.markdown("Comparing the frequency of skills taught in universities vs. skills required in job postings.")
    
    # Calculate Supply (learned skills frequency)
    supply_freq = learned_skills['skill_name'].value_counts().reset_index()
    supply_freq.columns = ['Skill', 'Supply_Score']
    
    # Calculate Demand (required skills frequency)
    demand_freq = required_skills['skill_name'].value_counts().reset_index()
    demand_freq.columns = ['Skill', 'Demand_Score']
    
    # Merge
    mismatch_df = pd.merge(demand_freq, supply_freq, on='Skill', how='outer').fillna(0)
    
    # Normalize scores for better visualization
    if not mismatch_df.empty:
        mismatch_df['Supply_Norm'] = (mismatch_df['Supply_Score'] / mismatch_df['Supply_Score'].max()) * 100
        mismatch_df['Demand_Norm'] = (mismatch_df['Demand_Score'] / mismatch_df['Demand_Score'].max()) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Chart 3.1: Diverging Bar Chart approximation (Grouped Bar)
            viz_df = mismatch_df.melt(id_vars='Skill', value_vars=['Supply_Norm', 'Demand_Norm'], var_name='Type', value_name='Score')
            viz_df['Type'] = viz_df['Type'].replace({'Supply_Norm': 'Supply (Universities)', 'Demand_Norm': 'Demand (Jobs)'})
            
            fig31 = px.bar(viz_df, x='Score', y='Skill', color='Type', barmode='group', orientation='h', 
                           title="Skill Supply vs Demand (Normalized)", height=600)
            st.plotly_chart(fig31, use_container_width=True)
            
        with col2:
            # Chart 3.2: Mismatch Matrix Scatter Plot
            mismatch_df['Mismatch_Gap'] = mismatch_df['Demand_Norm'] - mismatch_df['Supply_Norm']
            
            fig32 = px.scatter(mismatch_df, x='Demand_Norm', y='Supply_Norm', text='Skill', 
                               color='Mismatch_Gap', color_continuous_scale='RdYlGn_r',
                               title="Mismatch Matrix: Demand vs Supply",
                               labels={'Demand_Norm': 'Demand Score', 'Supply_Norm': 'Supply Score'},
                               height=600)
            
            # Add quadrant lines
            fig32.add_hline(y=50, line_dash="dash", line_color="gray")
            fig32.add_vline(x=50, line_dash="dash", line_color="gray")
            
            fig32.update_traces(textposition='top center')
            st.plotly_chart(fig32, use_container_width=True)

