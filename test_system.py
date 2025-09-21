#!/usr/bin/env python3
"""
Test script for the AI Career Advisor system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.skill_mapping import SkillMappingEngine
from modules.job_market_analysis import JobMarketAnalyzer
from modules.career_recommender import CareerRecommender
from modules.learning_planner import LearningPlanGenerator
from modules.resume_prep import ResumePreparation

def test_system():
    """Test all modules of the career advisor system"""
    print("🧠 Testing AI Career Advisor System...")
    
    # Sample student data
    student_data = {
        'skills': ['Python Programming', 'Data Analysis', 'Communication'],
        'interests': ['Technology', 'Business'],
        'education': "Bachelor's Degree",
        'experience': '1-2 years',
        'goals': 'Want to become a data scientist'
    }
    
    try:
        # Test Skill Mapping Engine
        print("\n1. Testing Skill Mapping Engine...")
        skill_mapper = SkillMappingEngine()
        skill_analysis = skill_mapper.analyze_skills(student_data)
        print(f"✅ Skill analysis completed. Strength score: {skill_analysis['skill_strength_score']}%")
        
        # Test Job Market Analysis
        print("\n2. Testing Job Market Analysis...")
        job_analyzer = JobMarketAnalyzer()
        market_analysis = job_analyzer.analyze_market(skill_analysis)
        print(f"✅ Market analysis completed. Found {len(market_analysis['industry_opportunities'])} industry opportunities")
        
        # Test Career Recommender
        print("\n3. Testing Career Recommender...")
        career_recommender = CareerRecommender()
        career_recommendations = career_recommender.get_recommendations(
            skill_analysis, market_analysis, student_data
        )
        print(f"✅ Career recommendations completed. Found {len(career_recommendations['top_careers'])} career options")
        
        # Test Learning Plan Generator
        print("\n4. Testing Learning Plan Generator...")
        learning_planner = LearningPlanGenerator()
        learning_plan = learning_planner.generate_plan(
            skill_analysis, career_recommendations, student_data
        )
        print(f"✅ Learning plan completed. Found {len(learning_plan['course_recommendations'])} course recommendations")
        
        # Test Resume Preparation
        print("\n5. Testing Resume Preparation...")
        resume_prep = ResumePreparation()
        resume_guidance = resume_prep.prepare_guidance(
            student_data, career_recommendations, skill_analysis
        )
        print(f"✅ Resume guidance completed. Generated interview preparation materials")
        
        print("\n🎉 All tests passed! The AI Career Advisor system is working correctly.")
        
        # Display sample results
        print("\n📊 Sample Results:")
        print(f"Top Career: {career_recommendations['top_careers'][0]['title']}")
        print(f"Compatibility: {career_recommendations['top_careers'][0]['compatibility_score']}%")
        print(f"Recommended Skills: {len(skill_analysis['recommended_skills'])} skills")
        print(f"Learning Timeline: {len(learning_plan['learning_timeline'])} phases")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_system()
    sys.exit(0 if success else 1)



