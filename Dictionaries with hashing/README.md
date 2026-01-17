# Hash Table Duel: Chaining vs. Open Addressing

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Data_Structures-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Educational-green?style=flat)

Projekt edukacyjny w Pythonie prezentujący dwie klasyczne implementacje tablicy haszującej:
- Separate Chaining (łańcuchowanie)
- Open Addressing z linear probing

Celem projektu jest pokazanie, jak działają kolizje, usuwanie elementów oraz rehashing bez użycia wbudowanego `dict` w języku Python.

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
| **Próg resize** | Load factor ≥ 10.0 | Load factor ≥ 0.7 | Standardowa biblioteka Pythona

## Uruchomienie

Sklonuj repozytorium:

```bash
git clone https://github.com/twoj-user/hash-table-internals.git
```

## Status
Projekt stworzony wyłącznie w celach edukacyjnych.
