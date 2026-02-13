# -*- coding: utf-8 -*-
import sys

# Γ2. Συνάρτηση
def TYPOS_EMB(hlikia):
    if 40 <= hlikia <= 50:
        return "Τύπος 1"
    elif 51 <= hlikia <= 60:
        return "Τύπος 2"
    elif 61 <= hlikia <= 70:
        return "Τύπος 3"
    else:
        return "Τύπος 4"

# Αρχικοποίηση
max_hlikia = -1
max_fylo = ""
max_amka = ""
count_gynaikes = 0
count_total = 0

print "--- ΕΝΑΡΞΗ ΠΡΟΓΡΑΜΜΑΤΟΣ ---"

# Γ1. Είσοδος
try:
    line = raw_input("Δώστε ηλικία ( < 40 για έξοδο): ")
    hlikia = int(line)
except EOFError:
    hlikia = 0 # Αν δεν βρει είσοδο, σταματάει

while hlikia >= 40:
    # Έλεγχος ορθότητας φύλου
    fylo = raw_input("Δώστε φύλο (Α/Γ): ").strip().upper()
    while fylo != "Α" and fylo != "Γ":
        print "Λάθος είσοδος φύλου."
        fylo = raw_input("Δώστε φύλο (Α/Γ): ").strip().upper()
    
    amka = raw_input("Δώστε ΑΜΚΑ: ")
    
    # Γ3. Εμφάνιση
    typos = TYPOS_EMB(hlikia)
    print "ΑΜΚΑ:", amka, "| Εμβόλιο:", typos
    
    # Γ4. Max ηλικία
    if hlikia > max_hlikia:
        max_hlikia = hlikia
        max_fylo = fylo
        max_amka = amka
        
    # Γ5. Καταμέτρηση
    count_total += 1
    if fylo == "Γ":
        count_gynaikes += 1
        
    # Επόμενη επανάληψη
    try:
        line = raw_input("Δώστε επόμενη ηλικία: ")
        hlikia = int(line)
    except EOFError:
        break

# Τελικά αποτελέσματα
print "\n--- ΣΤΑΤΙΣΤΙΚΑ ---"
if count_total > 0:
    print "Γηραιότερος -> Φύλο:", max_fylo, "ΑΜΚΑ:", max_amka
    pososto = (float(count_gynaikes) / count_total) * 100
    print "Ποσοστό γυναικών:", pososto, "%"
else:
    print "Δεν δόθηκαν δεδομένα."
