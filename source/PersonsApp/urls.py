from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('persons',views.listPersons,name='listPersons'),
    path('persons/<int:id>',views.aSpecificPersons,name='aSpecificPersons'),
]
urlpatterns=format_suffix_patterns(urlpatterns)
