#!/usr/bin/env python3
"""
Comprehensive test for the complete Career Advisor system
"""

import requests
import json
import time

def test_web_interface():
    print("🌐 Testing Web Interface...")
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code == 200:
            print("✅ Web interface is accessible")
            return True
        else:
            print(f"❌ Web interface returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Web interface not accessible: {e}")
        return False

def test_skill_assessment():
    print("🧠 Testing AI Skill Assessment...")
    try:
        # Start assessment
        response = requests.post("http://localhost:5000/api/assessment/start", 
                               json={}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'session_id' in data:
                session_id = data['session_id']
                print(f"✅ Assessment started: {session_id}")
                
                # Submit a few answers
                for i in range(3):
                    answer_response = requests.post("http://localhost:5000/api/assessment/submit",
                                                  json={'user_id': session_id, 'answer': i}, timeout=10)
                    if answer_response.status_code == 200:
                        print(f"✅ Answer {i+1} submitted")
                    else:
                        print(f"❌ Failed to submit answer {i+1}")
                
                return True
            else:
                print(f"❌ Assessment start failed: {data.get('error')}")
                return False
        else:
            print(f"❌ Assessment API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Skill assessment test failed: {e}")
        return False

def test_interview_prep():
    print("🎤 Testing AI Interview Preparation...")
    try:
        # Start interview
        response = requests.post("http://localhost:5000/api/interview/start", 
                               json={
                                   'interview_type': 'mixed',
                                   'difficulty': 'intermediate',
                                   'user_id': 'test_user_interview'
                               }, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'session_id' in data:
                session_id = data['session_id']
                print(f"✅ Interview started: {session_id}")
                
                # Submit a sample answer
                answer_response = requests.post("http://localhost:5000/api/interview/submit",
                                              json={
                                                  'user_id': session_id, 
                                                  'answer': 'I have experience with Python programming and data analysis. I have worked on several projects involving machine learning and statistical analysis.'
                                              }, timeout=10)
                if answer_response.status_code == 200:
                    print("✅ Interview answer submitted")
                    return True
                else:
                    print(f"❌ Failed to submit interview answer: {answer_response.status_code}")
                    return False
            else:
                print(f"❌ Interview start failed: {data.get('error')}")
                return False
        else:
            print(f"❌ Interview API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Interview preparation test failed: {e}")
        return False

def test_career_analysis():
    print("🎯 Testing Career Analysis...")
    try:
        sample_data = {
            'skills': ['Python Programming', 'Machine Learning', 'Data Analysis'],
            'interests': ['Technology', 'Data Science'],
            'experience_level': 'Intermediate',
            'education': 'Bachelor\'s Degree'
        }
        
        response = requests.post("http://localhost:5000/api/analyze", 
                               json=sample_data, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Career analysis completed successfully")
                print(f"   - Found {len(data.get('career_recommendations', {}))} career recommendations")
                print(f"   - Generated learning plan with {len(data.get('learning_plan', {}).get('course_recommendations', []))} courses")
                return True
            else:
                print(f"❌ Career analysis failed: {data.get('error')}")
                return False
        else:
            print(f"❌ Career analysis API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Career analysis test failed: {e}")
        return False

def test_resume_generation():
    print("📄 Testing Resume Generation...")
    try:
        sample_resume_data = {
            'personal_info': {
                'full_name': 'Test User',
                'email': 'test@example.com',
                'phone': '+91 98765 43210'
            },
            'summary': 'Test summary for resume generation',
            'experience': [],
            'education': [],
            'skills': {},
            'projects': [],
            'template': 'modern'
        }
        
        response = requests.post("http://localhost:5000/api/generate-resume", 
                               json=sample_resume_data, timeout=20)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Resume generation completed successfully")
                print(f"   - Download URL: {data.get('download_url', 'N/A')}")
                return True
            else:
                print(f"❌ Resume generation failed: {data.get('error')}")
                return False
        else:
            print(f"❌ Resume generation API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Resume generation test failed: {e}")
        return False

def main():
    print("🚀 Starting Comprehensive System Test...\n")
    
    # Wait for server to be ready
    print("⏳ Waiting for server to be ready...")
    time.sleep(3)
    
    tests = [
        ("Web Interface", test_web_interface),
        ("Career Analysis", test_career_analysis),
        ("AI Skill Assessment", test_skill_assessment),
        ("AI Interview Preparation", test_interview_prep),
        ("Resume Generation", test_resume_generation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        result = test_func()
        results.append((test_name, result))
        print(f"{'='*50}")
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 TEST SUMMARY")
    print(f"{'='*50}")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is fully functional.")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
    
    return passed == total

if __name__ == "__main__":
    main()
