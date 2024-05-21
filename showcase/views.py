from typing import Any
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import ProjectsData, ProfileData
from .forms import ContactFormForm


class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        profile = ProfileData.objects.first()
        context["profile"] = profile
        return context


class ProjectsListView(ListView):
    queryset = ProjectsData.objects.order_by("-updated_date")
    template_name = "projects_list.html"
    
    
class ProjectDetailView(DetailView):
    model = ProjectsData
    template_name = "project_detail.html"
    context_object_name = "project"
    
    
class ContactFormView(FormView):
    form_class = ContactFormForm
    template_name = "contact_form.html"