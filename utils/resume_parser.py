import PyPDF2
import docx
import pdfplumber
import spacy
import re
from typing import Dict, List, Optional

class ResumeParser:
    def __init__(self):
        # Load spaCy model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            raise Exception("Please install spaCy English model: python -m spacy download en_core_web_sm")
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text from PDF file using pdfplumber"""
        text = ""
        try:
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            # Fallback to PyPDF2
            try:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            except Exception as e2:
                raise Exception(f"Failed to extract PDF text: {e2}")
        return text
    
    def extract_text_from_docx(self, docx_file) -> str:
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(docx_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            raise Exception(f"Failed to extract DOCX text: {e}")
    
    def extract_contact_info(self, text: str) -> Dict[str, Optional[str]]:
        """Extract contact information from resume text"""
        contact_info = {
            'email': None,
            'phone': None,
            'name': None
        }
        
        # Email extraction
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, text)
        if email_match:
            contact_info['email'] = email_match.group()
        
        # Phone extraction
        phone_pattern = r'(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        phone_match = re.search(phone_pattern, text)
        if phone_match:
            contact_info['phone'] = phone_match.group()
        
        # Name extraction (first few words, usually name)
        lines = text.split('\n')
        for line in lines[:5]:  # Check first 5 lines
            line = line.strip()
            if line and len(line.split()) <= 4 and len(line) > 3:
                # Simple heuristic: if it's short and at the top, likely a name
                if not any(char.isdigit() or char in '@.com' for char in line):
                    contact_info['name'] = line
                    break
        
        return contact_info
    
    def extract_skills(self, text: str, skills_database: List[str]) -> List[str]:
        """Extract skills from resume text using predefined skills database"""
        found_skills = []
        text_lower = text.lower()
        
        for skill in skills_database:
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(skill)
        
        return list(set(found_skills))  # Remove duplicates
    
    def extract_experience_years(self, text: str) -> int:
        """Extract years of experience from resume text"""
        # Look for patterns like "3 years", "5+ years", etc.
        experience_patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'experience\s*[:\-]?\s*(\d+)\+?\s*years?',
            r'(\d+)\+?\s*years?\s*in',
        ]
        
        years = []
        for pattern in experience_patterns:
            matches = re.findall(pattern, text.lower())
            years.extend([int(match) for match in matches])
        
        return max(years) if years else 0
    
    def extract_education(self, text: str) -> List[str]:
        """Extract education information from resume text"""
        education_keywords = [
            'bachelor', 'master', 'phd', 'doctorate', 'mba', 'b.s.', 'm.s.', 
            'b.a.', 'm.a.', 'b.tech', 'm.tech', 'diploma', 'certificate'
        ]
        
        education = []
        lines = text.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in education_keywords):
                education.append(line.strip())
        
        return education
    
    def parse_resume(self, file_content, file_type: str, skills_database: List[str]) -> Dict:
        """Main parsing function that orchestrates all extraction methods"""
        # Extract text based on file type
        if file_type == 'pdf':
            text = self.extract_text_from_pdf(file_content)
        elif file_type == 'docx':
            text = self.extract_text_from_docx(file_content)
        else:
            text = file_content  # Assume it's already text
        
        # Extract all information
        contact_info = self.extract_contact_info(text)
        skills = self.extract_skills(text, skills_database)
        experience_years = self.extract_experience_years(text)
        education = self.extract_education(text)
        
        return {
            'raw_text': text,
            'contact_info': contact_info,
            'skills': skills,
            'experience_years': experience_years,
            'education': education,
            'word_count': len(text.split())
        }