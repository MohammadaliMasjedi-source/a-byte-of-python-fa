# یک بایت پایتون به فارسی (A Byte of Python, Persian)

Draft Persian translation of the free book "A Byte of Python" by Swaroop C H.
Chapters 00 to 09 (preface to data structures) are translated; the rest of the book is not.
Text is CC BY-SA 4.0, code is BSD-3-Clause; AI-assisted draft, human review pending.

ترجمهٔ فارسیِ کتابِ آزادِ **A Byte of Python** نوشتهٔ **Swaroop C H** — یک راهنمای مقدماتیِ پایتون برای تازه‌کارها.
مترجم: **Mohammadali Masjedi**.

- متنِ اصلی: <https://python.swaroopch.com> · مخزن: <https://github.com/swaroopch/byte-of-python>
- مجوز: متن (اصلی و این ترجمه) **CC BY-SA 4.0**، فایل `LICENSE` · کد و اسکریپت‌ها **BSD سه‌بندی**، فایل `LICENSE-CODE`
- انتساب و فهرست تغییرها: `NOTICE.md` و `TRANSLATORS-NOTE.md`

> **این ترجمه از نویسندهٔ اصلیِ کتاب نیست.**
> (This translation is **not from the original author** of the book.)

## پنج دقیقه پایتون را امتحان کن

[**همین‌جا بازی کن: هشت حدس پایتونی**](labs/PLAY.md) · [نسخهٔ قابل اجرا و منابع](labs/README.md): چرا دو «آ» که یکسان دیده می‌شوند برابر نیستند؟ اگر دو عکس بهترین امتیاز فوکوس را داشته باشند کدام برنده می‌شود؟ این بخش مکملِ فارسیِ مخزن است. برای شروعِ خودِ کتاب به [نخستین گام‌ها](translation/03-first-steps.md) برو.

## ترجمهٔ کاملِ دیگر

پیش از این پروژه، **Najmeh Ghaderi** ترجمهٔ فارسیِ کاملی از همین کتاب منتشر کرده است
(معرفی‌شده در صفحهٔ ترجمه‌های کتابِ اصلی):
<https://najmeh-ghaderi.github.io/Persian-translation-of-a-byte-of-Python/>

این مخزن یک ترجمهٔ مستقل و هنوز ناتمام است و جایگزینِ آن نیست.

---

## وضعیتِ صادقانه

- ✅ **فصل‌های ۰۰ تا ۰۹** (ده فصل؛ «تقدیم‌نامه» ترجمه نشده است) به‌صورتِ **پیش‌نویس** ترجمه شده‌اند:
  پیش‌گفتار، دربارهٔ پایتون، نصب، نخستین گام‌ها، پایه‌ها (متغیرها/نوع‌ها)، عملگرها و عبارت‌ها،
  جریانِ کنترل، توابع، ماژول‌ها، ساختارهای داده.
- ⚠️ همهٔ فصل‌ها با برچسبِ «**پیش‌نویس — نیازمندِ بازخوانیِ نهاییِ مترجم**» علامت‌گذاری شده‌اند.
- ⬜ باقیِ کتاب (حلِ مسئله، برنامه‌نویسیِ شیءگرا، ورودی/خروجی، استثناها، کتابخانهٔ استاندارد، نکاتِ بیشتر، بعد از این چه؟)
  **هنوز ترجمه نشده است**.
- `reading.html` (خوانندهٔ آفلاین) فقط فصل‌های **۰۰ تا ۰۸** را دارد. فصلِ ۰۹ فقط در `translation/09-data-structures.md` است.

---

## مدلِ حقوقی

کتابِ اصلی زیرِ **CC BY-SA 4.0** است. این دو شرط را رعایت می‌کنیم:

1. **انتساب:** نامِ **Swaroop C H** و پیوند به متنِ اصلی (<https://python.swaroopch.com>)، با تصریحِ این‌که
   متنِ اصلی از همان‌جا قابلِ دریافت است.
2. **هم‌سان‌سازی (ShareAlike):** چون این یک اثرِ مشتق است، خودِ ترجمه هم زیرِ CC BY-SA 4.0 منتشر می‌شود.

نسخه‌های فروشیِ این ترجمه باید روشن و برجسته بگویند که **از نویسندهٔ اصلیِ کتاب نیستند** (*not from the original author*)؛ قاعدهٔ نویسندهٔ اصلی در `NOTICE.md` آمده است.

---

## ساختار

```
translation/           # فصل‌های ترجمه‌شده (Markdown، فارسی، کد به انگلیسی)
├─ 00-preface.md
├─ 01-about-python.md
├─ 02-installation.md
├─ 03-first-steps.md
├─ 04-basics.md
├─ 05-operators-expressions.md
├─ 06-control-flow.md
├─ 07-functions.md
├─ 08-modules.md
└─ 09-data-structures.md
reading.html           # خوانندهٔ آفلاین (فصل‌های 00 تا 08)، RTL + کدِ LTR
tools/build_reader.py   # ساخت و بررسیِ reading.html از روی فصل‌های Markdown
LICENSE                # CC BY-SA 4.0، متنِ حقوقیِ کامل
LICENSE-CODE           # BSD سه‌بندی (کدِ کتاب)
NOTICE.md              # انتساب
TRANSLATORS-NOTE.md    # فهرستِ تغییرها نسبت به متنِ اصلی
TASKS.md · TODO.md     # کارهای باقی‌مانده
PUBLISH-NOTES.md       # پیشنهادِ توضیح و موضوع‌های GitHub
```

## اصولِ ترجمه

- **وفادار**: بدونِ افزودنِ محتوای ساختگی؛ معنا و ساختارِ متنِ اصلی حفظ می‌شود.
- **کد دست‌نخورده**: بلوک‌های کد عیناً به انگلیسی می‌مانند.
- **اصطلاحاتِ فنی**: به فارسیِ استاندارد، با معادلِ انگلیسی در پرانتز آنجا که کمک می‌کند.
- **فارسیِ روان و امروزی**، با نیم‌فاصله و نشانه‌گذاریِ درست.
