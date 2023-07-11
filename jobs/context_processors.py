from job_portal.settings import MEDIA_URL
from jobs.models import Category


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories, 'MEDIA_URL': MEDIA_URL}
