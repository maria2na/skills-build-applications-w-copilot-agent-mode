from datetime import datetime

def get_test_data():
    return {
        "users": [
            {"email": "thundergod@mhigh.edu", "name": "Thor", "created_at": datetime(2025, 4, 9)},
            {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "created_at": datetime(2025, 4, 9)},
            {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "created_at": datetime(2025, 4, 9)},
            {"email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff", "created_at": datetime(2025, 4, 9)},
            {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "created_at": datetime(2025, 4, 9)},
        ],
        "teams": [
            {"name": "Avengers", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu", "zerocool@mhigh.edu", "crashoverride@mhigh.edu", "sleeptoken@mhigh.edu"]},
        ],
        "activities": [
            {"user": "thundergod@mhigh.edu", "activity_type": "Cycling", "duration": 60, "date": "2025-04-09"},
            {"user": "metalgeek@mhigh.edu", "activity_type": "Crossfit", "duration": 120, "date": "2025-04-08"},
            {"user": "zerocool@mhigh.edu", "activity_type": "Running", "duration": 90, "date": "2025-04-07"},
            {"user": "crashoverride@mhigh.edu", "activity_type": "Strength", "duration": 30, "date": "2025-04-06"},
            {"user": "sleeptoken@mhigh.edu", "activity_type": "Swimming", "duration": 75, "date": "2025-04-05"},
        ],
        "leaderboard": [
            {"user": "thundergod@mhigh.edu", "score": 100},
            {"user": "metalgeek@mhigh.edu", "score": 90},
            {"user": "zerocool@mhigh.edu", "score": 95},
            {"user": "crashoverride@mhigh.edu", "score": 85},
            {"user": "sleeptoken@mhigh.edu", "score": 80},
        ],
        "workouts": [
            {"name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
            {"name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
            {"name": "Running Training", "description": "Training for a marathon", "duration": 90},
            {"name": "Strength Training", "description": "Training for strength", "duration": 30},
            {"name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
        ],
    }
