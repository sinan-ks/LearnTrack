from django.urls import path

from StudentHub import views

urlpatterns = [
    
    path("", views.Home.as_view(), name="home"),

    path("category/add/", views.CatFormView.as_view(), name="category-add"),

    path("student/add/", views.StuFormView.as_view(), name="student-add"),

    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student-detail"),

    path("student/<int:pk>/remove/", views.StudentDeleteView.as_view(), name="student-delete"),

    path("student/<int:pk>/update/", views.StudentUpdateView.as_view(), name="student-edit"),

    path('category/all/', views.CategoryListView.as_view(), name='category-list'),

    path('category/<int:pk>/update/', views.CategoryEditView.as_view(), name='category-edit'),

    path('category/<int:pk>/remove/', views.CategoryDeleteView.as_view(), name='category-delete')

]