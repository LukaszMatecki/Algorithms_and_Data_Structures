# Hash Table Duel: Chaining vs. Open Addressing

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Data_Structures-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Educational-green?style=flat)

> **Surowa implementacja tablic mieszających w Pythonie. Bez użycia wbudowanego `dict`.**

## O projekcie

To repozytorium to techniczne porównanie dwóch fundamentalnych strategii rozwiązywania kolizji. Kod pokazuje, co dzieje się „pod maską” systemów bazodanowych.

Zaimplementowano od zera:

1. **Separate Chaining** (metoda łańcuchowa)  
2. **Open Addressing** (adresowanie otwarte z próbkowaniem liniowym)

## Architektura i algorytmy

### 1. ChainingHashTable

Każdy indeks w tablicy to „wiadro” (lista).

- **Strategia:** nieskończona pojemność pojedynczego indeksu  
- **Kolizja:** elementy o tym samym hashu są dopisywane do listy  
- **Load factor:** może przekraczać 1.0  

### 2. OpenAddressingHashTable

Płaska struktura pamięci. Jeden slot = jeden element.

- **Strategia:** jeśli miejsce jest zajęte, szukamy pierwszego wolnego `(index + 1)`  
- **Ciekawostka (Active Cluster Maintenance):**  
  Ten kod **nie używa „nagrobków” (flag DELETED)** przy usuwaniu.  
  Gdy usuwamy element, algorytm wykonuje reinsercję kolejnych elementów klastra, aby „załatać dziurę”.  
  Dzięki temu tablica pozostaje spójna.

## Porównanie implementacji

| Cecha | Chaining | Open Addressing |
|--------|-----------|------------------|
| **Rozwiązywanie kolizji** | Lista (bucket) | Linear probing |
| **Wydajność pamięci** | Narzut na listy | Brak narzutu (płaska tablica) |
| **Cache locality** | Średnia | Wysoka (dane obok siebie) |
| **Próg resize** | Load factor ≥ 10.0 | Load factor ≥ 0.7 |

## Przegląd kodu

### Skalowanie (Rehashing)

Różne strategie dla różnych potrzeb:

```python
# Chaining: pozwala na długie łańcuchy
if self.count / self.size >= 10:
    self._rehash(self.size * 2)

# Open Addressing: musi być luźny, by unikać klastrów
if self.count / self.size >= 0.7:
    self._rehash(self.size * 2)

# ...usunięcie elementu...
next_index = (index + 1) % self.size

# Przesuwamy kolejne elementy, aby załatać dziurę
while self.table[next_index] is not None:
    key, val = self.table[next_index]
    self.table[next_index] = None
    self.count -= 1
    self.insert(key, val)  # reinsert znajdzie optymalne miejsce
    next_index = (next_index + 1) % self.size

Kod nie wymaga instalacji żadnych bibliotek.

Jak uruchomić
1. Sklonuj repozytorium
git clone https://github.com/twoj-user/hash-table-internals.git

2. Uruchom skrypt
python hash_tables.py

Przykładowy output
TEST: OpenAddressingHashTable
Inserted (10, 10) at index 0
Inserted (30, 30) at index 1  <-- kolizja z indeksem 0
Removing key 17 from index 7
Hash Table: [0:(10, '10')] [1:(30, '30')] ...

Status projektu

Kod stworzony wyłącznie w celach edukacyjnych – do nauki struktur danych i mechaniki tablic haszujących.
