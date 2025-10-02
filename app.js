// Sample Data
const sampleData = {
    jobDescriptions: {
        'software-engineer': {
            title: "Software Engineer",
            description: "We are looking for a Software Engineer with 3+ years of experience in Python, JavaScript, and React. Must have experience with cloud platforms like AWS, Docker, and REST APIs. Bachelor's degree in Computer Science required. Experience with agile development, Git, and SQL databases preferred."
        },
        'data-scientist': {
            title: "Data Scientist", 
            description: "Seeking a Data Scientist with expertise in Python, R, machine learning, and statistical analysis. Must have experience with pandas, scikit-learn, TensorFlow, and data visualization tools. PhD or Master's in Statistics, Mathematics, or related field required. 2+ years of industry experience with big data technologies."
        },
        'frontend-developer': {
            title: "Frontend Developer",
            description: "Frontend Developer needed with strong skills in HTML, CSS, JavaScript, React, and TypeScript. Experience with responsive design, RESTful APIs, and modern build tools required. 2+ years of professional experience. Knowledge of testing frameworks and accessibility standards preferred."
        }
    },
    resumes: {
        'john-doe': "John Doe\nSoftware Engineer\nEmail: john.doe@email.com\nPhone: (555) 123-4567\n\nEXPERIENCE:\nSoftware Developer | TechCorp | 2021-2024\n- Developed web applications using Python and Django\n- Built RESTful APIs and microservices\n- Worked with MySQL and PostgreSQL databases\n- Collaborated using Git and Agile methodologies\n\nJunior Developer | StartupXYZ | 2020-2021\n- Created responsive web interfaces using HTML, CSS, JavaScript\n- Implemented React components and state management\n- Participated in code reviews and sprint planning\n\nEDUCATION:\nBachelor of Science in Computer Science\nState University | 2016-2020\nGPA: 3.7/4.0\n\nSKILLS:\nPython, JavaScript, React, Django, MySQL, Git, HTML, CSS, REST APIs, Agile Development",
        'jane-smith': "Jane Smith\nData Scientist\nEmail: jane.smith@email.com\nPhone: (555) 987-6543\n\nEXPERIENCE:\nData Analyst | DataTech Solutions | 2022-2024\n- Performed statistical analysis using Python and R\n- Built machine learning models with scikit-learn\n- Created data visualizations using matplotlib and seaborn\n- Worked with large datasets and SQL databases\n\nResearch Assistant | University Lab | 2021-2022\n- Conducted statistical research on behavioral data\n- Applied machine learning techniques for pattern recognition\n- Published findings in peer-reviewed journals\n\nEDUCATION:\nMaster of Science in Statistics\nTech University | 2020-2022\nThesis: \"Machine Learning Applications in Behavioral Analysis\"\n\nBachelor of Science in Mathematics\nState College | 2016-2020\n\nSKILLS:\nPython, R, Machine Learning, Statistics, pandas, scikit-learn, SQL, Data Visualization, Research"
    }
};

// DOM Elements
const jobDescriptionTextarea = document.getElementById('jobDescription');
const resumeTextarea = document.getElementById('resumeText');
const fileInput = document.getElementById('fileInput');
const fileUploadArea = document.getElementById('fileUploadArea');
const uploadedFile = document.getElementById('uploadedFile');
const fileName = document.getElementById('fileName');
const removeFileBtn = document.getElementById('removeFile');
const browseBtn = document.getElementById('browseBtn');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultsSection = document.getElementById('resultsSection');
const sampleJobSelect = document.getElementById('sampleJobSelect');
const sampleResumeSelect = document.getElementById('sampleResumeSelect');
const clearJobBtn = document.getElementById('clearJobBtn');
const clearResumeBtn = document.getElementById('clearResumeBtn');
const charCount = document.getElementById('charCount');

// Initialize App
document.addEventListener('DOMContentLoaded', function() {
    console.log('App initialized');
    initializeEventListeners();
    updateAnalyzeButtonState();
});

