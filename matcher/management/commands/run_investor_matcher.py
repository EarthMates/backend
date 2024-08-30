from django.core.management.base import BaseCommand
from api.models import Startup, Investor
from users.models import CustomUser
from matcher.models import Matching
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
        user = CustomUser.objects.get(investor=investor)
        startup_list = Startup.objects.all()
        matches = []

        for startup in startup_list:
            # Check if match exists
            existing_match = Matching.objects.filter(user=user, matched_with=startup.name).first()

            print("Checking match of " + investor.name + " and " + startup.name + "")

            # Check if any of the conditions fail
            if (
                startup.market.target_market != investor.preferences.target_market or 
                startup.details.industry not in investor.preferences.industry or 
                startup.financials.stage not in investor.preferences.funding_stage or 
                not (set(startup.details.target_group) & set(investor.preferences.target_group)) or 
                not (set(startup.preferences.investment_instrument) & set(investor.preferences.investment_instrument)) or 
                not (set(startup.preferences.exit_strategy) & set(investor.preferences.exit_strategy))
            ):
                # Log the specific reason for failure
                if startup.market.target_market != investor.preferences.target_market: 
                    print("Startup market " + startup.market.target_market + " and investor market " + str(investor.preferences.target_market) + " do not match")
                if startup.details.industry not in investor.preferences.industry: 
                    print("Startup industry " + startup.details.industry + " and investor industry " + str(investor.preferences.industry) + " do not match")
                if startup.financials.stage not in investor.preferences.funding_stage: 
                    print("Startup stage " + startup.financials.stage + " and investor stages " + str(investor.preferences.funding_stage) + " do not match")
                if not (set(startup.details.target_group) & set(investor.preferences.target_group)):
                    print("Startup target group " + str(startup.details.target_group) + " and investor target group " + str(investor.preferences.target_group) + " do not match") 
                if not (set(startup.preferences.investment_instrument) & set(investor.preferences.investment_instrument)): 
                    print("Startup instrument " + str(startup.preferences.investment_instrument) + " and investor instrument " + str(investor.preferences.investment_instrument) + " do not match")
                if not (set(startup.preferences.exit_strategy) & set(investor.preferences.exit_strategy)): 
                    print("Startup strategy " + str(startup.preferences.exit_strategy) + " and investor strategy " + str(investor.preferences.exit_strategy) + " do not match")

                # If match exists, delete it
                if existing_match:
                    existing_match.delete()
                    print(f"Deleted existing match between {investor.name} and {startup.name}")
                    # Also delete the reciprocal match (investor user, startup name)
                    startup_user = CustomUser.objects.get(startup=startup)
                    reciprocal_match = Matching.objects.filter(user=startup_user, matched_with=investor.name).first()
                    if reciprocal_match:
                        reciprocal_match.delete()
                        print(f"Deleted reciprocal match between {startup.name} and {investor.name}")
                continue

            
            match_score = 50 # minimum matching score

            # missing sdg filter

            lower_bound, upper_bound = extract_numbers_from_range(investor.preferences.ticket_size)

            if (startup.financials.funding_required < lower_bound) or (startup.financials.funding_required > upper_bound):
                print("Startup funding " + str(startup.financials.funding_required) + " and investor funding " + str(lower_bound) + "-" + str(upper_bound) + " do not match")
            else:
                match_score = match_score + 5

            if (startup.impact.impact_level < investor.preferences.impact_level - 1) or (startup.impact.impact_level > investor.preferences.impact_level + 1):
                print("Startup impact " + str(startup.impact.impact_level) + " and investor impact " + str(investor.preferences.impact_level) + " do not match")
            else:
                match_score = match_score + 10

            common_languages = list(set(startup.team.languages) & set(investor.preferences.languages))

            if len(common_languages) == 0: 
                print("Startup languages " + str(startup.team.languages) + " and investor languages " + str(investor.preferences.languages) + " do not match")
                continue
            if len(common_languages) == 1:
                match_score = match_score + 2
            if len(common_languages) > 1:
                match_score = match_score + 5

            common_qualities = list(set(startup.preferences.investor_qualities) & set(investor.preferences.qualities))

            if len(common_qualities) == 0: 
                print("Startup qualities " + str(startup.preferences.investor_qualities) + " and investor qualities " + str(investor.preferences.qualities) + " do not match")
                continue
            if len(common_qualities) <= 2:
                match_score = match_score + 5
            else:
                match_score = match_score + 10

            common_expertise = list(set(startup.preferences.investor_expertise) & set(investor.preferences.expertise))

            if len(common_expertise) == 0: 
                print("Startup expertise " + str(startup.preferences.investor_expertise) + " and investor expertise " + str(investor.preferences.expertise) + " do not match")
                continue
            if len(common_expertise) <= 2:
                match_score = match_score + 5
            else:
                match_score = match_score + 10

            common_values = list(set(startup.team.values) & set(investor.preferences.team_values))

            if len(common_values) == 0: 
                print("Startup values " + str(startup.team.values) + " and investor values " + str(investor.preferences.team_values) + " do not match")
                continue
            if len(common_values) <= 2:
                match_score = match_score + 5
            else:
                match_score = match_score + 10

            matches.append({"startup": startup, "name": startup.name, "score": match_score})

       # Iterate over found matches 
        for match in matches:
            # Check if a matching object exists
            if Matching.objects.filter(user=user, matched_with=match["name"]).exists():
                # Get the existing match
                existing_match = Matching.objects.get(user=user, matched_with=match["name"])

                # Print information about the existing match
                print(f"Match {existing_match.user.investor.name} and {existing_match.matched_with} exists with score: {existing_match.match_score}")

                # Update the match score
                existing_match.match_score = match["score"]
                existing_match.save(update_fields=["match_score"])
                
            else:
                Matching.objects.create(user=user, matched_with=match["name"], match_score=match["score"])
                # add match from investor side

            
            startup_user = CustomUser.objects.get(startup=match["startup"])
            if Matching.objects.filter(user=startup_user, matched_with=investor.name).exists():
                # Get the existing match
                existing_match = Matching.objects.get(user=startup_user, matched_with=investor.name)

                # Print information about the existing match
                print(f"Match {existing_match.user.startup.name} and {existing_match.matched_with} exists with score: {existing_match.match_score}")

                # Update the match score
                existing_match.match_score = match["score"]
                existing_match.save(update_fields=["match_score"])
            else:
                Matching.objects.create(user=startup_user, matched_with=investor.name, match_score=match["score"])
            