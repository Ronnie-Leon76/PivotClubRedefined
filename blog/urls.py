from django.urls import path

from blog import views

urlpatterns = [
    path("create/", views.ArticleCreateView.as_view(), name="article-create"),
    path("", views.ArticleListView.as_view(), name="blog"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("genre/<str:genre>/", views.ArticleGenreView.as_view(), name="genre"),
    path("<slug:slug>/", views.ArticleUpdateView.as_view(), name="article-update"),
    path("<slug:slug>/", views.ArticleDeleteView.as_view(), name="article-update"),
]
