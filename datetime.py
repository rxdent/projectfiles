import datetime

tday = datetime.date.today()
bday = datetime.date(2025,12,18)
sbreak = datetime.date(2026,5,22)
fbreak = datetime.date(2025,10,6)
wbreak = datetime.date(2025,12,22)

print(f"Time until birthday: {bday - tday}")
print(f"Time until summer break: {sbreak - tday}")
print(f"Time until fall break: {fbreak - tday}")
print(f"Time until winter break: {wbreak - tday}")