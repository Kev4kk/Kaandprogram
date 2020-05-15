# Kaanamine
8. klassi loovtöö 2018/19 õppeaastal\
Miina Härma Gümnaasium\
Autor: Kevin Akkermann\
Python 3.7\
juhendaja Allar Aav
 
## Nõuded arvutile:
Kindlasti töötab Windows 10-l\
Vajalik on Python 3.x olemasolu\
Python peab olema Path muutujas, kuna programm kasutab kolme pip-iga installitavat moodulit, mille programm ise installib\
Kasutajal peab olema arvutis adminiõigused\
Vajalik on internetiühendus

## Programmi sisu:
Programmi eesmärk on käänata otsitud sõna\
Selleks lehitseb programm otsitud sõna ÕS-i, et saada käändelõpud\
Kui ühel sõnal on kaks sama vormi, kuid erinevad tähendused\
Programm väljastab kõikides ainsuse ja mitmuse käänetes\
Vasakus ülemises nurgas saab vahetada UI keelt\
Konsooli väljastab programm selle, mille ta leidis lehelt
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

## Contributing/panustamine
Pull requeste pole vaja, lõpetatud programm\
Kui leiate mõne errori (mitte valesti käänatud sõna), siis võtke minuga ühendust.
