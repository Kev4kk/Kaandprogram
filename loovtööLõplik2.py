#Sõnade Käänamine
#Kevin Akkermann 2018/19

#!/usr/bin/python
# python3
# -*- coding: utf-8 -*-
import os, re, sys, time

#process = psutil.Process(os.getpid())



try:#vajadusel installib moodulid
  import requests
except ImportError:
  print("Hakkan laadima moodulit: requests")
  os.system('python -m pip install requests')
from urllib.request import urlopen
print("Avatud moodul requests")

try:
  import bs4
except ImportError:
  print("Hakkan laadima moodulit: bs4\n")
  os.system('python -m pip install beautifulsoup4')
  os.system('python -m pip install lxml')
from bs4 import BeautifulSoup
print("Avatud moodul bs4")

from tkinter import *
print("Avatud moodul tkinter")



#funktsioonid

def sonekontroll(sone):#asendab sõnes täpitähed ja väljastab sõna
    sonelist = list(sone) 
    for y in range(len(sonelist)):
        if sonelist[y] == "õ":
            sonelist[y] = "%C3%B5"
        elif sonelist[y] == "ä":
            sonelist[y] = "%C3%A4"
        elif sonelist[y] == "ö":
            sonelist[y] = "%C3%B6"
        elif sonelist[y] == "ü":
            sonelist[y] = "%C3%BC"
        elif sonelist[y] == "š":
            sonelist[y] = "%C5%A1"
        elif sonelist[y] == "ž":
            sonelist[y] = "%C5%BE"
    return ''.join(sonelist)

def puhasta(string, märk): #puhastab märgist ja tagastab sõne
    return string.replace(märk, "")

def clearDictionary(diction, algsõna):#teeb dictionary tühjaks ja väljastab selle
    diction = diction.fromkeys(diction, "")
    diction["nimetav"] = algsõna
    return diction

def silbita(sõna):#returnib silbitatud sõna listina
    taishaalikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashaalikud = ["h", "j", "l", "m", "n", "r", "s", "h", "f", "v",  "š", "z", "ž", "f", "k", "p", "t", "g", "b", "d"]
    silbid = []
    if len(sõna) <= 2:
        return sõna
    pikkus = len(sõna)
    i = 1
    while i < pikkus:
        #print(sõna, silbid, i, pikkus)
        if i +1== pikkus:
            silbid.append(sõna)
            break
        elif (sõna[i] in kaashaalikud and sõna[i+1] in taishaalikud):
            silbid.append(sõna[0:i])
            sõna = sõna[i:]
            pikkus -= len(silbid[-1])
            i = 0
        elif pikkus - i >= 3 and sõna[i] in taishaalikud and sõna[i+1] in taishaalikud and sõna[i+1] != sõna[i] and sõna[i+2] in taishaalikud and sõna[i+2] != sõna[i] and sõna[i+2] == sõna[i+1]:
            silbid.append(sõna[0:i+1])
            sõna = sõna[i+1:]
            pikkus -= len(silbid[-1])
            i = 0
        elif pikkus - i == 1 and sõna[i] in taishaalikud:
            pass
        i+= 1
    #print(silbid)
    return silbid


def omastaVäärtus(dictionary, key, value):#omastab väärtuse sõnastikule ja väljastab sõnastiku
    dictionary[key] = value#tegin lihtsalt selle, sest on hea praktika kasutada "private" muutujaid
    return dictionary
  
def printDict(dictionary):#väljastab dictionary
    for i in dictionary:
        print(i + ": " + dictionary[i])
    return


