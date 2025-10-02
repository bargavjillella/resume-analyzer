import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from typing import Dict, List, Tuple
import spacy

class ResumeAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=1000,
            ngram_range=(1, 2)
        )
    
    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess text for analysis"""
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        # Remove special characters but keep important ones
        text = re.sub(r'[^\w\s\+\#\-\.]', ' ', text)
        return text.lower()
    
    def extract_keywords_from_job_description(self, job_description: str) -> Dict[str, List[str]]:
        """Extract key requirements from job description"""
        doc = self.nlp(job_description)
        
        # Technical skills patterns
        technical_patterns = [
            r'\b(?:python|java|javascript|react|angular|vue|node\.js|django|flask|spring|\.net)\b',
            r'\b(?:aws|azure|gcp|docker|kubernetes|git|sql|nosql|mongodb|postgresql)\b',
            r'\b(?:machine learning|deep learning|ai|ml|nlp|tensorflow|pytorch|scikit-learn)\b',
            r'\b(?:html|css|bootstrap|tailwind|scss|sass)\b'
        ]
        
        # Experience requirements
        experience_patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'minimum\s*(\d+)\s*years?',
            r'at least\s*(\d+)\s*years?'
        ]
        
        # Education requirements
        education_patterns = [
            r'bachelor[\'s]?\s*degree',
            r'master[\'s]?\s*degree',
            r'phd|doctorate',
            r'computer science|engineering|mathematics|statistics'
        ]
        
        technical_skills = []
        for pattern in technical_patterns:
            matches = re.findall(pattern, job_description.lower())
            technical_skills.extend(matches)
        
        experience_years = []
        for pattern in experience_patterns:
            matches = re.findall(pattern, job_description.lower())
            experience_years.extend([int(year) for year in matches])
        
        education_requirements = []
        for pattern in education_patterns:
            matches = re.findall(pattern, job_description.lower())
            education_requirements.extend(matches)
        
        # Extract entities using spaCy
        entities = []
        for ent in doc.ents:
            if ent.label_ in ['ORG', 'PRODUCT', 'GPE']:  # Organizations, products, locations
                entities.append(ent.text)
        
        return {
            'technical_skills': list(set(technical_skills)),
            'experience_years': max(experience_years) if experience_years else 0,
            'education_requirements': list(set(education_requirements)),
            'entities': entities,
            'all_keywords': self.extract_important_keywords(job_description)
        }
    
    def extract_important_keywords(self, text: str) -> List[str]:
        """Extract important keywords using TF-IDF"""
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        # Get TF-IDF scores
        tfidf_matrix = self.vectorizer.fit_transform([processed_text])
        feature_names = self.vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]
        
        # Get top keywords
        keyword_scores = list(zip(feature_names, scores))
        keyword_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return top 20 keywords
        return [keyword for keyword, score in keyword_scores[:20] if score > 0]
    
    def calculate_similarity_score(self, resume_text: str, job_description: str) -> float:
        """Calculate similarity between resume and job description using TF-IDF and cosine similarity"""
        # Preprocess texts
        resume_processed = self.preprocess_text(resume_text)
        job_processed = self.preprocess_text(job_description)
        
        # Calculate TF-IDF vectors
        tfidf_matrix = self.vectorizer.fit_transform([resume_processed, job_processed])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        return similarity
    
    def analyze_skill_match(self, resume_skills: List[str], job_requirements: Dict) -> Dict[str, List[str]]:
        """Analyze skill matching between resume and job requirements"""
        required_skills = job_requirements['technical_skills'] + job_requirements['all_keywords']
        required_skills_lower = [skill.lower() for skill in required_skills]
        resume_skills_lower = [skill.lower() for skill in resume_skills]
        
        # Find matches
        matched_skills = []
        for skill in resume_skills:
            if skill.lower() in required_skills_lower:
                matched_skills.append(skill)
        
        # Find missing skills
        missing_skills = []
        for skill in required_skills:
            if skill.lower() not in resume_skills_lower:
                missing_skills.append(skill)
        
        # Find additional skills (in resume but not required)
        additional_skills = []
        for skill in resume_skills:
            if skill.lower() not in required_skills_lower:
                additional_skills.append(skill)
        
        return {
            'matched_skills': list(set(matched_skills)),
            'missing_skills': list(set(missing_skills)),
            'additional_skills': list(set(additional_skills))
        }
    
    def calculate_overall_score(self, resume_data: Dict, job_requirements: Dict, 
                              skill_analysis: Dict, similarity_score: float) -> int:
        """Calculate overall compatibility score (0-100)"""
        score_components = []
        
        # Similarity score (40% weight)
        similarity_component = similarity_score * 40
        score_components.append(similarity_component)
        
        # Skill matching (35% weight)
        total_required_skills = len(job_requirements['technical_skills'])
        if total_required_skills > 0:
            skill_match_ratio = len(skill_analysis['matched_skills']) / total_required_skills
            skill_component = skill_match_ratio * 35
        else:
            skill_component = 35  # If no specific skills required
        score_components.append(skill_component)
        
        # Experience matching (15% weight)
        required_experience = job_requirements['experience_years']
        candidate_experience = resume_data['experience_years']
        if required_experience > 0:
            experience_ratio = min(candidate_experience / required_experience, 1.0)
            experience_component = experience_ratio * 15
        else:
            experience_component = 15
        score_components.append(experience_component)
        
        # Education and other factors (10% weight)
        education_component = 10  # Simplified for now
        score_components.append(education_component)
        
        # Calculate final score
        final_score = sum(score_components)
        return min(int(final_score), 100)  # Cap at 100
    
    def generate_score_breakdown(self, resume_data: Dict, job_requirements: Dict, 
                               skill_analysis: Dict, similarity_score: float) -> Dict:
        """Generate detailed score breakdown"""
        breakdown = {
            'overall_score': self.calculate_overall_score(
                resume_data, job_requirements, skill_analysis, similarity_score
            ),
            'similarity_score': round(similarity_score * 100, 1),
            'skill_match_percentage': 0,
            'experience_match': 'Unknown',
            'education_match': 'Not evaluated'
        }
        
        # Calculate skill match percentage
        total_required = len(job_requirements['technical_skills'])
        if total_required > 0:
            matched = len(skill_analysis['matched_skills'])
            breakdown['skill_match_percentage'] = round((matched / total_required) * 100, 1)
        
        # Experience analysis
        required_exp = job_requirements['experience_years']
        candidate_exp = resume_data['experience_years']
        if required_exp > 0:
            if candidate_exp >= required_exp:
                breakdown['experience_match'] = f"Meets requirement ({candidate_exp} years)"
            else:
                shortage = required_exp - candidate_exp
                breakdown['experience_match'] = f"Short by {shortage} years"
        
        return breakdown
    
    def perform_full_analysis(self, resume_data: Dict, job_description: str) -> Dict:
        """Perform complete analysis and return all results"""
        # Extract job requirements
        job_requirements = self.extract_keywords_from_job_description(job_description)
        
        # Calculate similarity
        similarity_score = self.calculate_similarity_score(resume_data['raw_text'], job_description)
        
        # Analyze skills
        skill_analysis = self.analyze_skill_match(resume_data['skills'], job_requirements)
        
        # Generate score breakdown
        score_breakdown = self.generate_score_breakdown(
            resume_data, job_requirements, skill_analysis, similarity_score
        )
        
        return {
            'job_requirements': job_requirements,
            'skill_analysis': skill_analysis,
            'score_breakdown': score_breakdown,
            'similarity_score': similarity_score
        }