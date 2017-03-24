from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ReportForm
from .bid_form import BidForm
from .models import (Project, Report, ProjectTable, 
	ReportedProjectTable, DocumentTable, UpcomingProject, 
	Bidding, UpcomingProjectTable)
from django_tables2 import RequestConfig



class ReportFormView(FormView):
	form_class = ReportForm
	# model = Contact
	initial = {'key': 'value'}
	template_name = 'report_form.html'
	success_url = '/thanks/'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, self.template_name, {'form': form})

class BidFormView(FormView):
	form_class = BidForm
	# model = Contact
	initial = {'key': 'value'}
	template_name = 'bid_form.html'
	success_url = '/thanks/'

	def get(self, request, *args, **kwargs):
		self.initial['project_name'] = UpcomingProject.objects.get(pk=kwargs.get('pk'))
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, self.template_name, {'form': form})

class ProjectDetailView(DetailView):
	model = Project
	template_name = 'inner.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		return context


class ProjectListView(ListView):
	model = Project
	template_name = 'project_list.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		return context


def home(request):
	template_name = 'index.html'
	return render(request, template_name, {})

class ReportedProjectListView(ListView):
	model = Report
	template_name = 'reported_project_list.html'

	def get_context_data(self, **kwargs):
		context = super(ReportedProjectListView, self).get_context_data(**kwargs)
		return context

class ReportedProjectDetailView(DetailView):
	model = Report
	template_name = 'template.html'
	context_object_name = 'project_name'

	def get_context_data(self, **kwargs):
	    context = {}
	    if self.object:
	        context['object'] = self.object
	        context_object_name = self.get_context_object_name(self.object)
	        if context_object_name:
	            context[context_object_name] = self.object
	    context.update(kwargs)
	    return super(ReportedProjectDetailView, self).get_context_data(**context)


def projectList(request):
	projects=Project.objects.all()
	table=ProjectTable(projects)
	RequestConfig(request).configure(table)
	template_name='project_lists.html'
	return render(request, template_name,{'table':table})

def reportedprojectList(request):
	reported_projects=Report.objects.all()
	table=ReportedProjectTable(reported_projects)
	RequestConfig(request).configure(table)
	template_name='reported_project_lists.html'
	return render(request, template_name,{'table':table})

def documentList(request):
	documents=Project.objects.all()
	table=DocumentTable(documents)
	RequestConfig(request).configure(table)
	template_name='documents.html'
	return render(request, template_name,{'table':table})

def upcomingprojectList(request):
	upcoming_projects=UpcomingProject.objects.all()
	table=UpcomingProjectTable(upcoming_projects)
	RequestConfig(request).configure(table)
	template_name='upcoming_project_lists.html'
	return render(request, template_name,{'table':table})