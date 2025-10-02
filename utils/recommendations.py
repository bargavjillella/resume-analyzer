from typing import Dict, List
import random

class RecommendationEngine:
    def __init__(self):
        self.ats_tips = [
            "Use standard section headers like 'EXPERIENCE', 'EDUCATION', 'SKILLS'",
            "Save your resume as a PDF to preserve formatting",
            "Avoid using tables, graphics, or complex formatting",
            "Include keywords from the job description naturally in your content",
            "Use a clean, professional font like Arial or Calibri",
            "Keep your resume to 1-2 pages maximum",
            "Include your contact information at the top",
            "Use bullet points to highlight achievements and responsibilities"
        ]
        
        self.content_improvements = {
            'low_score': [
                "Add more specific technical skills relevant to the role",
                "Include quantified achievements and results in your experience",
                "Expand your work experience descriptions with relevant details",
                "Add relevant certifications or training programs",
                "Include keywords from the job description naturally"
            ],
            'medium_score': [
                "Fine-tune your skill descriptions to better match job requirements",
                "Add more specific examples of your technical expertise",
                "Include relevant projects that demonstrate your capabilities",
                "Optimize your summary or objective statement"
            ],
            'high_score': [
                "Your resume is well-aligned! Consider minor keyword optimization",
                "Add any recently acquired skills or certifications",
                "Ensure your contact information is up to date"
            ]
        }
    
    def generate_skill_recommendations(self, skill_analysis: Dict, job_requirements: Dict) -> List[str]:
        """Generate specific skill-based recommendations"""
        recommendations = []
        
        # Missing critical skills
        missing_skills = skill_analysis['missing_skills']
        if missing_skills:
            critical_skills = missing_skills[:5]  # Top 5 missing skills
            for skill in critical_skills:
                recommendations.append(f"Add '{skill}' to your skills section and experience descriptions")
        
        # Skill enhancement suggestions
        matched_skills = skill_analysis['matched_skills']
        if len(matched_skills) < len(job_requirements['technical_skills']) * 0.7:
            recommendations.append("Consider taking online courses to acquire missing technical skills")
            recommendations.append("Highlight transferable skills that relate to the missing requirements")
        
        return recommendations
    
    def generate_experience_recommendations(self, resume_data: Dict, job_requirements: Dict) -> List[str]:
        """Generate experience-related recommendations"""
        recommendations = []
        
        required_experience = job_requirements['experience_years']
        candidate_experience = resume_data['experience_years']
        
        if required_experience > candidate_experience:
            gap = required_experience - candidate_experience
            recommendations.extend([
                f"Consider highlighting {gap} years of relevant project or internship experience",
                "Emphasize freelance work, volunteer projects, or personal projects",
                "Include relevant coursework or academic projects that demonstrate skills",
                "Consider pursuing additional certifications to strengthen your profile"
            ])
        
        # Work experience enhancement
        if resume_data['word_count'] < 300:
            recommendations.append("Expand your work experience descriptions with specific achievements")
            recommendations.append("Add quantified results and metrics to your accomplishments")
        
        return recommendations
    
    def generate_keyword_optimization_tips(self, skill_analysis: Dict, job_requirements: Dict) -> List[str]:
        """Generate keyword optimization recommendations"""
        tips = []
        
        missing_keywords = skill_analysis['missing_skills'][:10]  # Top 10 missing
        
        for keyword in missing_keywords:
            tips.append(f"Include '{keyword}' naturally in your experience or skills section")
        
        if len(missing_keywords) > 5:
            tips.extend([
                "Review the job description and identify industry-specific terms to include",
                "Use variations of important keywords throughout your resume",
                "Include acronyms and full forms of technical terms (e.g., 'AI' and 'Artificial Intelligence')"
            ])
        
        return tips
    
    def generate_formatting_recommendations(self, resume_data: Dict) -> List[str]:
        """Generate formatting and structure recommendations"""
        recommendations = []
        
        # Basic formatting tips
        recommendations.extend(random.sample(self.ats_tips, 3))
        
        # Content-specific recommendations
        if resume_data['word_count'] < 200:
            recommendations.append("Consider adding more detailed descriptions of your experience")
        elif resume_data['word_count'] > 800:
            recommendations.append("Consider condensing your resume content for better readability")
        
        if not resume_data['contact_info']['email']:
            recommendations.append("Ensure your email address is clearly visible at the top")
        
        if not resume_data['contact_info']['phone']:
            recommendations.append("Include your phone number in the contact section")
        
        return recommendations
    
    def get_improvement_priority(self, score_breakdown: Dict) -> str:
        """Determine the priority level for improvements"""
        overall_score = score_breakdown['overall_score']
        
        if overall_score >= 80:
            return 'high_score'
        elif overall_score >= 60:
            return 'medium_score'
        else:
            return 'low_score'
    
    def generate_comprehensive_recommendations(self, resume_data: Dict, job_requirements: Dict, 
                                            skill_analysis: Dict, score_breakdown: Dict) -> Dict[str, List[str]]:
        """Generate comprehensive recommendations based on analysis"""
        priority = self.get_improvement_priority(score_breakdown)
        
        recommendations = {
            'skill_recommendations': self.generate_skill_recommendations(skill_analysis, job_requirements),
            'experience_recommendations': self.generate_experience_recommendations(resume_data, job_requirements),
            'keyword_optimization': self.generate_keyword_optimization_tips(skill_analysis, job_requirements),
            'formatting_tips': self.generate_formatting_recommendations(resume_data),
            'content_improvements': self.content_improvements[priority],
            'ats_optimization': random.sample(self.ats_tips, 4)
        }
        
        return recommendations
    
    def generate_action_plan(self, recommendations: Dict[str, List[str]], score_breakdown: Dict) -> List[Dict[str, str]]:
        """Generate a prioritized action plan"""
        action_items = []
        
        overall_score = score_breakdown['overall_score']
        
        # High priority items for low scores
        if overall_score < 60:
            action_items.extend([
                {
                    'priority': 'High',
                    'action': recommendations['skill_recommendations'][0] if recommendations['skill_recommendations'] else 'Add relevant technical skills',
                    'category': 'Skills'
                },
                {
                    'priority': 'High', 
                    'action': recommendations['experience_recommendations'][0] if recommendations['experience_recommendations'] else 'Expand work experience descriptions',
                    'category': 'Experience'
                }
            ])
        
        # Medium priority items
        if recommendations['keyword_optimization']:
            action_items.append({
                'priority': 'Medium',
                'action': recommendations['keyword_optimization'][0],
                'category': 'Keywords'
            })
        
        # Low priority formatting items
        if recommendations['formatting_tips']:
            action_items.append({
                'priority': 'Low',
                'action': recommendations['formatting_tips'][0],
                'category': 'Formatting'
            })
        
        return action_items[:6]