from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Startup, Investor
from users.models import CustomUser
from matcher.models import Matching

def update_matching_for_startup(startup):
    user = CustomUser.objects.get(startup=startup)
    investor_list = Investor.objects.all()
    matches = []

    for investor in investor_list:
        # Check if match exists
        existing_match = Matching.objects.filter(user=user, matched_with=investor.name).first()

        # Check if any of the conditions fail
        if (
            startup.market.target_market != investor.preferences.target_market or 
            startup.details.industry not in investor.preferences.industry or 
            startup.financials.stage not in investor.preferences.funding_stage or 
            not (set(startup.details.target_group) & set(investor.preferences.target_group)) or 
            not (set(startup.preferences.investment_instrument) & set(investor.preferences.investment_instrument)) or 
            not (set(startup.preferences.exit_strategy) & set(investor.preferences.exit_strategy))
        ):
            # If match exists, delete it
            if existing_match:
                existing_match.delete()
                # Also delete the reciprocal match (investor user, startup name)
                investor_user = CustomUser.objects.get(investor=investor)
                reciprocal_match = Matching.objects.filter(user=investor_user, matched_with=startup.name).first()
                if reciprocal_match:
                    reciprocal_match.delete()
            continue

        match_score = 50  # minimum matching score

        # Missing SDG filter

        lower_bound, upper_bound = extract_numbers_from_range(investor.preferences.ticket_size)

        if (startup.financials.funding_required < lower_bound) or (startup.financials.funding_required > upper_bound):
            continue
        else:
            match_score += 5

        if (startup.impact.impact_level < investor.preferences.impact_level - 1) or (startup.impact.impact_level > investor.preferences.impact_level + 1):
            continue
        else:
            match_score += 10

        common_languages = list(set(startup.team.languages) & set(investor.preferences.languages))

        if len(common_languages) == 0: 
            continue
        if len(common_languages) == 1:
            match_score += 2
        if len(common_languages) > 1:
            match_score += 5

        common_qualities = list(set(startup.preferences.investor_qualities) & set(investor.preferences.qualities))

        if len(common_qualities) == 0: 
            continue
        if len(common_qualities) <= 2:
            match_score += 5
        else:
            match_score += 10

        common_expertise = list(set(startup.preferences.investor_expertise) & set(investor.preferences.expertise))

        if len(common_expertise) == 0: 
            continue
        if len(common_expertise) <= 2:
            match_score += 5
        else:
            match_score += 10

        common_values = list(set(startup.team.values) & set(investor.preferences.team_values))

        if len(common_values) == 0: 
            continue
        if len(common_values) <= 2:
            match_score += 5
        else:
            match_score += 10

        matches.append({"investor": investor, "name": investor.name, "score": match_score})

    # Iterate over found matches 
    for match in matches:
        # Check if a matching object exists
        if Matching.objects.filter(user=user, matched_with=match["name"]).exists():
            existing_match = Matching.objects.get(user=user, matched_with=match["name"])
            existing_match.match_score = match["score"]
            existing_match.save(update_fields=["match_score"])
        else:
            Matching.objects.create(user=user, matched_with=match["name"], match_score=match["score"])
            # Add match from investor side
            investor_user = CustomUser.objects.get(investor=match["investor"])
            if Matching.objects.filter(user=investor_user, matched_with=startup.name).exists():
                existing_match = Matching.objects.get(user=investor_user, matched_with=startup.name)
                existing_match.match_score = match["score"]
                existing_match.save(update_fields=["match_score"])
            else:
                Matching.objects.create(user=investor_user, matched_with=startup.name, match_score=match["score"])

