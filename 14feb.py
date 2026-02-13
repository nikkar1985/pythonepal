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


ΑΠΟ ΕΔΩ ΚΑΙ ΠΕΡΑ ΕΙΝΑΙ ΤΑ ΔΕΔΟΜΕΝΑ ΠΟΥ ΒΑΖΟΥΜΕ 

45
Α
111222333
55
Γ
444555666
30

ΑΠΟΤΕΛΕΣΜΑΤΑ 

 
-- ΕΝΑΡΞΗ ΠΡΟΓΡΑΜΜΑΤΟΣ ---
Δώστε ηλικία ( < 40 για έξοδο): Δώστε φύλο (Α/Γ): Δώστε ΑΜΚΑ: ΑΜΚΑ: 111222333 | Εμβόλιο: Τύπος 1
Δώστε επόμενη ηλικία: Δώστε φύλο (Α/Γ): Δώστε ΑΜΚΑ: ΑΜΚΑ: 444555666 | Εμβόλιο: Τύπος 2
Δώστε επόμενη ηλικία: 
--- ΣΤΑΤΙΣΤΙΚΑ ---
Γηραιότερος -> Φύλο: Γ ΑΜΚΑ: 444555666
Ποσοστό γυναικών: 50.0 %






ΑΣΚΗΣΗ ΜΕ ΤΑΞΙΝΟΜΗΣΗ

# -*- coding: utf-8 -*-

# Η λίστα που έδωσες
L = [55, 34, 5, 3, 2, 1, 1]

# Εφαρμογή του αλγορίθμου από την εικόνα
N = len(L)

for i in range(N):
    # range(N-1, 0, -1) σημαίνει: ξεκίνα από το τέλος και πήγαινε προς το 1
    for j in range(N-1, 0, -1):
        if L[j] < L[j-1]:
            # Ανταλλαγή τιμών (swap) με τον τρόπο της Python
            L[j], L[j-1] = L[j-1], L[j]

# Εμφάνιση αποτελέσματος
print "Η ταξινομημένη λίστα είναι:"
print L
