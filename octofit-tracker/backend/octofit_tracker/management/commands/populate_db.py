from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data (replace with actual data from docs/mona-high-school-fitness-tracker.md)
        users = [
            {"email": "alice@example.com", "name": "Alice", "team": "Red", "score": 120},
            {"email": "bob@example.com", "name": "Bob", "team": "Blue", "score": 95},
        ]
        teams = [
            {"name": "Red", "members": ["alice@example.com"]},
            {"name": "Blue", "members": ["bob@example.com"]},
        ]
        activities = [
            {"user": "alice@example.com", "activity": "Running", "duration": 30},
            {"user": "bob@example.com", "activity": "Cycling", "duration": 45},
        ]
        leaderboard = [
            {"team": "Red", "score": 120},
            {"team": "Blue", "score": 95},
        ]
        workouts = [
            {"user": "alice@example.com", "workout": "Pushups", "count": 50},
            {"user": "bob@example.com", "workout": "Situps", "count": 40},
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
