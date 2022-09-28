from django.contrib import admin

from .models import External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak

admin.site.register(External_conflict)
admin.site.register(Internal_conflict)
admin.site.register(External_conflict_side)
admin.site.register(Agricultural_population)
admin.site.register(Arable_land)
admin.site.register(Arable_land_per_farmer)
admin.site.register(Gross_grain_shared_per_agricultural_population)
admin.site.register(Net_grain_shared_per_agricultural_population)
admin.site.register(Surplus)
admin.site.register(Military_expense)
admin.site.register(Silver_inflow)
admin.site.register(Silver_stock)
admin.site.register(Total_population)
admin.site.register(Gdp_per_capita)
admin.site.register(Drought_event)
admin.site.register(Locust_event)
admin.site.register(Socioeconomic_turmoil_event)
admin.site.register(Crop_failure_event)
admin.site.register(Famine_event)
admin.site.register(Disease_outbreak)
