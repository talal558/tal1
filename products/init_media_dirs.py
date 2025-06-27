import os
from pathlib import Path

# حدد المسار الأساسي بناءً على موقع هذا الملف
BASE_DIR = Path(__file__).resolve().parent

# المسارات التي سيتم التأكد منها أو إنشاؤها
MEDIA_DIR = BASE_DIR / 'media'
PRODUCTS_DIR = MEDIA_DIR / 'products'

def ensure_directory(path):
    """يتأكد من وجود المجلد أو يقوم بإنشائه."""
    if not path.exists():
        path.mkdir(parents=True)
        print(f"📁 تم إنشاء المجلد: {path}")
    else:
        print(f"✅ المجلد موجود مسبقًا: {path}")

def main():
    print("🔍 فحص مجلدات الوسائط:")
    ensure_directory(MEDIA_DIR)
    ensure_directory(PRODUCTS_DIR)
    print("🎉 تم الفحص أو الإنشاء بنجاح.")

if __name__ == "__main__":
    main()
