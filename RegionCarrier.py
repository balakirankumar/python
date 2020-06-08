import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
number=input("enter no. to check location:")
ch_number=phonenumbers.parse(number,'IN')
print(geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier 
s_num=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(s_num, "en"))
print("hahhaha")
gb_number = phonenumbers.parse(number, "IN")
print(timezone.time_zones_for_number(gb_number))


print("hahhaha")