def KoledadIfid(sõna, tyyp, dic, kaanded):#string, array, dictionary, array
    #peenhäälestus teatud sõnadele
    käändeLõpud = ["sse", "s", "st", "le", "l", "lt", "ks", "ni", "na", "ta", "ga"]
    käändedAinsuses = {"nimetav": sõna, "omastav": "", "osastav": "", "sisseütlev": "", "seesütlev": "", "seestütlev": "", "alaleütlev": "", "alalütlev": "", "alaltütlev": "", "saav": "", "rajav": "", "olev": "", "ilmaütlev": "", "kaasaütlev": "", }
    käändedList = list(käändedAinsuses.keys())
    if dic["osastav"] == "":
        if "2" in tyyp or "2e" in tyyp or "16" in tyyp or "1" in tyyp or "1e" in tyyp:
            if tyyp == ["1e"]:
                if dic["omastav"] == "":
                    dic["omastav"] = dic["nimetav"]
            dic["osastav"] = dic["omastav"]+"t"
        elif  "26" in tyyp or "26i" in tyyp:
            if dic["omastav"] == "":
                dic["omastav"] = sõna
            dic["osastav"] = dic["omastav"] + "d"
            
    if "22e" in tyyp or "22" in tyyp or "22i" in tyyp or "22u" in tyyp or "23e" in tyyp or "23i" in tyyp or "23u" in tyyp or "24" in tyyp or "24e" in tyyp or "24i" in tyyp or "24u" in tyyp:
        dic["sisseütlev"] = dic["sisseütlev"] + " ja " + dic["osastav"]

    if "13" in tyyp:
        dic["sisseütlev"] = sõna + "de" + " ja " + dic["sisseütlev"]

    if "16" in tyyp:
        if dic["omastav"] == "":
            dic["omastav"] = sõna
            dic["osastav"] = sõna + "t"
        
        
    
    if "17" in tyyp or "17e" in tyyp or "17i" in tyyp or "17u" in tyyp:
        if dic["omastav"] == "":
            dic["omastav"] = sõna
        dic["osastav"] = sõna
            
        if kaanded[0] not in tyyp:
            dic["sisseütlev"] = kaanded[0]
        if dic["omastav"] == kaanded[0]:
            dic["omastav"] = dic["nimetav"]
        #print(dic)
        for l in range(len(kaanded)):
            dic[käändedList[l+3]] = kaanded[l]
        if "ja" in dic["seesütlev"]:
            for p in range(4, 14):
                #print(p)
                dic[käändedList[p]] = dic["omastav"] + käändeLõpud[p-3]
                
    if tyyp == ["11"]:
        if dic["omastav"] == "":
            dic["omastav"] = sõna+"e"
        if dic["osastav"] == "":
            dic["osastav"] = sõna + "t"
        dic["sisseütlev"] = dic["sisseütlev"] + " ja " + sõna + "se"

    if tyyp == ["12"] or ("12" in tyyp and "10" in tyyp):
        if sõna[-2:] == "ne":
            var = dic["omastav"].find(sõna[-4:-2])
            dic["omastav"] = dic["omastav"][:var+1] + dic["omastav"][var+3:]
        if dic["osastav"] == "":
            dic["osastav"] = dic["omastav"][:-1] + "t"
        dic["sisseütlev"] = dic["omastav"][:-1]+ "se" + " ja " + dic["omastav"] + "sse"
    if "11" in tyyp and "9" in tyyp:
        if dic["osastav"] == "":
            dic["osastav"] = sõna + "t"
    if tyyp == ["25"]:
      dic["sisseütlev"] = dic["sisseütlev"] + " ja " + dic["osastav"]
    if "19" in tyyp:
       dic["sisseütlev"] = dic["sisseütlev"] + " ja " + dic["osastav"]
    if kaanded[0] == "17 ja 16":
        dic["sisseütlev"] = sõna + "sse"
    if "12" in tyyp and "10" in tyyp:
        if dic["osastav"] == "":
            dic["osastav"] = dic["omastav"][:-1] + "t"
    if "26" in tyyp[0]:
        if dic["omastav"].isalpha() == False:
            dic["omastav"] = dic["nimetav"]
        if len(dic["osastav"]) < 2:
            dic["osastav"] = dic["omastav"] + "d"
        for z in range(3, 14):
            dic[käändedList[z]] = str(dic["omastav"] + käändeLõpud[z-3])
    for i, j in dic.items():
        if j.isdecimal() == True:
            dic[i] = dic["omastav"] + käändeLõpud[käändedList.index(i)-3]

    if "ja" in dic["omastav"]:
            algomastav = dic["omastav"][0:dic["omastav"].find(" ")]
            for j in range(3, 14):
                dic[käändedList[j]] = str(algomastav+ käändeLõpud[j-3])
   
    if dic["omastav"][-1] == "a":
        for i in range(3, 14):
            dic[käändedList[i]] = dic["omastav"]+ käändeLõpud[i-3]
    for j in range(3, 14):
        if dic[käändedList[j]] == "":
            
            dic[käändedList[j]] = str(dic["omastav"] + käändeLõpud[j-3])
    return dic


        


def puhastaHtmlTag(sõna):
    #print(sõna)
    markalanud = False
    sõna = list(str(sõna))
    i= 0
    pikk = len(sõna)
    while i < pikk:
        if sõna[i] == "<":
            markalanud = True
            del sõna[i]
            pikk-= 1
            i-= 1
        elif sõna[i] == ">":
            markalanud = False
            del sõna[i]
            pikk-= 1
            i-= 1
        elif markalanud:
            del sõna[i]
            pikk-= 1
            i-= 1
        i+=1
    return "".join(sõna)
            

