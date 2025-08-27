from openai import OpenAI
import os, requests
from django.core.files.temp import NamedTemporaryFile


API_KEY = os.getenv("OPENROUTER_API_KEY", "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")

# ✅ خلي الـ client يشتغل مع OpenRouter مش OpenAI مباشرة
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def generate_article_content(category_name, auto_title=False, title=None):
    if auto_title:
        prompt = f"اكتب لي عنوان جذاب ومقال احترافي عن قسم {category_name}."
    else:
        prompt = f"اكتب مقال احترافي بعنوان: {title}"

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",   # ✅ لازم تحدد provider/model صح عند OpenRouter
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    content = response.choices[0].message.content.strip()

    if auto_title:
        lines = content.split("\n", 1)
        ai_title = lines[0].replace("عنوان:", "").strip()
        ai_content = lines[1].strip() if len(lines) > 1 else ""
        return ai_title, ai_content
    else:
        return title, content



def generate_article_image(prompt):
    """
    يجيب صورة مناسبة للمقال من Unsplash (بدون API Key)
    """
    try:
        # Unsplash بيوفر لينك مباشر للصور حسب الكلمة
        url = f"https://source.unsplash.com/800x600/?{prompt}"

        response = requests.get(url, stream=True)
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
