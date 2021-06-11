from django.urls import path

from blog import views

urlpatterns = [
    path("create/", views.ArticleCreateView.as_view(), name="article-create"),
    path("", views.ArticleListView.as_view(), name="blog"),
    path("<int:pk>", views.ArticleDetailView.as_view(), name="article-detail"),
    path("<int:pk>", views.ArticleUpdateView.as_view(), name="article-update"),
    path("<int:pk>", views.ArticleDeleteView.as_view(), name="article-update"),
]