def pohiprogramm(sona):
    nim = []
    om = []
    os = []
    sis = []
    ses = []
    sst = []
    lle = []
    lal = []
    llt = []
    sav = []
    raj = []
    olv = []
    ilm = []
    kaa = []
    tyybid = []
    sona = sona.lower()
    mitmussd = []
    htmlsone = sonekontroll(sona)
    link = "https://www.eki.ee/dict/qs/index.cgi?Q="+htmlsone+"&F=M"
    tugevadsulghaalikud = ["k", "p", "t"]
    norgadsulghaalikud = ["g", "b", "d"]
    taishaalikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashaalikud = ["h", "j", "l", "m", "n", "r", "s", "h", "f", "š", "z", "ž", "k", "p", "t", "g", "b", "d"]
    tegusonad = ["27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "37i", "38", "38i"]
    #dictionary kõikide käänete jaoks
    käändedAinsuses = {"nimetav": sona, "omastav": "", "osastav": "", "sisseütlev": "", "seesütlev": "", "seestütlev": "", "alaleütlev": "", "alalütlev": "", "alaltütlev": "", "saav": "", "rajav": "", "olev": "", "ilmaütlev": "", "kaasaütlev": "", }
    käändedList = list(käändedAinsuses.keys())
    #alates sisseütlevast
    käändeLõpud = ["sse", "s", "st", "le", "l", "lt", "ks", "ni", "na", "ta", "ga"]
    #põhiprogramm




    
    html = urlopen(link)
    
    soup = BeautifulSoup(html, "lxml")
    teg = False
    lõpptäht = ""
    mitusõna = 0
    JärgLeitud = 0
    spanstr = ""
    ad = soup.find_all("p", {"class": "inf"})
    #print(puhastaHtmlTag(ad[0]), "\n")
    span = soup.find_all("span")
    liitsonaproov = soup.find_all("span", {"class": "m leitud_id"})
    leitudsonaproov = soup.find("span", {"class": "m"})
    #print(liitsonaproov)
    #print(leitudsonaproov)
    #print(span)
    for j in range(0, len(span)):
        osa = span[j]
        for content in osa:
            spanstr += str(content)#leiab koodist rea kaupa kõik span tagiga read ja salvestab stringi
        #print(spanstr)

            #kui pole sama sõna nt külmkapp
        if "ÕS" in spanstr:
            JärgLeitud = 3
        elif JärgLeitud == 3:
            if puhastaHtmlTag(puhasta(puhasta(spanstr, "`"), "'")) == puhasta(sona, "`"):
                JärgLeitud = 0
            else:
                #print("Tegu pole sama sõnaga, kuid sama tähendusega või on tehtud typo")
                #print(spanstr)
                sona = puhastaHtmlTag(puhasta(puhasta(spanstr, "`"), "'"))
                omastaVäärtus(käändedAinsuses, "nimetav", sona)
                JärgLeitud = 0


        elif "javascript" in spanstr and '"mt"' in spanstr:
            print(spanstr)
            muutujaKusOnKoikVajalikInfoAgaMaOlinLiigaLollEtMärgata = puhasta(puhasta(puhastaHtmlTag(spanstr), "'"), "`")
            pool = muutujaKusOnKoikVajalikInfoAgaMaOlinLiigaLollEtMärgata.split(":")
            tyypnumber = pool[0]
            tyypnumber = puhasta(puhasta(puhasta(puhasta(tyypnumber, "("), ")"), "´"), " ").split("ja")
            kaanded = puhasta(muutujaKusOnKoikVajalikInfoAgaMaOlinLiigaLollEtMärgata, "´").split(":")[-1]
            kaanded = str(kaanded).split(";")
            kaandedainsus = kaanded[0].split(",")
            if len(kaanded) >= 2:
                mitmuss = kaanded[1].split(",")
            else:
              mitmuss = []
            
            #tegusõnade eraldamiseks
            for r in tyypnumber:
                if r in tegusonad:
                    teg = True
                    #print("Tegusõna, seda ma ei kääna")
                    return "Tegusõna"
            while teg == False:
                for s in range(len(kaandedainsus)):
                    if kaandedainsus[s][0] == " ":
                        kaandedainsus[s] = kaandedainsus[s][1:]

                        
                if kaanded == tyypnumber:#pole käändeid
                    käändedAinsuses["omastav"] = sona
                elif len(kaandedainsus) == 1 and "-" not in kaandedainsus[0]:
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "omastav", kaandedainsus[0])
                    for u in range(0, 11):
                        käändedAinsuses = omastaVäärtus(käändedAinsuses, käändedList[u+3], kaandedainsus[0] + käändeLõpud[u])
                elif len(kaandedainsus) == 2 and "-" not in kaandedainsus[0]:
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "omastav", kaandedainsus[0])
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "osastav", kaandedainsus[1])
                    for u in range(0, 11):
                        käändedAinsuses = omastaVäärtus(käändedAinsuses, käändedList[u+3], kaandedainsus[0]+käändeLõpud[u])

                elif len(kaandedainsus) == 3 and "-" not in kaandedainsus[0]:
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "omastav", kaandedainsus[0])
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "osastav", kaandedainsus[1])
                    käändedAinsuses = omastaVäärtus(käändedAinsuses, "sisseütlev", kaandedainsus[2])
                    for u in range(1, 11):
                        käändedAinsuses = omastaVäärtus(käändedAinsuses, käändedList[u+3], kaandedainsus[0]+käändeLõpud[u])

                
                elif kaandedainsus[0][0] == "-":
                    if len(kaandedainsus) == 1:
                        if len(puhasta(kaandedainsus[0], "-")) <= 2:
                            käändedAinsuses = omastaVäärtus(käändedAinsuses, "omastav", sona+puhasta(kaandedainsus[0], "-"))
                        else:
                            var = silbita(sona)
                            del var[-1]
                            var = str("".join(var))
                            käändedAinsus = omastaVäärtus(käändedAinsuses, "omastav", var+puhasta(kaandedainsus[0], "-"))
                            
                    elif len(kaandedainsus)  == 2:
                        if len(puhasta(kaandedainsus[0], "-")) <= 2 and len(puhasta(kaandedainsus[1], "-")) <=2:
                            käändedAinsuses = omastaVäärtus(käändedAinsuses, "omastav", sona+puhasta(kaandedainsus[0], "-"))
                            käändedAinsuses = omastaVäärtus(käändedAinsuses, "osastav", sona+puhasta(kaandedainsus[1], "-"))
                        else:
                            var = silbita(sona)
                            del var[-1]
                            var = str("".join(var))
                            käändedAinsus = omastaVäärtus(käändedAinsuses, "omastav", var+puhasta(kaandedainsus[0], "-"))

                            var = silbita(sona)
                            del var[-1]
                            var = str("".join(var))
                            #print(var)
                            käändedAinsuses = omastaVäärtus(käändedAinsuses, "osastav", var+puhasta(kaandedainsus[1], "-"))


                            
                        for j in range(3, 14):
                            if käändedAinsuses[käändedList[j]] == "":
                                käändedAinsuses[käändedList[j]] = str(käändedAinsuses["omastav"] + käändeLõpud[j-3])
                JärgLeitud = 0  
                käändedAinsuses = KoledadIfid(sona, tyypnumber, käändedAinsuses, kaandedainsus)
                print(tyypnumber, kaandedainsus)
                #printDict(käändedAinsuses) 
                #mitmus(käändedAinsuses, tyypnumber, mitmuss)
                #return käändedAinsuses, puhastaHtmlTag(ad[0]), tyypnumber, mitmuss##IDEE; dictionarylistina mitmeid "viis"
                #print("\n")

                nim.append(käändedAinsuses["nimetav"])
                om.append(käändedAinsuses["omastav"])
                os.append(käändedAinsuses["osastav"])
                sis.append(käändedAinsuses["sisseütlev"])
                ses.append(käändedAinsuses["seesütlev"])
                sst.append(käändedAinsuses["seestütlev"])
                lle.append(käändedAinsuses["alaleütlev"])
                lal.append(käändedAinsuses["alalütlev"])
                llt.append(käändedAinsuses["alaltütlev"])
                sav.append(käändedAinsuses["saav"])
                raj.append(käändedAinsuses["rajav"])
                olv.append(käändedAinsuses["olev"])
                ilm.append(käändedAinsuses["ilmaütlev"])
                kaa.append(käändedAinsuses["kaasaütlev"])
                tyybid.append(tyypnumber)
                #print(mitmuss)
                if mitmuss == []:
                    mitmussd.append([])
                else:
                    mitmussd.append(mitmuss)
                #print(tyybid, kaandedainsus)
                #print(nim, om, os, sis, ses, sst, lle, lal, llt, sav, raj, olv, ilm, kaa)
                clearDictionary(käändedAinsuses, sona)
                mitmuss = []
                teg = False
                break
        spanstr=''


        puhas = ""
    #print("\n", mitmussd)
    return [nim, om, os, sis, ses, sst, lle, lal, llt, sav, raj, olv, ilm, kaa], puhastaHtmlTag(ad[0]), tyybid, mitmussd