function initializeEventListeners() {
    // Character counter
    jobDescriptionTextarea.addEventListener('input', updateCharacterCount);
    
    // File upload
    browseBtn.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', handleFileUpload);
    removeFileBtn.addEventListener('click', removeFile);
    
    // Drag and drop
    fileUploadArea.addEventListener('dragover', handleDragOver);
    fileUploadArea.addEventListener('dragleave', handleDragLeave);
    fileUploadArea.addEventListener('drop', handleFileDrop);
    
    // Sample data selection - Fixed event listeners
    sampleJobSelect.addEventListener('change', function(event) {
        loadSampleJob(event.target.value);
    });
    sampleResumeSelect.addEventListener('change', function(event) {
        loadSampleResume(event.target.value);
    });
    
    // Clear buttons
    clearJobBtn.addEventListener('click', clearJobDescription);
    clearResumeBtn.addEventListener('click', clearResume);
    
    // Input validation
    jobDescriptionTextarea.addEventListener('input', updateAnalyzeButtonState);
    resumeTextarea.addEventListener('input', updateAnalyzeButtonState);
    
    // Analyze button
    analyzeBtn.addEventListener('click', analyzeResume);
    
    console.log('All event listeners initialized');
}

function updateCharacterCount() {
    const count = jobDescriptionTextarea.value.length;
    charCount.textContent = count.toLocaleString();
}

function updateAnalyzeButtonState() {
    const hasJobDescription = jobDescriptionTextarea.value.trim().length > 0;
    const hasResume = resumeTextarea.value.trim().length > 0 || fileInput.files.length > 0;
    
    analyzeBtn.disabled = !(hasJobDescription && hasResume);
}

// File Upload Functions
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        displayUploadedFile(file);
        simulateFileRead(file);
    }
}

function handleDragOver(event) {
    event.preventDefault();
    fileUploadArea.classList.add('dragover');
}

function handleDragLeave(event) {
    event.preventDefault();
    fileUploadArea.classList.remove('dragover');
}

function handleFileDrop(event) {
    event.preventDefault();
    fileUploadArea.classList.remove('dragover');
    
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        const file = files[0];
        fileInput.files = files;
        displayUploadedFile(file);
        simulateFileRead(file);
    }
}

function displayUploadedFile(file) {
    fileName.textContent = file.name;
    fileUploadArea.style.display = 'none';
    uploadedFile.style.display = 'block';
    updateAnalyzeButtonState();
}

function removeFile() {
    fileInput.value = '';
    fileUploadArea.style.display = 'block';
    uploadedFile.style.display = 'none';
    resumeTextarea.value = '';
    updateAnalyzeButtonState();
}

function simulateFileRead(file) {
    // Simulate file reading - in real implementation, you'd use FileReader API
    // For demo purposes, we'll use sample resume text
    const sampleText = "Sample resume content from uploaded file: " + file.name + "\n\n" + 
                      sampleData.resumes['john-doe'];
    resumeTextarea.value = sampleText;
}

// Sample Data Functions - Fixed functions
function loadSampleJob(selectedJob) {
    console.log('Loading sample job:', selectedJob);
    if (selectedJob && sampleData.jobDescriptions[selectedJob]) {
        jobDescriptionTextarea.value = sampleData.jobDescriptions[selectedJob].description;
        updateCharacterCount();
        updateAnalyzeButtonState();
    }
}

function loadSampleResume(selectedResume) {
    console.log('Loading sample resume:', selectedResume);
    if (selectedResume && sampleData.resumes[selectedResume]) {
        resumeTextarea.value = sampleData.resumes[selectedResume];
        removeFile(); // Clear any uploaded file
        updateAnalyzeButtonState();
    }
}

function clearJobDescription() {
    jobDescriptionTextarea.value = '';
    sampleJobSelect.value = '';
    updateCharacterCount();
    updateAnalyzeButtonState();
}

function clearResume() {
    resumeTextarea.value = '';
    sampleResumeSelect.value = '';
    removeFile();
    updateAnalyzeButtonState();
}

// Analysis Functions
async function analyzeResume() {
    const jobDescription = jobDescriptionTextarea.value.trim();
    const resumeText = resumeTextarea.value.trim();
    
    if (!jobDescription || !resumeText) {
        alert('Please provide both job description and resume text.');
        return;
    }
    
    // Show loading state
    showLoadingState();
    
    // Simulate analysis delay
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Perform analysis
    const analysisResults = performResumeAnalysis(jobDescription, resumeText);
    
    // Hide loading state and show results
    hideLoadingState();
    displayResults(analysisResults);
}

