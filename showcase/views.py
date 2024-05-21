from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import ProjectsData


class ProjectsList(ListView):
    model = ProjectsData
    template_name = "projects_list.html"
    context_object_name = "projects"