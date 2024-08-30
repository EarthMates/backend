# for the testing of the alghorithm:
# python3 manage.py shell
# copy all the code of this file and paste it into the shell
# actually using this file for testing: initialize_startups.py, initialize_investors .py
from matcher.models import Matching
from api.models import Startup, Investor
from django.core.management.base import BaseCommand
from users.models import CustomUser

# investitori filtrati su industria,type of busines stage e type of investement

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        investors = list(Investor.objects.all())
        matches =[]
        i = 0
        for investor in investors:
            # print(f'\n-----------Investor n.{i}-----------\n')
            # filtri su: 'industry', 'type_of_business', 'type_of_investment'
            startup_filt = list(Startup.objects.filter(industry = investor.industry, type_of_business= investor.type_of_business, type_of_investment=investor.type_of_investment))
            if len(startup_filt) == 0:
                # print(f'(0) - Initial filters not passed:\n. Investor: {investor}\n. Startups: {startup_filt}\n')
                i +=1
                continue
            i +=1
            # print(f'\n-FIRSTI FILTER-: {startup_filt}\n')
            for startup in startup_filt:
                sdg_stp = set(startup.sdg.values())
                sdg_inv = set(investor.sdg.values())
                common_sdg = sdg_stp.intersection(sdg_inv)
                # filtro sdg
                if len(common_sdg) == 0:
                    # print(f'(1) - sdg filter not passed:\n. Investor: {investor}, {sdg_inv}\n. Startup: {startup}, {sdg_stp}\n')
                    continue
                # filtro impact_value
                if not investor.impact_value <= startup.impact_value +1 or not investor.impact_value >= startup.impact_value -1:
                    # print(f'(2) - impact value filter not passed:\n. Investor: {investor}, {investor.impact_value}\n. Startup: {startup}, { startup.impact_value}\n')
                    continue
                lan_inv = set(investor.languages)
                lan_stp = set(startup.team_languages)
                common_languages = lan_inv.intersection(lan_stp)
                # filtro capital
                if  startup.capital >= investor.capital:
                    # print(f'(3) - capital filter not passed:\n. Investor: {investor}, {investor.capital} \n. Startup: {startup} {startup.capital}\n')
                    continue
                # filtro lingue
                if len(common_languages) == 0:
                    # print(f'(4) - languages filter not passed:\n. Investor: {investor}, {lan_inv}\n. Startup: {startup}, {lan_stp}\n')
                    continue
                values_stp = set(startup.team_values)
                values_inv = set(investor.team_values)
                common_values = values_stp.intersection(values_inv)
                stage_stp = startup.stage
                stage_inv = investor.stage
                #filtro stage
                if stage_stp not in stage_inv:
                    # print(f'(5) - stage filter not passed:\n. Investor: {investor}, {stage_inv} \n. Startup: {startup}, {stage_stp}\n')
                    continue
                # filtro team_values
                if len(common_values) == 0:
                    # print(f'(6) - common values filter not passed:\n. Investor: {investor}, {values_inv}\n. Startup: {startup}, {values_stp}\n')
                    continue
                else:
                    print(f'-(MATCH)-\n. Investor: {investor} industry:{investor.industry} type_of_business:{investor.type_of_business}\n. Startup: {startup} industry:{startup.industry} type_of_business:{startup.type_of_business}\n\n')
                    score = 50
                    # team values filter
                    if len(common_values) >= 3:
                        score += 10
                    if startup.financial_tables:
                        score += 5
                    motives_stp = set(startup.team_motives)
                    motive_inv = set(investor.team_motives)
                    common_motives = motives_stp.intersection(motive_inv)
                    #team_motives filter
                    if len(common_motives) > 0:
                        score += 10
                    expertice_stp = set(startup.investor_expertise)
                    expertice_inv = set(investor.investor_expertise)
                    common_expertice = expertice_stp.intersection(expertice_inv)
                    #expertice filter
                    if len(common_expertice) > 0:
                        score += 5
                        if len(common_expertice)>3:
                            score +=5
                    founds_use_stp = set(startup.use_of_funds.keys())
                    use_founds_intersect=expertice_inv.intersection(founds_use_stp)
                    #use of found filter
                    if len(use_founds_intersect) > 0:
                        score += 5
                    # stp_user = CustomUser.objects.get(email=startup.user.email).pk
                    # inv_user = CustomUser.objects.get(email=investor.user.email).pk
                    matches.append((startup.user, startup.name, investor.user , investor.company_name, score))
        print(f'\n.------MATCHES------.\n\n {matches}')
        for match in matches:
            Matching.objects.create(startup_user = match[0], startup_name = match[1], investor_name = match[3],investor_user = match[2], match_score= match[4])
        print('--------------------------------')
        print(Matching.objects.all())

        self.stdout.write(self.style.SUCCESS('Test succesfully completed!'))
        

# -(MATCH)-
# . Investor: sales@bioGrid.org
# . Startup: info@astroVibes.com
# [(<CustomUser: admin@mail.com>, <CustomUser: admin@mail.com>, 70), (<CustomUser: connect@aquaminds.co>, <CustomUser: team@ecotech.co>, 60), (<CustomUser: connect@econet.co>, <CustomUser: info@quantumleap.io>, 60), (<CustomUser: info@futureleap.com>, <CustomUser: info@astrovibes.com>, 70), (<CustomUser: support@quantumtech.org>, <CustomUser: admin@stellargrid.io>, 70), (<CustomUser: services@quantumnet.com>, <CustomUser: hello@biosphere.org>, 60), (<CustomUser: inquiries@astronet.net>, <CustomUser: team@ecopulse.net>, 80), (<CustomUser: support@stellarpulse.org>, <CustomUser: sales@stellargrid.org>, 70), (<CustomUser: connect@cosmicnet.co>, <CustomUser: support@stellarpulse.org>, 75), (<CustomUser: connect@nebulaminds.co>, <CustomUser: team@quantumwave.co>, 60)]