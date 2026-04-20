# tal1/views.py
from django.shortcuts import render

# الصفحة الرئيسية — تعرض templates/home.html
def home(request):
    return render(request, "home.html")
