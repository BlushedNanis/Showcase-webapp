from typing import Any
from django.core.mail import EmailMessage
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from .models import ProjectsData, ProfileData, ContactForm
from .forms import ContactFormForm
from dotenv import load_dotenv
from os import getenv

load_dotenv()


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
    success_url = reverse_lazy('success')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["subjects"] = ContactForm.SUBJECT_CHOICES
        return context
    
    def form_valid(self, form):
        form_submission = form.save(commit=False)
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        
        form_submission.name = name
        form_submission.email = email
        form_submission.subject = subject
        form_submission.message = message
        
        message_sent = f"""Thank you for your submission, {name}
            
I will get in touch with you as soon as possible.

Please, don't respond to this e-mail since I only use it for automation purposes.
            
Best regards, John Smith"""

        message_receive = f"""You have a new form submission!, {subject}
            
A user sent you a contact form:

-Name: {name}
-Email: {email}
-Subject: {subject}
-Message: {message}
            
From myself to myself, have a great day!"""

        try:
            email_message_user = EmailMessage(subject="Form submission confirmation",
                                         body=message_sent, to=[email])
            email_message_user.send(fail_silently=False)
            form_submission.email_sent = True
        except Exception:
            form_submission.email_sent = False
            
        try:
            email_message_me = EmailMessage(subject="Form submission confirmation",
                                         body=message_receive, to=[getenv('email')])
            email_message_me.send(fail_silently=False)
            form_submission.email_received = True
        except Exception:
            form_submission.email_received = False
            
        form_submission.save()
        
        return super().form_valid(form)
    
    
class SuccessView(TemplateView):
    template_name = "success.html"