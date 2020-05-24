# Käändprogramm
English Below\
8. klassi loovtöö 2018/19 õppeaastal\
Miina Härma Gümnaasium\
Autor: Kevin Akkermann\
Python 3.7.0\
beautifoulsoup4 4.6.3\
lxml 4.2.5\
requests 2.20.1\
urllib3 1.24.1\
juhendaja Allar Aav

## Programmi sisu:
Programmi eesmärk on käänata otsitud sõna\
Selleks lehitseb programm otsitud sõna ÕS-i, et saada käändelõpud\
Kui ühel sõnal on kaks sama vormi, kuid erinevad tähendused\
Programm väljastab kõikides ainsuse ja mitmuse käänetes\
Vasakus ülemises nurgas saab vahetada UI keelt\
Konsooli väljastab programm selle, mille ta leidis lehelt\
Osad sõnad on vigased, kuna erinevaid erandeid on mustmiljon

## Tavalised probleemid:
#### Kui tekib ModuleError
Programm ei suutnud õiget moodulit installida\
Kas Python on PATH muutujas ja kas oled adminiõigustega?\
Manuaalne moodulite install\
Käsureale:
```
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install lxml
```
Soovitatav on esimesel korral kaks korda käivitada programmi

## Panustamine
Pull requeste pole vaja, lõpetatud programm\
Kui leiate mõne errori (mitte valesti käänatud sõna), siis võtke minuga ühendust.

## Nõuded arvutile:
Kindlasti töötab Windows 10-l\
Vajalik on vähemalt Python 3.7 olemasolu\
Python peab olema Path muutujas, kuna programm kasutab kolme pip-iga installitavat moodulit, mille programm ise installib\
Kasutajal peab olema arvutis adminiõigused\
Vajalik on internetiühendus

# English
8th grade project on 2018/19 year\
Miina Härma Gymnasium\
Made by: Kevin Akkermann\
Using Python 3.7.0\
beautifoulsoup4 4.6.3\
lxml 4.2.5\
requests 2.20.1\
urllib 1.24.1\
Supervised by Allar Aav

## The program
The goal for the program is to modify Estonian nouns\
It uses web scraping on ÕS to find the necessary data for modifying\
If a word has two different meanings and conjugation forms, the program will display both\
The program outputs both singular and plural modifications\
You can change the language of the UI in the top left corner\
There still may be buggy words, because there are too many exceptions in a language

## Common problems
#### Python ModuleError
The program couldn't open a certain module\
Make sure that Python is in the PATH environment variable and You have admin rights on the computer you're using\
If this doesn't help, manually install all the modules through command prompt
```
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install lxml
```
It is recommended to launch the program two times on first time use

## Contribution
No need for pull requests since it's a finished project\
If You do find some bugs that crash the program please let me know

## Specifications
The program definitely works on Windows 10\
The Python version should be 3.7.0 and up\
Python needs to be in the PATH variable, since it uses pip to install certain modules\
The user needs to have admin rights on the PC that they are using\
A stable internet connection is required
