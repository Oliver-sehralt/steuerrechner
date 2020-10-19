print()
print('Finanzamt Musterstadt')
print()

grenze1 = 10000
grenze2 = 30000
grenze3 = 70000

steuersatz1 = 0.4
steuersatz2 = 0.55
steuersatz3 = 0.75
steuersatz4 = 0.82

vorname = input('Vorname des Steuerzahlers:')
nachname = input('Nachname des Steuerzahlers:')

einkommen = 0.0
while einkommen >= 0.0:
    einkommen = float(input("Einkommen in €:"))
if einkommen <= 0.0:
    print('Eingabe ungültig. Bitte geben Sie Ihr Einkommen nochmals ein:')

steuer = 0.0
if einkommen <= grenze1:
    steuer = einkommen * steuersatz1
elif einkommen <= grenze2:
    steuer = einkommen * steuersatz2
elif einkommen <= grenze3:
    steuer = einkommen * steuersatz3
else:
    steuer = einkommen * steuersatz4

print(vorname +""+ nachname + 'hat für das laufenden Jahr Steuern in Höhe von €', round(steuer), 'zu zahlen.')
