from django.urls import path
from .views import ShowDetail, EndedShowList, AnimalList, AnimalDetail

urlpatterns = [
    path('show/<slug:slug>/', ShowDetail.as_view(), name='show'),
    path('ended_show/', EndedShowList.as_view(), name='ended_show'),
    path('animals/', AnimalList.as_view(), name='animals_list'),
    path('animals/<slug:slug>/', AnimalDetail.as_view(), name='animals'),
]