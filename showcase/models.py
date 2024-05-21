from django.db import models


class ProjectsData(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="showcase\\static\\images\\")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def short_description(self):
        first_words = self.description.split()[:20]
        short_description = " ".join(first_words)
        return short_description
    
    def img_static_path(self):
        return self.image.url[16:]
    
    def __str__(self) -> str:
        return self.title
    
    
class ProfileData(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=200)
    extra1 = models.TextField(null=True, blank=True)
    extra2 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="showcase\\static\\profile\\")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def img_static_path(self):
        return self.image.url[16:]
    
    def split_extra1_by_slash(self):
        splitted_extra = self.extra1.split("/")
        cleaned_extra = [item.strip() for item in splitted_extra]
        return cleaned_extra
    
    def split_extra2_by_slash(self):
        splitted_extra = self.extra2.split("/")
        cleaned_extra = [item.strip() for item in splitted_extra]
        return cleaned_extra
    
    def __str__(self) -> str:
        return self.name
    
    
class ContactForm(models.Model):
    SUBJECT_CHOICES = [
        ('career_opportunity', 'Career Opportunity'),
        ('collaboration_interest', 'Collaboration Interest'),
        ('technical_inquiry', 'Technical Inquiry'),
        ('general_comment', 'General Comment'),
        ('feedback', 'Feedback'),
        ('suggestions', 'Suggestions'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)
    email_received = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.subject} from {self.name}"
    