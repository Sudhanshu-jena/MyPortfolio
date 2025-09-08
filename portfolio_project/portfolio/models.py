# portfolio/models.py

from django.db import models
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('data', 'Data Engineering'),
        ('App', 'Android App'),
        ('api', 'API Development'),
        ('automation', 'Automation'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=500)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=80)  # Percentage
    category = models.CharField(max_length=50)  # Backend, Frontend, Data, etc.
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} at {self.company}"