function showLoadingState() {
    analyzeBtn.querySelector('.btn-text').style.display = 'none';
    analyzeBtn.querySelector('.loading-spinner').style.display = 'block';
    analyzeBtn.disabled = true;
}

function hideLoadingState() {
    analyzeBtn.querySelector('.btn-text').style.display = 'block';
    analyzeBtn.querySelector('.loading-spinner').style.display = 'none';
    analyzeBtn.disabled = false;
    updateAnalyzeButtonState();
}

function performResumeAnalysis(jobDescription, resumeText) {
    // Extract skills and keywords
    const jobSkills = extractSkills(jobDescription);
    const resumeSkills = extractSkills(resumeText);
    
    // Calculate matches
    const matchedSkills = jobSkills.filter(skill => 
        resumeSkills.some(resumeSkill => 
            resumeSkill.toLowerCase().includes(skill.toLowerCase()) ||
            skill.toLowerCase().includes(resumeSkill.toLowerCase())
        )
    );
    
    const missingSkills = jobSkills.filter(skill => 
        !matchedSkills.some(matched => 
            matched.toLowerCase() === skill.toLowerCase()
        )
    );
    
    const additionalSkills = resumeSkills.filter(skill => 
        !jobSkills.some(jobSkill => 
            jobSkill.toLowerCase().includes(skill.toLowerCase()) ||
            skill.toLowerCase().includes(jobSkill.toLowerCase())
        )
    );
    
    // Calculate score
    const score = calculateMatchScore(matchedSkills.length, jobSkills.length, resumeText, jobDescription);
    
    // Generate recommendations
    const recommendations = generateRecommendations(missingSkills, jobDescription, resumeText);
    
    return {
        score,
        matchedSkills,
        missingSkills,
        additionalSkills,
        recommendations,
        experienceAnalysis: analyzeExperience(jobDescription, resumeText),
        actionItems: generateActionItems(missingSkills, score)
    };
}

function extractSkills(text) {
    const commonSkills = [
        'Python', 'JavaScript', 'React', 'AWS', 'Docker', 'Git', 'SQL', 'HTML', 'CSS',
        'REST APIs', 'Machine Learning', 'Data Science', 'TensorFlow', 'pandas', 'scikit-learn',
        'R', 'Statistics', 'Java', 'C++', 'Node.js', 'Angular', 'Vue.js', 'TypeScript',
        'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Kubernetes', 'Jenkins', 'CI/CD',
        'Agile', 'Scrum', 'Project Management', 'Leadership', 'Communication', 'Teamwork',
        'Problem Solving', 'Django', 'Flask', 'Express.js', 'Spring Boot', 'GraphQL',
        'Microservices', 'DevOps', 'Azure', 'GCP', 'Terraform', 'Ansible'
    ];
    
    const foundSkills = [];
    const lowerText = text.toLowerCase();
    
    commonSkills.forEach(skill => {
        if (lowerText.includes(skill.toLowerCase())) {
            foundSkills.push(skill);
        }
    });
    
    return foundSkills;
}

function calculateMatchScore(matchedCount, totalRequired, resumeText, jobDescription) {
    const baseScore = totalRequired > 0 ? (matchedCount / totalRequired) * 70 : 0;
    
    // Additional scoring factors
    let bonusPoints = 0;
    
    // Education bonus
    if (jobDescription.toLowerCase().includes('bachelor') && resumeText.toLowerCase().includes('bachelor')) {
        bonusPoints += 10;
    }
    if (jobDescription.toLowerCase().includes('master') && resumeText.toLowerCase().includes('master')) {
        bonusPoints += 15;
    }
    
    // Experience bonus
    const experienceMatch = checkExperienceMatch(jobDescription, resumeText);
    bonusPoints += experienceMatch;
    
    // Keywords density bonus
    const keywordDensity = calculateKeywordDensity(jobDescription, resumeText);
    bonusPoints += keywordDensity;
    
    return Math.min(100, Math.round(baseScore + bonusPoints));
}

