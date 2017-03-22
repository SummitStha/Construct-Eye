from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (ReportFormView, ProjectDetailView, ProjectListView, 
	home, ReportedProjectListView, ReportedProjectDetailView, 
	projectList, reportedprojectList, documentList,
	BidFormView, upcomingprojectList,)


urlpatterns=[
url(r'^$', home, name='home'),
url(r'^report-form/$', ReportFormView.as_view(), name='report-form'),
url(r'^bid-form/(?P<pk>\d+)$', BidFormView.as_view(), name='bid-form'),

url(r'^detail/project/(?P<pk>\d+)$', ProjectDetailView.as_view(), name='detail-project'),
url(r'^list/project/$', ProjectListView.as_view(), name='list-project'),
url(r'^list/reported-projects/$', ReportedProjectListView.as_view(), name='reported-list-project'),
url(r'^detail/reported-project/(?P<pk>\d+)$', ReportedProjectDetailView.as_view(), name='reported-detail-project'),
url(r'^project-list/$', projectList, name='project_list'),
url(r'^upcoming-project-list/$', upcomingprojectList, name='upcoming_project_list'),

url(r'^reported-project-list/$', reportedprojectList, name='reported_project_list'),
url(r'^document-list/$', documentList, name='document_list'),
url(r'^map/$',TemplateView.as_view(template_name="main_map/map.html"),
                   name='map'),

]
