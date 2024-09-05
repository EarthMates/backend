""" from django.urls import path
from .views import StartupCreate, StartupDelete, InvestorCreate, InvestorDelete
from . import views

urlpatterns = [
    path('startup/', StartupCreate.as_view(), name='startup-list-create'),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('', views.getRoutes),
    path('startup/delete/<int:pk>/', StartupDelete.as_view(), name='startup-retrieve-update-destroy'),
    path('investor/', InvestorCreate.as_view(), name='startup-list-create'),
    path('investor/delete/<int:pk>/', InvestorDelete.as_view(), name='startup-retrieve-update-destroy'),
] """

from django.urls import path
from .views import (
    StartupRetrieveUpdateView,
    StartupCreateView,
    StartupDetailsView,
    StartupOfferingView,
    StartupFinancialsView,
    StartupImpactView,
    StartupTeamView,
    StartupMarketView,
    StartupPreferencesView,
    StartupRetrieveByNameView,
    StartupCoverUploadView
)

from .views import (
    InvestorRetrieveUpdateView,
    InvestorCreateView,
    InvestorDetailsView,
    InvestorPreferencesView,
    InvestorPortfolioView,
    InvestorRetrieveByNameView,
    InvestorCoverUploadView
)

urlpatterns = [
    path('startup/', StartupRetrieveUpdateView.as_view(), name='get_update_startup'),
    path('startup/create/', StartupCreateView.as_view(), name='create_startup'),
    path('startup/upload-cover/', StartupCoverUploadView.as_view(), name='startup-upload-cover'),
    path('startup/details/', StartupDetailsView.as_view(), name='get_update_startup_details'),
    path('startup/offerings/', StartupOfferingView.as_view(), name='get_update_startup_offerings'),
    path('startup/financials/', StartupFinancialsView.as_view(), name='get_update_startup_financials'),
    path('startup/impact/', StartupImpactView.as_view(), name='get_update_startup_impact'),
    path('startup/team/', StartupTeamView.as_view(), name='get_update_startup_team'),
    path('startup/market/', StartupMarketView.as_view(), name='get_update_startup_market'),
    path('startup/preferences/', StartupPreferencesView.as_view(), name='get_update_startup_preferences'),
    path('startup/get-by-name/', StartupRetrieveByNameView.as_view(), name='get_startup_by_name'),
    path('investor/', InvestorRetrieveUpdateView.as_view(), name='get_update_investor'),
    path('investor/create/', InvestorCreateView.as_view(), name='create_investor'),
    path('investor/upload-cover/', InvestorCoverUploadView.as_view(), name='investor-upload-cover'),
    path('investor/details/', InvestorDetailsView.as_view(), name='get_update_investor_details'),
    path('investor/preferences/', InvestorPreferencesView.as_view(), name='get_update_investor_preferences'),
    path('investor/portfolio/', InvestorPortfolioView.as_view(), name='get_update_investor_portfolio'),
    path('investor/get-by-name/', InvestorRetrieveByNameView.as_view(), name='get_investor_by_name'),
]