function checkExperienceMatch(jobDescription, resumeText) {
    const jobYears = extractYearsExperience(jobDescription);
    const resumeYears = extractYearsExperience(resumeText);
    
    if (jobYears && resumeYears) {
        if (resumeYears >= jobYears) return 10;
        if (resumeYears >= jobYears * 0.7) return 5;
    }
    
    return 0;
}

function extractYearsExperience(text) {
    const match = text.match(/(\d+)\+?\s*years?/i);
    return match ? parseInt(match[1]) : null;
}

function calculateKeywordDensity(jobDescription, resumeText) {
    const jobWords = jobDescription.toLowerCase().split(/\W+/);
    const resumeWords = resumeText.toLowerCase().split(/\W+/);
    
    const importantJobWords = jobWords.filter(word => 
        word.length > 3 && 
        !['this', 'that', 'with', 'will', 'have', 'must', 'required', 'preferred'].includes(word)
    );
    
    const matchingWords = importantJobWords.filter(word => 
        resumeWords.includes(word)
    );
    
    const density = importantJobWords.length > 0 ? 
        (matchingWords.length / importantJobWords.length) * 10 : 0;
    
    return Math.round(density);
}

function generateRecommendations(missingSkills, jobDescription, resumeText) {
    const recommendations = {
        improvements: [],
        keywords: [],
        ats: [
            "Use standard section headers like 'EXPERIENCE' and 'EDUCATION'",
            "Include keywords from the job description naturally in your content",
            "Save your resume as a PDF with a simple, clean format",
            "Avoid graphics, tables, and complex formatting that may confuse ATS systems",
            "Use bullet points to improve readability"
        ]
    };
    
    // Generate improvement suggestions
    if (missingSkills.length > 0) {
        recommendations.improvements.push(
            `Add experience with ${missingSkills.slice(0, 3).join(', ')} to strengthen your technical profile`
        );
        recommendations.improvements.push(
            `Include projects or coursework that demonstrate ${missingSkills[0]} skills`
        );
    }
    
    if (!resumeText.toLowerCase().includes('project')) {
        recommendations.improvements.push(
            "Add a 'Projects' section to showcase your technical abilities"
        );
    }
    
    if (!resumeText.toLowerCase().includes('certification')) {
        recommendations.improvements.push(
            "Consider adding relevant certifications to boost your qualifications"
        );
    }
    
    recommendations.improvements.push(
        "Quantify your achievements with specific metrics and numbers",
        "Use action verbs to start each bullet point in your experience section"
    );
    
    // Generate keyword suggestions
    recommendations.keywords = missingSkills.slice(0, 5);
    
    return recommendations;
}

function analyzeExperience(jobDescription, resumeText) {
    const analysis = {};
    
    // Experience Level
    const jobYears = extractYearsExperience(jobDescription);
    const resumeYears = extractYearsExperience(resumeText);
    
    analysis.experienceLevel = {
        required: jobYears ? `${jobYears}+ years` : 'Not specified',
        found: resumeYears ? `${resumeYears} years` : 'Not clearly specified',
        match: jobYears && resumeYears ? resumeYears >= jobYears : false
    };
    
    // Education
    const educationRequirement = extractEducationRequirement(jobDescription);
    const educationFound = extractEducationFound(resumeText);
    
    analysis.education = {
        required: educationRequirement,
        found: educationFound,
        match: checkEducationMatch(educationRequirement, educationFound)
    };
    
    // Industry Experience
    analysis.industryFit = {
        score: calculateIndustryFit(jobDescription, resumeText),
        description: "Based on relevant industry keywords and context"
    };
    
    return analysis;
}

function extractEducationRequirement(text) {
    if (text.toLowerCase().includes('phd')) return 'PhD';
    if (text.toLowerCase().includes('master')) return "Master's Degree";
    if (text.toLowerCase().includes('bachelor')) return "Bachelor's Degree";
    return 'Not specified';
}

function extractEducationFound(text) {
    if (text.toLowerCase().includes('phd')) return 'PhD';
    if (text.toLowerCase().includes('master')) return "Master's Degree";
    if (text.toLowerCase().includes('bachelor')) return "Bachelor's Degree";
    return 'Not specified';
}

