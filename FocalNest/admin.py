from django.contrib import admin
from .models import BlogPost, ServicePost, Gallery, GalleryImage, Enquiry

class BlogPostAdmin(admin.ModelAdmin):  
    prepopulated_fields = {'Title_url': ('Blog_title',)}
    change_list_template = 'admin/blog-admin.html'

class ServicePostAdmin(admin.ModelAdmin):  
    prepopulated_fields = {'Title_Url': ('title',)}
    change_list_template = 'admin/service-admin.html'
    
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryAdmin(admin.ModelAdmin): 
    actions = None
    list_display = ('Gallery_Title', 'service')
    search_fields = ['Gallery_Title']
    list_filter = ['service']
    inlines = [GalleryImageInline]

    def has_add_permission(self, request, obj=None):
        return False

class EnquiryAdmin(admin.ModelAdmin): 
    change_list_template = 'admin/enquiry-admin.html'

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ServicePost, ServicePostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
