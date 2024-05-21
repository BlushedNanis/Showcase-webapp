from django.urls import path
from .views import ProjectsListView, HomePageView, ProjectDetailView, ContactFormView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("projects/", ProjectsListView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("contact/", ContactFormView.as_view(), name="contact"),
]