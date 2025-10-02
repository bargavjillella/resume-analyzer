TECHNICAL_SKILLS = [
    # Programming Languages
    'Python', 'Java', 'JavaScript', 'TypeScript', 'C++', 'C#', 'C', 'Go', 'Rust', 'Swift',
    'Kotlin', 'PHP', 'Ruby', 'Scala', 'R', 'MATLAB', 'Perl', 'Shell Scripting', 'PowerShell',
    
    # Web Technologies
    'HTML', 'CSS', 'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'Next.js', 'Nuxt.js',
    'Django', 'Flask', 'FastAPI', 'Spring', 'Spring Boot', 'ASP.NET', 'Laravel', 'Ruby on Rails',
    'Bootstrap', 'Tailwind CSS', 'SASS', 'SCSS', 'jQuery', 'Redux', 'Vuex', 'GraphQL', 'REST API',
    
    # Databases
    'SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'SQLite', 'Oracle', 'SQL Server', 'Redis',
    'Cassandra', 'DynamoDB', 'Neo4j', 'Elasticsearch', 'InfluxDB',
    
    # Cloud Platforms
    'AWS', 'Azure', 'Google Cloud Platform', 'GCP', 'Docker', 'Kubernetes', 'Jenkins',
    'Terraform', 'Ansible', 'CloudFormation', 'Serverless', 'Lambda', 'EC2', 'S3',
    
    # Data Science & ML
    'Machine Learning', 'Deep Learning', 'Natural Language Processing', 'NLP', 'Computer Vision',
    'TensorFlow', 'PyTorch', 'Scikit-learn', 'Keras', 'Pandas', 'NumPy', 'Matplotlib',
    'Seaborn', 'Plotly', 'Jupyter', 'Apache Spark', 'Hadoop', 'Tableau', 'Power BI',
    
    # DevOps & Tools
    'Git', 'GitHub', 'GitLab', 'Bitbucket', 'CI/CD', 'Agile', 'Scrum', 'JIRA', 'Confluence',
    'Linux', 'Unix', 'Windows Server', 'VMware', 'VirtualBox', 'Nginx', 'Apache',
    
    # Mobile Development
    'Android', 'iOS', 'React Native', 'Flutter', 'Xamarin', 'Ionic', 'Cordova',
    
    # Testing
    'Unit Testing', 'Integration Testing', 'Selenium', 'Jest', 'Pytest', 'JUnit', 'Cypress',
    'Test Automation', 'Performance Testing', 'Load Testing',
    
    # Security
    'Cybersecurity', 'Information Security', 'Network Security', 'Penetration Testing',
    'Vulnerability Assessment', 'OWASP', 'SSL/TLS', 'OAuth', 'JWT'
]

SOFT_SKILLS = [
    'Communication', 'Leadership', 'Teamwork', 'Problem Solving', 'Critical Thinking',
    'Project Management', 'Time Management', 'Adaptability', 'Creativity', 'Initiative',
    'Analytical Thinking', 'Decision Making', 'Conflict Resolution', 'Negotiation',
    'Presentation Skills', 'Public Speaking', 'Writing Skills', 'Research Skills',
    'Customer Service', 'Sales', 'Marketing', 'Strategic Planning', 'Innovation'
]

CERTIFICATIONS = [
    'AWS Certified Solutions Architect', 'AWS Certified Developer', 'Azure Fundamentals',
    'Google Cloud Professional', 'PMP', 'Scrum Master', 'CISSP', 'CompTIA Security+',
    'Cisco CCNA', 'Red Hat Certified', 'Oracle Certified', 'Microsoft Certified',
    'Salesforce Certified', 'Six Sigma', 'ITIL', 'Agile Certified'
]

INDUSTRIES = [
    'Software Development', 'Data Science', 'Machine Learning', 'Artificial Intelligence',
    'Web Development', 'Mobile Development', 'DevOps', 'Cloud Computing', 'Cybersecurity',
    'Database Administration', 'Network Administration', 'IT Support', 'Quality Assurance',
    'Product Management', 'Project Management', 'Business Analysis', 'Digital Marketing',
    'E-commerce', 'FinTech', 'HealthTech', 'EdTech', 'Gaming', 'Blockchain'
]

def get_all_skills():
    """Return all skills combined"""
    return TECHNICAL_SKILLS + SOFT_SKILLS + CERTIFICATIONS + INDUSTRIES

def get_skills_by_category():
    """Return skills organized by category"""
    return {
        'technical': TECHNICAL_SKILLS,
        'soft': SOFT_SKILLS,
        'certifications': CERTIFICATIONS,
        'industries': INDUSTRIES
    }