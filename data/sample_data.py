SAMPLE_JOB_DESCRIPTIONS = {
    "Software Engineer": """
    We are looking for a skilled Software Engineer to join our development team. 
    
    Requirements:
    - 3+ years of experience in software development
    - Proficiency in Python, JavaScript, and React
    - Experience with cloud platforms (AWS preferred)
    - Knowledge of Docker and Kubernetes
    - Experience with REST APIs and microservices
    - Bachelor's degree in Computer Science or related field
    - Strong understanding of Git, Agile development, and CI/CD
    - Experience with SQL databases (PostgreSQL, MySQL)
    
    Preferred:
    - Experience with Django or Flask
    - Knowledge of machine learning libraries
    - AWS certifications
    - Experience with automated testing
    """,
    
    "Data Scientist": """
    We are seeking a Data Scientist to analyze complex datasets and build predictive models.
    
    Requirements:
    - Master's degree in Statistics, Mathematics, Computer Science, or related field
    - 2+ years of experience in data science or analytics
    - Proficiency in Python and R
    - Experience with machine learning libraries (scikit-learn, TensorFlow, PyTorch)
    - Strong knowledge of statistics and statistical modeling
    - Experience with data visualization tools (Tableau, Power BI, matplotlib)
    - Knowledge of SQL and database management
    - Experience with pandas, NumPy, and Jupyter notebooks
    
    Preferred:
    - PhD in quantitative field
    - Experience with big data technologies (Spark, Hadoop)
    - Knowledge of cloud platforms (AWS, Azure, GCP)
    - Experience with NLP and deep learning
    """,
    
    "Frontend Developer": """
    We are looking for a Frontend Developer to create engaging user interfaces.
    
    Requirements:
    - 2+ years of frontend development experience
    - Proficiency in HTML, CSS, and JavaScript
    - Strong experience with React or Angular
    - Knowledge of responsive design and cross-browser compatibility
    - Experience with modern build tools (Webpack, Vite, etc.)
    - Understanding of RESTful APIs and AJAX
    - Version control with Git
    - Bachelor's degree or equivalent experience
    
    Preferred:
    - Experience with TypeScript
    - Knowledge of CSS preprocessors (SASS, SCSS)
    - Experience with testing frameworks (Jest, Cypress)
    - Understanding of accessibility standards
    - Experience with design systems and component libraries
    """
}

SAMPLE_RESUMES = {
    "software_engineer": """
    John Doe
    Software Engineer
    Email: john.doe@email.com
    Phone: (555) 123-4567
    
    PROFESSIONAL SUMMARY
    Experienced Software Engineer with 4 years of developing scalable web applications using Python and JavaScript.
    
    EXPERIENCE
    Software Developer | TechCorp Inc. | Jan 2021 - Present
    • Developed and maintained web applications using Python, Django, and React
    • Built RESTful APIs serving 100,000+ daily requests
    • Implemented CI/CD pipelines using Jenkins and Docker
    • Collaborated with cross-functional teams using Agile methodologies
    • Worked with PostgreSQL and Redis databases
    • Deployed applications on AWS EC2 and managed infrastructure
    
    Junior Developer | StartupXYZ | Jun 2020 - Dec 2020
    • Created responsive web interfaces using HTML, CSS, and JavaScript
    • Developed React components and implemented state management with Redux
    • Participated in code reviews and sprint planning sessions
    • Used Git for version control and collaborated with team of 5 developers
    
    EDUCATION
    Bachelor of Science in Computer Science
    State University | 2016 - 2020
    GPA: 3.7/4.0
    
    TECHNICAL SKILLS
    Programming Languages: Python, JavaScript, Java, SQL
    Frameworks: Django, React, Flask, Node.js
    Databases: PostgreSQL, MySQL, Redis
    Cloud: AWS (EC2, S3, Lambda), Docker, Kubernetes
    Tools: Git, Jenkins, JIRA, VS Code
    Other: REST APIs, Agile, Test-Driven Development
    
    PROJECTS
    E-commerce Platform | Personal Project
    • Built full-stack e-commerce application using Django and React
    • Implemented payment processing with Stripe API
    • Deployed on AWS with automated CI/CD pipeline
    
    CERTIFICATIONS
    • AWS Certified Developer Associate (2023)
    • Scrum Master Certification (2022)
    """,
    
    "data_scientist": """
    Jane Smith
    Data Scientist
    Email: jane.smith@email.com
    Phone: (555) 987-6543
    
    PROFESSIONAL SUMMARY
    Data Scientist with 3 years of experience in machine learning, statistical analysis, and data visualization.
    
    EXPERIENCE
    Data Scientist | DataTech Solutions | Mar 2022 - Present
    • Developed machine learning models improving customer retention by 25%
    • Performed statistical analysis on datasets with 1M+ records using Python and R
    • Created interactive dashboards using Tableau and Power BI for executive reporting
    • Implemented predictive models using scikit-learn, TensorFlow, and PyTorch
    • Collaborated with product teams to define key metrics and KPIs
    • Built automated data pipelines using Apache Airflow
    
    Data Analyst | Analytics Corp | Jan 2021 - Feb 2022
    • Analyzed customer behavior data to identify trends and patterns
    • Created data visualizations using matplotlib, seaborn, and plotly
    • Performed A/B testing analysis and statistical significance testing
    • Worked with SQL databases to extract and transform data
    • Generated weekly reports for stakeholders using Jupyter notebooks
    
    EDUCATION
    Master of Science in Statistics
    Tech University | 2019 - 2021
    Thesis: "Machine Learning Applications in Customer Behavior Analysis"
    GPA: 3.8/4.0
    
    Bachelor of Science in Mathematics
    State College | 2015 - 2019
    Minor in Computer Science
    
    TECHNICAL SKILLS
    Programming: Python, R, SQL, MATLAB
    Machine Learning: scikit-learn, TensorFlow, PyTorch, Keras
    Data Analysis: pandas, NumPy, SciPy, statsmodels
    Visualization: Tableau, Power BI, matplotlib, seaborn, plotly
    Databases: PostgreSQL, MySQL, MongoDB
    Cloud: AWS (S3, Redshift, SageMaker), Google Cloud Platform
    Tools: Jupyter, Git, Docker, Apache Airflow
    
    PROJECTS
    Customer Churn Prediction Model
    • Built ensemble model achieving 92% accuracy in predicting customer churn
    • Used feature engineering and hyperparameter tuning to optimize performance
    • Deployed model using Flask API on AWS EC2
    
    Time Series Forecasting for Sales
    • Developed LSTM model for sales forecasting with 15% improvement over baseline
    • Implemented using TensorFlow and deployed on Google Cloud Platform
    
    CERTIFICATIONS
    • AWS Certified Machine Learning Specialty (2023)
    • Tableau Desktop Specialist (2022)
    • Google Analytics Certified (2021)
    
    PUBLICATIONS
    • "Advanced Statistical Methods for Customer Analysis" - Journal of Data Science (2023)
    """
}

def get_sample_job_description(job_type: str) -> str:
    """Get sample job description by type"""
    return SAMPLE_JOB_DESCRIPTIONS.get(job_type, "")

def get_sample_resume(resume_type: str) -> str:
    """Get sample resume by type"""
    return SAMPLE_RESUMES.get(resume_type, "")

def get_all_samples():
    """Get all sample data"""
    return {
        'job_descriptions': SAMPLE_JOB_DESCRIPTIONS,
        'resumes': SAMPLE_RESUMES
    }