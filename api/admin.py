from django.contrib import admin
from .models import Startup, Investor, InvestorPortfolio, InvestorPreferences
from .models import Startup, StartupDetails, StartupOffering, StartupFinancials, StartupImpact, StartupTeam, StartupMarket, StartupMatchingPreferences

admin.site.register(Startup)
admin.site.register(StartupDetails)
admin.site.register(StartupOffering)
admin.site.register(StartupFinancials)
admin.site.register(StartupImpact)
admin.site.register(StartupTeam)
admin.site.register(StartupMarket)
admin.site.register(StartupMatchingPreferences)
admin.site.register(Investor)
admin.site.register(InvestorPreferences)
admin.site.register(InvestorPortfolio)