from django.db import models

# Create your models here.

# Startup model:
# - name
# - stage
# - industry
# - location
# - capital required

# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]
# - 10000 <= capital required <= 100 M


# Investor model:
# - name
# - stage
# - industry
# - location

# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]