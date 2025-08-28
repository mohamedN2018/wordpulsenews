from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsCategory, NewsArticle, Comment, FlickrPhoto
from .forms import CommentForm
from django.db.models import Q
from django.http import HttpResponse
from django.utils.text import slugify
from .ai_service import generate_article_content, generate_article_image
from django.core.files.base import ContentFile
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contact.models import SocialMediaIcon, InformationContact
from django.conf import settings
import requests

def home(request, category_slug=None):
    photos = FlickrPhoto.objects.all().order_by('-created_at')[:12]  # آخر 6 صور
    breaking_news = NewsArticle.objects.filter(is_breaking=True).order_by('-created_at')[:5]  # آخر 5 أخبار عاجلة
    popular_articles = NewsArticle.objects.order_by('-views')[:6]
    # جلب أحدث المقالات مع التأكد من وجود slug
    latest_articles = NewsArticle.objects.exclude(slug='').order_by('-id')[:9]

    # Main News Slider Start
    latest_articles_slider = NewsArticle.objects.order_by('-created_at')[:5]
    main_featured_slider = NewsArticle.objects.filter(is_featured=True).order_by('-created_at')[:5]
    trending_news_main = NewsArticle.objects.filter(is_trending=True).order_by('-created_at')[:4]

    # TRENDING NEWS
    trending_news = NewsArticle.objects.filter(is_trending=True).order_by('-created_at')[:5]

    # جلب كل التصنيفات
    categories = NewsCategory.objects.all()
    # جلب معلومات الاتصال
    information = InformationContact.objects.first()
    icon = SocialMediaIcon.objects.all()

    # YouTube API
    api_key = settings.YOUTUBE_API_KEY
    channel_id = "UCPP15i6IPmPFS8Il7aIP5Sw"  # حط ID القناة بتاعتك
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
    response = requests.get(url).json()
 # التحقق من وجود البيانات
    subscribers = 0
    if "items" in response and len(response["items"]) > 0:
        subscribers = response["items"][0]["statistics"].get("subscriberCount", 0)
    else:
        print("Error fetching YouTube data:", response)  # مفيد للتصحيح

    context = {
            "categories": categories,
        "latest_articles": latest_articles,
        "popular_articles": popular_articles,
        "breaking_news": breaking_news,
        "photos": photos,
        "information": information,
        "icon": icon,
        "youtube_subscribers": subscribers,
        "main_featured_slider": main_featured_slider,
        "trending_news": trending_news,
        "latest_articles_slider": latest_articles_slider,
        "trending_news_main": trending_news_main,

    }

    return render(request, "home.html", context)



def category_list(request, category_slug):
    breaking_news = NewsArticle.objects.filter(is_breaking=True).order_by('-created_at')[:5]  # آخر 5 أخبار عاجلة
    popular_articles = NewsArticle.objects.order_by('-views')[:6]
    # جلب التصنيف أو 404 لو مش موجود
    category = get_object_or_404(NewsCategory, slug=category_slug)
    photos = FlickrPhoto.objects.all().order_by('-created_at')[:12]  # آخر 12 صورة
    # جلب المقالات الخاصة بالتصنيف
    articles = NewsArticle.objects.filter(category=category).order_by('-id')
    information = InformationContact.objects.first()
    icon = SocialMediaIcon.objects.all()
 
    # جلب كل التصنيفات للـ navbar
    categories = NewsCategory.objects.all()



    # YouTube API
    api_key = settings.YOUTUBE_API_KEY
    channel_id = "UCPP15i6IPmPFS8Il7aIP5Sw"  # حط ID القناة بتاعتك
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
    response = requests.get(url).json()
 # التحقق من وجود البيانات
    subscribers = 0
    if "items" in response and len(response["items"]) > 0:
        subscribers = response["items"][0]["statistics"].get("subscriberCount", 0)
    else:
        print("Error fetching YouTube data:", response)  # مفيد للتصحيح




    return render(request, "category_list.html", {
        "category": category,
        "articles": articles,
        "categories": categories,
        "popular_articles": popular_articles,
        "breaking_news": breaking_news,
        "photos": photos,
        "information": information,
        "icon": icon,
        "youtube_subscribers": subscribers,
    })



