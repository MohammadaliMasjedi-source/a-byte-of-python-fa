> ⚠️ **پیش‌نویس — نیازمندِ بازخوانیِ نهاییِ مترجم** · ترجمه از *A Byte of Python* اثرِ Swaroop C H — <https://python.swaroopch.com> — CC BY-SA 4.0

> **یادداشت مترجم:** این فصل، ترجمهٔ کمک‌گرفته از هوش مصنوعی و هنوز در انتظار بازخوانیِ انسانی است. کدها و خروجی‌های نمونه عین متنِ اصلی‌اند؛ نسخهٔ سوم عمداً خطای نحوی دارد. اول‌شخصِ متن، صدای نویسندهٔ کتاب است، نه گزارشی از تجربهٔ مترجم.

# حلِ مسئله

تا اینجا با بخش‌های مختلفِ زبان پایتون آشنا شده‌ایم. حالا برنامه‌ای طراحی می‌کنیم و می‌نویسیم که کار مفیدی *انجام دهد* تا ببینیم این بخش‌ها چگونه کنار هم قرار می‌گیرند. هدف این است که یاد بگیریم خودمان یک اسکریپت پایتون بنویسیم.

## مسئله

مسئله‌ای که می‌خواهیم حل کنیم این است:

> برنامه‌ای می‌خواهم که از همهٔ فایل‌های مهمم نسخهٔ پشتیبان بگیرد.

مسئله ساده به نظر می‌رسد، اما هنوز اطلاعات کافی برای شروع نداریم. باید کمی بیشتر آن را *تحلیل* کنیم. مثلاً چطور مشخص کنیم از *کدام* فایل‌ها نسخهٔ پشتیبان گرفته شود؟ فایل‌های پشتیبان *چطور* و *کجا* ذخیره شوند؟

پس از تحلیلِ درستِ مسئله، نوبت به *طراحی* برنامه می‌رسد. فهرستی از ویژگی‌های موردنظر می‌نویسیم. من برای این برنامه فهرست زیر را تهیه کرده‌ام. اگر شما آن را طراحی کنید، ممکن است به تحلیل متفاوتی برسید؛ هرکس روش خودش را دارد و این کاملاً طبیعی است.

- فایل‌ها و پوشه‌هایی که باید از آنها نسخهٔ پشتیبان بگیریم، در یک فهرست مشخص می‌شوند.
- نسخه‌های پشتیبان باید در یک پوشهٔ اصلی ذخیره شوند.
- فایل‌های پشتیبان را در یک فایل zip قرار می‌دهیم.
- نام فایل zip، تاریخ و ساعتِ همان لحظه است.
- از فرمان استاندارد `zip` استفاده می‌کنیم که به‌طور پیش‌فرض در توزیع‌های متعارف GNU/Linux یا Unix در دسترس است. هر فرمانِ بایگانیِ دیگری هم که رابط خط فرمان داشته باشد قابل استفاده است.

