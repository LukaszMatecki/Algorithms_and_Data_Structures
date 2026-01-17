# Hash Table Duel: Chaining vs. Open Addressing

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Data_Structures-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Educational-green?style=flat)

> **Surowa implementacja Tablic Mieszających w Pythonie. Bez użycia wbudowanego `dict`.**

## O Projekcie

To repozytorium to techniczne porównanie dwóch fundamentalnych strategii rozwiązywania kolizji. Kod pokazuje, co dzieje się "pod maską" systemów bazodanowych.

Zaimplementowano od zera:
1. **Separate Chaining** (Metoda Łańcuchowa)
2. **Open Addressing** (Adresowanie Otwarte z próbkowaniem liniowym)

## Architektura i Algorytmy

### 1. ChainingHashTable
Każdy indeks w tablicy to "wiadro" (lista).
* **Strategia:** Nieskończona pojemność pojedynczego indeksu.
* **Kolizja:** Elementy o tym samym hashu są dopisywane do listy.
* **Load Factor:** Może przekraczać 1.0.

### 2. OpenAddressingHashTable
Płaska struktura pamięci. Jeden slot = jeden element.
* **Strategia:** Jeśli miejsce jest zajęte, szukamy pierwszego wolnego `(index + 1)`.
* **Ciekawostka (Active Cluster Maintenance):**
  Ten kod **nie używa "nagrobków" (flag DELETED)** przy usuwaniu. Gdy usuwamy element, algorytm przesuwa (wykonuje re-insert) kolejne elementy klastra, aby załatać "dziurę". Dzięki temu tablica jest zawsze spójna.

## Porównanie Implementacji

| Cecha | Chaining | Open Addressing |
| :--- | :--- | :--- |
| **Rozwiązywanie Kolizji** | Lista (Bucket) | Linear Probing |
| **Wydajność Pamięci** | Narzut na listy | Brak narzutu (płaska tablica) |
| **Cache Locality** | Średnia | Wysoka (dane obok siebie) |
| **Próg Resize** | Load Factor ≥ 10.0 | Load Factor ≥ 0.7 |

## Przegląd Kodu

### 1. Skalowanie (Rehashing)
Różne strategie dla różnych potrzeb:

``python
# Chaining: Pozwala na długie łańcuchy
if self.count / self.size >= 10:
    self._rehash(self.size * 2)

# Open Addressing: Musi być luźny, by unikać klastrów
if self.count / self.size >= 0.7:
    self._rehash(self.size * 2)

# ...usunięcie elementu...
next_index = (index + 1) % self.size

# Przesuwamy kolejne elementy, aby załatać dziurę
while self.table[next_index] is not None:
    key, val = self.table[next_index]
    self.table[next_index] = None
    self.count -= 1
    self.insert(key, val) # Re-insert znajdzie optymalne miejsce
    next_index = (next_index + 1) % self.size

Kod nie wymaga instalacji żadnych bibliotek.

Sklonuj repozytorium:

Bash

git clone [https://github.com/twoj-user/hash-table-internals.git](https://github.com/twoj-user/hash-table-internals.git)
Uruchom skrypt:

Bash

python hash_tables.py
Przykładowy Output
Plaintext

TEST: OpenAddressingHashTable
Inserted (10, 10) at index 0
Inserted (30, 30) at index 1  <-- Kolizja z indexem 0
Removing key 17 from index 7
Hash Table: [0:(10, '10')] [1:(30, '30')] ...
Kod stworzony w celach edukacyjnych.
