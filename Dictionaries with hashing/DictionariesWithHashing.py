# TABLICA HASZUJĄCA Z ŁAŃCUCHOWANIEM
class TablicaHaszujacaLancuchowanie:
    def __init__(self, rozmiar=10):
        self.rozmiar = rozmiar
        self.prog_obciazenia = 10  # Po przekroczeniu tego progu wykonujemy rehaszowanie
        self.licznik = 0  # Liczba elementów w słowniku
        self.tablica = [[] for _ in range(rozmiar)]

    def _hash(self, klucz):
        return hash(klucz) % self.rozmiar

    def _rehash(self, nowy_rozmiar):
        nowa_tablica = [[] for _ in range(nowy_rozmiar)]
        for lancuch in self.tablica:
            for para in lancuch:
                nowy_indeks = self._hash(para[0])
                nowa_tablica[nowy_indeks].append(para)
        self.tablica = nowa_tablica
        self.rozmiar = nowy_rozmiar

    def wstaw(self, klucz, wartosc):
        if self.licznik / self.rozmiar >= self.prog_obciazenia:
            self._rehash(self.rozmiar * 2)

        indeks = self._hash(klucz)
        lancuch = self.tablica[indeks]

        for para in lancuch:
            if para[0] == klucz:
                para[1] = wartosc
                return

        lancuch.append([klucz, wartosc])
        self.licznik += 1
        print(f"Wstawiono ({klucz}, {wartosc}) do indeksu {indeks}")
        self.wydruk_tablicy()

    def znajdz(self, klucz):
        indeks = self._hash(klucz)
        lancuch = self.tablica[indeks]

        for para in lancuch:
            if para[0] == klucz:
                return para[1]

        return None

    def usun(self, klucz):
        indeks = self._hash(klucz)
        lancuch = self.tablica[indeks]

        for i, para in enumerate(lancuch):
            if para[0] == klucz:
                del lancuch[i]
                self.licznik -= 1
                print(f"Usunięto klucz {klucz} z indeksu {indeks}")
                self.wydruk_tablicy()

                if self.rozmiar > 10 and self.licznik / self.rozmiar <= 0.2:
                    self._rehash(self.rozmiar // 2)
                return

    def wydruk_tablicy(self):
        print("Tablica (łańcuchowanie):")
        for i, lancuch in enumerate(self.tablica):
            print(f"[{i}]: {lancuch}")
        print()


# TABLICA HASZUJĄCA – ADRESOWANIE OTWARTE O(m+n)
class TablicaHaszujacaOtwarta:
    def __init__(self, rozmiar=10):
        self.rozmiar = rozmiar
        self.prog_obciazenia = 0.7
        self.licznik = 0
        self.tablica = [None] * rozmiar

    def _hash(self, klucz):
        return hash(klucz) % self.rozmiar

    def _rehash(self, nowy_rozmiar):
        nowa_tablica = [None] * nowy_rozmiar
        stary_rozmiar = self.rozmiar
        self.rozmiar = nowy_rozmiar
        for element in self.tablica:
            if element is not None:
                indeks = self._hash(element[0])
                while nowa_tablica[indeks] is not None:
                    indeks = (indeks + 1) % nowy_rozmiar
                nowa_tablica[indeks] = element
        self.tablica = nowa_tablica

    def wstaw(self, klucz, wartosc):
        if self.licznik / self.rozmiar >= self.prog_obciazenia:
            self._rehash(self.rozmiar * 2)

        indeks = self._hash(klucz)
        while self.tablica[indeks] is not None and self.tablica[indeks][0] != klucz:
            indeks = (indeks + 1) % self.rozmiar

        if self.tablica[indeks] is None:
            self.licznik += 1

        self.tablica[indeks] = (klucz, wartosc)
        print(f"Wstawiono ({klucz}, {wartosc}) do indeksu {indeks}")
        self.wydruk_tablicy()

    def znajdz(self, klucz):
        indeks = self._hash(klucz)
        start = indeks
        while self.tablica[indeks] is not None:
            if self.tablica[indeks][0] == klucz:
                return self.tablica[indeks][1]
            indeks = (indeks + 1) % self.rozmiar
            if indeks == start:
                break
        return None

    def usun(self, klucz):
        indeks = self._hash(klucz)
        start = indeks
        while self.tablica[indeks] is not None:
            if self.tablica[indeks][0] == klucz:
                break
            indeks = (indeks + 1) % self.rozmiar
            if indeks == start:
                return
        else:
            return

        # Usuwanie elementu i przesunięcie
        print(f"\nUsuwamy klucz {klucz} z indeksu {indeks}")
        self.tablica[indeks] = None
        self.licznik -= 1
        self.wydruk_tablicy()

        nastepny_indeks = (indeks + 1) % self.rozmiar
        while self.tablica[nastepny_indeks] is not None:
            klucz_przesun = self.tablica[nastepny_indeks][0]
            wartosc_przesun = self.tablica[nastepny_indeks][1]
            self.tablica[nastepny_indeks] = None
            self.licznik -= 1
            self.wstaw(klucz_przesun, wartosc_przesun)
            nastepny_indeks = (nastepny_indeks + 1) % self.rozmiar

        # Opcjonalnie zmniejszamy tablicę
        if self.rozmiar > 10 and self.licznik / self.rozmiar <= 0.2:
            self._rehash(self.rozmiar // 2)

    def wydruk_tablicy(self):
        print("Tablica:", end=" ")
        for i, elem in enumerate(self.tablica):
            print(f"[{i}:{elem}]", end=" ")
        print("\n")

# Test działania
if __name__ == "__main__":

    print("\nTEST: TablicaHaszujacaLancuchowanie")
    lancuch = TablicaHaszujacaLancuchowanie()
    lancuch.wstaw(5, "5")
    lancuch.wstaw(11, "11")
    lancuch.wstaw(15, "15")
    lancuch.wstaw(25, "25")
    lancuch.wstaw(35, "35")
    #print(lancuch.znajdz(5))
    #print(lancuch.znajdz(15))
    #print(lancuch.znajdz(10))
    lancuch.usun(5)
    #print(lancuch.znajdz(5))
    lancuch.wstaw(5, "5")

    print("\nTEST: TablicaHaszujacaOtwarta")
    mapa = TablicaHaszujacaOtwarta()
    mapa.wstaw(10, "10")
    mapa.wstaw(17, "17")
    mapa.wstaw(30, "30")
    mapa.wstaw(40, "40")
    mapa.wstaw(50, "50")
    mapa.wstaw(13, "13")
    mapa.wstaw(27, "27")
    print("\n--- STAN TABLICY PRZED USUNIĘCIEM ---")
    mapa.wydruk_tablicy()
    mapa.usun(17)
    mapa.usun(30)
    print("\n--- STAN TABLICY PO USUNIĘCIU 17 i 30 ---")
    mapa.wydruk_tablicy()
    mapa.wstaw(20, "20")
    print("\n--- STAN TABLICY PO DODANIU 20 ---")
    mapa.wydruk_tablicy()

    # print("\nTEST: TablicaHaszujacaOtwarta")
    # mapa = TablicaHaszujacaOtwarta()
    # mapa.wstaw(10, "10")
    # mapa.wstaw(17, "17")
    # mapa.wstaw(30, "30")
    # mapa.wstaw(40, "40")
    # mapa.wstaw(50, "50")
    # mapa.wstaw(13, "13")
    # mapa.wstaw(14, "14")
    # mapa.wstaw(15, "15")
    # mapa.wstaw(16, "16")
    # mapa.wstaw(55, "55")
    # mapa.wstaw(27, "27")
    # print("\n--- STAN TABLICY PRZED USUNIĘCIEM ---")
    # mapa.wydruk_tablicy()
    # mapa.usun(17)
    # mapa.usun(30)
    # mapa.usun(15)
    # print("\n--- STAN TABLICY PO USUNIĘCIU 17 i 30 i 15 ---")
    # mapa.wydruk_tablicy()
    # mapa.wstaw(20, "20")
    # print("\n--- STAN TABLICY PO DODANIU 20 ---")
    # mapa.wydruk_tablicy()