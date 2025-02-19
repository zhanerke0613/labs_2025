import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50}{'Description':<20}{'Speed':<8}{'MTU':<6}")
print("-" * 50 + " " + "-" * 18 + " " + "-" * 6 + " " + "-" * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    desc = attributes.get("descr", "")  
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50}{desc:<20}{speed:<8}{mtu:<6}")