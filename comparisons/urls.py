from django.urls import path
from comparisons import views

urlpatterns = [
    path('', views.ComparisonList.as_view()),
    path('<int:pk>/', views.ComparisonDetail.as_view()),
]
