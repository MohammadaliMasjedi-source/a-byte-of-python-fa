# چهار حدس دیگر: ریتم، گیتار، تست و اندازه‌گیری

[فارسی](PLAY.md) · [English](PLAY.en.md) · [Offline HTML](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/raw/refs/heads/main/labs/python-pocket-lab.html) · [اتاق معماها / Puzzle desk](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/issues/6)

<a name="music"></a>

## ضرب هفتم کجای ریتم می‌افتد؟

```python
from itertools import cycle, islice
bar = cycle(["DUM", "tak", "tak"])
print(next(islice(bar, 6, None)))
```

`tak`　/　`DUM`

<details><summary>حدست را زدی؟ پاسخ و دلیل</summary>

**خروجی: `DUM`**

شش ضرب، دو دور کامل است. پس ضرب هفتم دوباره صدای اول است.

</details>

[مرجع پایتون](https://docs.python.org/3/library/itertools.html#itertools.cycle)

<a name="pitch"></a>

## یک نیم‌پرده زیرِ نت مرجع، در کدام اکتاو است؟

```python
semitones = -1
print(semitones // 12, semitones % 12)
```

`-1 11`　/　`0 -1`

<details><summary>حدست را زدی؟ پاسخ و دلیل</summary>

**خروجی: `-1 11`**

تقسیم صحیح به سمت منفی بی‌نهایت گرد می‌کند: منفی یک برابر است با ۱۲ ضرب‌در منفی یک، به‌علاوهٔ ۱۱.

</details>

[مرجع پایتون](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)

<a name="qa"></a>

## کدام آزمایش اول رد شد؟

```python
passed = [True, False, False]
print(next(n for n, ok in enumerate(passed, 1) if not ok))
```

`1`　/　`2`

<details><summary>حدست را زدی؟ پاسخ و دلیل</summary>

**خروجی: `2`**

شماره‌گذاری این بار از یک شروع می‌شود. next فقط اولین نتیجه‌ای را می‌گیرد که False بوده است.

</details>

[مرجع پایتون](https://docs.python.org/3/library/functions.html#enumerate)

<a name="meter"></a>

## دو عدد نیمه‌صحیح چطور گرد می‌شوند؟

```python
print(round(2.5), round(3.5))
```

`2 4`　/　`3 4`

<details><summary>حدست را زدی؟ پاسخ و دلیل</summary>

**خروجی: `2 4`**

در این دو مقدارِ دقیقاً نیمه، round عدد زوج نزدیک‌تر را انتخاب می‌کند. این با «همیشه نیم را به بالا گرد کن» فرق دارد.

</details>

[مرجع پایتون](https://docs.python.org/3/library/functions.html#round)
