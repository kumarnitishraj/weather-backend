from django.contrib import admin
from .models import Weather,WeatherCreate
from django.contrib.auth.models import Group
# Register your models here.


#---------- Video Admin model ----------------------
class WeatherModelAdmin(admin.ModelAdmin):
	list_display = ["day_name","weather"]
	list_display_links = ["day_name"]
	search_fields = ["day_name"]

	class Meta:
		model=Weather

class WeatherCreateAdmin(admin.ModelAdmin):
	list_display = ["day_name","weather"]
	list_display_links = ["day_name"]
	search_fields = ["day_name"]

	class Meta:
		model=WeatherCreate


admin.site.unregister(Group)
admin.site.register(Weather, WeatherModelAdmin)
admin.site.register(WeatherCreate, WeatherCreateAdmin)
