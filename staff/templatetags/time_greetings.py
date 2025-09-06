from django import template
from datetime import datetime
import pytz

register = template.Library()

@register.simple_tag
def get_time_greeting():
    """
    Returns appropriate Arabic greeting based on current time in Riyadh timezone
    """
    # Get current time in Riyadh timezone (as specified in settings.py)
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    current_time = datetime.now(riyadh_tz)
    hour = current_time.hour
    
    # Define time-based greetings in Arabic
    if 4 <= hour < 12:
        return "صباح الخير"  # Good morning (4 AM - 12 PM)
    elif 12 <= hour < 17:
        return "مساء الخير"  # Good afternoon (12 PM - 5 PM)
    elif 17 <= hour < 21:
        return "مساء الخير"  # Good evening (5 PM - 9 PM)
    else:
        return "مرحباً"      # General greeting (9 PM - 4 AM)