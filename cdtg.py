try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests

def MonthTranslate(monthText):
    if monthText == "OCAK":
        return "JANUARY"
    elif monthText == "ŞUBAT":
        return "FEBRURARY"
    elif monthText == "MART":
        return "MARCH"
    elif monthText == "NİSAN":
        return "APRIL"
    elif monthText == "MAYIS":
        return "MAY"
    elif monthText == "HAZIRAN":
        return "JUNE"
    elif monthText == "TEMMUZ":
        return "JULY"
    elif monthText == "AĞUSTOS":
        return "AUGUST"
    elif monthText == "EYLÜL":
        return "SEPTEMBER"
    elif monthText == "EKİM":
        return "OCTOBER"
    elif monthText == "KASIM":
        return "NOVEMBER"
    elif monthText == "ARALIK":
        return "DECEMBER"

r = requests.get("https://covid19.saglik.gov.tr/")
page_source = r.content
parsed_html = BeautifulSoup(page_source, features="html.parser")
t_count = str((parsed_html.body.find_all("span")[1].text).strip())
v_count = str((parsed_html.body.find_all("span")[3].text).strip())
d_count = str((parsed_html.body.find_all("span")[5].text).strip())
b_count = str((parsed_html.body.find_all("span")[7].text).strip())
e_count = str((parsed_html.body.find_all("span")[9].text).strip())
c_count = str((parsed_html.body.find_all("span")[11].text).strip())
tt_count = str((parsed_html.body.find_all("span")[13].text).strip())
tv_count = str((parsed_html.body.find_all("span")[15].text).strip())
td_count = str((parsed_html.body.find_all("span")[17].text).strip())
tc_count = str((parsed_html.body.find_all("span")[19].text).strip())
day = str((parsed_html.body.find_all("p")[1].text).strip())
month = str((parsed_html.body.find_all("p")[2].text).strip())
year = str((parsed_html.body.find_all("p")[3].text).strip())
print("-------Türkiye Koronavirüs Durumu-------")
print("Tarih -> %s %s %s"%(day, month, year))
print("Test Sayısı -> %s"%(t_count))
print("Vaka Sayısı -> %s"%(v_count))
print("Ölüm Sayısı -> %s"%(d_count))
print("Yoğun Bakım Sayısı -> %s"%(b_count))
print("Entube Sayısı -> %s"%(e_count))
print("Tedavi Olan Sayısı -> %s"%(c_count))
print("Günlük Test Sayısı -> %s"%(tt_count))
print("Günlük Vaka Sayısı -> %s"%(tv_count))
print("Günlük Ölüm Sayısı -> %s"%(td_count))
print("Günlük İyileşen Sayısı -> %s"%(tc_count))
print("----------------------------------------")
print("-------Turkish Coronavirus Status-------")
print("Date -> %s %s %s"%(day, MonthTranslate(month), year))
print("Test Count -> %s"%(t_count))
print("Sick Count -> %s"%(v_count))
print("Death Count -> %s"%(d_count))
print("Intensive Care Count -> %s"%(b_count))
print("Entube Count -> %s"%(e_count))
print("Cured Count -> %s"%(c_count))
print("Daily Test Sayısı -> %s"%(tt_count))
print("Daily Sick Sayısı -> %s"%(tv_count))
print("Daily Death Sayısı -> %s"%(td_count))
print("Daily Cured Sayısı -> %s"%(tc_count))
print("----------------------------------------")
