from django.core.management.base import BaseCommand
from api.models import Startup, Investor
from users.models import CustomUser
from matcher.models import Matching
from matcher.utils import run_investor_matcher
import re

def extract_numbers_from_range(s):
    # Use regular expression to find all numbers in the string
    numbers = re.findall(r'\$([\d,]+)', s)
    
    # Convert the extracted strings to integers
    num1 = int(numbers[0].replace(',', ''))
    num2 = int(numbers[1].replace(',', ''))
    
    return num1, num2

class Command(BaseCommand):
    help = 'Running matching algorithm'

    def add_arguments(self, parser):
        # Optional: Add command-line arguments here
        parser.add_argument('investor-name', type=str, help='The investor name')

    def handle(self, *args, **kwargs):
        investor = Investor.objects.get(name=kwargs['investor-name'])
        
        run_investor_matcher(investor_name=investor)