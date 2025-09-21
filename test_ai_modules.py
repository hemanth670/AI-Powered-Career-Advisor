#!/usr/bin/env python3
"""
Test script for AI modules
"""

from modules.ai_skill_assessment import AISkillAssessment
from modules.ai_interview_prep import AIInterviewPreparation

def test_ai_skill_assessment():
    print("🧠 Testing AI Skill Assessment...")
    
    assessment = AISkillAssessment()
    
    # Test starting assessment
    result = assessment.start_assessment("test_user_123")
    print(f"✅ Assessment started: {result.get('session_id', 'N/A')}")
    print(f"   Current phase: {result.get('current_phase', 'N/A')}")
    print(f"   Total questions: {result.get('total_questions', 'N/A')}")
    
    # Test submitting answers
    session_id = result['session_id']
    
    # Submit a few answers
    for i in range(3):
        answer_result = assessment.submit_answer(session_id, i)  # Answer with index i
        if 'error' in answer_result:
            print(f"❌ Error submitting answer {i}: {answer_result['error']}")
            break
        print(f"✅ Answer {i+1} submitted successfully")
    
    print("🎯 AI Skill Assessment test completed!\n")

def test_ai_interview_prep():
    print("🎤 Testing AI Interview Preparation...")
    
    interview = AIInterviewPreparation()
    
    # Test starting interview
    result = interview.start_mock_interview("test_user_123", "mixed", "intermediate")
    print(f"✅ Interview started: {result.get('session_id', 'N/A')}")
    print(f"   Interview type: {result.get('interview_type', 'N/A')}")
    print(f"   Total questions: {result.get('total_questions', 'N/A')}")
    
    # Test submitting answers
    session_id = result['session_id']
    
    # Submit a few answers
    sample_answers = [
        "I have experience with Python programming and data analysis. I've worked on several projects involving machine learning and statistical analysis.",
        "In my previous role, I had to work with a difficult team member who had different communication styles. I focused on understanding their perspective and found common ground to work effectively together.",
        "I would design a scalable system using microservices architecture, implement proper caching with Redis, and use load balancers to handle traffic distribution."
    ]
    
    for i, answer in enumerate(sample_answers):
        answer_result = interview.submit_answer(session_id, answer)
        if 'error' in answer_result:
            print(f"❌ Error submitting answer {i}: {answer_result['error']}")
            break
        print(f"✅ Answer {i+1} submitted successfully")
        if answer_result.get('status') == 'completed':
            print(f"🎉 Interview completed! Overall score: {answer_result.get('overall_score', 'N/A')}")
            break
    
    print("🎯 AI Interview Preparation test completed!\n")

def test_api_endpoints():
    print("🌐 Testing API endpoints...")
    
    import requests
    import json
    
    base_url = "http://localhost:5000"
    
    # Test assessment start
    try:
        response = requests.post(f"{base_url}/api/assessment/start", 
                               json={}, 
                               timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Assessment API working: {data.get('success', False)}")
        else:
            print(f"❌ Assessment API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Assessment API connection error: {e}")
    
    # Test interview start
    try:
        response = requests.post(f"{base_url}/api/interview/start", 
                               json={
                                   "interview_type": "mixed",
                                   "difficulty": "intermediate",
                                   "user_id": "test_user_api"
                               }, 
                               timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Interview API working: {data.get('success', False)}")
        else:
            print(f"❌ Interview API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Interview API connection error: {e}")
    
    print("🎯 API endpoints test completed!\n")

if __name__ == "__main__":
    print("🚀 Starting AI Modules Test Suite...\n")
    
    test_ai_skill_assessment()
    test_ai_interview_prep()
    test_api_endpoints()
    
    print("✅ All tests completed!")
