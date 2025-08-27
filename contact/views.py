from django.shortcuts import render
from .models import SocialMediaIcon, InformationContact
from main_core.models import FlickrPhoto, NewsArticle, NewsCategory
import requests
from django.conf import settings

# Create your views here.

app_name = 'contact'

def contact(request):
    information = InformationContact.objects.first()
    icon = SocialMediaIcon.objects.all()
    photos = FlickrPhoto.objects.all().order_by('-created_at')[:12]  # آخر 12 صورة
    breaking_news = NewsArticle.objects.filter(is_breaking=True).order_by('-created_at')[:5]  # آخر 5 أخبار عاجلة
    # جلب كل التصنيفات
    categories = NewsCategory.objects.all()
    popular_articles = NewsArticle.objects.order_by('-views')[:6]

    # جلب أحدث المقالات مع التأكد من وجود slug
    latest_articles = NewsArticle.objects.exclude(slug='').order_by('-id')[:9]


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

    fb_page_id = "mohamednabilpro2026"
    access_token = settings.FB_ACCESS_TOKEN

    url = f"https://graph.facebook.com/v16.0/{fb_page_id}?fields=followers_count&access_token={access_token}"
    response = requests.get(url).json()
# التحقق من وجود البيانات
    followers_count = 0
    if "followers_count" in response:
        followers_count = response["followers_count"]
    else:
        print("Error fetching YouTube data:", response)  # مفيد للتصحيح


    return render(request, 'contact_home.html', {
        'photos': photos,
        'breaking_news': breaking_news,
        'categories': categories,
        'popular_articles': popular_articles,
        'latest_articles': latest_articles,
        'social_media_icons': icon,
        'information': information,
        "youtube_subscribers": subscribers,
        "fb_followers": followers_count,
    })
