# portfolio/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience
from .forms import ContactForm

def index(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    skills = Skill.objects.all()[:6]
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'index.html', context)

def about(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    context = {
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'about.html', context)

def projects(request):
    all_projects = Project.objects.all()
    recent_projects = Project.objects.all()[:6]
    categories = Project.CATEGORY_CHOICES
    
    # Filter by category if requested
    category = request.GET.get('category')
    if category:
        all_projects = all_projects.filter(category=category)
    
    context = {
        'all_projects': all_projects,
        'recent_projects': recent_projects,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'projects.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email
            try:
                send_mail(
                    f"Portfolio Contact: {contact.subject}",
                    f"From: {contact.name} ({contact.email})\n\nMessage:\n{contact.message}",
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except:
                messages.warning(request, 'Message saved but email could not be sent.')
            
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})