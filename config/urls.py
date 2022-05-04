from django.contrib import admin
from django.urls import path, include
#from polls import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    #path('polls/<int:question_id>/', views.detail, name='detail'),
    #path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    #path('polls/<int:question_id>/results/', views.results, name='results'),
]
