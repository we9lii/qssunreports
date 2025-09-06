from django.test import TestCase
from datetime import datetime
from unittest.mock import patch
from staff.templatetags.time_greetings import get_time_greeting


class TimeGreetingTestCase(TestCase):
    """Test cases for time-based greeting functionality"""
    
    @patch('staff.templatetags.time_greetings.datetime')
    def test_morning_greeting(self, mock_datetime):
        """Test morning greeting (صباح الخير) for hours 4-11"""
        # Mock morning time (8 AM)
        mock_now = datetime(2025, 1, 1, 8, 0)
        mock_datetime.now.return_value = mock_now
        
        greeting = get_time_greeting()
        self.assertEqual(greeting, "صباح الخير")
    
    @patch('staff.templatetags.time_greetings.datetime')
    def test_afternoon_greeting(self, mock_datetime):
        """Test afternoon greeting (مساء الخير) for hours 12-16"""
        # Mock afternoon time (2 PM)
        mock_now = datetime(2025, 1, 1, 14, 0)
        mock_datetime.now.return_value = mock_now
        
        greeting = get_time_greeting()
        self.assertEqual(greeting, "مساء الخير")
    
    @patch('staff.templatetags.time_greetings.datetime')
    def test_evening_greeting(self, mock_datetime):
        """Test evening greeting (مساء الخير) for hours 17-20"""
        # Mock evening time (7 PM)
        mock_now = datetime(2025, 1, 1, 19, 0)
        mock_datetime.now.return_value = mock_now
        
        greeting = get_time_greeting()
        self.assertEqual(greeting, "مساء الخير")
    
    @patch('staff.templatetags.time_greetings.datetime')
    def test_night_greeting(self, mock_datetime):
        """Test night greeting (مرحباً) for hours 21-3"""
        # Mock night time (11 PM)
        mock_now = datetime(2025, 1, 1, 23, 0)
        mock_datetime.now.return_value = mock_now
        
        greeting = get_time_greeting()
        self.assertEqual(greeting, "مرحباً")
