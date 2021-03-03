import requests
from lxml import html
import json

buffer = json.loads(html.fromstring(requests.get("https://covid19.saglik.gov.tr/", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"}).content).xpath('//script[contains(., "sondurumjson")]/text()')[1].replace("\n", "").replace("//<![CDATA[", "").replace("//]]>", "").replace("var sondurumjson = [", "").replace("];", ""))
date = buffer["tarih"]
daily_tests = buffer["gunluk_test"]
daily_detections = buffer["gunluk_vaka"]
daily_deaths = buffer["gunluk_vefat"]
daily_cures = buffer["gunluk_iyilesen"]
all_tests = buffer["toplam_test"]
all_detections = buffer["toplam_hasta"]
all_deaths = buffer["toplam_vefat"]
all_cures = buffer["toplam_iyilesen"]
pneumonia_rate = buffer["hastalarda_zaturre_oran"]
print("-------Türkiye Koronavirüs Durumu-------")
print("Tarih (gg/AA/yyyy) -> %s"%(date))
print("Test Sayısı -> %s"%(all_tests))
print("Vaka Sayısı -> %s"%(all_detections))
print("Ölüm Sayısı -> %s"%(all_deaths))
#print("Yoğun Bakım Sayısı -> %s"%(b_count)) DEVLET BU KONUDA VERI AKISINI DURDURDU
#print("Entube Sayısı -> %s"%(e_count)) DEVLET BU KONUDA VERI AKISINI DURDURDU
print("Tedavi Olan Sayısı -> %s"%(all_cures))
print("Günlük Test Sayısı -> %s"%(daily_tests))
print("Günlük Vaka Sayısı -> %s"%(daily_detections))
print("Günlük Ölüm Sayısı -> %s"%(daily_deaths))
print("Günlük İyileşen Sayısı -> %s"%(daily_cures))
print("----------------------------------------")
print("-------Turkish Coronavirus Status-------")
print("Date (dd/MM/yyyy) -> %s"%(date))
print("Test Count -> %s"%(all_tests))
print("Sick Count -> %s"%(all_detections))
print("Death Count -> %s"%(all_deaths))
#print("Intensive Care Count -> %s"%(b_count)) GOVERMENT STOPPED GIVING THIS DATA
#print("Entube Count -> %s"%(e_count)) GOVERMENT STOPPED GIVING THIS DATA
print("Cured Count -> %s"%(all_cures))
print("Daily Test Sayısı -> %s"%(daily_tests))
print("Daily Sick Sayısı -> %s"%(daily_detections))
print("Daily Death Sayısı -> %s"%(daily_deaths))
print("Daily Cured Sayısı -> %s"%(daily_cures))
print("----------------------------------------")
