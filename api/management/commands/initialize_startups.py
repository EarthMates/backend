import json
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from api.models import Startup
from users.models import CustomUser


#Funzionante, associa le starup alla variabile 'user'
class Command(BaseCommand):
    help = 'Initialize startup models with meaningful values'

    def handle(self, *args, **options):
        # Ensure there is at least one user to assign as the creator of the startups
        User = get_user_model()
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR('No users found in the database. Create at least one user before running this script.'))
            return

        user = list(User.objects.all())

        startups_data = [
            {
                "name": "Green Innovate",
                "code": "GI101",
                "location": "Austin, TX",
                "industry": "Real Estate",
                "founding_date": "2023-04-15",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://greeninnovate.com",
                "facebook": "https://facebook.com/greeninnovate",
                "linkedin": "https://linkedin.com/company/greeninnovate",
                "twitter": "https://twitter.com/greeninnovate",
                "description": "Pioneering renewable energy solutions.",
                "mission": "To empower sustainable living.",
                "product_description": "Solar panels and wind turbines.",
                "customer_problem": "Lack of affordable green energy options.",
                "usp": "Low-cost, high-efficiency solar solutions.",
                "capital": 2000000, 
                "stage": "Series A",
                "target_investor_n": 4,
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30}, 
                "financial_tables": "Financial data here.",
                "already_invested_n": 3,
                "impact_value": 9.0,
                "team_values": ["Integrity", "Innovation"],
                "team_motives": ["Resource Management"],
                "funding_experience": 'Yes',
                "team_languages": ["English"],
                "investor_expertise": ["Management", "HR"],
                "investor_expectations": ["has a big network"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global energy market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 13": "Climate Action",
                    'SDG 6': 'Clean Water and Sanitation',
                }
            },
            
            {
                "name": "Green Innovate",
                "code": "GI101",
                "location": "Austin, TX",
                "industry": "Real Estate",
                "founding_date": "2023-04-15",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://greeninnovate.com",
                "facebook": "https://facebook.com/greeninnovate",
                "linkedin": "https://linkedin.com/company/greeninnovate",
                "twitter": "https://twitter.com/greeninnovate",
                "description": "Pioneering renewable energy solutions.",
                "mission": "To empower sustainable living.",
                "product_description": "Solar panels and wind turbines.",
                "customer_problem": "Lack of affordable green energy options.",
                "usp": "Low-cost, high-efficiency solar solutions.",
                "capital": 2000000,
                "stage": "Series A",
                "target_investor_n": 4,
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 3,
                "impact_value": 9.0,
                "team_values": ["Integrity", "Innovation"],
                "team_motives": ["Resource Management"],
                "funding_experience": "Yes",
                "team_languages": ["English"],
                "investor_expertise": ["Management", "HR"],
                "investor_expectations": ["has a big network"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global energy market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 13": "Climate Action",
                    "SDG 6": "Clean Water and Sanitation"
                }
            },
            {
                "name": "AquaTech Solutions",
                "code": "ATS102",
                "location": "New York, NY",
                "industry": "Real Estate",
                "founding_date": "2021-08-10",
                "legal_form": "LLC",
                "type_of_business": "B2B",
                "website": "https://aquatechsolutions.com",
                "facebook": "https://facebook.com/aquatechsolutions",
                "linkedin": "https://linkedin.com/company/aquatechsolutions",
                "twitter": "https://twitter.com/aquatechsolutions",
                "description": "Innovative water purification systems.",
                "mission": "Ensuring clean water for all.",
                "product_description": "Advanced water filtration devices.",
                "customer_problem": "Contaminated water sources.",
                "usp": "High-efficiency, low-maintenance filters.",
                "capital": 5000000,
                "stage": "Seed",
                "target_investor_n": 5,
                "use_of_funds": {"R&D": 50, "Marketing": 20, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 2,
                "impact_value": 8.5,
                "team_values": ["Integrity", "Sustainability"],
                "team_motives": ["Resource Management", "Innovation"],
                "funding_experience": "Yes",
                "team_languages": ["English", "Spanish"],
                "investor_expertise": ["Water Management", "Environmental Science"],
                "investor_expectations": ["long-term commitment"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global water market.",
                "sdg": {
                    "SDG 6": "Clean Water and Sanitation",
                    "SDG 9": "Industry, Innovation, and Infrastructure"
                }
            },
            {
                "name": "SustainTech Innovators",
                "code": "STI103",
                "location": "Chicago, IL",
                "industry": "Real Estate",
                "founding_date": "2022-01-20",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://sustaintechinnovators.com",
                "facebook": "https://facebook.com/sustaintechinnovators",
                "linkedin": "https://linkedin.com/company/sustaintechinnovators",
                "twitter": "https://twitter.com/sustaintechinnovators",
                "description": "Developing sustainable building materials.",
                "mission": "Revolutionizing the construction industry with eco-friendly materials.",
                "product_description": "Biodegradable and recyclable construction materials.",
                "customer_problem": "High environmental impact of traditional building materials.",
                "usp": "Eco-friendly, durable materials.",
                "capital": 3000000,
                "stage": "Series A",
                "target_investor_n": 3,
                "use_of_funds": {"R&D": 60, "Marketing": 20, "Operations": 20},
                "financial_tables": "Financial data here.",
                "already_invested_n": 1,
                "impact_value": 8.0,
                "team_values": ["Sustainability", "Innovation"],
                "team_motives": ["Environmental Protection"],
                "funding_experience": "No",
                "team_languages": ["English"],
                "investor_expertise": ["Construction", "Materials Science"],
                "investor_expectations": ["high ROI"],
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global construction market.",
                "sdg": {
                    "SDG 11": "Sustainable Cities and Communities",
                    "SDG 12": "Responsible Consumption and Production"
                }
            },
            {
                "name": "EcoBuild Innovations",
                "code": "EBI104",
                "location": "San Francisco, CA",
                "industry": "Real Estate",
                "founding_date": "2020-11-05",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://ecobuildinnovations.com",
                "facebook": "https://facebook.com/ecobuildinnovations",
                "linkedin": "https://linkedin.com/company/ecobuildinnovations",
                "twitter": "https://twitter.com/ecobuildinnovations",
                "description": "Green construction technologies.",
                "mission": "Building a sustainable future.",
                "product_description": "Energy-efficient building systems.",
                "customer_problem": "High energy consumption in buildings.",
                "usp": "Energy-saving construction technologies.",
                "capital": 7000000,
                "stage": "Series B",
                "target_investor_n": 6,
                "use_of_funds": {"R&D": 30, "Marketing": 40, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 4,
                "impact_value": 9.5,
                "team_values": ["Sustainability", "Efficiency"],
                "team_motives": ["Tech Advancement"],
                "funding_experience": "Yes",
                "team_languages": ["English", "French"],
                "investor_expertise": ["Energy Efficiency", "Construction"],
                "investor_expectations": ["strong partnership"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global construction market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 11": "Sustainable Cities and Communities"
                }
            },
            {
                "name": "RenewGen Power",
                "code": "RGP105",
                "location": "Seattle, WA",
                "industry": "Real Estate",
                "founding_date": "2021-03-15",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://renewgenpower.com",
                "facebook": "https://facebook.com/renewgenpower",
                "linkedin": "https://linkedin.com/company/renewgenpower",
                "twitter": "https://twitter.com/renewgenpower",
                "description": "Renewable energy solutions for homes.",
                "mission": "Making renewable energy accessible to everyone.",
                "product_description": "Home solar and wind energy systems.",
                "customer_problem": "High cost of renewable energy installation.",
                "usp": "Affordable and efficient energy solutions.",
                "capital": 6000000,
                "stage": "Series A",
                "target_investor_n": 5,
                "use_of_funds": {"R&D": 50, "Marketing": 30, "Operations": 20},
                "financial_tables": "Financial data here.",
                "already_invested_n": 2,
                "impact_value": 9.0,
                "team_values": ["Innovation", "Accessibility"],
                "team_motives": ["Environmental Protection"],
                "funding_experience": "Yes",
                "team_languages": ["English", "German"],
                "investor_expertise": ["Renewable Energy", "Technology"],
                "investor_expectations": ["high returns"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global renewable energy market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 13": "Climate Action"
                }
            }
        ]
        
        

        for i in range(11):
            Startup.objects.create(
                        user=user[i],
                        **startups_data[i]
                    )
        self.stdout.write(self.style.SUCCESS('Successfully initialized startup models.'))