function checkEducationMatch(required, found) {
    const levels = ['Not specified', "Bachelor's Degree", "Master's Degree", 'PhD'];
    const requiredLevel = levels.indexOf(required);
    const foundLevel = levels.indexOf(found);
    return foundLevel >= requiredLevel;
}

function calculateIndustryFit(jobDescription, resumeText) {
    const industryKeywords = [
        'software', 'technology', 'development', 'engineering', 'data', 'analytics',
        'machine learning', 'artificial intelligence', 'web', 'mobile', 'cloud'
    ];
    
    const jobIndustryWords = industryKeywords.filter(keyword => 
        jobDescription.toLowerCase().includes(keyword)
    );
    
    const resumeIndustryWords = industryKeywords.filter(keyword => 
        resumeText.toLowerCase().includes(keyword)
    );
    
    const commonWords = jobIndustryWords.filter(word => 
        resumeIndustryWords.includes(word)
    );
    
    return jobIndustryWords.length > 0 ? 
        Math.round((commonWords.length / jobIndustryWords.length) * 100) : 50;
}

function generateActionItems(missingSkills, score) {
    const items = [];
    
    if (score < 40) {
        items.push({
            priority: 'HIGH',
            text: 'Major resume overhaul needed - consider restructuring entire resume'
        });
    }
    
    if (missingSkills.length > 5) {
        items.push({
            priority: 'HIGH',
            text: `Add ${missingSkills.slice(0, 3).join(', ')} skills through projects or training`
        });
    }
    
    if (missingSkills.length > 2) {
        items.push({
            priority: 'MEDIUM',
            text: 'Include relevant coursework or online certifications'
        });
    }
    
    items.push({
        priority: 'MEDIUM',
        text: 'Optimize resume formatting for ATS compatibility'
    });
    
    items.push({
        priority: 'LOW',
        text: 'Add quantifiable achievements and metrics to experience section'
    });
    
    return items;
}

function displayResults(results) {
    // Show results section
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
    
    // Display score
    displayScore(results.score);
    
    // Display skills analysis
    displaySkills(results.matchedSkills, results.missingSkills, results.additionalSkills);
    
    // Display recommendations
    displayRecommendations(results.recommendations);
    
    // Display experience analysis
    displayExperienceAnalysis(results.experienceAnalysis);
    
    // Display action items
    displayActionItems(results.actionItems);
}

function displayScore(score) {
    const progressValue = document.getElementById('progressValue');
    const compatibilityRating = document.getElementById('compatibilityRating');
    const scoreDescription = document.getElementById('scoreDescription');
    const circularProgress = document.getElementById('circularProgress');
    
    // Animate score
    let currentScore = 0;
    const increment = score / 50;
    const timer = setInterval(() => {
        currentScore += increment;
        if (currentScore >= score) {
            currentScore = score;
            clearInterval(timer);
        }
        progressValue.textContent = Math.round(currentScore) + '%';
        
        // Update circular progress
        circularProgress.style.setProperty('--score', currentScore);
    }, 40);
    
    // Set rating and description
    if (score >= 80) {
        compatibilityRating.textContent = 'Excellent Match';
        scoreDescription.textContent = 'Your resume is highly compatible with this job role.';
        circularProgress.className = 'circular-progress score-excellent';
    } else if (score >= 60) {
        compatibilityRating.textContent = 'Good Match';
        scoreDescription.textContent = 'Your resume shows good compatibility with some areas for improvement.';
        circularProgress.className = 'circular-progress score-good';
    } else if (score >= 40) {
        compatibilityRating.textContent = 'Needs Improvement';
        scoreDescription.textContent = 'Your resume needs significant improvements to match this role.';
        circularProgress.className = 'circular-progress score-needs-improvement';
    } else {
        compatibilityRating.textContent = 'Poor Match';
        scoreDescription.textContent = 'Major changes are needed to align with this job role.';
        circularProgress.className = 'circular-progress score-poor';
    }
}

