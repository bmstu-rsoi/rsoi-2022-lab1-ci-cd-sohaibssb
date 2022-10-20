from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('persons',views.person_LIST,name='person_LIST'),
    path('persons',views.person_Post,name='person_Post'),
    path('persons/<int:id>',views.person_detail,name='person_detail'),
    path('persons/<int:id>',views.person_update,name='person_update'),
    path('persons/<int:id>',views.person_remove,name='person_remove'),
]
urlpatterns=format_suffix_patterns(urlpatterns)
