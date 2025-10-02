import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO
import os
import tempfile
from typing import Dict, List

# Import our custom modules
from utils.resume_parser import ResumeParser
from utils.analyzer import ResumeAnalyzer
from utils.recommendations import RecommendationEngine
from data.skills_database import get_all_skills
from data.sample_data import get_sample_job_description, get_sample_resume

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .score-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .skill-tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        margin: 0.25rem;
        border-radius: 20px;
        font-size: 0.875rem;
    }
    
    .skill-matched {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    
    .skill-missing {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    
    .skill-additional {
        background-color: #cce7ff;
        color: #004085;
        border: 1px solid #b3d9ff;
    }
    
    .recommendation-item {
        background: #f8f9fa;
        color: #111111;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #007bff;
        border-radius: 5px;
    }
    
    .priority-high {
        border-left-color: #dc3545;
    }
    
    .priority-medium {
        border-left-color: #ffc107;
    }
    
    .priority-low {
        border-left-color: #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'resume_data' not in st.session_state:
    st.session_state.resume_data = None

# Initialize components
@st.cache_resource
def load_components():
    """Load and cache the analysis components"""
    parser = ResumeParser()
    analyzer = ResumeAnalyzer()
    recommender = RecommendationEngine()
    skills_db = get_all_skills()
    return parser, analyzer, recommender, skills_db

def create_score_gauge(score: int) -> go.Figure:
    """Create a gauge chart for the overall score"""
    color = "red" if score < 40 else "orange" if score < 70 else "green"
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Overall Compatibility Score"},
        delta = {'reference': 80},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 40], 'color': "lightgray"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "lightgreen"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(height=300)
    return fig

def create_skills_chart(skill_analysis: Dict) -> go.Figure:
    """Create a bar chart for skills analysis"""
    categories = ['Matched Skills', 'Missing Skills', 'Additional Skills']
    values = [
        len(skill_analysis['matched_skills']),
        len(skill_analysis['missing_skills']),
        len(skill_analysis['additional_skills'])
    ]
    colors = ['#28a745', '#dc3545', '#007bff']
    
    fig = go.Figure(data=[
        go.Bar(x=categories, y=values, marker_color=colors)
    ])
    
    fig.update_layout(
        title="Skills Analysis Breakdown",
        xaxis_title="Skill Categories",
        yaxis_title="Number of Skills",
        height=400
    )
    
    return fig

def display_skills(skills: List[str], skill_type: str) -> None:
    """Display skills as colored tags"""
    if not skills:
        st.write("None")
        return
    
    css_class = f"skill-{skill_type}"
    skills_html = ""
    for skill in skills[:20]:  # Limit display to first 20 skills
        skills_html += f'<span class="skill-tag {css_class}">{skill}</span>'
    
    if len(skills) > 20:
        skills_html += f'<span class="skill-tag {css_class}">... and {len(skills) - 20} more</span>'
    
    st.markdown(skills_html, unsafe_allow_html=True)

def display_recommendations(recommendations: Dict[str, List[str]]) -> None:
    """Display recommendations in an organized manner"""
    
    tab1, tab2, tab3, tab4 = st.tabs([" Priority Actions", " Skills", " Content", " ATS Optimization"])
    
    with tab1:
        st.subheader("High Priority Recommendations")
        priority_items = (
            recommendations['skill_recommendations'][:3] +
            recommendations['experience_recommendations'][:2]
        )
        for i, item in enumerate(priority_items, 1):
            st.markdown(f"""
            <div class="recommendation-item priority-high">
                <strong>{i}.</strong> {item}
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("Skills Enhancement")
        for item in recommendations['skill_recommendations']:
            st.markdown(f"• {item}")
        
        st.subheader("Keyword Optimization")
        for item in recommendations['keyword_optimization'][:5]:
            st.markdown(f"• {item}")
    
    with tab3:
        st.subheader("Content Improvements")
        for item in recommendations['content_improvements']:
            st.markdown(f"• {item}")
        
        st.subheader("Experience Enhancement")
        for item in recommendations['experience_recommendations']:
            st.markdown(f"• {item}")
    
    with tab4:
        st.subheader("ATS Optimization Tips")
        for item in recommendations['ats_optimization']:
            st.markdown(f"• {item}")
        
        st.subheader("Formatting Recommendations")
        for item in recommendations['formatting_tips']:
            st.markdown(f"• {item}")

def main():
    """Main application function"""
    
    # Load components
    parser, analyzer, recommender, skills_db = load_components()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Resume Analyzer</h1>
        <p>Optimize Your Resume for Any Job Role with AI-Powered Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for sample data
    with st.sidebar:
        st.header("🔧 Quick Start")
        st.write("Try our sample data to see the analyzer in action!")
        
        st.subheader("Sample Job Descriptions")
        sample_job = st.selectbox(
            "Choose a sample job:",
            ["None", "Software Engineer", "Data Scientist", "Frontend Developer"]
        )
        
        st.subheader("Sample Resumes")
        sample_resume = st.selectbox(
            "Choose a sample resume:",
            ["None", "Software Engineer Resume", "Data Scientist Resume"]
        )
        
        if st.button("Load Sample Data"):
            if sample_job != "None" and sample_resume != "None":
                # Load sample job description
                job_desc = get_sample_job_description(sample_job)
                resume_text = get_sample_resume(
                    "software_engineer" if "Software Engineer" in sample_resume 
                    else "data_scientist"
                )
                
                st.session_state.sample_job = job_desc
                st.session_state.sample_resume = resume_text
                st.success("Sample data loaded! Check the main panel.")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(" Job Description")
        
        # Use sample data if available
        default_job = st.session_state.get('sample_job', '')
        job_description = st.text_area(
            "Paste the job description here:",
            value=default_job,
            height=300,
            help="Copy and paste the complete job description you want to analyze against"
        )
        
        char_count = len(job_description)
        st.caption(f"Characters: {char_count}")
        
        if st.button("Clear Job Description"):
            job_description = ""
            st.rerun()
    
    with col2:
        st.subheader(" Resume Upload")
        
        # File upload option
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF or DOCX):",
            type=['pdf', 'docx'],
            help="Upload your resume in PDF or DOCX format"
        )
        
        st.write("**OR**")
        
        # Text input option
        default_resume = st.session_state.get('sample_resume', '')
        resume_text = st.text_area(
            "Paste your resume text here:",
            value=default_resume,
            height=200,
            help="Copy and paste your resume text directly"
        )
    
    # Analysis section
    st.markdown("---")
    
    # Check if we have both inputs
    has_job_description = bool(job_description.strip())
    has_resume = bool(uploaded_file or resume_text.strip())
    
    if has_job_description and has_resume:
        if st.button(" Analyze Resume", type="primary", use_container_width=True):
            with st.spinner(" Analyzing your resume... This may take a moment."):
                try:
                    # Parse resume
                    if uploaded_file:
                        # Handle file upload
                        file_type = 'pdf' if uploaded_file.type == 'application/pdf' else 'docx'
                        resume_data = parser.parse_resume(uploaded_file, file_type, skills_db)
                    else:
                        # Handle text input
                        resume_data = parser.parse_resume(resume_text, 'text', skills_db)
                    
                    # Perform analysis
                    analysis_results = analyzer.perform_full_analysis(resume_data, job_description)
                    
                    # Generate recommendations
                    recommendations = recommender.generate_comprehensive_recommendations(
                        resume_data, 
                        analysis_results['job_requirements'],
                        analysis_results['skill_analysis'],
                        analysis_results['score_breakdown']
                    )
                    
                    # Store results in session state
                    st.session_state.analysis_results = analysis_results
                    st.session_state.resume_data = resume_data
                    st.session_state.recommendations = recommendations
                    
                    st.success(" Analysis completed successfully!")
                    
                except Exception as e:
                    st.error(f" An error occurred during analysis: {str(e)}")
                    st.info("Please check your resume format and try again.")
    
    else:
        # Show requirements
        missing = []
        if not has_job_description:
            missing.append("job description")
        if not has_resume:
            missing.append("resume")
        
        st.info(f" Please provide {' and '.join(missing)} to start the analysis.")
    
    # Display results if available
    if st.session_state.analysis_results:
        st.markdown("---")
        st.header(" Analysis Results")
        
        analysis = st.session_state.analysis_results
        resume_data = st.session_state.resume_data
        recommendations = st.session_state.recommendations
        
        # Overall score
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            score_fig = create_score_gauge(analysis['score_breakdown']['overall_score'])
            st.plotly_chart(score_fig, use_container_width=True)
        
        with col2:
            st.metric(
                label="Similarity Score",
                value=f"{analysis['score_breakdown']['similarity_score']}%"
            )
            st.metric(
                label="Skills Match",
                value=f"{analysis['score_breakdown']['skill_match_percentage']}%"
            )
        
        with col3:
            st.metric(
                label="Experience",
                value=analysis['score_breakdown']['experience_match']
            )
            
            # Overall rating
            score = analysis['score_breakdown']['overall_score']
            if score >= 80:
                rating = " Excellent Match"
            elif score >= 60:
                rating = " Good Match"
            elif score >= 40:
                rating = " Needs Improvement"
            else:
                rating = " Poor Match"
            
            st.metric("Overall Rating", rating)
        
        # Skills analysis
        st.subheader(" Skills Analysis")
        
        skills_fig = create_skills_chart(analysis['skill_analysis'])
        st.plotly_chart(skills_fig, use_container_width=True)
        
        # Detailed skills breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("** Matched Skills**")
            display_skills(analysis['skill_analysis']['matched_skills'], 'matched')
        
        with col2:
            st.write("** Missing Skills**")
            display_skills(analysis['skill_analysis']['missing_skills'], 'missing')
        
        with col3:
            st.write("** Additional Skills**")
            display_skills(analysis['skill_analysis']['additional_skills'], 'additional')
        
        # Recommendations
        st.subheader(" Personalized Recommendations")
        display_recommendations(recommendations)
        
        # Detailed breakdown
        with st.expander(" Detailed Score Breakdown"):
            breakdown_df = pd.DataFrame([
                {"Metric": "Overall Compatibility", "Score": f"{analysis['score_breakdown']['overall_score']}%"},
                {"Metric": "Content Similarity", "Score": f"{analysis['score_breakdown']['similarity_score']}%"},
                {"Metric": "Skills Match", "Score": f"{analysis['score_breakdown']['skill_match_percentage']}%"},
                {"Metric": "Experience Match", "Score": analysis['score_breakdown']['experience_match']},
            ])
            st.dataframe(breakdown_df, use_container_width=True)
        
        # Contact information
        with st.expander(" Extracted Contact Information"):
            contact_info = resume_data['contact_info']
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Name:** {contact_info.get('name', 'Not found')}")
            with col2:
                st.write(f"**Email:** {contact_info.get('email', 'Not found')}")
            with col3:
                st.write(f"**Phone:** {contact_info.get('phone', 'Not found')}")

if __name__ == "__main__":
    main()