
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'
    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        users = list(get_user_model().objects.all())  # Get the first user (you should adjust this query according to your needs)
        investor_data = [
            {
            'company_name': 'Eco Ventures',
            'location': 'San Francisco, CA',
            'industry': 'Real Estate',
            'type_of_business': 'B2B', # B2B or B2C 
            'linkedin': 'https://linkedin.com/company/ecovenures',
            'twitter': 'https://twitter.com/ecovenures',
            'description': 'Investing in water saving technologies and businesses.',
            'mission': 'To alleviate global water scarcity through smart investments.',
            'capital': 20000000,
            'stage':  ['Series A', 'Pre Seed'], # stage of the startup: Series A, Series B, Series C, Seed, Pre Seed, Bridge
            'impact_value': 9.0,
            'team_values': ['Sustainability', 'Efficiency', 'Innovation'],
            'team_motives': ['Resource Management', 'Tech Advancement', 'Sustainability'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Water Management', 'HR'],
            'investor_offering':['Has a big network'], 
            'investor_value': ['Sustainability', 'Long-term Gains'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global water conservation sector',
            'sdg': {
                'SDG 6': 'Clean Water and Sanitation',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            } # sdg must to be n the sdg goals
        },
        {
            'company_name': 'Green Horizons',
            'location': 'New York, NY',
            'industry': 'Renewable Energy',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/greenhorizons',
            'twitter': 'https://twitter.com/greenhorizons',
            'description': 'Focused on investing in solar and wind energy startups.',
            'mission': 'To accelerate the transition to renewable energy sources worldwide.',
            'capital': 50000000,
            'stage': ['Series B', 'Series C'],
            'impact_value': 8.5,
            'team_values': ['Innovation', 'Sustainability', 'Growth'],
            'team_motives': ['Environmental Impact', 'Tech Leadership', 'Sustainability'],
            'languages': ['English', 'German'],
            'investor_expertise': ['Renewable Energy', 'Finance'],
            'investor_offering': ['Extensive industry connections'],
            'investor_value': ['Environmental Impact', 'High Returns'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Equity',
            'market': 'Global renewable energy sector',
            'sdg': {
                'SDG 7': 'Affordable and Clean Energy',
                'SDG 13': 'Climate Action'
            }
        },
        {
            'company_name': 'Tech Innovators',
            'location': 'Austin, TX',
            'industry': 'Technology',
            'type_of_business': 'B2C',
            'linkedin': 'https://linkedin.com/company/techinnovators',
            'twitter': 'https://twitter.com/techinnovators',
            'description': 'Investing in cutting-edge consumer technology products.',
            'mission': 'To foster innovation in consumer technology.',
            'capital': 30000000,
            'stage': ['Seed', 'Series A'],
            'impact_value': 7.5,
            'team_values': ['Innovation', 'User Experience', 'Scalability'],
            'team_motives': ['Tech Advancement', 'Market Disruption', 'User Satisfaction'],
            'languages': ['English', 'Chinese'],
            'investor_expertise': ['Consumer Tech', 'Product Development'],
            'investor_offering': ['Product development expertise'],
            'investor_value': ['Innovation', 'Market Leadership'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global consumer technology market',
            'sdg': {
                'SDG 9': 'Industry, Innovation, and Infrastructure',
                'SDG 8': 'Decent Work and Economic Growth'
            }
        },
        {
            'company_name': 'Health Ventures',
            'location': 'Boston, MA',
            'industry': 'Healthcare',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/healthventures',
            'twitter': 'https://twitter.com/healthventures',
            'description': 'Investing in innovative healthcare solutions and biotech.',
            'mission': 'To improve global health through strategic investments.',
            'capital': 40000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 9.0,
            'team_values': ['Health', 'Innovation', 'Patient Care'],
            'team_motives': ['Medical Advancements', 'Patient Outcomes', 'Innovation'],
            'languages': ['English', 'French'],
            'investor_expertise': ['Healthcare', 'Biotechnology'],
            'investor_offering': ['Medical industry insights'],
            'investor_value': ['Health Impact', 'Sustainable Growth'],
            'exit_strategy': 'Merger',
            'type_of_investment': 'Equity',
            'market': 'Global healthcare sector',
            'sdg': {
                'SDG 3': 'Good Health and Well-being',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        },
        {
            'company_name': 'AgriFund',
            'location': 'Chicago, IL',
            'industry': 'Agriculture',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/agrifund',
            'twitter': 'https://twitter.com/agrifund',
            'description': 'Investing in sustainable agriculture and food technology.',
            'mission': 'To support sustainable agricultural practices and food security.',
            'capital': 35000000,
            'stage': ['Pre Seed', 'Seed'],
            'impact_value': 8.0,
            'team_values': ['Sustainability', 'Innovation', 'Food Security'],
            'team_motives': ['Sustainable Farming', 'Food Innovation', 'Resource Management'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Agriculture', 'Sustainability'],
            'investor_offering': ['Agricultural expertise'],
            'investor_value': ['Sustainability', 'Long-term Growth'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Debt',
            'market': 'Global agriculture and food technology sector',
            'sdg': {
                'SDG 2': 'Zero Hunger',
                'SDG 12': 'Responsible Consumption and Production'
            }
        },
        {
            'company_name': 'Urban Growth Partners',
            'location': 'Los Angeles, CA',
            'industry': 'Urban Development',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/urbangrowthpartners',
            'twitter': 'https://twitter.com/urbangrowthpartners',
            'description': 'Investing in urban development and smart city technologies.',
            'mission': 'To create sustainable and smart urban spaces.',
            'capital': 45000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 8.8,
            'team_values': ['Sustainability', 'Innovation', 'Community'],
            'team_motives': ['Urban Innovation', 'Community Development', 'Sustainability'],
            'languages': ['English', 'Japanese'],
            'investor_expertise': ['Urban Development', 'Technology'],
            'investor_offering': ['Urban planning insights'],
            'investor_value': ['Sustainability', 'Community Impact'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global urban development sector',
            'sdg': {
                'SDG 11': 'Sustainable Cities and Communities',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        },]
    #     {
    #         "company_name": "Eco Ventures",
    #         "location": "San Francisco, CA",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/ecovenures",
    #         "twitter": "https://twitter.com/ecovenures",
    #         "description": "Investing in water saving technologies and businesses.",
    #         "mission": "To alleviate global water scarcity through smart investments.",
    #         "capital": [20000,5000000], # first number min value and secon number is max value, (max 1000000000)
    #         "stage": ["Series A", "Pre Seed"],
    #         "impact_value": 9.0,
    #         "team_values": ["Sustainability", "Efficiency", "Innovation"],
    #         "team_motives": ["Resource Management", "Tech Advancement", "Sustainability"],
    #         "languages": ["English", "Spanish"],
    #         "investor_expertise": ["Water Management", "HR"],
    #         "investor_offering": ["Has a big network"],
    #         "investor_value": ["Sustainability", "Long-term Gains"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global water conservation sector",
    #         "sdg": {
    #             "SDG 6": "Clean Water and Sanitation",
    #             "SDG 9": "Industry, Innovation, and Infrastructure"
    #         }
    #     },
    #     {
    #         "company_name": "Green Capital",
    #         "location": "Boston, MA",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/greencapital",
    #         "twitter": "https://twitter.com/greencapital",
    #         "description": "Funding green energy startups.",
    #         "mission": "To promote the growth of renewable energy.",
    #         "capital": 30000000,
    #         "stage": ["Series A", "Series B"],
    #         "impact_value": 8.5,
    #         "team_values": ["Innovation", "Growth"],
    #         "team_motives": ["Renewable Energy", "Sustainability"],
    #         "languages": ["English", "French"],
    #         "investor_expertise": ["Renewable Energy", "Finance"],
    #         "investor_offering": ["Industry connections"],
    #         "investor_value": ["High ROI", "Sustainability"],
    #         "exit_strategy": "Acquisition",
    #         "type_of_investment": "Equity",
    #         "market": "Global renewable energy market",
    #         "sdg": {
    #             "SDG 7": "Affordable and Clean Energy",
    #             "SDG 13": "Climate Action"
    #         }
    #     },
    #     {
    #         "company_name": "Sustainable Future Investments",
    #         "location": "New York, NY",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/sustainablefutureinvestments",
    #         "twitter": "https://twitter.com/sustainablefutureinvestments",
    #         "description": "Supporting sustainable technology enterprises.",
    #         "mission": "To foster innovation in sustainable technologies.",
    #         "capital": 25000000,
    #         "stage": ["Series A", "Seed"],
    #         "impact_value": 9.5,
    #         "team_values": ["Innovation", "Sustainability"],
    #         "team_motives": ["Tech Advancement", "Environmental Protection"],
    #         "languages": ["English", "German"],
    #         "investor_expertise": ["Technology", "Environmental Science"],
    #         "investor_offering": ["Technical expertise"],
    #         "investor_value": ["Sustainability", "Innovation"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global tech market",
    #         "sdg": {
    #             "SDG 9": "Industry, Innovation, and Infrastructure",
    #             "SDG 12": "Responsible Consumption and Production"
    #         }
    #     },
    #     {
    #         "company_name": "Renewable Investments",
    #         "location": "Austin, TX",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/renewableinvestments",
    #         "twitter": "https://twitter.com/renewableinvestments",
    #         "description": "Investing in renewable energy projects.",
    #         "mission": "To make renewable energy the primary energy source.",
    #         "capital": 40000000,
    #         "stage": ["Series A", "Series C"],
    #         "impact_value": 8.0,
    #         "team_values": ["Sustainability", "Growth"],
    #         "team_motives": ["Renewable Energy", "Tech Advancement"],
    #         "languages": ["English"],
    #         "investor_expertise": ["Renewable Energy", "Project Management"],
    #         "investor_offering": ["Strategic partnerships"],
    #         "investor_value": ["High ROI", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global renewable energy market",
    #         "sdg": {
    #             "SDG 7": "Affordable and Clean Energy",
    #             "SDG 13": "Climate Action"
    #         }
    #     },
    #     {
    #         "company_name": "Impact Ventures",
    #         "location": "Chicago, IL",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/impactventures",
    #         "twitter": "https://twitter.com/impactventures",
    #         "description": "Investing in high-impact startups.",
    #         "mission": "To create positive social and environmental impact.",
    #         "capital": 35000000,
    #         "stage": ["Series A", "Pre Seed"],
    #         "impact_value": 9.0,
    #         "team_values": ["Integrity", "Impact"],
    #         "team_motives": ["Sustainability", "Resource Management"],
    #         "languages": ["English", "Spanish"],
    #         "investor_expertise": ["Social Impact", "Environmental Science"],
    #         "investor_offering": ["Expert guidance"],
    #         "investor_value": ["High Impact", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global impact market",
    #         "sdg": {
    #             "SDG 13": "Climate Action",
    #             "SDG 6": "Clean Water and Sanitation"
    #         }
    #     },
    #     {
    #         "company_name": "Eco Innovate Partners",
    #         "location": "Los Angeles, CA",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/ecoinnovatepartners",
    #         "twitter": "https://twitter.com/ecoinnovatepartners",
    #         "description": "Backing innovative eco-friendly startups.",
    #         "mission": "To support the growth of eco-friendly businesses.",
    #         "capital": 28000000,
    #         "stage": ["Series A", "Seed"],
    #         "impact_value": 9.5,
    #         "team_values": ["Innovation", "Sustainability"],
    #         "team_motives": ["Environmental Protection", "Tech Advancement"],
    #         "languages": ["English", "French"],
    #         "investor_expertise": ["Technology", "Environmental Science"],
    #         "investor_offering": ["Technical expertise"],
    #         "investor_value": ["Innovation", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global tech market",
    #         "sdg": {
    #             "SDG 9": "Industry, Innovation, and Infrastructure",
    #             "SDG 12": "Responsible Consumption and Production"
    #         }
    #     },
    #     {
    #         "company_name": "Green Future Fund",
    #         "location": "Denver, CO",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/greenfuturefund",
    #         "twitter": "https://twitter.com/greenfuturefund",
    #         "description": "Investing in future green technologies.",
    #         "mission": "To pave the way for a greener future.",
    #         "capital": 32000000,
    #         "stage": ["Series A", "Series B"],
    #         "impact_value": 8.5,
    #         "team_values": ["Innovation", "Sustainability"],
    #         "team_motives": ["Tech Advancement", "Environmental Protection"],
    #         "languages": ["English", "German"],
    #         "investor_expertise": ["Green Technology", "Finance"],
    #         "investor_offering": ["Industry connections"],
    #         "investor_value": ["High ROI", "Sustainability"],
    #         "exit_strategy": "Acquisition",
    #         "type_of_investment": "Equity",
    #         "market": "Global green tech market",
    #         "sdg": {
    #             "SDG 9": "Industry, Innovation, and Infrastructure",
    #             "SDG 7": "Affordable and Clean Energy"
    #         }
    #     },
    #     {
    #         "company_name": "Eco Growth Capital",
    #         "location": "Miami, FL",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/ecogrowthcapital",
    #         "twitter": "https://twitter.com/ecogrowthcapital",
    #         "description": "Investing in scalable eco-friendly businesses.",
    #         "mission": "To drive growth in eco-friendly markets.",
    #         "capital": 27000000,
    #         "stage": ["Series A", "Series B"],
    #         "impact_value": 8.0,
    #         "team_values": ["Growth", "Sustainability"],
    #         "team_motives": ["Environmental Protection", "Resource Management"],
    #         "languages": ["English", "Spanish"],
    #         "investor_expertise": ["Finance", "Green Technology"],
    #         "investor_offering": ["Growth support"],
    #         "investor_value": ["High ROI", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global green tech market",
    #         "sdg": {
    #             "SDG 7": "Affordable and Clean Energy",
    #             "SDG 13": "Climate Action"
    #         }
    #     },
    #     {
    #         "company_name": "Sustainability Ventures",
    #         "location": "San Diego, CA",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/sustainabilityventures",
    #         "twitter": "https://twitter.com/sustainabilityventures",
    #         "description": "Funding sustainable innovation.",
    #         "mission": "To support businesses that prioritize sustainability.",
    #         "capital": 26000000,
    #         "stage": ["Series A", "Seed"],
    #         "impact_value": 9.0,
    #         "team_values": ["Innovation", "Sustainability"],
    #         "team_motives": ["Tech Advancement", "Environmental Protection"],
    #         "languages": ["English", "French"],
    #         "investor_expertise": ["Technology", "Environmental Science"],
    #         "investor_offering": ["Technical expertise"],
    #         "investor_value": ["Innovation", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global tech market",
    #         "sdg": {
    #             "SDG 9": "Industry, Innovation, and Infrastructure",
    #             "SDG 12": "Responsible Consumption and Production"
    #         }
    #     },{
    #         "company_name": "Future Impact Investments",
    #         "location": "San Jose, CA",
    #         "industry": "Real Estate",
    #         "type_of_business": "B2B",
    #         "linkedin": "https://linkedin.com/company/futureimpactinvestments",
    #         "twitter": "https://twitter.com/futureimpactinvestments",
    #         "description": "Investing in high-impact startups.",
    #         "mission": "To create positive social and environmental impact.",
    #         "capital": 35000000,
    #         "stage": ["Series A", "Pre Seed"],
    #         "impact_value": 9.0,
    #         "team_values": ["Integrity", "Impact"],
    #         "team_motives": ["Sustainability", "Resource Management"],
    #         "languages": ["English", "Spanish"],
    #         "investor_expertise": ["Social Impact", "Environmental Science"],
    #         "investor_offering": ["Expert guidance"],
    #         "investor_value": ["High Impact", "Sustainability"],
    #         "exit_strategy": "IPO",
    #         "type_of_investment": "Equity",
    #         "market": "Global impact market",
    #         "sdg": {
    #             "SDG 13": "Climate Action",
    #             "SDG 6": "Clean Water and Sanitation"
    #         }
    #     }

    # ]
#         investor_data=[
#     {
#         "name": "Green Innovate",
#         "code": "GI101",
#         "location": "Austin, TX",
#         "industry": "Real Estate",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://greeninnovate.com",
#         "facebook": "https://facebook.com/greeninnovate",
#         "linkedin": "https://linkedin.com/company/greeninnovate",
#         "twitter": "https://twitter.com/greeninnovate",
#         "description": "Pioneering solar solutions.",
#         "mission": "To Empower sustainable living.",
#         "product_description": "Solar panels.",
#         "customer_problem": "Lack of affordable solar options.",
#         "usp": "Low-cost, high-efficiency solutions",
#         "capital": 500000,
#         "stage": "Seed",
#         "target_investor_n": 1,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 0,
#         "impact_value": 0.0,
#         "team_values": [
#             "Integrity",
#             "Innovation"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Real Estate Development",
#             "Sustainable Building"
#         ],
#         "investor_expectations": [
#             "Long-term ROI",
#             "Land acquisition expertise"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global real estate market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "BioHealth Systems",
#         "code": "BH102",
#         "location": "Austin, TX",
#         "industry": "Healthcare",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://biohealthsystems.com",
#         "facebook": "https://facebook.com/biohealthsystems",
#         "linkedin": "https://linkedin.com/company/biohealthsystems",
#         "twitter": "https://twitter.com/biohealthsystems",
#         "description": "Pioneering biomedical solutions.",
#         "mission": "To Improve global health.",
#         "product_description": "Biomedical devices.",
#         "customer_problem": "Lack of affordable biomedical options.",
#         "usp": "Cutting-edge healthcare technology",
#         "capital": 600000,
#         "stage": "Seed",
#         "target_investor_n": 2,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 1,
#         "impact_value": 1.0,
#         "team_values": [
#             "Innovation",
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Healthcare Technology",
#             "Medical Innovation"
#         ],
#         "investor_expectations": [
#             "Innovative product pipeline",
#             "Regulatory expertise"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global healthcare market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Future Robotics",
#         "code": "FR103",
#         "location": "Austin, TX",
#         "industry": "Technology",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://futurerobotics.com",
#         "facebook": "https://facebook.com/futurerobotics",
#         "linkedin": "https://linkedin.com/company/futurerobotics",
#         "twitter": "https://twitter.com/futurerobotics",
#         "description": "Pioneering automation solutions.",
#         "mission": "To Lead in automation.",
#         "product_description": "Automation robots.",
#         "customer_problem": "Lack of affordable automation options.",
#         "usp": "Advanced AI integration",
#         "capital": 700000,
#         "stage": "Seed",
#         "target_investor_n": 3,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 2,
#         "impact_value": 2.0,
#         "team_values": [
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Robotics",
#             "AI Development"
#         ],
#         "investor_expectations": [
#             "Cutting-edge technology",
#             "Patent portfolio"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global technology market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Eco Transport",
#         "code": "ET104",
#         "location": "Austin, TX",
#         "industry": "Transportation",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://ecotransport.com",
#         "facebook": "https://facebook.com/ecotransport",
#         "linkedin": "https://linkedin.com/company/ecotransport",
#         "twitter": "https://twitter.com/ecotransport",
#         "description": "Pioneering electric solutions.",
#         "mission": "To Reduce carbon emissions.",
#         "product_description": "Electric vehicles.",
#         "customer_problem": "Lack of affordable electric options.",
#         "usp": "Zero-emission transportation",
#         "capital": 800000,
#         "stage": "Seed",
#         "target_investor_n": 4,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 0,
#         "impact_value": 3.0,
#         "team_values": [
#             "Integrity",
#             "Innovation"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Eco-friendly Transportation",
#             "Automotive Engineering"
#         ],
#         "investor_expectations": [
#             "Carbon neutral initiatives",
#             "Fleet management"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global transportation market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Virtual Market",
#         "code": "VM105",
#         "location": "Austin, TX",
#         "industry": "Retail",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://virtualmarket.com",
#         "facebook": "https://facebook.com/virtualmarket",
#         "linkedin": "https://linkedin.com/company/virtualmarket",
#         "twitter": "https://twitter.com/virtualmarket",
#         "description": "Pioneering vr solutions.",
#         "mission": "To Enhance shopping experience.",
#         "product_description": "VR platforms.",
#         "customer_problem": "Lack of affordable vr options.",
#         "usp": "Personalized shopping experience",
#         "capital": 900000,
#         "stage": "Seed",
#         "target_investor_n": 5,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 1,
#         "impact_value": 4.0,
#         "team_values": [
#             "Innovation",
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "E-commerce",
#             "Consumer Experience"
#         ],
#         "investor_expectations": [
#             "Global scale operations",
#             "Brand loyalty"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global retail market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Smart Farming",
#         "code": "SF106",
#         "location": "Austin, TX",
#         "industry": "Agriculture",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://smartfarming.com",
#         "facebook": "https://facebook.com/smartfarming",
#         "linkedin": "https://linkedin.com/company/smartfarming",
#         "twitter": "https://twitter.com/smartfarming",
#         "description": "Pioneering precision solutions.",
#         "mission": "To Boost agricultural efficiency.",
#         "product_description": "Precision farming tools.",
#         "customer_problem": "Lack of affordable precision options.",
#         "usp": "Drones for efficient crop monitoring",
#         "capital": 1000000,
#         "stage": "Series A",
#         "target_investor_n": 1,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 2,
#         "impact_value": 5.0,
#         "team_values": [
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Agritech",
#             "Sustainable Farming"
#         ],
#         "investor_expectations": [
#             "High crop yield",
#             "Biotechnology"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global agriculture market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Clean Ocean Tech",
#         "code": "CT107",
#         "location": "Austin, TX",
#         "industry": "Environmental Services",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://cleanoceantech.com",
#         "facebook": "https://facebook.com/cleanoceantech",
#         "linkedin": "https://linkedin.com/company/cleanoceantech",
#         "twitter": "https://twitter.com/cleanoceantech",
#         "description": "Pioneering ocean solutions.",
#         "mission": "To Protect marine life.",
#         "product_description": "Ocean cleaning drones.",
#         "customer_problem": "Lack of affordable ocean options.",
#         "usp": "Automated waste collection",
#         "capital": 1100000,
#         "stage": "Series A",
#         "target_investor_n": 2,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 0,
#         "impact_value": 6.0,
#         "team_values": [
#             "Integrity",
#             "Innovation"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Waste Management",
#             "Ecology"
#         ],
#         "investor_expectations": [
#             "Impact on local ecosystems",
#             "Compliance with environmental regulations"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global environmental services market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Data Secure",
#         "code": "DS108",
#         "location": "Austin, TX",
#         "industry": "Cybersecurity",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://datasecure.com",
#         "facebook": "https://facebook.com/datasecure",
#         "linkedin": "https://linkedin.com/company/datasecure",
#         "twitter": "https://twitter.com/datasecure",
#         "description": "Pioneering encryption solutions.",
#         "mission": "To Ensure data privacy.",
#         "product_description": "Encryption solutions.",
#         "customer_problem": "Lack of affordable encryption options.",
#         "usp": "Unbreakable encryption",
#         "capital": 1200000,
#         "stage": "Series A",
#         "target_investor_n": 3,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 1,
#         "impact_value": 7.0,
#         "team_values": [
#             "Innovation",
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Data Protection",
#             "Network Security"
#         ],
#         "investor_expectations": [
#             "Government contracts",
#             "Advanced cyber defense"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global cybersecurity market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "AI Education",
#         "code": "AE109",
#         "location": "Austin, TX",
#         "industry": "Education",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://aieducation.com",
#         "facebook": "https://facebook.com/aieducation",
#         "linkedin": "https://linkedin.com/company/aieducation",
#         "twitter": "https://twitter.com/aieducation",
#         "description": "Pioneering ai solutions.",
#         "mission": "To Revolutionize learning.",
#         "product_description": "AI tutors.",
#         "customer_problem": "Lack of affordable ai options.",
#         "usp": "Customized learning plans",
#         "capital": 1300000,
#         "stage": "Series A",
#         "target_investor_n": 4,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 2,
#         "impact_value": 8.0,
#         "team_values": [
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "EdTech",
#             "Curriculum Development"
#         ],
#         "investor_expectations": [
#             "Adaptive learning technologies",
#             "Student engagement"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global education market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Urban Renew",
#         "code": "UR110",
#         "location": "Austin, TX",
#         "industry": "Construction",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://urbanrenew.com",
#         "facebook": "https://facebook.com/urbanrenew",
#         "linkedin": "https://linkedin.com/company/urbanrenew",
#         "twitter": "https://twitter.com/urbanrenew",
#         "description": "Pioneering smart solutions.",
#         "mission": "To Transform urban environments.",
#         "product_description": "Smart construction materials.",
#         "customer_problem": "Lack of affordable smart options.",
#         "usp": "Eco-friendly materials",
#         "capital": 1400000,
#         "stage": "Series A",
#         "target_investor_n": 5,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 0,
#         "impact_value": 9.0,
#         "team_values": [
#             "Integrity",
#             "Innovation"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Green Construction",
#             "Urban Planning"
#         ],
#         "investor_expectations": [
#             "Eco-friendly materials",
#             "Cost-efficient building techniques"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global construction market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Green Build",
#         "code": "GB111",
#         "location": "Austin, TX",
#         "industry": "Aerospace",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://greenbuild.com",
#         "facebook": "https://facebook.com/greenbuild",
#         "linkedin": "https://linkedin.com/company/greenbuild",
#         "twitter": "https://twitter.com/greenbuild",
#         "description": "Pioneering reused solutions.",
#         "mission": "To Promote green building.",
#         "product_description": "Reused materials in construction.",
#         "customer_problem": "Lack of affordable reused options.",
#         "usp": "Cost-effective space exploration",
#         "capital": 1500000,
#         "stage": "Series B",
#         "target_investor_n": 1,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 1,
#         "impact_value": 0.0,
#         "team_values": [
#             "Innovation",
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Space Technology",
#             "Aerospace Engineering"
#         ],
#         "investor_expectations": [
#             "Commercial viability of space projects",
#             "Innovative spacecraft design"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global aerospace market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Space Pioneers",
#         "code": "SP112",
#         "location": "Austin, TX",
#         "industry": "Food & Beverages",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://spacepioneers.com",
#         "facebook": "https://facebook.com/spacepioneers",
#         "linkedin": "https://linkedin.com/company/spacepioneers",
#         "twitter": "https://twitter.com/spacepioneers",
#         "description": "Pioneering satellites solutions.",
#         "mission": "To Explore new frontiers.",
#         "product_description": "Satellites.",
#         "customer_problem": "Lack of affordable satellites options.",
#         "usp": "Innovative digital protection",
#         "capital": 1600000,
#         "stage": "Series B",
#         "target_investor_n": 2,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 2,
#         "impact_value": 1.0,
#         "team_values": [
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Food Tech",
#             "Nutritional Science"
#         ],
#         "investor_expectations": [
#             "Sustainable sourcing",
#             "Health-conscious products"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global food & beverages market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "CyberSafe",
#         "code": "CS113",
#         "location": "Austin, TX",
#         "industry": "Water Management",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://cybersafe.com",
#         "facebook": "https://facebook.com/cybersafe",
#         "linkedin": "https://linkedin.com/company/cybersafe",
#         "twitter": "https://twitter.com/cybersafe",
#         "description": "Pioneering firewall solutions.",
#         "mission": "To Safeguard digital assets.",
#         "product_description": "Firewall solutions.",
#         "customer_problem": "Lack of affordable firewall options.",
#         "usp": "Sustainable food production",
#         "capital": 1700000,
#         "stage": "Series B",
#         "target_investor_n": 3,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 0,
#         "impact_value": 2.0,
#         "team_values": [
#             "Integrity",
#             "Innovation"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Water Treatment Technology",
#             "Sustainability"
#         ],
#         "investor_expectations": [
#             "Resource conservation",
#             "Infrastructure development"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global water management market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Food Revolution",
#         "code": "FR114",
#         "location": "Austin, TX",
#         "industry": "Real Estate",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://foodrevolution.com",
#         "facebook": "https://facebook.com/foodrevolution",
#         "linkedin": "https://linkedin.com/company/foodrevolution",
#         "twitter": "https://twitter.com/foodrevolution",
#         "description": "Pioneering plant-based solutions.",
#         "mission": "To Disrupt the food industry.",
#         "product_description": "Plant-based foods.",
#         "customer_problem": "Lack of affordable plant-based options.",
#         "usp": "Effective water purification",
#         "capital": 1800000,
#         "stage": "Series B",
#         "target_investor_n": 4,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 1,
#         "impact_value": 3.0,
#         "team_values": [
#             "Innovation",
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "No",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Real Estate Development",
#             "Sustainable Building"
#         ],
#         "investor_expectations": [
#             "Long-term ROI",
#             "Land acquisition expertise"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global real estate market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     },
#     {
#         "name": "Water Purify",
#         "code": "WP115",
#         "location": "Austin, TX",
#         "industry": "Healthcare",
#         "founding_date": "2023-01-01",
#         "legal_form": "Corporation",
#         "type_of_business": "B2B",
#         "website": "https://waterpurify.com",
#         "facebook": "https://facebook.com/waterpurify",
#         "linkedin": "https://linkedin.com/company/waterpurify",
#         "twitter": "https://twitter.com/waterpurify",
#         "description": "Pioneering water solutions.",
#         "mission": "To Provide clean water.",
#         "product_description": "Water filtration systems.",
#         "customer_problem": "Lack of affordable water options.",
#         "usp": "Low-cost, high-efficiency solutions",
#         "capital": 1900000,
#         "stage": "Series B",
#         "target_investor_n": 5,
#         "use_of_funds": {
#             "R&D": 40,
#             "Marketing": 30,
#             "Operations": 30
#         },
#         "financial_tables": "Financial data here.",
#         "already_invested_n": 2,
#         "impact_value": 4.0,
#         "team_values": [
#             "Sustainability"
#         ],
#         "team_motives": [
#             "Resource Management"
#         ],
#         "funding_experience": "Yes",
#         "team_languages": [
#             "English"
#         ],
#         "investor_expertise": [
#             "Healthcare Technology",
#             "Medical Innovation"
#         ],
#         "investor_expectations": [
#             "Innovative product pipeline",
#             "Regulatory expertise"
#         ],
#         "exit_strategy": "Acquisition",
#         "type_of_investment": "Equity",
#         "market": "Global healthcare market.",
#         "sdg": {
#             "SDG 7": "Affordable and Clean Energy",
#             "SDG 13": "Climate Action",
#             "SDG 6": "Clean Water and Sanitation"
#         }
#     }
# ]


        for i in range(16):
            Investor.objects.create(
                        user = users[i],
                        **investor_data[i]
                    )

        
        self.stdout.write(self.style.SUCCESS('Successfully created Investors'))
