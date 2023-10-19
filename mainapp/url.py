from django.urls import path, include
from django.views.generic import TemplateView

from mainapp.urls import account, workstatus_review, workstatus_worker, assignment
from mainapp.views.workstatus_worker import server
from mainapp.views.first_page import test

app_name = "mainapp"

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="mainapp/first_page.html"), name="main"
    ),
    path("server/", server, name="server"),
]


urlpatterns += account.patterns
urlpatterns += workstatus_review.patterns
urlpatterns += workstatus_worker.patterns
urlpatterns += assignment.patterns
