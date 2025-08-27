from django.urls import path
from . import views

app_name = "main_core"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:category_slug>/", views.category_list, name="category_list"),
    path("article/<slug:slug>/", views.article_detail, name="article_detail"),  # ✅ slug統一
    path("search/", views.search_articles, name="search_articles"),

    path('article/<slug:slug>/comment/', views.add_comment, name='add_comment'),

    # ✅ لينك توليد مقال بالذكاء الاصطناعي
    path("category/<slug:category_slug>/generate/", views.generate_ai_article, name="generate_ai_article"),

    # ✅ توليد مقال كامل (العنوان + المحتوى) تلقائي من AI
    path("category/<slug:category_slug>/auto_generate/", views.auto_generate_ai_article, name="auto_generate_ai_article"),
]