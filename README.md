# 🚀 Guevara App Store

ستۆری تێلیگرامی بۆ داونلۆدکردنی بەرنامەکانی iOS بە شیوەی دەستکاریکراو.

## 📋 فیچرەکان

✨ **ڕووکاری جوان**: لاپەڕەیەکی مۆدێرن و ڕەسپانسیو بە تێمای تاریک  
🔍 **پشکنینی خۆکار**: سکریپتی پایتۆن بۆ دڵنیابوونەوە لەوێی هەموو لینکەکان کاردەکەن  
📱 **نیشتمانی مۆبایل**: ڕووکار لە تێفۆنەکان بۆ جوان کردەوە  
🌍 **پشتیوانی کوردی**: تەواوی پیشاندانی بە کوردی (سۆرانی)  
⚡ **بارکردنی تێز**: داینامیکی بارکردن لە `apps.json`

## 📁 ستروکتیوری پڕۆژە

```
ipa/
├── apps.json              # داتای بەرنامەکان
├── index.html             # لاپەڕەی سەرەکی
├── check_apps.py          # سکریپتی پشکنین
└── README.md              # فایلی ئەم کتێبە
```

## 🔧 چۆن بەکاری بێنی

### 1️⃣ داونلۆدکردنی Repo
```bash
git clone https://github.com/aramtayar7-dev/ipa.git
cd ipa
```

### 2️⃣ کردنەوەی لاپەڕە
فایلی `index.html`ی بکردنەوە لە براوسڕت:
```bash
# بە Safari یان Chrome
open index.html

# یان لە ڕێگەی localhost
python3 -m http.server 8000
# ئینجا بڕۆ http://localhost:8000
```

### 3️⃣ پشکنینی بەرنامەکان
```bash
python3 check_apps.py
```

## 📝 زیادکردنی بەرنامەی نوێ

فایلی `apps.json`ی بکردنەوە و ئەم فۆرمێتە پەیڕەو بکە:

```json
{
  "name": "ناوی بەرنامە",
  "bundleIdentifier": "com.domain.app",
  "version": "1.0.0",
  "versionDate": "2026-05-07",
  "size": 100000000,
  "downloadURL": "https://github.com/user/repo/releases/download/v1.0.0/app.ipa",
  "developerName": "ناوی بەرھەمھێنەر",
  "iconURL": "https://example.com/icon.png",
  "localizedDescription": "وەسفی بەرنامە بە کوردی"
}
```

## 🔗 لینکەکان

- 🔗 **GitHub**: https://github.com/aramtayar7-dev/ipa
- 👤 **Developer**: aramtayar7-dev
- 📦 **Format**: JSON + HTML + Python

## 📊 بەرنامەکانی دەستدا

- ✅ **OldRoll** (وەشانی جیاجیا)
- ✅ **YouTube+** (بێ ڕێکلام)
- ✅ **CapCut PRO** (دەستکاریکراو)
- ✅ **Spotify++** (گوێگرتن بێ ڕێکلام)
- ✅ **Instagram Rocket** (داونلۆدکار)
- ✅ **TikTok Unicode** (فۆنتی دەستکاریکراو)

## ⚙️ پیویست

- **Python 3.7+** (بۆ سکریپتی پشکنین)
- **بڕاوسر نوێ** (بۆ لاپەڕە)
- **قسیې ئینتەرنەت** (بۆ داونلۆدکردن)

## 🛠️ تێجەریبکردن

### لە VS Code
```bash
# کردنەوەی Terminal
Ctrl + `

# ڕاکردنی سکریپت
python3 check_apps.py

# دروستکردنی سێرڤەری لۆکڵ
python3 -m http.server 3000
```

### لە Git
```bash
# پۆش کردنی تێگۆرە
git add .
git commit -m "زیادکردنی بەرنامەی نوێ"
git push origin main
```

## 📞 پشتگیری

ئەگەر پرسیارێک یان پێداوێسستیت هەبێت، یاریدەدەرێ Issue بکەیت یا PR بدیتەوە:
- 📮 Issues: https://github.com/aramtayar7-dev/ipa/issues
- 🔀 Pull Requests: https://github.com/aramtayar7-dev/ipa/pulls

## 📄 مافچاویت

© 2026 **Guevara App Store**. تەمام مافان پارێزراوە.

---

**نووسینی کورت**: ستۆری سادە و بێ قورپان بۆ داونلۆدکردنی بەرنامە!