def mitmus(ainsus, tyyp, mitmu): #dict, list, list
    käändeLõpud = ["sse", "s", "st", "le", "l", "lt", "ks", "ni", "na", "ta", "ga"]
    kaashaalikud = ["h", "j", "l", "m", "n", "r", "s", "h", "f", "š", "z", "ž", "k", "p", "t", "g", "b", "d"]
    käändedMitmuses = {"nimetav": "", "omastav": "", "osastav": "", "sisseütlev": "", "seesütlev": "", "seestütlev": "", "alaleütlev": "", "alalütlev": "", "alaltütlev": "", "saav": "", "rajav": "", "olev": "", "ilmaütlev": "", "kaasaütlev": ""}
    käändedList = list(käändedMitmuses.keys())
    #print(käändedList)
    
    käändedMitmuses["nimetav"] = ainsus["omastav"] + "d"
    #print(mitmu)
    z = 0
    while z < len(mitmu):
        if mitmu == [""]:
            mitmu = []
            break
        if mitmu[z][0] == " ":
            mitmu[z] = mitmu[z][1:]
            #if mitmu[z][0] == " ":
                #mitmu[z] = mitmu[z][1:]
        #print(mitmu[z][0:4])
        if mitmu[z][0:5] == "keskv":
            del mitmu[z]
            z-=1
        elif mitmu[z][0:4] == "üliv":
            del mitmu[z]
            break
        z+=1
        if puhasta(mitmu[0], " ") == "täiendinaeikäändu":
            del mitmu[0]
    if tyyp[0][0:4] == "argi":
      tyyp[0] = tyyp[0][4:]
    if len(mitmu) == 3:
        for g in range(1, len(mitmu)-1):
            käändedMitmuses[käändedList[g]] = mitmu[g-1]
    else:
        for g in range(2, len(mitmu) + 2):
            käändedMitmuses[käändedList[g]] = mitmu[g-2]
    
    
    if käändedMitmuses["omastav"] == "":
        if "1" in tyyp or "1e" in tyyp or "2" in tyyp or "2e" in tyyp or "3" in tyyp or "3e" in tyyp or "4" in tyyp or "5" in tyyp or "5e" in tyyp:
            käändedMitmuses["omastav"] = ainsus["omastav"] + "te"
        elif "6" in tyyp or "7" in tyyp or tyyp == ["7e"] or "9" in tyyp or "11" in tyyp or "23e" in tyyp or "23i" in tyyp or "23u" in tyyp or "13" in tyyp:
            #kaashäälikuühend
            if ainsus["nimetav"][-1] == ainsus["nimetav"][-2] and ainsus["nimetav"][-1] in kaashaalikud:
                käändedMitmuses["omastav"] = ainsus["nimetav"][:-1] + "te"
            else:
                käändedMitmuses["omastav"] = ainsus["nimetav"] + "te"
        elif "8" in tyyp or "16" in tyyp or "17" in tyyp or "17e" in tyyp or "17i" in tyyp or "17u" in tyyp or "18" in tyyp or "18e" in tyyp or "18u" in tyyp or "26i" in tyyp:
            käändedMitmuses["omastav"] = ainsus["nimetav"] + "de"
        elif "10" in tyyp or "12" in tyyp or "14" in tyyp or "26" in tyyp or "26" in tyyp or "26" in tyyp[0]:
            käändedMitmuses["omastav"] = ainsus["osastav"] + "e"
        elif "15" in tyyp or "24" in tyyp:
            käändedMitmuses["omastav"] = ainsus["osastav"][:-1] + "e"
            
        elif "19" in tyyp or "20" in tyyp or "21" in tyyp or "22" in tyyp or "22e" in tyyp or "22i" in tyyp or "22u" in tyyp or "24" in tyyp or "24e" in tyyp or "24i" in tyyp or "24u" in tyyp:
            käändedMitmuses["omastav"] = ainsus["osastav"] + "de"
        elif "25" in tyyp:
            käändedMitmuses["omastav"] = ainsus["nimetav"] + "e" + " ja " + ainsus["osastav"] + "de"
    if käändedMitmuses["osastav"] == "":
        if "1" in tyyp or "2" in tyyp or "3" in tyyp or "4" in tyyp or "5" in tyyp or "6" in tyyp or "7" in tyyp or "8" in tyyp or "9" in tyyp or "10" in tyyp:
            käändedMitmuses["osastav"] = ainsus["omastav"] + "id"
        elif "1e" in tyyp or "2e" in tyyp or "3e" in tyyp or "5e" in tyyp or "7e" in tyyp:
            käändedMitmuses["osastav"] = ainsus["omastav"][:-1] + "eid"
        elif "11" in tyyp or "13" in tyyp or "14" in tyyp:
            käändedMitmuses["osastav"] = ainsus["nimetav"] + "i"
        elif "12" in tyyp or "15" in tyyp:
            käändedMitmuses["osastav"] = ainsus["omastav"][:-1] + "i"
        elif "16" in tyyp or "17" in tyyp or "17e" in tyyp or "17i" in tyyp or "17u" in tyyp or "18" in tyyp or "18e" in tyyp or "18u" in tyyp or "26" in tyyp or "26i" in tyyp:
            käändedMitmuses["osastav"] = ainsus["nimetav"] + "sid"
        elif "19" in tyyp or "23i" in tyyp:
            käändedMitmuses["osastav"] = ainsus["nimetav"] + "e"
        elif "20" in tyyp:
            käändedMitmuses["osastav"] = ainsus["omastav"] + "sid"
        elif "21" in tyyp or "22" in tyyp or "22e" in tyyp or "22i" in tyyp or "22u" in tyyp or "23i" in tyyp or "23u" in tyyp or "24" in tyyp or "24e" in tyyp or "24i" in tyyp or "24u" in tyyp:
            käändedMitmuses["osastav"] = ainsus["osastav"] + "sid"
        elif "25" in tyyp:
            käändedMitmuses["osastav"] = ainsus["nimetav"] + "ke"

    if "25" in tyyp:
        for n in range(3, 14):
            if käändedMitmuses[käändedList[n]] == "":
                käändedMitmuses[käändedList[n]] = käändedMitmuses["omastav"].split()[0] + käändeLõpud[n-3] + " ja " + käändedMitmuses["omastav"].split()[-1] + käändeLõpud[n-3]
    else:
        for n in range(3, 14):
            if käändedMitmuses[käändedList[n]] == "":
                käändedMitmuses[käändedList[n]] = käändedMitmuses["omastav"] + käändeLõpud[n-3]
    if "ja" not in käändedMitmuses["sisseütlev"]:
        if "1" in tyyp or "2" in tyyp or "3" in tyyp or "4" in tyyp or "5" in tyyp or "6" in tyyp or "7" in tyyp or "8" in tyyp or tyyp == ["9"] in tyyp or "10" in tyyp:
            for g in range(3, 14):
                käändedMitmuses[käändedList[g]] = käändedMitmuses[käändedList[g]] + " ja " + ainsus["omastav"] + "i"+käändeLõpud[g-3]
        elif "1e" in tyyp or "2e" in tyyp or "3e" in tyyp or "5e" in tyyp or "7e" in tyyp:
            for g in range(3, 14):
                käändedMitmuses[käändedList[g]] = käändedMitmuses[käändedList[g]] + " ja "+ käändedMitmuses["osastav"][:-1]+käändeLõpud[g-3]
        elif "11" in tyyp or "12" in tyyp or "13" in tyyp or "14" in tyyp or "15" in tyyp:
            for g in range(3, 14):
                käändedMitmuses[käändedList[g]] = käändedMitmuses[käändedList[g]] + " (ja "+ainsus["omastav"][:-1]+"i"+käändeLõpud[g-3] + ")"
        #printDict(käändedMitmuses)
    #print("\n")
    #17x, 18, 19, 22, 23, 24, 26
    return käändedMitmuses
