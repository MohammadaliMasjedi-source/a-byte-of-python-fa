# هشت حدس پایتونی | بازی پنج‌دقیقه‌ای

دو «آ» که یکسان دیده می‌شوند؛ دو عکس که امتیاز یکسان دارند؛ دو صفر که به معنی «هیچ داده‌ای نداریم» نیستند. کدامشان پایتون را گول می‌زند؟

**روش بازی:** کد را بخوان و روی گزینه‌ای که به نظرت چاپ می‌شود بزن؛ دلیلش همان‌جا باز می‌شود. به اولین حدس درستت یک امتیاز بده. نصب، حساب کاربری یا اجرای کد لازم نیست. برای فرستادن یک سؤال به دوستت، لینک «همین سؤال» را کپی کن.

<a name="q1"></a>

## ۱. یک حرف، چند بایت؟

```python
print(len("آ".encode("utf-8")))
```

<details>
<summary><code>1</code></summary>

یک بار دیگر نگاه کن. یک، تعداد کدپوینت‌های همین رشته است؛ بعد از encode داریم بایت می‌شماریم.

</details>

<details>
<summary><code>2</code></summary>

درست حدس زدی. UTF-8 برای این حرف دو بایت لازم دارد.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q1)

<a name="q2"></a>

## ۲. یک شکل، دو رشته؟

```python
print("آ" == "ا" + "\u0653")
```

<details>
<summary><code>False</code></summary>

درست حدس زدی. نمایش یکسان می‌تواند از دو توالی متفاوت یونیکد ساخته شود.

</details>

<details>
<summary><code>True</code></summary>

یک بار دیگر نگاه کن. چشم شکل را می‌بیند، اما پایتون توالی کدپوینت‌ها را مقایسه می‌کند.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q2)

<a name="q3"></a>

## ۳. چند درس در نسخهٔ قدیمی ماند؟

```python
lessons = ["نور"]
old = lessons.copy()
lessons.append("صدا")
print(len(old))
```

<details>
<summary><code>2</code></summary>

یک بار دیگر نگاه کن. اگر نوشته بودیم old = lessons این پاسخ درست بود.

</details>

<details>
<summary><code>1</code></summary>

درست حدس زدی. کپی پیش از اضافه‌شدن «صدا» ساخته شده است.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q3)

<a name="q4"></a>

## ۴. مرتب شد؛ ولی چه چیزی برگشت؟

```python
scores = [8, 2, 5]
print(scores.sort())
```

<details>
<summary><code>[2, 5, 8]</code></summary>

یک بار دیگر نگاه کن. این نتیجهٔ print(scores) بعد از مرتب‌سازی است؛ سؤال دربارهٔ خروجی خود sort بود.

</details>

<details>
<summary><code>None</code></summary>

درست حدس زدی. خود فهرست مرتب شد. متد sort مقدار تازه‌ای برنمی‌گرداند.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q4)

<a name="q5"></a>

## ۵. کدام عکس در تساوی برنده است؟

```python
scores = [12, 19, 19, 10]
print(max(range(len(scores)), key=scores.__getitem__))
```

<details>
<summary><code>1</code></summary>

درست حدس زدی. هر دو عکس امتیاز ۱۹ دارند؛ max اولین بیشینه را نگه می‌دارد.

</details>

<details>
<summary><code>2</code></summary>

یک بار دیگر نگاه کن. شمارهٔ ۲ هم بالاترین امتیاز را دارد، ولی بعد از شمارهٔ ۱ آمده است.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q5)

<a name="q6"></a>

## ۶. برای سه عکس و دو برچسب چند جفت داریم؟

```python
print(len(list(zip(["a", "b", "c"], [10, 12]))))
```

<details>
<summary><code>2</code></summary>

درست حدس زدی. با تمام‌شدن برچسب‌ها، zip عادی متوقف می‌شود.

</details>

<details>
<summary><code>3</code></summary>

یک بار دیگر نگاه کن. zip برای عکس سوم خودش برچسب خالی نمی‌سازد.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q6)

<a name="q7"></a>

## ۷. آیا اندازه‌گیری انجام شده؟

```python
readings = [0, 0]
print(bool(readings), any(readings))
```

<details>
<summary><code>False False</code></summary>

یک بار دیگر نگاه کن. دو خوانش صفر با نداشتنِ هیچ خوانشی فرق دارد.

</details>

<details>
<summary><code>True False</code></summary>

درست حدس زدی. فهرست خالی نیست، اما هیچ عضوی مقدارِ درست ندارد.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q7)

<a name="q8"></a>

## ۸. صفرِ اول کجا رفت؟

```python
print(int("۰۷") + 1)
```

<details>
<summary><code>8</code></summary>

درست حدس زدی. رقم‌ها برای محاسبه به عدد تبدیل شده‌اند؛ صفر اول جزو مقدار عدد نیست.

</details>

<details>
<summary><code>۰۸</code></summary>

یک بار دیگر نگاه کن. اعداد پایتون شکل رقم یا قالب ورودی را نگه نمی‌دارند.

</details>

[لینک همین سؤال](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/blob/main/labs/PLAY.md#q8)

**چند تا را بار اول درست گفتی؟** برای هر حدس اشتباه یک چیز را در کد عوض کن تا جوابِ دیگرت درست از آب دربیاید. مثلاً در سؤال سوم فقط `.copy()` را بردار.

[اجرای همین ایده‌ها با پایتون و دیدن منابع](README.md) · [آزمایش فوکوس بدون دوربین](https://github.com/MohammadaliMasjedi-source/rpi-camera-af/blob/main/examples/focus_scores.py) · [یک معمای تازه پیشنهاد بده](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/issues) · [پروفایل سازنده](https://github.com/MohammadaliMasjedi-source)

این بازی مکمل مستقلِ ترجمه است. [مجوز متن](../LICENSE) · [مجوز کد](../LICENSE-CODE)
