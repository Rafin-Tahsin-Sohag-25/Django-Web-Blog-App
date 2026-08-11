from .models import Category
from linkMedia.models import SocialPlatform

def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_social_link(request):
    social_link=SocialPlatform.objects.all()
    return dict(social_link=social_link)