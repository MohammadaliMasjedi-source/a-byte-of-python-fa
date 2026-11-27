# Twelve Python predictions

Pick an output before you open the explanation. No installation needed.

[فارسی](PLAY.md) · [English](PLAY.en.md) · [Download the offline game](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/raw/refs/heads/main/labs/python-pocket-lab.html)

<a name="q1"></a>

## One letter. How many bytes?

```python
print(len("آ".encode("utf-8")))
```

`1` / `2`

<details>
<summary>Reveal the answer</summary>

`2` — UTF-8 uses two bytes for this letter. One is the number of Unicode code points before encoding.

</details>

[Python reference](https://docs.python.org/3/library/stdtypes.html#str.encode)

<a name="q2"></a>

## Two strings, one shape?

```python
print("آ" == "ا" + "\u0653")
```

`False` / `True`

<details>
<summary>Reveal the answer</summary>

`False` — The first string contains one code point. The second contains an alef and a combining mark. They can look alike without comparing equal.

</details>

[Python reference](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize)

<a name="q3"></a>

## What stayed in the old lesson list?

```python
lessons = ["نور"]
old = lessons.copy()
lessons.append("صدا")
print(len(old))
```

`2` / `1`

<details>
<summary>Reveal the answer</summary>

`1` — The shallow copy was made before the second lesson was appended. Plain assignment would have kept both names pointing to the same list.

</details>

[Python reference](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<a name="q4"></a>

## The list is sorted. What did sort return?

```python
scores = [8, 2, 5]
print(scores.sort())
```

`[2, 5, 8]` / `None`

<details>
<summary>Reveal the answer</summary>

`None` — sort() changes the list in place and returns None. To see the sorted values, print the list afterwards.

</details>

[Python reference](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

<a name="q5"></a>

## Two frames tie. Which index wins?

```python
scores = [12, 19, 19, 10]
print(max(range(len(scores)), key=scores.__getitem__))
```

`1` / `2`

<details>
<summary>Reveal the answer</summary>

`1` — max keeps the first maximum. Both scores are 19, but index 1 comes first.

</details>

[Python reference](https://docs.python.org/3/library/functions.html#max)

<a name="q6"></a>

## Three photos, two labels. How many pairs?

```python
print(len(list(zip(["a", "b", "c"], [10, 12]))))
```

`2` / `3`

<details>
<summary>Reveal the answer</summary>

`2` — Ordinary zip stops when the shorter input runs out. It does not invent a label for the last photo.

</details>

[Python reference](https://docs.python.org/3/library/functions.html#zip)

<a name="q7"></a>

## Did the sensor record anything?

```python
readings = [0, 0]
print(bool(readings), any(readings))
```

`False False` / `True False`

<details>
<summary>Reveal the answer</summary>

`True False` — A list with two zeroes is nonempty, so its truth value is True. Neither reading is truthy, so any returns False.

</details>

[Python reference](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

<a name="q8"></a>

## Where did the leading zero go?

```python
print(int("۰۷") + 1)
```

`8` / `۰۸`

<details>
<summary>Reveal the answer</summary>

`8` — int accepts decimal digits written in Persian. The integer retains neither the spelling nor the leading zero.

</details>

[Python reference](https://docs.python.org/3/library/functions.html#int)

<a name="music"></a>

## Where does beat seven land?

```python
from itertools import cycle, islice
bar = cycle(["DUM", "tak", "tak"])
print(next(islice(bar, 6, None)))
```

`tak` / `DUM`

<details>
<summary>Reveal the answer</summary>

`DUM` — Six beats make two whole bars of three. Skipping them puts us back on the first sound.

</details>

[Python reference](https://docs.python.org/3/library/itertools.html#itertools.cycle)

<a name="pitch"></a>

## One semitone below the reference: which octave?

```python
semitones = -1
print(semitones // 12, semitones % 12)
```

`-1 11` / `0 -1`

<details>
<summary>Reveal the answer</summary>

`-1 11` — Floor division rounds down. The octave is −1 and the position inside that octave is 11: −1 = 12 × (−1) + 11.

</details>

[Python reference](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)

<a name="qa"></a>

## Which check failed first?

```python
passed = [True, False, False]
print(next(n for n, ok in enumerate(passed, 1) if not ok))
```

`1` / `2`

<details>
<summary>Reveal the answer</summary>

`2` — Numbering explicitly starts at one. next takes just the first failed check.

</details>

[Python reference](https://docs.python.org/3/library/functions.html#enumerate)

<a name="meter"></a>

## What happens at two exact ties?

```python
print(round(2.5), round(3.5))
```

`2 4` / `3 4`

<details>
<summary>Reveal the answer</summary>

`2 4` — At these exactly representable ties, round chooses the even integer. That differs from rounding every half upward.

</details>

[Python reference](https://docs.python.org/3/library/functions.html#round)

[Run a camera experiment](https://github.com/MohammadaliMasjedi-source/rpi-camera-af/blob/main/examples/focus_scores.py) · [Suggest a puzzle](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/issues) · [Text license](../LICENSE) · [Code license](../LICENSE-CODE)
