from django.contrib import admin
from .models import Landing_Page

class Landing_Page_Admin(admin.ModelAdmin):
	pass


admin.site.register(Landing_Page, Landing_Page_Admin)
