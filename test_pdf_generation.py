#!/usr/bin/env python3
"""
Test script for PDF Resume Generation
"""

from modules.resume_prep import ResumePreparation
import os

def test_pdf_generation():
    print('📄 Testing PDF Resume Generation...')
    
    # Create sample resume data
    resume_data = {
        'personal_info': {
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '+91 98765 43210',
            'linkedin': 'linkedin.com/in/johndoe',
            'github': 'github.com/johndoe',
            'location': 'Mumbai, India'
        },
        'summary': 'Experienced software engineer with 5+ years in Python development and machine learning. Passionate about building scalable applications and solving complex problems.',
        'experience': [
            {
                'job_title': 'Senior Software Engineer',
                'company': 'Tech Corp',
                'location': 'Mumbai, India',
                'start_date': '2020-01',
                'end_date': '2023-12',
                'current': False,
                'achievements': 'Led development of ML pipeline\nImproved system performance by 40%\nMentored 3 junior developers'
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Technology',
                'major': 'Computer Science',
                'university': 'IIT Mumbai',
                'graduation_year': '2019',
                'gpa': '8.5/10',
                'achievements': 'Dean\'s List\nFinal Year Project Award'
            }
        ],
        'skills': {
            'technical_skills': ['Python', 'Machine Learning', 'Django', 'PostgreSQL'],
            'soft_skills': ['Leadership', 'Communication', 'Problem Solving'],
            'tools': ['Git', 'Docker', 'AWS', 'Jenkins']
        },
        'projects': [
            {
                'project_name': 'E-commerce ML Recommendation System',
                'description': 'Built a recommendation engine using collaborative filtering',
                'technologies': ['Python', 'Scikit-learn', 'Django', 'PostgreSQL'],
                'github_url': 'github.com/johndoe/recommendation-system',
                'live_url': 'recommendations.example.com',
                'achievements': 'Increased user engagement by 25%\nReduced bounce rate by 15%'
            }
        ],
        'template': 'modern'
    }
    
    # Test PDF generation
    resume_prep = ResumePreparation()
    try:
        pdf_path = resume_prep.generate_pdf_resume(resume_data, 'test_resume.pdf')
        print(f'✅ PDF generated successfully: {pdf_path}')
        
        # Check if file exists
        if os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            print(f'✅ File exists and is {file_size} bytes')
        else:
            print('❌ PDF file was not created')
            
    except Exception as e:
        print(f'❌ Error generating PDF: {e}')
        import traceback
        traceback.print_exc()
    
    print('🎯 PDF generation test completed!')

if __name__ == "__main__":
    test_pdf_generation()
