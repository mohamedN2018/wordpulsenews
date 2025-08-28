import os
import requests
from openai import OpenAI
from django.core.files.temp import NamedTemporaryFile
from django.http import JsonResponse
from openai import OpenAI
from decouple import config
import json
# =========================
# إعداد الـ API
# =========================
API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
    "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"
)

# ✅ OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


# =========================
# توليد مقال بالذكاء الاصطناعي
# =========================
def generate_article_content(category_name, auto_title=True):
    try:
        prompt = f"""
        اكتب مقال احترافي عن مجال: {category_name}.
        ارجع النتيجة كـ JSON بالصيغة التالية فقط:
        {{
            "title": "عنوان قصير وجذاب",
            "content": "المقال هنا..."
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        ai_text = response.choices[0].message.content

        # 🛠 محاولة قراءة النص كـ JSON
        try:
            data = json.loads(ai_text)
            ai_title = data.get("title", "").strip()
            ai_content = data.get("content", "").strip()
        except json.JSONDecodeError:
            ai_title = f"مقال عن {category_name}"
            ai_content = ai_text.strip() if ai_text else "لم يتم توليد محتوى."

        if not ai_title:
            ai_title = f"مقال عن {category_name}"
        if not ai_content:
            ai_content = "لم يتمكن الذكاء الاصطناعي من كتابة المحتوى."

        return ai_title, ai_content

    except Exception as e:
        return f"مقال عن {category_name}", f"خطأ أثناء توليد المقال: {str(e)}"


# =========================
# جلب صورة مناسبة من Unsplash
# =========================
def generate_article_image(prompt):
    """
    يجيب صورة مناسبة من Unsplash (بدون API Key)
    """
    try:
        url = f"https://source.unsplash.com/800x600/?{prompt}"
        response = requests.get(url, stream=True, timeout=10)

        if response.status_code == 200:
            img_temp = NamedTemporaryFile(delete=False, suffix=".jpg")
            img_temp.write(response.content)
            img_temp.flush()
            response.close()
            return img_temp
        else:
            response.close()
            return None
    except Exception as e:
        print("Unsplash error:", e)
        return None
