napis = input("Podaj napis: ")
ile_samoglosek = 0

samogloski = "aeiouy"

for litera in napis:
    if litera.lower() in samogloski:
        ile_samoglosek += 1

print(f"W napisie '{napis}' jest {ile_samoglosek} samogłosek.")
