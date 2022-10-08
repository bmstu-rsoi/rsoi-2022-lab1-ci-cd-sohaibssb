from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('persons',views.person_LIST,name='person_LIST'),
    path('persons/<int:id>',views.person_detail,name='person_detail'),
]
urlpatterns=format_suffix_patterns(urlpatterns)