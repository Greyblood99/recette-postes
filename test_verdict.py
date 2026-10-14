from comparaison import calculer_verdict

test1 = [
    {"verdict": "Conforme", "gravite": "majeur"}
]

test2 = [
    {"verdict": "Écart", "gravite": "mineur"}
]

test3 = [
    {"verdict": "Écart", "gravite": "majeur"}
]

test4 = [
    {"verdict": "Indéterminé", "gravite": "majeur"}
]

print("Test 1 :", calculer_verdict(test1))
print("Test 2 :", calculer_verdict(test2))
print("Test 3 :", calculer_verdict(test3))
print("Test 4 :", calculer_verdict(test4))