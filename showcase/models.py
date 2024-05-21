from django.db import models


class ProjectsData(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="showcase\\static\\images\\")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def short_description(self):
        first_words = self.description.split()[:10]
        short_description = " ".join(first_words)
        return short_description
    
    def img_static_path(self):
        return self.image[23:]
    
    def __str__(self) -> str:
        return self.title