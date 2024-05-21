from django.contrib import admin
from .models import ProjectsData, ProfileData, ContactForm


class ProfileDataAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "updated_date")
    readonly_fields = ("created_date", "updated_date")
    

class ProjectsDataAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "updated_date")
    readonly_fields = ("created_date", "updated_date")
    list_filter = ("created_date", "updated_date")
    sortable_by = ("title", "created_date", "updated_date")
    
    
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "timestamp", "email_sent",
                    "email_received")
    readonly_fields = ("name", "email", "subject", "message", "timestamp",
                       "email_sent", "email_received")
    list_filter = ("subject", "email", "email_sent", "email_received")
    sortable_by = ("created_date", "updated_date", "email_sent", "email_received")
    
admin.site.register(ProfileData, ProfileDataAdmin)
admin.site.register(ProjectsData, ProjectsDataAdmin)
admin.site.register(ContactForm, ContactFormAdmin)