from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from modules.skill_mapping import SkillMappingEngine
from modules.job_market_analysis import JobMarketAnalyzer
from modules.career_recommender import CareerRecommender
from modules.learning_planner import LearningPlanGenerator
from modules.resume_prep import ResumePreparation
from modules.ai_skill_assessment import AISkillAssessment
from modules.ai_interview_prep import AIInterviewPreparation
import sqlite3

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize AI modules
skill_mapper = SkillMappingEngine()
job_analyzer = JobMarketAnalyzer()
career_recommender = CareerRecommender()
learning_planner = LearningPlanGenerator()
resume_prep = ResumePreparation()
ai_assessment = AISkillAssessment()
ai_interview = AIInterviewPreparation()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_student():
    try:
        data = request.json
        student_data = {
            'skills': data.get('skills', []),
            'interests': data.get('interests', []),
            'education': data.get('education', ''),
            'experience': data.get('experience', ''),
            'goals': data.get('goals', '')
        }
        
        # Step 1: Skill Mapping
        skill_analysis = skill_mapper.analyze_skills(student_data)
        
        # Step 2: Job Market Analysis
        market_analysis = job_analyzer.analyze_market(skill_analysis)
        
        # Step 3: Career Recommendations
        career_recommendations = career_recommender.get_recommendations(
            skill_analysis, market_analysis, student_data
        )
        
        # Step 4: Learning Plan
        learning_plan = learning_planner.generate_plan(
            skill_analysis, career_recommendations, student_data
        )
        
        # Step 5: Resume & Interview Prep
        resume_guidance = resume_prep.prepare_guidance(
            student_data, career_recommendations, skill_analysis
        )
        
        return jsonify({
            'success': True,
            'skill_analysis': skill_analysis,
            'market_analysis': market_analysis,
            'career_recommendations': career_recommendations,
            'learning_plan': learning_plan,
            'resume_guidance': resume_guidance
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/skills', methods=['GET'])
def get_skills():
    """Get available skills from the database"""
    return jsonify(skill_mapper.get_available_skills())

@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Get available industries for interest selection"""
    return jsonify(job_analyzer.get_available_industries())

def init_database():
    """Initialize SQLite database with sample data"""
    conn = sqlite3.connect('career_advisor.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            category TEXT,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS careers (
            id INTEGER PRIMARY KEY,
            title TEXT,
            industry TEXT,
            required_skills TEXT,
            salary_range TEXT,
            growth_rate REAL,
            description TEXT
        )
    ''')
    
    # Insert sample data
    sample_skills = [
        ('Python Programming', 'Technical', 'Programming language for data science and web development'),
        ('Machine Learning', 'Technical', 'AI/ML algorithms and model development'),
        ('Data Analysis', 'Technical', 'Statistical analysis and data visualization'),
        ('Project Management', 'Soft Skills', 'Leading teams and managing projects'),
        ('Communication', 'Soft Skills', 'Verbal and written communication skills'),
        ('Problem Solving', 'Soft Skills', 'Analytical thinking and creative solutions'),
        ('JavaScript', 'Technical', 'Web development and frontend programming'),
        ('SQL', 'Technical', 'Database management and querying'),
        ('Leadership', 'Soft Skills', 'Team leadership and management'),
        ('Critical Thinking', 'Soft Skills', 'Logical analysis and evaluation')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO skills (name, category, description) VALUES (?, ?, ?)', sample_skills)
    
    sample_careers = [
        ('Data Scientist', 'Technology', 'Python Programming,Machine Learning,Data Analysis,Statistics', '₹8,00,000 - ₹15,00,000', 15.0, 'Analyze complex data to help organizations make decisions'),
        ('Software Engineer', 'Technology', 'Python Programming,JavaScript,SQL,Problem Solving', '₹7,00,000 - ₹13,00,000', 12.0, 'Design and develop software applications'),
        ('Product Manager', 'Technology', 'Project Management,Communication,Leadership,Critical Thinking', '₹9,00,000 - ₹16,00,000', 8.0, 'Lead product development and strategy'),
        ('Data Analyst', 'Technology', 'Data Analysis,SQL,Python Programming,Communication', '₹6,00,000 - ₹10,00,000', 10.0, 'Interpret data and turn it into information'),
        ('Machine Learning Engineer', 'Technology', 'Machine Learning,Python Programming,Data Analysis,Problem Solving', '₹8,50,000 - ₹14,00,000', 20.0, 'Build and deploy ML models in production')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO careers (title, industry, required_skills, salary_range, growth_rate, description) VALUES (?, ?, ?, ?, ?, ?)', sample_careers)
    
    conn.commit()
    conn.close()

# AI Skill Assessment Routes
@app.route('/api/assessment/start', methods=['POST'])
def start_assessment():
    try:
        data = request.json
        user_id = data.get('user_id')
        result = ai_assessment.start_assessment(user_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/assessment/submit', methods=['POST'])
def submit_assessment():
    try:
        data = request.json
        user_id = data.get('user_id')
        answer = data.get('answer')
        result = ai_assessment.submit_answer(user_id, answer)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/assessment/history/<user_id>', methods=['GET'])
def get_assessment_history(user_id):
    try:
        history = ai_assessment.get_assessment_history(user_id)
        return jsonify(history)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/assessment/insights/<user_id>', methods=['GET'])
def get_assessment_insights(user_id):
    try:
        insights = ai_assessment.get_skill_insights(user_id)
        return jsonify(insights)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# AI Interview Preparation Routes
@app.route('/api/interview/start', methods=['POST'])
def start_interview():
    try:
        data = request.json
        user_id = data.get('user_id')
        interview_type = data.get('interview_type', 'technical')
        difficulty = data.get('difficulty', 'intermediate')
        result = ai_interview.start_mock_interview(user_id, interview_type, difficulty)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/interview/submit', methods=['POST'])
def submit_interview():
    try:
        data = request.json
        user_id = data.get('user_id')
        answer = data.get('answer')
        result = ai_interview.submit_answer(user_id, answer)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/interview/history/<user_id>', methods=['GET'])
def get_interview_history(user_id):
    try:
        history = ai_interview.get_interview_history(user_id)
        return jsonify(history)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/interview/insights/<user_id>', methods=['GET'])
def get_interview_insights(user_id):
    try:
        insights = ai_interview.get_interview_insights(user_id)
        return jsonify(insights)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Resume Generation Route
@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    try:
        data = request.json
        resume_data = {
            'personal_info': data.get('personal_info', {}),
            'experience': data.get('experience', []),
            'education': data.get('education', []),
            'skills': data.get('skills', {}),
            'use_ai': data.get('use_ai', False)
        }
        
        # Generate resume content
        resume_content = resume_prep.generate_resume_content(resume_data)
        
        # Generate PDF
        pdf_filename = resume_prep.generate_pdf_resume(resume_content, resume_data['personal_info'].get('full_name', 'Resume'))
        
        # Extract just the filename from the full path
        filename_only = os.path.basename(pdf_filename)
        
        return jsonify({
            'success': True,
            'resume_content': resume_content,
            'download_url': f'/downloads/{filename_only}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/downloads/<filename>')
def download_file(filename):
    try:
        from flask import send_file
        import os
        file_path = os.path.join('downloads', filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize database
    init_database()
    app.run(debug=True, host='0.0.0.0', port=5000)
