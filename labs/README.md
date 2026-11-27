# اول حدس بزن، بعد اجرا کن

هشت آزمایش کوتاه برای کنارِ «یک بایت پایتون». از هر کدام که دوست داری شروع کن. کد را در محیط تعاملی پایتون ۳ وارد کن؛ خط‌هایی که با `>>>` آغاز نمی‌شوند خروجیِ مورد انتظارند. برای بررسیِ همهٔ جواب‌ها از ریشهٔ مخزن بزن: `python3 -m doctest -v labs/README.md`. نه بسته‌ای لازم داری، نه اینترنت.

این مثال‌ها افزودهٔ آموزشیِ مستقلِ این مخزن‌اند و جزو متن یا ترجمهٔ کتابِ Swaroop C H نیستند. متن: [CC BY-SA 4.0](../LICENSE)؛ مثال‌های کد: [BSD-3-Clause](../LICENSE-CODE).

### ۱. یک «آ» چند بایت است؟

پیش از اجرا: آیا شمارش حرف‌ها و شمارش بایت‌های فایل یک جواب می‌دهد؟

```pycon
>>> len("آ"), len("آ".encode("utf-8"))
(1, 2)

```

`len` روی رشته، کدپوینت‌های یونیکد را می‌شمارد؛ روی دادهٔ رمزگذاری‌شده، بایت‌ها را. چالش: «آ» را با A عوض کن. [مرجع: رشته و رمزگذاری](https://docs.python.org/3/library/stdtypes.html#str.encode) · [فصل پایه‌ها](../translation/04-basics.md)

### ۲. دو نوشته که یکسان دیده می‌شوند، همیشه برابرند؟

```pycon
>>> import unicodedata
>>> typed = "آ"
>>> decomposed = "ا" + "\u0653"
>>> typed == decomposed
False
>>> unicodedata.normalize("NFC", decomposed) == typed
True

```

دومی از الف و علامتِ مد ساخته شده است. اینجا NFC کمک می‌کند؛ اما قرار نیست املای متفاوت یا همهٔ حروف شبیه به هم را یکی کند. مثلاً «ی» فارسی و «ي» عربی را هم امتحان کن. [مرجع: نرمال‌سازی](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize)

### ۳. کپی گرفتی یا فقط اسم تازه گذاشتی؟

```pycon
>>> lessons = ["نور"]
>>> alias = lessons
>>> snapshot = lessons.copy()
>>> lessons.append("صدا")
>>> len(alias), len(snapshot)
(2, 1)

```

`alias` همان فهرست است. کپی اینجا مستقل است، اما کپی سطحی، فهرستِ توی فهرست را تکثیر نمی‌کند. [مرجع: کپی فهرست](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) · [فصل ساختار داده](../translation/09-data-structures.md)

### ۴. چرا حاصل مرتب‌سازی گم شد؟

```pycon
>>> scores = [8, 2, 5]
>>> before = sorted(scores)
>>> scores, before
([8, 2, 5], [2, 5, 8])
>>> result = scores.sort()
>>> scores, result is None
([2, 5, 8], True)

```

اگر مقادیر به ترتیبِ ثبت‌شدنشان معنی دارند، نسخهٔ مرتب را جدا نگه دار. [مرجع: مرتب‌سازی فهرست](https://docs.python.org/3/library/stdtypes.html#list.sort)

### ۵. اگر دو عکس بهترین امتیاز را داشته باشند چه؟

```pycon
>>> sharpness = [12, 19, 19, 10]
>>> max(enumerate(sharpness), key=lambda pair: pair[1])
(1, 19)

```

شماره‌ها از صفر شروع می‌شوند. وقتی امتیاز برابر است، `max` اولین مورد را برمی‌گرداند. چالش: چطور شمارهٔ *هر دو* عکس برتر را پیدا می‌کنی؟ [مرجع: max](https://docs.python.org/3/library/functions.html#max) · [در پروژهٔ واقعی دوربین ببین امتیاز از کجا می‌آید](https://github.com/MohammadaliMasjedi-source/rpi-camera-af/blob/main/Autofocus.py)

### ۶. سطر آخر کجا رفت؟

```pycon
>>> list(zip(["a", "b", "c"], [10, 12]))
[('a', 10), ('b', 12)]

```

`zip` به‌صورت پیش‌فرض با پایانِ ورودی کوتاه‌تر متوقف می‌شود. اگر برای هر تصویر دقیقاً یک برچسب لازم داری، در پایتون ۳٫۱۰ به بعد `strict=True` بگذار و نتیجه را مصرف کن تا طولِ نابرابر خطا بدهد. [مرجع: zip](https://docs.python.org/3/library/functions.html#zip)

### ۷. اگر تمام امتیازها صفر باشند، اصلاً امتیازی داریم؟

```pycon
>>> readings = [0, 0]
>>> bool(readings), any(readings)
(True, False)

```

پرسش اول اینجاست که «آیا فهرست عضوی دارد؟» و دومی اینکه «حداقل یک عضو مقدارِ درست دارد؟». حالا هر دو را با فهرست خالی امتحان کن. [مرجع: مقدار صدق](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) · [فصل جریان کنترل](../translation/06-control-flow.md)

### ۸. آیا رقم فارسی برای پایتون عدد است؟

```pycon
>>> int("۰۷") + 1
8
>>> "۰۷" == "07"
False

```

برای محاسبه، `int` رقم‌های ده‌دهی یونیکد را می‌پذیرد. برای شناسه‌ای مثل شمارهٔ کارتِ درس، تبدیل به عدد ممکن است صفرِ اول را هم از بین ببرد. [مرجع: int](https://docs.python.org/3/library/functions.html#int)

**بعدش چه؟** اگر مثال دوم یا هشتم برایت جالب بود، [مدل محتوای سحر](https://github.com/MohammadaliMasjedi-source/Sahar/blob/main/docs/CONTENT-MODEL.md) را باز کن و ببین یک درس چندزبانه چطور ذخیره می‌شود. اگر از پیدا کردن رفتار غافلگیرکننده لذت بردی، [گزارش‌های نمونهٔ QA](https://github.com/MohammadaliMasjedi-source/MohammadaliMasjedi-source/blob/main/qa-testing-portfolio/docs/BUG-REPORTS.md) را ببین: بین «فکر می‌کردم این‌طور باشد» و یک گزارش قابل تکرار چه فرقی هست؟

**نوبت تو:** یک مثالِ سه‌خطی پیشنهاد بده: کد، حدسِ خودت، خروجیِ واقعی و نسخهٔ پایتونت. اگر توضیح فارسی گنگ بود، همان جمله و بازنویسیِ پیشنهادی‌ات را در [Issues](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/issues) بگذار.
