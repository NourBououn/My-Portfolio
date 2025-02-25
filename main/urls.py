from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("skills/", views.skills, name="skills"),
    path("about_me/", views.about_me, name="about_me"),
    path("project/<int:id>/", views.project, name="project"),
    path('recent-projects/', views.recent_projects, name='recent_projects')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)