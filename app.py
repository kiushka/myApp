import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-123!')

# دیتای خدمات خودرو
CAR_SERVICES = [
    {
        'id': 1,
        'title': 'مالیات بر ارزش افزوده خودرو',
        'icon': 'fa-percent',
        'description': 'پرداخت آنلاین مالیات ارزش افزوده خودروهای نو و کارکرده',
        'requirements': ['کارت ملی', 'سند خودرو', 'کد رهگیری']
    },
    {
        'id': 2,
        'title': 'عوارض شهرداری',
        'icon': 'fa-city',
        'description': 'پرداخت عوارض سالیانه شهرداری برای کلیه خودروها',
        'requirements': ['شناسنامه خودرو', 'کارت بیمه']
    },
    {
        'id': 3,
        'title': 'سامانه سخا',
        'icon': 'fa-file-contract',
        'description': 'ثبت نام و پیگیری معاینات فنی خودرو',
        'requirements': ['معاینه فنی معتبر', 'کارت خودرو']
    },
    {
        'id': 4,
        'title': 'نوبت تعویض پلاک',
        'icon': 'fa-calendar-alt',
        'description': 'دریافت نوبت آنلاین برای تعویض پلاک خودرو',
        'requirements': ['سند مالکیت', 'گزارش تخلفات']
    },
    {
        'id': 5,
        'title': 'بیمه شخص ثالث',
        'icon': 'fa-shield-alt',
        'description': 'خرید آنلاین بیمه شخص ثالث و بدنه',
        'requirements': ['کارت ملی', 'شناسنامه خودرو']
    },
    {
        'id': 6,
        'title': 'خودروهای وارداتی',
        'icon': 'fa-ship',
        'description': 'پیگیری مراحل ثبت و ترخیص خودروهای وارداتی',
        'requirements': ['گواهی ترخیص', 'رسید گمرکی']
    }
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/car-services')
def car_services():
    return render_template(
        "car_services.html",
        services=CAR_SERVICES,
        working_hours={
            'normal': 'شنبه تا چهارشنبه: ۸:۳۰ تا ۱۴:۳۰',
            'thursday': 'پنجشنبه‌ها: ۸:۳۰ تا ۱۲:۳۰'
        }
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode,
        ssl_context='adhoc' if os.environ.get('USE_SSL') else None
    )