def update_matching_for_investor(investor):
    user = CustomUser.objects.get(investor=investor)
    startup_list = Startup.objects.all()
    matches = []

    for startup in startup_list:
        # Check if match exists
        existing_match = Matching.objects.filter(user=user, matched_with=startup.name).first()

        # Check if any of the conditions fail
        if (
            startup.market.target_market != investor.preferences.target_market or 
            startup.details.industry not in investor.preferences.industry or 
            startup.financials.stage not in investor.preferences.funding_stage or 
            not (set(startup.details.target_group) & set(investor.preferences.target_group)) or 
            not (set(startup.preferences.investment_instrument) & set(investor.preferences.investment_instrument)) or 
            not (set(startup.preferences.exit_strategy) & set(investor.preferences.exit_strategy))
        ):
            # If match exists, delete it
            if existing_match:
                existing_match.delete()
                # Also delete the reciprocal match (startup user, investor name)
                startup_user = CustomUser.objects.get(startup=startup)
                reciprocal_match = Matching.objects.filter(user=startup_user, matched_with=investor.name).first()
                if reciprocal_match:
                    reciprocal_match.delete()
            continue

        match_score = 50  # minimum matching score

        # Missing SDG filter

        lower_bound, upper_bound = extract_numbers_from_range(investor.preferences.ticket_size)

        if (startup.financials.funding_required < lower_bound) or (startup.financials.funding_required > upper_bound):
            continue
        else:
            match_score += 5

        if (startup.impact.impact_level < investor.preferences.impact_level - 1) or (startup.impact.impact_level > investor.preferences.impact_level + 1):
            continue
        else:
            match_score += 10

        common_languages = list(set(startup.team.languages) & set(investor.preferences.languages))

        if len(common_languages) == 0: 
            continue
        if len(common_languages) == 1:
            match_score += 2
        if len(common_languages) > 1:
            match_score += 5

        common_qualities = list(set(startup.preferences.investor_qualities) & set(investor.preferences.qualities))

        if len(common_qualities) == 0: 
            continue
        if len(common_qualities) <= 2:
            match_score += 5
        else:
            match_score += 10

        common_expertise = list(set(startup.preferences.investor_expertise) & set(investor.preferences.expertise))

        if len(common_expertise) == 0: 
            continue
        if len(common_expertise) <= 2:
            match_score += 5
        else:
            match_score += 10

        common_values = list(set(startup.team.values) & set(investor.preferences.team_values))

        if len(common_values) == 0: 
            continue
        if len(common_values) <= 2:
            match_score += 5
        else:
            match_score += 10

        matches.append({"startup": startup, "name": startup.name, "score": match_score})

    # Iterate over found matches 
    for match in matches:
        # Check if a matching object exists
        if Matching.objects.filter(user=user, matched_with=match["name"]).exists():
            existing_match = Matching.objects.get(user=user, matched_with=match["name"])
            existing_match.match_score = match["score"]
            existing_match.save(update_fields=["match_score"])
        else:
            Matching.objects.create(user=user, matched_with=match["name"], match_score=match["score"])
            # Add match from startup side
            startup_user = CustomUser.objects.get(startup=match["startup"])
            if Matching.objects.filter(user=startup_user, matched_with=investor.name).exists():
                existing_match = Matching.objects.get(user=startup_user, matched_with=investor.name)
                existing_match.match_score = match["score"]
                existing_match.save(update_fields=["match_score"])
            else:
                Matching.objects.create(user=startup_user, matched_with=investor.name, match_score=match["score"])

@receiver(post_save, sender=Startup)
def create_or_update_matching_for_startup(sender, instance, created, **kwargs):
    update_matching_for_startup(instance)

@receiver(post_save, sender=Investor)
def create_or_update_matching_for_investor(sender, instance, created, **kwargs):
    update_matching_for_investor(instance)

@receiver(post_delete, sender=Startup)
@receiver(post_delete, sender=Investor)
def delete_matching(sender, instance, **kwargs):
    # Handle Startup deletion
    if isinstance(instance, Startup):
        user = CustomUser.objects.get(startup=instance)
        user_matches = Matching.objects.filter(user=user)
        reciprocal_matches = Matching.objects.filter(matched_with=instance.name)
        
    # Handle Investor deletion
    elif isinstance(instance, Investor):
        user = CustomUser.objects.get(investor=instance)
        user_matches = Matching.objects.filter(user=user)
        reciprocal_matches = Matching.objects.filter(matched_with=instance.name)

    # Delete the user's matches and reciprocal matches
    user_matches.delete()
    reciprocal_matches.delete()
    
    # Optionally, delete the user if desired
    user.delete()