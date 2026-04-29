from django.shortcuts import render, redirect
from datetime import datetime

# الصفحة الرئيسية (form)
def index(request):
    if request.method == "POST":
        money = float(request.POST.get('money'))
        start = request.POST.get('start')
        end = request.POST.get('end')

        # نحسب عدد الأيام
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        days = (end_date - start_date).days + 1

        daily = round(money / days, 1)

        # 👇 نسبة الصرف (مبدئي)
        percentage = 0

        # 👇 الألوان
        if percentage >= 150:
            color = "green"
            status = "Good 👍"
        elif percentage < 150 and percentage >= 70:
            color = "yellow"
            status = "Warning ⚠️"
        else:
            color = "red"
            status = "Danger 🔴"

        # 👇 نبعت كل حاجة للداشبورد
        return render(request, 'pages/dashboard.html', {
            'money': money,
            'days': days,
            'daily': daily,
            'percentage': percentage,
            'color': color,
            'status': status
        })

    return render(request, 'pages/index.html')


# الداشبورد (لو دخل عليها مباشر)
def dashboard(request):
    return render(request, 'pages/dashboard.html')


# صفحة المصروفات
def expenses(request):
    return render(request, 'pages/expenses.html')