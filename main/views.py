from django.shortcuts import render
from .models import Project, Tag, ProjectImage
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import CVUploadForm
from django.conf import settings
import os

# Create your views here.
#display a page we need to create a view witch is a function
#called when we go to a specific route like /project or smthng

def home(request):
    projects = Project.objects.all().order_by('-created_at') #Access to all the projects
    tags = Tag.objects.all()
    #we add a dictionary value : key that we can pass into the template so we can use to render different dynammic data
    return render(request, "home.html", {"projects" : projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

def skills(request):
    return render(request, "skills.html")

def about_me(request):
    if request.method == 'POST' and request.FILES['cv']:
        cv = request.FILES['cv']
        # You can save the file if you want to store it on the server
        file_path = os.path.join(settings.MEDIA_ROOT, 'cvs', cv.name)

        with open(file_path, 'wb') as f:
            for chunk in cv.chunks():
                f.write(chunk)
        return HttpResponse("CV uploaded successfully")

    form = CVUploadForm()
    return render(request, 'about_me.html', {'form': form})
   

def project(request, id): #we added the id of the project
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html",{"project" : project})

def recent_projects(request):
    # Fetch recent projects from the database
    recent_projects = Project.objects.order_by('-created_at')[:3]  # Modify as needed to get the most recent ones

    return render(request, 'recent_projects.html', {'recent_projects': recent_projects})

def project_detail(request, id):  # Use id or slug depending on your URL pattern
    project = get_object_or_404(Project, id=id)  # Or use slug=slug if you're using slugs
    return render(request, 'project_detail.html', {'project': project})