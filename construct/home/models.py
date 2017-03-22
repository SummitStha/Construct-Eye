from __future__ import unicode_literals

from django.db import models
import django_tables2 as tables

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	location = models.CharField(max_length=30)
	tender_contract = models.CharField(max_length=50)
	start_date = models.DateTimeField(auto_now_add=True)
	completion_date = models.DateField()
	budget = models.CharField(max_length=150)
	media = models.ImageField(upload_to = 'Photos', blank = True)
	documents = models.FileField(upload_to = 'Documents', blank = True)
	status = models.CharField(max_length=15)

	def __str__(self):
		return self.name

class UpcomingProject(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	location = models.CharField(max_length=30)
	bid_start_date = models.DateTimeField(auto_now_add=True)
	bid_end_date = models.DateField()
	estimated_budget = models.CharField(max_length=150)
	media = models.ImageField(upload_to = 'Photos', blank = True)
	documents = models.FileField(upload_to = 'Documents', blank = True)
	publish = models.BooleanField(default = False)

	def __str__(self):
		return self.name



class Report(models.Model):
	project_name = models.ForeignKey(Project, on_delete = models.CASCADE)
	complaint = models.TextField()
	image = models.ImageField(upload_to = 'Report_Images', blank = True)
	publish = models.BooleanField(default = False)

	def __str__(self):
		report = 'Report Description{}'.format(self.complaint)
		return report[:20]

class Bidding(models.Model):
	project_name = models.ForeignKey(UpcomingProject, on_delete = models.PROTECT)
	bidder_name = models.CharField(max_length=30)
	company_name = models.CharField(max_length=30)
	bidder_location = models.CharField(max_length=30)
	bidder_email = models.EmailField(blank = True)
	bidder_contact = models.CharField(max_length=15)
	bidder_job = models.CharField(max_length=30, blank = True)
	projects_involved = models.IntegerField()
	bid_amount = models.CharField(max_length=100)
	estimted_completion_date = models.DateField()
	media = models.ImageField(upload_to = 'Photos', blank = True)
	documents = models.FileField(upload_to = 'Documents', blank = True)

	def __str__(self):
		return self.company_name


class UpcomingProjectTable(tables.Table):
	bidding = tables.TemplateColumn('<a href = "{% url \'bid-form\' record.id %}"><input type = "button" value="Bid.."></a>')
	class Meta:
		model = UpcomingProject
		exclude = ('description','media','publish' )
		#fields = ('name', 'location', 'status')
class ProjectTable(tables.Table):
	view_more = tables.TemplateColumn('<a href = "{% url \'detail-project\' record.id %}">Show Details..</a>')
	class Meta:
		model=Project
		exclude = ('description', )


class ReportedProjectTable(tables.Table):
	view_more = tables.TemplateColumn('<a href = "{% url \'reported-detail-project\' record.id %}">Show Details..</a>')
	class Meta:
		model=Report
		fields = ('project_name', )

class DocumentTable(tables.Table):
	class Meta:
		model=Project
		fields = ('name', 'tender_contract', 'documents', )