import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # فایل باید در پوشه templates باشه

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))  # گرفتن پورت از متغیر محیطی
    app.run(host='0.0.0.0', port=port)       # گوش دادن روی همه اینترفیس‌ها
