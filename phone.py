print('Hello')
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers.phonenumberutil import number_type
num=input("Enther The Number You Want To Track The Location (add your country code) : ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
carier=carrier.name_for_number(phone,'en')
registration=geocoder.description_for_number(phone,'en')
print("------------------------------------------")
print(time)
print(phone)
print("Company Name : ",carier)
print("Country is : ",registration)
