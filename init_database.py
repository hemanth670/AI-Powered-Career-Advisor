#!/usr/bin/env python3
"""
Database initialization script for AI Career Advisor
"""

import sqlite3
import os

def init_database():
    """Initialize SQLite database with sample data"""
    print("🗄️ Initializing database...")
    
    # Remove existing database if it exists
    if os.path.exists('career_advisor.db'):
        os.remove('career_advisor.db')
        print("Removed existing database")
    
    conn = sqlite3.connect('career_advisor.db')
    cursor = conn.cursor()
    
    # Create tables
    print("Creating tables...")
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
    
    # Insert sample skills
    print("Inserting sample skills...")
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
        ('Critical Thinking', 'Soft Skills', 'Logical analysis and evaluation'),
        ('Statistics', 'Technical', 'Statistical methods and data interpretation'),
        ('Cloud Computing', 'Technical', 'Cloud platforms and services'),
        ('Agile', 'Soft Skills', 'Agile development methodologies'),
        ('Time Management', 'Soft Skills', 'Efficient task and time organization'),
        ('Teamwork', 'Soft Skills', 'Collaborative work and team dynamics')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO skills (name, category, description) VALUES (?, ?, ?)', sample_skills)
    
    # Insert sample careers
    print("Inserting sample careers...")
    sample_careers = [
        ('Data Scientist', 'Technology', 'Python Programming,Machine Learning,Data Analysis,Statistics', '$80,000 - $150,000', 15.0, 'Analyze complex data to help organizations make decisions'),
        ('Software Engineer', 'Technology', 'Python Programming,JavaScript,SQL,Problem Solving', '$70,000 - $130,000', 12.0, 'Design and develop software applications'),
        ('Product Manager', 'Technology', 'Project Management,Communication,Leadership,Critical Thinking', '$90,000 - $160,000', 8.0, 'Lead product development and strategy'),
        ('Data Analyst', 'Technology', 'Data Analysis,SQL,Python Programming,Communication', '$60,000 - $100,000', 10.0, 'Interpret data and turn it into information'),
        ('Machine Learning Engineer', 'Technology', 'Machine Learning,Python Programming,Data Analysis,Problem Solving', '$85,000 - $140,000', 20.0, 'Build and deploy ML models in production'),
        ('Business Analyst', 'Business', 'Data Analysis,Communication,Critical Thinking,Problem Solving', '$65,000 - $110,000', 7.0, 'Analyze business processes and recommend improvements'),
        ('Project Manager', 'Business', 'Project Management,Leadership,Communication,Time Management', '$75,000 - $125,000', 6.0, 'Plan and execute projects to achieve business goals'),
        ('Data Engineer', 'Technology', 'Python Programming,SQL,Cloud Computing,Data Analysis', '$80,000 - $135,000', 18.0, 'Build and maintain data infrastructure'),
        ('DevOps Engineer', 'Technology', 'Cloud Computing,Python Programming,Problem Solving,Teamwork', '$85,000 - $145,000', 16.0, 'Manage deployment and infrastructure'),
        ('UX Designer', 'Technology', 'Communication,Critical Thinking,Problem Solving,Teamwork', '$70,000 - $120,000', 14.0, 'Design user experiences for digital products')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO careers (title, industry, required_skills, salary_range, growth_rate, description) VALUES (?, ?, ?, ?, ?, ?)', sample_careers)
    
    conn.commit()
    conn.close()
    
    print("✅ Database initialized successfully!")
    print(f"Inserted {len(sample_skills)} skills and {len(sample_careers)} careers")

if __name__ == "__main__":
    init_database()



