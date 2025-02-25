from django.contrib import admin
from .models import Tag, Project, ProjectImage
# Register your models here.

#Custom registration 
#-> Specify diffirent fields and how wz want to view these diffirent projects

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 
    

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","link") #review a list show as the title and the link
    inlines = [ProjectImageInline] #
    search_fields = ("title", "description") #We can search based on the title or the description It's tuple we can not modify it
    list_filter = ("tags",) # the coma to be treated as a table and it's for filtering different objects based on tags
    
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

#yaani fel admin najémou nethakmou fel project mta3nna fel admin pannel o yaatina qques fonction de filtrage et de recherche