keelint = 0
keel = [["English", "Sisesta sõna:", "Ainsus:", "Mitmus:", "Nimetav:", "Omastav:", "Osastav:", "Sisseütlev:", "Seesütlev:", "Seestütlev:", "Alaleütlev:", "Alalütlev:", "Alaltütlev:", "Saav:", "Rajav:", "Olev:", "Ilmaütlev:", "Kaasaütlev:", "Kääna (Enter)"], ["Eesti", "Enter a word:", "Singular:", "Plural:", "Nominative:", "Genitive:", "Partitive:", "Illative:",  "Inessive:", "Elative:", "Allative:", "Adessive:", "Ablative:", "Translative:", "Terminative:", "Essive:", "Abessive:", "Comitative:", "Decline(Enter)"]]
#We're in the endgame now
def GUI():
    global btn_txt
    global keel
    global keelint
    raam = Tk()
    raam.title(" ")
    #raam.geometry("300x550")
    raam.resizable(False, False)
    raam.esimene = True

    mnim = []
    mom = []
    mos = []
    msis = []
    mses = []
    msst = []
    mlle = []
    mlal = []
    mllt = []
    msav = []
    mraj = []
    molv = []
    milm = []
    mkaa = []
    knddlist = ["nimetav", "omastav", "osastav", "sisseütlev", "seesütlev", "seestütlev", "alaleütlev", "alalütlev", "alaltütlev", "saav", "rajav", "olev", "ilmaütlev", "kaasaütlev"]
    def valjPettus(event):
        valj()
    
    
    def valj():
        sis.selection_range(0, END)
        streng.set("")
        mnim = []
        mom = []
        mos = []
        msis = []
        mses = []
        msst = []
        mlle = []
        mlal = []
        mllt = []
        msav = []
        mraj = []
        molv = []
        milm = []
        mkaa = []
        sisend = sis.get()
        if sisend.isalpha() == False:
            strin.set("Palun sisesta ainult tähtedest koosnev sõna")
            streng.set("Please enter a word only consisting of letters")
            return
        vastus = pohiprogramm(sisend)
        if vastus == "Tegusõna":
            strin.set("Tegemist on tegusõnaga")
            streng.set("It is a verb")
            return
        #print(vastus)
        try:
            vastus[0]
        except TypeError:
            strin.set("Tegu on muutumatu sõnaga")
            streng.set("It is not a noun")
            return
        vastusdict = vastus[0]
        #mtms = mitmus(vastus[0], vastus[2], vastus[3])
        mitmdict = {}
        strin.set(vastus[1])
        for w in range(len(vastusdict[0])):
            for g in range(14):
                mitmdict[knddlist[g]] = vastusdict[g][w]
            #print("\n", mitmdict)
            #print(vastus[2][w], vastus[3][w])
            mtms = mitmus(mitmdict, vastus[2][w], vastus[3][w])
            #print(mtms)
            mnim.append(mtms["nimetav"])
            mom.append(mtms["omastav"])
            mos.append(mtms["osastav"])
            msis.append(mtms["sisseütlev"])
            mses.append(mtms["seesütlev"])
            msst.append(mtms["seestütlev"])
            mlle.append(mtms["alaleütlev"])
            mlal.append(mtms["alalütlev"])
            mllt.append(mtms["alaltütlev"])
            msav.append(mtms["saav"])
            mraj.append(mtms["rajav"])
            molv.append(mtms["olev"])
            milm.append(mtms["ilmaütlev"])
            mkaa.append(mtms["kaasaütlev"])
      
        
        ans1.set(", ".join(vastusdict[0]))
        ans2.set(", ".join(vastusdict[1]))
        ans3.set(", ".join(vastusdict[2]))
        ans4.set(", ".join(vastusdict[3]))
        ans5.set(", ".join(vastusdict[4]))
        ans6.set(", ".join(vastusdict[5]))
        ans7.set(", ".join(vastusdict[6]))
        ans8.set(", ".join(vastusdict[7]))
        ans9.set(", ".join(vastusdict[8]))
        ans10.set(", ".join(vastusdict[9]))
        ans11.set(", ".join(vastusdict[10]))
        ans12.set(", ".join(vastusdict[11]))
        ans13.set(", ".join(vastusdict[12]))
        ans14.set(", ".join(vastusdict[13]))
        
        mans1.set(", ".join(mnim))
        mans2.set(", ".join(mom))
        mans3.set(", ".join(mos))
        mans4.set(", ".join(msis))
        mans5.set(", ".join(mses))
        mans6.set(", ".join(msst))
        mans7.set(", ".join(mlle))
        mans8.set(", ".join(mlal))
        mans9.set(", ".join(mllt))
        mans10.set(", ".join(msav))
        mans11.set(", ".join(mraj))
        mans12.set(", ".join(molv))
        mans13.set(", ".join(milm))
        mans14.set(", ".join(mkaa))
        
        #print(raam.esimene)
        raam.esimene = False
    
    btn_txt = StringVar()    
    siltvar = StringVar()
    ainsusvar = StringVar()
    mitmusvar = StringVar()
    kaan1var = StringVar()
    kaan2var = StringVar()
    kaan3var = StringVar()
    kaan4var = StringVar()
    kaan5var = StringVar()
    kaan6var = StringVar()
    kaan7var = StringVar()
    kaan8var = StringVar()
    kaan9var = StringVar()
    kaan10var = StringVar()
    kaan11var = StringVar()
    kaan12var = StringVar()
    kaan13var = StringVar()
    kaan14var = StringVar()
    mkaan1var = StringVar()
    mkaan2var = StringVar()
    mkaan3var = StringVar()
    mkaan4var = StringVar()
    mkaan5var = StringVar()
    mkaan6var = StringVar()
    mkaan7var = StringVar()
    mkaan8var = StringVar()
    mkaan9var = StringVar()
    mkaan10var = StringVar()
    mkaan11var = StringVar()
    mkaan12var = StringVar()
    mkaan13var = StringVar()
    mkaan14var = StringVar()
    Käänatxt = StringVar()
    siltvar.set(keel[keelint][1])
    ainsusvar.set(keel[keelint][2])
    mitmusvar.set(keel[keelint][3])
    kaan1var.set(keel[keelint][4])
    kaan2var.set(keel[keelint][5])
    kaan3var.set(keel[keelint][6])
    kaan4var.set(keel[keelint][7])
    kaan5var.set(keel[keelint][8])
    kaan6var.set(keel[keelint][9])
    kaan7var.set(keel[keelint][10])
    kaan8var.set(keel[keelint][11])
    kaan9var.set(keel[keelint][12])
    kaan10var.set(keel[keelint][13])
    kaan11var.set(keel[keelint][14])
    kaan12var.set(keel[keelint][15])
    kaan13var.set(keel[keelint][16])
    kaan14var.set(keel[keelint][17])
    mkaan1var.set(keel[keelint][4])
    mkaan2var.set(keel[keelint][5])
    mkaan3var.set(keel[keelint][6])
    mkaan4var.set(keel[keelint][7])
    mkaan5var.set(keel[keelint][8])
    mkaan6var.set(keel[keelint][9])
    mkaan7var.set(keel[keelint][10])
    mkaan8var.set(keel[keelint][11])
    mkaan9var.set(keel[keelint][12])
    mkaan10var.set(keel[keelint][13])
    mkaan11var.set(keel[keelint][14])
    mkaan12var.set(keel[keelint][15])
    mkaan13var.set(keel[keelint][16])
    mkaan14var.set(keel[keelint][17])
    Käänatxt.set(keel[keelint][18])
    silt = Label(raam, textvariable = siltvar)
    silt.grid(column = 0, row = 0, padx = 10, pady = 5, sticky = (N, W))
    ainsussilt = Label(raam, textvariable = ainsusvar).grid(column = 0, row = 2, padx = 10, pady = 5, sticky = (W))
    mitmussilt = Label(raam, textvariable = mitmusvar).grid(column = 2, row = 2, padx = 10, pady = 5, sticky = (W))
    sis = Entry(raam)
    sis.grid(column = 1, row = 0, padx = 10, pady = 5, sticky = (W, E))
    sis.bind("<Return>", valjPettus)
    sis.focus()
    kaan1 = Label(raam,  textvariable = kaan1var )
    kaan1.grid(column = 0, row = 3, padx = 10, pady = 5, sticky = (W))
    kaan2 = Label(raam,  textvariable = kaan2var )
    kaan2.grid(column = 0, row = 4, padx = 10, pady = 5, sticky = (W))
    kaan3 = Label(raam,  textvariable = kaan3var )
    kaan3.grid(column = 0, row = 5, padx = 10, pady = 5, sticky = (W))
    kaan4 = Label(raam,  textvariable = kaan4var )
    kaan4.grid(column = 0, row = 6, padx = 10, pady = 5, sticky = (W))
    kaan5 = Label(raam,  textvariable = kaan5var )
    kaan5.grid(column = 0, row = 7, padx = 10, pady = 5, sticky = (W))
    kaan6 = Label(raam,  textvariable = kaan6var )
    kaan6.grid(column = 0, row = 8, padx = 10, pady = 5, sticky = (W))
    kaan7 = Label(raam,  textvariable = kaan7var )
    kaan7.grid(column = 0, row = 9, padx = 10, pady = 5, sticky = (W))
    kaan8 = Label(raam,  textvariable = kaan8var )
    kaan8.grid(column = 0, row = 10, padx = 10, pady = 5, sticky = (W))
    kaan9 = Label(raam,  textvariable = kaan9var )
    kaan9.grid(column = 0, row = 11, padx = 10, pady = 5, sticky = (W))
    kaan10 = Label(raam,  textvariable = kaan10var )
    kaan10.grid(column = 0, row = 12, padx = 10, pady = 5, sticky = (W))
    kaan11 = Label(raam,  textvariable = kaan11var )
    kaan11.grid(column = 0, row = 13, padx = 10, pady = 5, sticky = (W))
    kaan12 = Label(raam,  textvariable = kaan12var )
    kaan12.grid(column = 0, row = 14, padx = 10, pady = 5, sticky = (W))
    kaan13 = Label(raam,  textvariable = kaan13var )
    kaan13.grid(column = 0, row = 15, padx = 10, pady = 5, sticky = (W))
    kaan14 = Label(raam,  textvariable = kaan14var )
    kaan14.grid(column = 0, row = 16, padx = 10, pady = 5, sticky = (W))

    mkaan1 = Label(raam,  textvariable = mkaan1var )
    mkaan1.grid(column = 2, row = 3, padx = 10, pady = 5, sticky = (W))
    mkaan2 = Label(raam,  textvariable = mkaan2var )
    mkaan2.grid(column = 2, row = 4, padx = 10, pady = 5, sticky = (W))
    mkaan3 = Label(raam,  textvariable = mkaan3var )
    mkaan3.grid(column = 2, row = 5, padx = 10, pady = 5, sticky = (W))
    mkaan4 = Label(raam,  textvariable = mkaan4var )
    mkaan4.grid(column = 2, row = 6, padx = 10, pady = 5, sticky = (W))
    mkaan5 = Label(raam,  textvariable = mkaan5var )
    mkaan5.grid(column = 2, row = 7, padx = 10, pady = 5, sticky = (W))
    mkaan6 = Label(raam,  textvariable = mkaan6var )
    mkaan6.grid(column = 2, row = 8, padx = 10, pady = 5, sticky = (W))
    mkaan7 = Label(raam,  textvariable = mkaan7var )
    mkaan7.grid(column = 2, row = 9, padx = 10, pady = 5, sticky = (W))
    mkaan8 = Label(raam,  textvariable = mkaan8var )
    mkaan8.grid(column = 2, row = 10, padx = 10, pady = 5, sticky = (W))
    mkaan9 = Label(raam,  textvariable = mkaan9var )
    mkaan9.grid(column = 2, row = 11, padx = 10, pady = 5, sticky = (W))
    mkaan10 = Label(raam,  textvariable = mkaan10var )
    mkaan10.grid(column = 2, row = 12, padx = 10, pady = 5, sticky = (W))
    mkaan11 = Label(raam,  textvariable = mkaan11var)
    mkaan11.grid(column = 2, row = 13, padx = 10, pady = 5, sticky = (W))
    mkaan12 = Label(raam,  textvariable = mkaan12var)
    mkaan12.grid(column = 2, row = 14, padx = 10, pady = 5, sticky = (W))
    mkaan13 = Label(raam, textvariable = mkaan13var)
    mkaan13.grid(column = 2, row = 15, padx = 10, pady = 5, sticky = (W))
    mkaan14 = Label(raam, textvariable = mkaan14var)
    mkaan14.grid(column = 2, row = 16, padx = 10, pady = 5, sticky = (W))
    
    ans1 = StringVar()
    Label(raam, textvariable = ans1).grid(column = 1, row = 3, padx = 10, pady = 5, sticky = (W))
    ans2 = StringVar()
    Label(raam, textvariable = ans2).grid(column = 1, row = 4, padx = 10, pady = 5, sticky = (W))
    ans3 = StringVar()
    Label(raam, textvariable = ans3).grid(column = 1, row = 5, padx = 10, pady = 5, sticky = (W))
    ans4 = StringVar()
    Label(raam, textvariable = ans4).grid(column = 1, row = 6, padx = 10, pady = 5, sticky = (W))
    ans5 = StringVar()
    Label(raam, textvariable = ans5).grid(column = 1, row = 7, padx = 10, pady = 5, sticky = (W))
    ans6 = StringVar()
    Label(raam, textvariable = ans6).grid(column = 1, row = 8, padx = 10, pady = 5, sticky = (W))
    ans7 = StringVar()
    Label(raam, textvariable = ans7).grid(column = 1, row = 9, padx = 10, pady = 5, sticky = (W))
    ans8 = StringVar()
    Label(raam, textvariable = ans8).grid(column = 1, row = 10, padx = 10, pady = 5, sticky = (W))
    ans9 = StringVar()
    Label(raam, textvariable = ans9).grid(column = 1, row = 11, padx = 10, pady = 5, sticky = (W))
    ans10 = StringVar()
    Label(raam, textvariable = ans10).grid(column = 1, row = 12, padx = 10, pady = 5, sticky = (W))
    ans11 = StringVar()
    Label(raam, textvariable = ans11).grid(column = 1, row = 13, padx = 10, pady = 5, sticky = (W))
    ans12 = StringVar()
    Label(raam, textvariable = ans12).grid(column = 1, row = 14, padx = 10, pady = 5, sticky = (W))
    ans13 = StringVar()
    Label(raam, textvariable = ans13).grid(column = 1, row = 15, padx = 10, pady = 5, sticky = (W))
    ans14 = StringVar()
    Label(raam, textvariable = ans14).grid(column = 1, row = 16, padx = 10, pady = 5, sticky = (W))

    mans1 = StringVar()
    Label(raam, textvariable = mans1).grid(column = 3, row = 3, padx = 10, pady = 5, sticky = (W))
    mans2 = StringVar()
    Label(raam, textvariable = mans2).grid(column = 3, row = 4, padx = 10, pady = 5, sticky = (W))
    mans3 = StringVar()
    Label(raam, textvariable = mans3).grid(column = 3, row = 5, padx = 10, pady = 5, sticky = (W))
    mans4 = StringVar()
    Label(raam, textvariable = mans4).grid(column = 3, row = 6, padx = 10, pady = 5, sticky = (W))
    mans5 = StringVar()
    Label(raam, textvariable = mans5).grid(column = 3, row = 7, padx = 10, pady = 5, sticky = (W))
    mans6 = StringVar()
    Label(raam, textvariable = mans6).grid(column = 3, row = 8, padx = 10, pady = 5, sticky = (W))
    mans7 = StringVar()
    Label(raam, textvariable = mans7).grid(column = 3, row = 9, padx = 10, pady = 5, sticky = (W))
    mans8 = StringVar()
    Label(raam, textvariable = mans8).grid(column = 3, row = 10, padx = 10, pady = 5, sticky = (W))
    mans9 = StringVar()
    Label(raam, textvariable = mans9).grid(column = 3, row = 11, padx = 10, pady = 5, sticky = (W))
    mans10 = StringVar()
    Label(raam, textvariable = mans10).grid(column = 3, row = 12, padx = 10, pady = 5, sticky = (W))
    mans11 = StringVar()
    Label(raam, textvariable = mans11).grid(column = 3, row = 13, padx = 10, pady = 5, sticky = (W))
    mans12 = StringVar()
    Label(raam, textvariable = mans12).grid(column = 3, row = 14, padx = 10, pady = 5, sticky = (W))
    mans13 = StringVar()
    Label(raam, textvariable = mans13).grid(column = 3, row = 15, padx = 10, pady = 5, sticky = (W))
    mans14 = StringVar()
    Label(raam, textvariable = mans14).grid(column = 3, row = 16, padx = 10, pady = 5, sticky = (W))
    

    strin = StringVar()
    Label(raam, textvariable = strin).grid(column = 2, row = 0, columnspan = 4, padx = 10, pady = 5, sticky = (N, W))
    streng = StringVar()
    Label(raam, textvariable = streng).grid(column = 2, row = 1, padx = 10, pady = 5, sticky = (N, W))
    
    btn_txt.set(keel[keelint][0])
    def duolingo():#vahetab keelt
        global btn_txt
        global keel
        if btn_txt.get() == "English":
            keelint = 1
        elif btn_txt.get() == "Eesti":
            keelint = 0
        btn_txt.set(keel[keelint][0])
        siltvar.set(keel[keelint][1])
        ainsusvar.set(keel[keelint][2])
        mitmusvar.set(keel[keelint][3])
        kaan1var.set(keel[keelint][4])
        kaan2var.set(keel[keelint][5])
        kaan3var.set(keel[keelint][6])
        kaan4var.set(keel[keelint][7])
        kaan5var.set(keel[keelint][8])
        kaan6var.set(keel[keelint][9])
        kaan7var.set(keel[keelint][10])
        kaan8var.set(keel[keelint][11])
        kaan9var.set(keel[keelint][12])
        kaan10var.set(keel[keelint][13])
        kaan11var.set(keel[keelint][14])
        kaan12var.set(keel[keelint][15])
        kaan13var.set(keel[keelint][16])
        kaan14var.set(keel[keelint][17])
        mkaan1var.set(keel[keelint][4])
        mkaan2var.set(keel[keelint][5])
        mkaan3var.set(keel[keelint][6])
        mkaan4var.set(keel[keelint][7])
        mkaan5var.set(keel[keelint][8])
        mkaan6var.set(keel[keelint][9])
        mkaan7var.set(keel[keelint][10])
        mkaan8var.set(keel[keelint][11])
        mkaan9var.set(keel[keelint][12])
        mkaan10var.set(keel[keelint][13])
        mkaan11var.set(keel[keelint][14])
        mkaan12var.set(keel[keelint][15])
        mkaan13var.set(keel[keelint][16])
        mkaan14var.set(keel[keelint][17])
        Käänatxt.set(keel[keelint][18])
            

    
    keel_button = Button(raam, textvariable = btn_txt, command = duolingo)
    keel_button.grid(column = 0, row = 1, padx = 10, pady = 5, sticky = (W, E))
    b = Button(raam, textvariable = Käänatxt, command = valj)
    b.grid(column = 1, row = 1, padx = 10, pady = 5,  sticky = (W, E))
    
    mainloop()
GUI()

