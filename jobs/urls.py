from django.urls import path
from jobs import views

urlpatterns = [
    # 127.0.0.1:8000/jobs
    path('', views.show_jobs, name='jobs'),
    # 127.0.0.1:8000/jobs/single/1
    path('single/<jid>', views.show_single_job, name='single_job'),
    # 127.0.0.1:8000/jobs/search
    path('search', views.show_job_by_search, name='searched_jobs'),
    # 127.0.0.1:8000/jobs/1
    path('<category>', views.show_job_by_category, name='job_by_category'),

]