def article_detail(request, slug):
    breaking_news = NewsArticle.objects.filter(is_breaking=True).order_by('-created_at')[:5]  # آخر 5 أخبار عاجلة
    popular_articles = NewsArticle.objects.order_by('-views')[:6]
    categories = NewsCategory.objects.all()
    photos = FlickrPhoto.objects.all().order_by('-created_at')[:12]  # آخر 12 صورة

    information = InformationContact.objects.first()
    icon = SocialMediaIcon.objects.all()

   
   
    article = get_object_or_404(NewsArticle, slug=slug)
    article.save(update_fields=['views'])
    article.views += 1
    article.save(update_fields=['views'])
    article.author = article.author or "Unknown Author"  # Handle case where author might be None


    comments = article.comments.all().order_by('-created_at')  # عرض التعليقات الأحدث أولاً

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect("main_core:article_detail", slug=article.slug)
    else:
        form = CommentForm()



    # YouTube API
    api_key = settings.YOUTUBE_API_KEY
    channel_id = "UCPP15i6IPmPFS8Il7aIP5Sw"  # حط ID القناة بتاعتك
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
    response = requests.get(url).json()
 # التحقق من وجود البيانات
    subscribers = 0
    if "items" in response and len(response["items"]) > 0:
        subscribers = response["items"][0]["statistics"].get("subscriberCount", 0)
    else:
        print("Error fetching YouTube data:", response)  # مفيد للتصحيح



    return render(request, "article_detail.html", {
        "article": article,
        "categories": NewsCategory.objects.all(),
        "comment_form": form,
        "comments": comments,
        "popular_articles": popular_articles,
        "categories": categories,
        "breaking_news": breaking_news,
        "photos": photos,
        "information": information,
        "icon": icon,
        "youtube_subscribers": subscribers,
    })


@login_required
def add_comment(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                article=article,
                user=request.user,
                content=content
            )
    return redirect("main_core:article_detail", slug=article.slug)



def search_articles(request):
    query = request.GET.get("q")  # الكلمة اللي المستخدم كتبها
    results = []

    if query:
        results = NewsArticle.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, "search_results.html", {
        "query": query,
        "results": results,
        "categories": NewsCategory.objects.all(),
    })

def unique_slug(title):
    base_slug = slugify(title)
    slug = base_slug
    num = 1
    while NewsArticle.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{num}"
        num += 1
    return slug

def generate_ai_article(request, category_slug):
    photos = FlickrPhoto.objects.all().order_by('-created_at')[:12]  # آخر 6 صور
    # جلب كل التصنيفات
    categories = NewsCategory.objects.all()
    # جلب معلومات الاتصال
    information = InformationContact.objects.first()
    icon = SocialMediaIcon.objects.all()

    category = get_object_or_404(NewsCategory, slug=category_slug)
    popular_articles = NewsArticle.objects.order_by('-views')[:6]


    if request.method == "POST":
        # ✅ AI يولد العنوان + المقال
        ai_title, ai_content = generate_article_content(category.name, auto_title=True)
        # توليد slug فريد
        slug = unique_slug(ai_title)

        # محاولة إيجاد مقال بنفس العنوان
        article, created = NewsArticle.objects.get_or_create(
            slug=slug,
            defaults={
                "category": category,
                "title": ai_title,
                "content": ai_content,
                "author": request.user,

            }
        )
        article.save()

        # إذا تم إنشاء المقال أو الصورة جديدة، احفظ الصورة
        img_temp = generate_article_image(ai_title)
        if img_temp:
            article.image.save(f"{slug}.png", ContentFile(img_temp.read()), save=True)

        return redirect("main_core:article_detail", slug=article.slug)

    context = {
        "category": category,
        "photos": photos,
        "categories": categories,
        "information": information,
        "icon": icon,
        "popular_articles": popular_articles
    }

    return render(request, "generate_ai_article.html", context)



# ✅ توليد مقال كامل (عنوان + محتوى) باستخدام AI
def unique_slugify(model, title):
    """ يخلي الـ slug فريد عشان نتجنب UNIQUE constraint error """
    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


def auto_generate_ai_article(request, category_slug):
    category = get_object_or_404(NewsCategory, slug=category_slug)

    # ✅ توليد المقال بالـ AI
    ai_title, ai_content = generate_article_content(category.name, auto_title=True)

    # ✅ slug فريد
    article_slug = unique_slugify(NewsArticle, ai_title)

    # ✅ أنشئ المقال مربوط بالكاتيجوري
    article = NewsArticle.objects.create(
        category=category,
        title=ai_title,
        slug=article_slug,
        content=ai_content,
        author=request.user if request.user.is_authenticated else None,
    )
    article.save()

    # ✅ توليد صورة للمقال
    img_temp = generate_article_image(ai_title)
    if img_temp:
        article.image.save(f"{article_slug}.jpg", img_temp, save=True)

    # ✅ رجع لصفحة المقال
    return redirect("main_core:article_detail", article_slug=article_slug)