> **برای کاربران ویندوز**
>
> می‌توانید فرمان `zip` را از [صفحهٔ پروژهٔ GnuWin32](http://gnuwin32.sourceforge.net/packages/zip.htm) [نصب کنید](http://gnuwin32.sourceforge.net/downlinks/zip.php) و مسیر `C:\Program Files\GnuWin32\bin` را به متغیر محیطی `PATH` سیستم اضافه کنید؛ شبیه کاری که برای [شناساندنِ فرمان پایتون](./02-installation.md) انجام دادیم.

## راه‌حل

حالا که طراحیِ برنامه به اندازهٔ کافی روشن شده است، می‌توانیم کدی بنویسیم که *پیاده‌سازیِ* راه‌حل ما باشد.

با نامِ `backup_ver1.py` ذخیره کنید:

```python
import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we have to use double quotes inside a string
# for names with spaces in it.  We could have also used
# a raw string by writing [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
```

خروجی:

```text
$ python backup_ver1.py
Zip command is:
zip -r /Users/swa/backup/20140328084844.zip /Users/swa/notes
Running:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
Successful backup to /Users/swa/backup/20140328084844.zip
```

حالا وارد مرحلهٔ *آزمایش* می‌شویم: بررسی می‌کنیم که برنامه درست کار می‌کند یا نه. اگر رفتار برنامه مطابق انتظار نباشد، باید آن را *اشکال‌زدایی* کنیم؛ یعنی خطاها یا همان *باگ‌های* آن را پیدا و برطرف کنیم.

اگر برنامهٔ بالا برای شما کار نکرد، فرمانی را که پس از سطرِ `Zip command is` چاپ می‌شود کپی کنید و در پوستهٔ GNU/Linux یا Mac OS X، یا در `cmd` ویندوز اجرا کنید. پیام خطا را بخوانید و سعی کنید علت را برطرف کنید. راهنمای فرمان zip هم می‌تواند کمک کند. اگر خودِ فرمان درست اجرا شد، احتمال دارد اشکال در برنامهٔ پایتون باشد؛ بررسی کنید که کدتان دقیقاً با نمونهٔ بالا مطابقت داشته باشد.

**چگونه کار می‌کند**

می‌بینید که چطور *طراحی* را مرحله‌به‌مرحله به *کد* تبدیل کرده‌ایم.

ابتدا ماژول‌های `os` و `time` را وارد می‌کنیم. سپس در فهرستِ `source` فایل‌ها و پوشه‌های موردنظر برای پشتیبان‌گیری را مشخص می‌کنیم. پوشهٔ مقصد، جایی است که همهٔ نسخه‌های پشتیبان را نگه می‌داریم و آن را در متغیرِ `target_dir` قرار می‌دهیم. نام فایل zip را با تابعِ `time.strftime()` از تاریخ و ساعتِ فعلی می‌سازیم. این فایل پسوندِ `.zip` دارد و در پوشهٔ `target_dir` ذخیره می‌شود.

به `os.sep` توجه کنید: مقدارِ این متغیر، نویسهٔ جداکنندهٔ مسیر در سیستم‌عامل شماست؛ در GNU/Linux، Unix و macOS برابر با `'/'` و در ویندوز برابر با `'\\'` است. استفاده از `os.sep` به‌جای نوشتن مستقیمِ این نویسه‌ها کمک می‌کند برنامه روی سیستم‌های مختلف قابل اجرا باشد.

تابعِ `time.strftime()` یک رشتهٔ قالب می‌گیرد؛ مانند همان قالبی که در برنامه استفاده کردیم. `%Y` با سالِ چهاررقمی جایگزین می‌شود، `%m` با شمارهٔ ماه به شکل عددی از `01` تا `12`، و به همین ترتیب. فهرستِ کاملِ این قالب‌ها در [مرجع پایتون](http://docs.python.org/3/library/time.html#time.strftime) آمده است.

با عملگر جمع، رشته‌ها را *به هم می‌چسبانیم* و نام فایل zip مقصد را می‌سازیم. این عملگر دو رشته را به هم وصل می‌کند و رشتهٔ تازه‌ای برمی‌گرداند. سپس رشته‌ای به نامِ `zip_command` می‌سازیم که فرمانِ موردنظر برای اجرا را در خود دارد. می‌توانید آن را در پوسته، یعنی پایانهٔ GNU/Linux یا خط فرمان DOS، اجرا و بررسی کنید.

فرمانِ `zip` گزینه‌های مختلفی دارد. یکی از آنها `-r` است که می‌گوید پوشه‌ها را به‌صورت *بازگشتی* پردازش کند؛ یعنی فایل‌ها و زیرپوشه‌های داخلشان را هم در بایگانی قرار دهد. پس از گزینه‌ها، نام فایل zip موردنظر و بعد فهرستِ فایل‌ها و پوشه‌های منبع می‌آید. برای تبدیل فهرستِ `source` به یک رشته، از متدِ `join` رشته‌ها استفاده می‌کنیم که قبلاً با آن آشنا شده‌ایم.

در پایان، فرمان را با تابعِ `os.system` *اجرا* می‌کنیم. این تابع، فرمان را مانند زمانی اجرا می‌کند که آن را در پوستهٔ سیستم نوشته باشیم. در صورت اجرای موفق، `0` و در غیر این صورت، یک شمارهٔ خطا برمی‌گرداند.

بر اساس نتیجهٔ فرمان، پیامِ موفقیت یا شکستِ پشتیبان‌گیری را چاپ می‌کنیم.

به همین سادگی، اسکریپتی نوشته‌ایم که از فایل‌های مهممان نسخهٔ پشتیبان می‌گیرد!

> **نکته‌ای برای کاربران ویندوز**
>
> به‌جای دو بک‌اسلشِ پیاپی، می‌توانید از رشتهٔ خام استفاده کنید. مثلاً `'C:\\Documents'` یا `r'C:\Documents'` بنویسید. اما از `'C:\Documents'` استفاده *نکنید*، چون `\D` یک دنبالهٔ گریزِ ناشناخته است.

حالا که اسکریپتِ پشتیبان‌گیری کار می‌کند، هر وقت لازم باشد می‌توانیم از آن استفاده کنیم. به این مرحله، *بهره‌برداری* یا *استقرار* نرم‌افزار می‌گویند.

برنامهٔ بالا درست کار می‌کند، اما معمولاً اولین نسخهٔ برنامه‌ها دقیقاً مطابق انتظار پیش نمی‌رود. شاید طراحی ناقص باشد یا هنگام تایپِ کد اشتباهی کرده باشیم. در این صورت، بسته به نوع مسئله، باید به مرحلهٔ طراحی برگردیم یا برنامه را اشکال‌زدایی کنیم.

## نسخهٔ دوم

نسخهٔ اولِ اسکریپت کار می‌کند، اما می‌توانیم آن را برای استفادهٔ روزمره بهتر کنیم. این کار بخشی از مرحلهٔ *نگهداریِ* نرم‌افزار است.

یکی از بهبودهایی که مفید دیدم، روشِ نام‌گذاریِ فایل‌ها بود: در پوشهٔ اصلیِ پشتیبان‌گیری، برای هر *تاریخ* یک پوشه بسازیم و درونِ آن، فایل را با *ساعتِ* پشتیبان‌گیری نام‌گذاری کنیم. مزیتِ اول این است که نسخه‌ها به‌صورتِ سلسله‌مراتبی مرتب می‌شوند و مدیریتشان آسان‌تر است. دوم اینکه نام فایل‌ها کوتاه‌تر می‌شود. سوم اینکه وجودِ پوشهٔ هر روز نشان می‌دهد در آن روز نسخهٔ پشتیبان گرفته‌ایم؛ چون این پوشه فقط هنگامِ پشتیبان‌گیری ساخته می‌شود.

با نامِ `backup_ver2.py` ذخیره کنید:

```python
import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
```

خروجی:

```text
$ python backup_ver2.py
Successfully created directory /Users/swa/backup/20140329
Zip command is:
zip -r /Users/swa/backup/20140329/073201.zip /Users/swa/notes
Running:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
Successful backup to /Users/swa/backup/20140329/073201.zip
```

**چگونه کار می‌کند**

بیشترِ برنامه همان است. تفاوت اینجاست که با تابعِ `os.path.exists` بررسی می‌کنیم آیا در پوشهٔ اصلی، پوشه‌ای با تاریخِ امروز وجود دارد یا نه. اگر وجود نداشته باشد، با تابعِ `os.mkdir` آن را می‌سازیم.

## نسخهٔ سوم

نسخهٔ دوم برای پشتیبان‌گیری‌های مکرر خوب کار می‌کند، اما وقتی تعداد نسخه‌ها زیاد می‌شود، تشخیصِ اینکه هرکدام برای چه بوده‌اند دشوار است! مثلاً شاید تغییرهای مهمی در یک برنامه یا ارائه داده باشم و بخواهم نام فایل zip به آن تغییرها اشاره کند. راه ساده این است که توضیحی را از کاربر بگیریم و به نامِ فایل اضافه کنیم.

**هشدارِ متن اصلی:** برنامهٔ زیر کار نمی‌کند. نگران نباشید و توضیح را دنبال کنید؛ قرار است از همین خطا چیزی یاد بگیریم.

با نامِ `backup_ver3.py` ذخیره کنید:

```python
import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + 
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
```

خروجی:

```text
$ python backup_ver3.py
  File "backup_ver3.py", line 39
    target = today + os.sep + now + '_' +
                                        ^
SyntaxError: invalid syntax
```

**چرا این نسخه کار نمی‌کند**

*این برنامه کار نمی‌کند!* پایتون می‌گوید خطای نحوی وجود دارد؛ یعنی ساختارِ اسکریپت با چیزی که پایتون انتظار دارد سازگار نیست. پیام خطا، محلِ تشخیصِ خطا را هم نشان می‌دهد. پس اشکال‌زدایی را از همان سطر شروع می‌کنیم.

اگر دقیق‌تر نگاه کنیم، می‌بینیم یک سطرِ منطقی را به دو سطرِ فیزیکی شکسته‌ایم، اما مشخص نکرده‌ایم که این دو سطر به هم تعلق دارند. پایتون در سطر منطقی، عملگرِ جمعِ `+` را دیده، اما پس از آن عملوندی پیدا نکرده و نمی‌داند چطور ادامه دهد. یادتان هست که می‌توانیم با گذاشتن بک‌اسلش در پایانِ سطرِ فیزیکی، ادامهٔ سطرِ منطقی را در سطرِ بعد بنویسیم. پس این اصلاح را انجام می‌دهیم. به اصلاحِ برنامه پس از پیدا کردنِ خطا، *رفعِ اشکال* می‌گویند.

## نسخهٔ چهارم

با نامِ `backup_ver4.py` ذخیره کنید:

```python
import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
```

خروجی:

```text
$ python backup_ver4.py
Enter a comment --> added new examples
Zip command is:
zip -r /Users/swa/backup/20140329/074122_added_new_examples.zip /Users/swa/notes
Running:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
Successful backup to /Users/swa/backup/20140329/074122_added_new_examples.zip
```

**چگونه کار می‌کند**

حالا برنامه کار می‌کند! بیایید بهبودهایی را مرور کنیم که در نسخهٔ سوم در نظر گرفته بودیم. با تابعِ `input` توضیحِ کاربر را می‌گیریم. سپس با تابعِ `len` طولِ ورودی را بررسی می‌کنیم تا ببینیم آیا چیزی نوشته است یا نه. اگر کاربر بدون نوشتنِ چیزی فقط `enter` زده باشد، مثل قبل پیش می‌رویم؛ شاید صرفاً یک پشتیبان‌گیریِ روزمره بوده یا تغییرِ خاصی رخ نداده است.

اما اگر توضیحی نوشته باشد، آن را درست پیش از پسوندِ `.zip` به نام فایل اضافه می‌کنیم. به این نکته توجه کنید که فاصله‌های توضیح را با زیرخط جایگزین می‌کنیم؛ مدیریتِ نام فایل‌های بدون فاصله آسان‌تر است.

## بهبودهای بیشتر

نسخهٔ چهارم برای بیشترِ کاربران، اسکریپتِ قابل‌قبولی است؛ اما همیشه می‌توان آن را بهتر کرد. مثلاً با گزینهٔ `-v` می‌توانید خروجیِ فرمان zip را پرجزئیات‌تر کنید، یا با `-q` آن را کم‌حرف‌تر کنید.

بهبود دیگر این است که کاربر بتواند فایل‌ها و پوشه‌های بیشتری را از خط فرمان به اسکریپت بدهد. می‌توانیم نامِ آنها را از فهرستِ `sys.argv` بگیریم و با متدِ `extend` کلاسِ `list` به فهرستِ `source` اضافه کنیم.

مهم‌ترین بهبود این است که برای ساختنِ بایگانی، به‌جای `os.system` از ماژول‌های کتابخانهٔ استانداردِ [zipfile](http://docs.python.org/3/library/zipfile.html) یا [tarfile](http://docs.python.org/3/library/tarfile.html) استفاده کنیم. این ماژول‌ها بدون نیاز به نصبِ برنامهٔ جداگانهٔ zip در دسترس‌اند.

با این حال، در مثال‌های بالا صرفاً به دلیلِ آموزشی از روشِ `os.system` استفاده کرده‌ام: نمونه باید به‌اندازه‌ای ساده باشد که همه بتوانند آن را بفهمند و در عین حال، کاربردی هم باشد.

می‌توانید نسخهٔ پنجم را طوری بنویسید که به‌جای فراخوانیِ `os.system` از ماژولِ [zipfile](http://docs.python.org/3/library/zipfile.html) استفاده کند؟

## فرایندِ توسعهٔ نرم‌افزار

حالا مرحله‌های مختلفِ نوشتنِ یک نرم‌افزار را طی کرده‌ایم. می‌توانیم آنها را این‌طور خلاصه کنیم:

1. چه می‌خواهیم؟ — تحلیل (Analysis)
2. چطور انجامش دهیم؟ — طراحی (Design)
3. انجامش بده — پیاده‌سازی (Implementation)
4. بررسی‌اش کن — آزمایش و اشکال‌زدایی (Testing and Debugging)
5. به کارش بگیر — بهره‌برداری یا استقرار (Operation or Deployment)
6. بهترش کن — نگهداری و بهبود (Refinement)

روشِ پیشنهادی برای برنامه‌نویسی، همان مسیری است که برای ساختنِ اسکریپتِ پشتیبان‌گیری دنبال کردیم: اول تحلیل و طراحی، بعد پیاده‌سازیِ یک نسخهٔ ساده. آن را آزمایش و اشکال‌زدایی کنید و به کار بگیرید تا مطمئن شوید مطابق انتظار کار می‌کند. سپس قابلیت‌های دلخواه را اضافه کنید و چرخهٔ «انجام بده، آزمایش کن، به کار بگیر» را هرچند بار که لازم است تکرار کنید.

به یاد داشته باشید:

> نرم‌افزار پرورش می‌یابد، نه اینکه صرفاً ساخته شود.
> — [Bill de hÓra](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch97.html)

## جمع‌بندی

دیدیم چطور برنامه یا اسکریپتِ پایتونِ خودمان را بسازیم و برای نوشتنِ آن چه مرحله‌هایی را طی کنیم. حالا شما هم می‌توانید مانندِ نمونهٔ این فصل، برنامه‌ای برای خودتان بنویسید تا هم با پایتون راحت‌تر شوید و هم مهارتِ حلِ مسئله را تمرین کنید.

در فصلِ بعد، دربارهٔ برنامه‌نویسیِ شیءگرا صحبت می‌کنیم.

---

متنِ اصلی: [Problem Solving — A Byte of Python](https://python.swaroopch.com/problem_solving.html)، اثرِ Swaroop C H.
منبعِ این پیش‌نویس: [نسخهٔ ثابتِ فصل و مثال‌ها](https://github.com/swaroopch/byte-of-python/tree/84f4dd8d6f09836fa58226eaafe922b8a7baabc6)، بررسی‌شده در ۲۰ نوامبر ۲۰۲۶.
ترجمهٔ کمک‌گرفته از هوش مصنوعی در پروژهٔ Mohammadali Masjedi؛ بازخوانیِ نهاییِ انسانی هنوز انجام نشده است.
متن: CC BY-SA 4.0؛ کد و خروجیِ مثال‌های کتاب با انتساب و مجوزِ BSD سه‌بندیِ موجود در مخزن.