function displaySkills(matched, missing, additional) {
    const matchedContainer = document.getElementById('matchedSkills');
    const missingContainer = document.getElementById('missingSkills');
    const additionalContainer = document.getElementById('additionalSkills');
    
    // Clear containers
    [matchedContainer, missingContainer, additionalContainer].forEach(container => {
        container.innerHTML = '';
    });
    
    // Display matched skills
    if (matched.length > 0) {
        matched.forEach(skill => {
            const tag = createSkillTag(skill, 'matched');
            matchedContainer.appendChild(tag);
        });
    } else {
        matchedContainer.innerHTML = '<div class="empty-state">No matching skills found</div>';
    }
    
    // Display missing skills
    if (missing.length > 0) {
        missing.forEach(skill => {
            const tag = createSkillTag(skill, 'missing');
            missingContainer.appendChild(tag);
        });
    } else {
        missingContainer.innerHTML = '<div class="empty-state">No missing skills - great job!</div>';
    }
    
    // Display additional skills
    if (additional.length > 0) {
        additional.slice(0, 10).forEach(skill => {
            const tag = createSkillTag(skill, 'additional');
            additionalContainer.appendChild(tag);
        });
    } else {
        additionalContainer.innerHTML = '<div class="empty-state">No additional skills identified</div>';
    }
}

function createSkillTag(skill, type) {
    const tag = document.createElement('span');
    tag.className = `skill-tag skill-tag--${type}`;
    tag.textContent = skill;
    return tag;
}

function displayRecommendations(recommendations) {
    const improvementsContainer = document.getElementById('resumeImprovements');
    const keywordsContainer = document.getElementById('missingKeywords');
    const atsContainer = document.getElementById('atsOptimization');
    
    // Clear containers
    [improvementsContainer, keywordsContainer, atsContainer].forEach(container => {
        container.innerHTML = '';
    });
    
    // Display improvements
    recommendations.improvements.forEach(improvement => {
        const li = document.createElement('li');
        li.textContent = improvement;
        improvementsContainer.appendChild(li);
    });
    
    // Display missing keywords
    if (recommendations.keywords.length > 0) {
        recommendations.keywords.forEach(keyword => {
            const li = document.createElement('li');
            li.textContent = `Add "${keyword}" to relevant sections`;
            keywordsContainer.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'Good keyword coverage detected';
        keywordsContainer.appendChild(li);
    }
    
    // Display ATS optimization
    recommendations.ats.forEach(tip => {
        const li = document.createElement('li');
        li.textContent = tip;
        atsContainer.appendChild(li);
    });
}

function displayExperienceAnalysis(analysis) {
    const container = document.getElementById('experienceAnalysis');
    container.innerHTML = '';
    
    // Experience Level
    const expDiv = document.createElement('div');
    expDiv.className = 'experience-item';
    expDiv.innerHTML = `
        <strong>Experience Level</strong>
        <span>Required: ${analysis.experienceLevel.required}</span>
        <span>Found: ${analysis.experienceLevel.found}</span>
        <span style="color: ${analysis.experienceLevel.match ? 'var(--color-success)' : 'var(--color-error)'}">
            ${analysis.experienceLevel.match ? '✓ Meets requirement' : '✗ Below requirement'}
        </span>
    `;
    container.appendChild(expDiv);
    
    // Education
    const eduDiv = document.createElement('div');
    eduDiv.className = 'experience-item';
    eduDiv.innerHTML = `
        <strong>Education</strong>
        <span>Required: ${analysis.education.required}</span>
        <span>Found: ${analysis.education.found}</span>
        <span style="color: ${analysis.education.match ? 'var(--color-success)' : 'var(--color-error)'}">
            ${analysis.education.match ? '✓ Meets requirement' : '✗ Below requirement'}
        </span>
    `;
    container.appendChild(eduDiv);
    
    // Industry Fit
    const industryDiv = document.createElement('div');
    industryDiv.className = 'experience-item';
    industryDiv.innerHTML = `
        <strong>Industry Fit</strong>
        <span>${analysis.industryFit.score}% match</span>
        <span>${analysis.industryFit.description}</span>
    `;
    container.appendChild(industryDiv);
}

function displayActionItems(actionItems) {
    const container = document.getElementById('actionItems');
    container.innerHTML = '';
    
    actionItems.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'action-item';
        itemDiv.innerHTML = `
            <div class="action-priority action-priority--${item.priority.toLowerCase()}">${item.priority}</div>
            <div class="action-text">${item.text}</div>
        `;
        container.appendChild(itemDiv);
    });
}