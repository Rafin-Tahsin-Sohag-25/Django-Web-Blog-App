from django.contrib import admin
from. models import About,SocialPlatform
class aboutAdmin(admin.ModelAdmin):
   list_display=('about_heading','about_description','created_at','updated_at')
   def has_add_permission(self, request):
      count=About.objects.all().count()
      if count==0:
         return True
      else:
         return False
admin.site.register(About,aboutAdmin)
admin.site.register(SocialPlatform)