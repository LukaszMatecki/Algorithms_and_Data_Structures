# Złożoność obliczeniowa czasowa pesymistyczna O(m * n)
# Złożoność obliczeniowa czasowa optymistyczna O(m)
def algorytm_naiwny(wzorzec, tekst):
    dlugosc_tekstu = len(tekst)  # m
    dlugosc_wzorca = len(wzorzec)  # n
    wystapienia = []

    for i in range(0, dlugosc_tekstu - dlugosc_wzorca + 1):
        j = 0
        while j < dlugosc_wzorca:
            if tekst[i + j] != wzorzec[j]:
                break
            j += 1
            if j == dlugosc_wzorca:
                wystapienia.append(i)
    return wystapienia

# Złożoność obliczeniowa czasowa pesymistyczna O(m * n)
# Złożoność obliczeniowa czasowa optymistyczna O(m / n)
def algorytm_sunday(wzorzec, tekst):
    dlugosc_tekstu = len(tekst)
    dlugosc_wzorca = len(wzorzec)
    wystapienia = []

    # Tworzymy tablicę przesunięć dla wszystkich możliwych znaków
    przesuniecia = {}
    for i in range(0, dlugosc_wzorca):
        przesuniecia[wzorzec[i]] = dlugosc_wzorca - i
        print(przesuniecia)
    # Wyszukiwanie wzorca w tekście
    i = 0
    while i <= dlugosc_tekstu - dlugosc_wzorca:
        j = 0
        while j < dlugosc_wzorca:
            if tekst[i + j] != wzorzec[j]:
                break
            j += 1

        # Dodanie pozycji wystapienia do tablicy/listy wystapien
        if j == dlugosc_wzorca:
            wystapienia.append(i)

        # Przesuwanie wzorca - jesli znajdzie wartosc ze wzorca to przesuwa o tą wartosc w przeciwnym wypadku o dlugosc wzorca + 1
        if i + dlugosc_wzorca < dlugosc_tekstu:
            i += przesuniecia.get(tekst[i + dlugosc_wzorca], dlugosc_wzorca + 1)
        else:
            break
    return wystapienia

# Złożoność obliczeniowa czasowa pesymistyczna O(m * n)
# Złożoność obliczeniowa czasowa optymistyczna O(m / n)
def algorytm_sunday_pary(wzorzec, tekst):
    dlugosc_tekstu = len(tekst)
    dlugosc_wzorca = len(wzorzec)
    wystapienia = []
    przesuniecia = {}

    for i in range(dlugosc_wzorca - 1):
        para = wzorzec[i:i+2]
        przesuniecia[para] = dlugosc_wzorca - i - 1 #tak obliczamy przesuniecia
    # przesuniecia[wzorzec[-2:]] = 1

    print("Wzorzec:", wzorzec)
    print("Tablica przesunięć dla par liter:")
    for para, przesuniecie in przesuniecia.items():
        print(f"  {para} -> {przesuniecie}")

    i = 0
    while i <= dlugosc_tekstu - dlugosc_wzorca:
        j = 0
        while j < dlugosc_wzorca:
            if tekst[i + j] != wzorzec[j]:
                break
            j += 1

        if j == dlugosc_wzorca:
            wystapienia.append(i)

        if i + dlugosc_wzorca + 1 <= dlugosc_tekstu:
            para_tekstu = tekst[i + dlugosc_wzorca - 1 : i + dlugosc_wzorca + 1]
            i += przesuniecia.get(para_tekstu, dlugosc_wzorca)
        else:
            break
    return wystapienia

# Złożoność obliczeniowa czasowa optymistyczna i pesymistyczna O(m + n)
def algorytm_mp(wzorzec, tekst):
    dlugosc_wzorca = len(wzorzec)
    tablica_prefikso_sufiksow = [0] * dlugosc_wzorca
    j = 0

    # budowa tablicy prefiksów
    for i in range(1, dlugosc_wzorca):
        while j > 0 and wzorzec[i] != wzorzec[j]:
            j = tablica_prefikso_sufiksow[j - 1]
        if wzorzec[i] == wzorzec[j]:
            j += 1
        tablica_prefikso_sufiksow[i] = j

    print("Tablica prefikso-sufiksow:", tablica_prefikso_sufiksow)

    # wyszukiwanie wzorca w tekście
    dopasowania = []
    j = 0  # indeks we wzorcu

    for i in range(len(tekst)):
        while j > 0 and tekst[i] != wzorzec[j]:
            j = tablica_prefikso_sufiksow[j - 1]
        if tekst[i] == wzorzec[j]:
            j += 1
        if j == dlugosc_wzorca:
            dopasowania.append(i - dlugosc_wzorca + 1)
            j = tablica_prefikso_sufiksow[j - 1]

    return dopasowania

tekst = "BACABADEABADDEAABCCABAD"
wzorzec = "ABAD"
# tekst = "aabcbcbabacabaacabababababacacacvababacacacababcbacbabababcaacacbcccababababababcbacbabcbacbacbabcbacbabcabaacacaaaabacbbcbbababababababbababccccacac"
# wzorzec = "aba"
# tekst = "abcaabcabcbabcbacbabcbcababcabcbbabcbacb"
# wzorzec = "abcabc"
# tekst = "ABCDXYZABCDXYZABCDXXXBXXXXYYXXXXXXXXYZABCDXYZABCDXYZXYAB"
# wzorzec = "XYZAB"
# tekst = "ABCADBABCABC"
# wzorzec = "ABCABC"
# tekst = "bacbababadababacambabacaddababacasdsd"
# wzorzec = "ababaca"

print("\nTekst ktory bedziemy przeszukiwac: " + tekst)
print("Nasz wzorzec: " + wzorzec)
print("---------------------------------------\n")
print("[Algorytm naiwy]:")
print(algorytm_naiwny(wzorzec, tekst))
print("\n---------------------------------------\n")
print("[Algorytm Sunday'a]:")
print(algorytm_sunday(wzorzec, tekst))
print("\n---------------------------------------\n")
print("[Algorytm Sunday'a (pary liter)]:")
print(algorytm_sunday_pary(wzorzec, tekst))
print("\n---------------------------------------\n")
print("[Algorytm MP]: ")
print(algorytm_mp(wzorzec, tekst))