# portfolio/admin.py

from django.contrib import admin
from .models import Project, Contact, Skill, Experience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_date']
    list_filter = ['category', 'is_featured', 'created_date']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'duration', 'order']
    list_editable = ['order']
    search_fields = ['title', 'company']