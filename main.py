# This is a sample Python script.
import phonenumbers
from PhNo import number

from phonenumbers import geocoder
from phonenumbers import carrier

for num in number:
    ch_num = phonenumbers.parse(num, "CH")
    geo = geocoder.description_for_number(ch_num, "en")
    svcProv = phonenumbers.parse(num, "RO")
    svc_prov = carrier.name_for_number(svcProv, "en")
    print(num,":", geo,":", svc_prov )



