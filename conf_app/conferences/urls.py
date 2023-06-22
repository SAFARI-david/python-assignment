from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="hmoe")
    # path('conferences/', views.ConferenceList.as_view(), name='conference-list'),
    # path('conferences/create/', views.ConferenceCreate.as_view(), name='conference-create'),
    # path('conferences/<int:pk>/', views.ConferenceDetail.as_view(), name='conference-detail'),
    # path('conferences/<int:pk>/update/', views.ConferenceUpdate.as_view(), name='conference-update'),
    # path('conferences/<int:pk>/delete/', views.ConferenceDelete.as_view(), name='conference-delete'),
]
