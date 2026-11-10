
# Analyseur d'offres de marches publics
# Premier projet Python

offres = {
    "Entreprise Alpha": 120000,
    "Entreprise Beta": 95000,
    "Entreprise Gamma": 78000
}

moyenne = sum(offres.values()) / len(offres)

print("ANALYSE DES OFFRES")
print(f"Prix moyen : {moyenne:.2f} euros")

for entreprise, prix in offres.items():
    ecart = (prix - moyenne) / moyenne * 100
    print(f"{entreprise} : {prix} euros ({ecart:+.1f} %)")

    if ecart < -20:
        print("  A examiner : prix nettement inferieur")
print("\nCLASSEMENT DES OFFRES")

classement = sorted(offres.items(), key=lambda offre: offre[1])

for rang, (entreprise, prix) in enumerate(classement, start=1):
    print(f"{rang}. {entreprise} : {prix} euros")
