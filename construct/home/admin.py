from django.contrib import admin

# Register your models here.
from .models import Project, Report, UpcomingProject, Bidding
admin.site.register(Project)
admin.site.register(Report)
admin.site.register(UpcomingProject)
admin.site.register(Bidding)
