

# import json
# from django.core.management.base import BaseCommand
# from django.utils.timezone import now
# from django.contrib.auth import get_user_model
# from api.models import Startup
# from users.models import CustomUser

STP_NUM =150
INV_NUM =150
from api.models import Startup
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'
    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        users = list(get_user_model().objects.all())
        names =[
    "TechNova Innovations",
    "BlueWave Dynamics",
    "QuantumLeaf Solutions",
    "SynergySphere",
    "GreenPulse Ventures",
    "AeroNex Technologies",
    "UrbanGrid Systems",
    "EcoStream Resources",
    "NextGen Digital",
    "Solaris Edge",
    "SmartByte Solutions",
    "LuminaX Industries",
    "AquaForge Technologies",
    "Visionary Vortex",
    "Titanium Edge Systems",
    "DataCrest Analytics",
    "OrbitLink Networks",
    "BioFusion Labs",
    "SonicWave Innovations",
    "EcoVerde Enterprises",
    "CyberHawk Solutions",
    "ZenithCore Technologies",
    "Solaris Vista",
    "BrightScale Analytics",
    "EnerGen Dynamics",
    "SkyBridge Systems",
    "AstraWave Technologies",
    "OptimaFlow Solutions",
    "CrystalGrid Networks",
    "FusionPoint Industries",
    "InnoWave Ventures",
    "AquaSynergy",
    "NexusShift Technologies",
    "VertexEdge Systems",
    "TerraFusion Solutions",
    "PureVolt Energy",
    "UrbanPulse Dynamics",
    "EcoLink Resources",
    "Solaris Stream",
    "ProximaX Solutions",
    "CyberSphere Systems",
    "AlphaWave Innovations",
    "GreenEdge Ventures",
    "SkyNex Technologies",
    "DataLink Dynamics",
    "HorizonTech Systems",
    "EcoVibe Enterprises",
    "QuantumCore Labs",
    "Solaris Quantum",
    "BioWave Solutions",
    "TerraVolt Energy",
    "AstraLink Networks",
    "BrightForge Industries",
    "NexGen Dynamics",
    "SmartGrid Solutions",
    "CyberX Innovations",
    "AeroNex Systems",
    "ZenithLink Technologies",
    "Solaris Matrix",
    "BlueNova Ventures",
    "VisionTech Solutions",
    "AquaPulse Technologies",
    "FusionWave Labs",
    "GreenCore Dynamics",
    "SkyVolt Systems",
    "UrbanVista Enterprises",
    "Solaris Nexus",
    "TitanEdge Technologies",
    "DataWave Solutions",
    "OptimaNex Systems",
    "CrystalStream Networks",
    "HorizonCore Innovations",
    "EcoFusion Ventures",
    "NextWave Labs",
    "QuantumFlow Dynamics",
    "SkyTech Systems",
    "CyberStream Solutions",
    "AlphaCore Ventures",
    "GreenNex Technologies",
    "Solaris Link",
    "VisionNex Systems",
    "TerraCore Labs",
    "BrightWave Innovations",
    "EcoMatrix Solutions",
    "AeroVolt Dynamics",
    "NexusCore Technologies",
    "FusionLink Ventures",
    "CrystalVolt Networks",
    "SmartStream Systems",
    "ZenithFlow Labs",
    "ProximaCore Technologies",
    "SkyLink Ventures",
    "OptimaStream Solutions",
    "QuantumEdge Dynamics",
    "BlueCore Technologies",
    "VisionCore Innovations",
    "GreenLink Solutions",
    "Solaris Core",
    "CyberNex Systems",
    "HorizonEdge Ventures",
    "EcoVista Dynamics",
    "AquaCore Technologies",
    "FusionVista Labs",
    "NexusFlow Solutions",
    "AlphaLink Ventures",
    "BrightCore Systems",
    "TerraNex Technologies",
    "SkyCore Innovations",
    "EcoVolt Systems",
    "SmartVolt Ventures",
    "ProximaVista Technologies",
    "ZenithStream Solutions",
    "FusionCore Labs",
    "VisionEdge Dynamics",
    "AeroCore Systems",
    "Solaris Link Ventures",
    "DataVolt Solutions",
    "GreenStream Labs",
    "UrbanEdge Dynamics",
    "QuantumVista Technologies",
    "SkyVolt Innovations",
    "AstraCore Ventures",
    "EcoWave Solutions",
    "OptimaVolt Systems",
    "NexusStream Technologies",
    "CrystalCore Ventures",
    "FusionEdge Dynamics",
    "BlueStream Labs",
    "AlphaVista Solutions",
    "UrbanVolt Technologies",
    "SmartCore Ventures",
    "GreenCore Labs",
    "ProximaEdge Dynamics",
    "AquaVolt Systems",
    "Solaris Edge Ventures",
    "CyberCore Innovations",
    "ZenithNex Solutions",
    "DataStream Technologies",
    "HorizonVolt Systems",
    "NextCore Ventures",
    "VisionLink Dynamics",
    "EcoCore Technologies",
    "FusionVolt Labs",
    "AeroVista Solutions",
    "UrbanNex Technologies"
]

        languages =[
            "English",
            "German",
            "French",
            "Italian",
            "Spanish",
            "Chinese",
            "Arabic"
        ]

        industry =[
            "Real estate",
            "Nature protection",
            "Woman Empowerment",
            "Poverty alleviation",
            "Greentech",
            "Smart City",
            "Mobility",
            "Energy",
            "Education",
            "Health",
            "Sports",
            "Cosmetics",
            "Financial & Insurance",
            "Food",
            "Legal",
            "Rental & Repair",
            "Transportation & storage",
            "Information & Communication",
            "Arts, entertainment & recreation",
            "Support services",
            "Technical services",
            "Environmental Consulting",
            "Other"
        ]

        type_of_business =[
            "B2B",
            "B2C",
            "Consultancy",
            "All"
        ]

        team_values =[
        "nability",
        "Customer Orientation",
        "Efficiency",
        "Collaboration",
        "Common good",
        "Value-oriented",
        "Engagement",
        "Transparency",
        "Ethical Behavior",
        "Punctuality",
        "Quickness",
        "Ethics",
        "Integrity",
        "Openness to innovation",
        "Support and network",
        "Risk-taking",
        "Transparency",
        "Trust",
        "Long-term focus",
        "Social responsability",
        "Flexibility and adaptability",
        "Win-win-mentality"
        ]

        stage = [
            "Pre-Seed Phase",
            "Seed Stage",
            "Pre-Series A",
            "Series A",
            "Pre-Series B",
            "Series B",
            "Series C",
            "Bridge",
        ]

        expertice = [
            "Accounting / Bookkeeping",
            "Controlling",
            "Fundraising",
            "HR / Personnel",
            "Legal / Legal Affairs",
            "Logistics / Logistics",
            "Management",
            "Marketing",
            "PR",
            "Procurement / Purchasing",
            "Product Development",
            "Production",
            "Sales / Distribution",
            "Strategy",
            "Technology"
        ]

        type_of_investment =[
            "Equity",
            "Loan",
            "Convertible Loan"
        ]

        team_motives =[
        "extravagant",
        "Romantic",
        "Security",
        "activating",
        "Charming",
        "Clarity",
        "risk",
        "Friendly",
        "Functional",
        "daring",
        "Soft",
        "Diligent",
        "youthful",
        "Cosy",
        "Competence",
        "adventure",
        "Health",
        "Disciplined",
        "festive",
        "Gentle",
        "Powerful",
        "vivid",
        "Security",
        "Force",
        "joy",
        "Down to earth",
        "Superior",
        "indulgence",
        "Trust",
        "Status",
        "open-minded",
        "Reliable",
        "Exclusive",
        "Openness",
        "Traditional",
        "Responsibility"
        ]

        sdg_goals = {
            "SDG-1": "No Poverty",
            "SDG-2": "Zero Hunger",
            "SDG-3": "Good Health and Well-being",
            "SDG-4": "Quality Education",
            "SDG-5": "Gender Equality",
            "SDG-6": "Clean Water and Sanitation",
            "SDG-7": "Affordable and Clean Energy",
            "SDG-8": "Decent Work and Economic Growth",
            "SDG-9": "Industry, Innovation and Infrastructure",
            "SDG-10": "Reduced Inequalities",
            "SDG-11": "Sustainable Cities and Communities",
            "SDG-12": "Responsible Consumption and Production",
            "SDG-13": "Climate Action",
            "SDG-14": "Life Below Water",
            "SDG-15": "Life on Land",
            "SDG-16": "Peace, Justice and Strong Institutions",
            "SDG-17": "Partnerships for the Goals"
        }


        random.seed(120)
        investor_data =[]
        # initialize investor data 
        for i in range(len(names)):
            sdg_format  = random.sample(list(sdg_goals.keys()), k=8)
            investor_sample={
                'company_name': names[i],
                'location': 'San Francisco, CA',
                'industry': random.choice(industry),
                'type_of_business': random.choice(type_of_business),  # B2B or B2C
                'linkedin': 'https://linkedin.com/company/ecovenures',
                'twitter': 'https://twitter.com/ecovenures',
                'description': 'Investing in water saving technologies and businesses.',
                'mission': 'To alleviate global water scarcity through smart investments.',
                'capital': random.choice(range(100000, 1000000)),
                'stage': random.choices(stage, k =4),  # stage of the startup: Series A, Series B, Series C, Seed, Pre Seed, Bridge
                'impact_value': random.choice(range(5, 9)),
                'team_values': random.sample(team_values, k=4),
                'team_motives': random.sample(team_motives, k=6),
                'languages': random.sample(languages, k=3),
                'investor_expertise': random.sample(expertice, k=6),
                'investor_offering': ['Has a big network'],
                'investor_value': ['Sustainability', 'Long-term Gains'],
                'exit_strategy': 'IPO',
                'type_of_investment': random.choice(type_of_investment),
                'market': 'Global water conservation sector',
                'sdg': {sdg_format[0]: sdg_goals[sdg_format[0]], sdg_format[1]: sdg_goals[sdg_format[1]], sdg_format[2]: sdg_goals[sdg_format[2]],  
                        sdg_format[3]: sdg_goals[sdg_format[3]], sdg_format[4]: sdg_goals[sdg_format[4]], sdg_format[5]: sdg_goals[sdg_format[5]], 
                        sdg_format[6]: sdg_goals[sdg_format[6]],  sdg_format[7]: sdg_goals[sdg_format[7]]
                        }  # sdg must be in the sdg goals
            }
            investor_data.append(investor_sample)

        startups_data =[]

        # initialize startup data 
        for i in range(len(names)):
            sdg_format  = random.sample(list(sdg_goals.keys()), k=8)
            startup_sample ={
                "name": names[i],
                "code": "GI101",
                "location": "Austin, TX",
                "industry": random.choice(industry),
                "founding_date": "2023-04-15",
                "legal_form": "Corporation",
                "type_of_business":  random.choice(type_of_business),
                "website": "https://greeninnovate.com",
                "facebook": "https://facebook.com/greeninnovate",
                "linkedin": "https://linkedin.com/company/greeninnovate",
                "twitter": "https://twitter.com/greeninnovate",
                "description": "Pioneering renewable energy solutions.",
                "mission": "To empower sustainable living.",
                "product_description": "Solar panels and wind turbines.",
                "customer_problem": "Lack of affordable green energy options.",
                "usp": "Low-cost, high-efficiency solar solutions.",
                "capital": random.choice(range(5000, 100000)), 
                "stage": random.choice(stage),
                "target_investor_n": 4,
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30}, 
                "financial_tables": "Financial data here.",
                "already_invested_n": 3,
                "impact_value": random.choice(range(5, 9)),
                "team_values":  random.sample(team_values, k = 4 ),
                "team_motives": random.sample(team_motives, k = 4 ),
                "funding_experience": 'Yes',
                "team_languages": random.sample(languages, k = 3 ),
                "investor_expertise": random.sample(expertice, k = 6 ),
                "investor_expectations": ["has a big network"],
                "exit_strategy": "IPO",
                "type_of_investment": random.choice(type_of_investment),
                "market": "Global energy market.",
                "sdg": {sdg_format[0]: sdg_goals[sdg_format[0]], sdg_format[1]: sdg_goals[sdg_format[1]], sdg_format[2]: sdg_goals[sdg_format[2]],
                          sdg_format[3]: sdg_goals[sdg_format[3]], sdg_format[4]: sdg_goals[sdg_format[4]], sdg_format[5]: sdg_goals[sdg_format[5]], 
                          sdg_format[6]: sdg_goals[sdg_format[6]],  sdg_format[7]: sdg_goals[sdg_format[7]]
                          }, 
                }
            startups_data.append(startup_sample)

        #create Investor objects
        for i in range(len(names)):
            Investor.objects.create(
                        user = users[i],
                        **investor_data[i]
                    )
        
        # create startup objects
        for i in range(len(names)):
            Startup.objects.create(
                        user=users[i],
                        **startups_data[i]
                    )

            
        self.stdout.write(self.style.SUCCESS('Successfully created Data'))

