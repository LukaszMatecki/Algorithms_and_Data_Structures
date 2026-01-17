## Hash Table Duel: Chaining vs. Open Addressing

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Data_Structures-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)

> **A deep-dive, bare-metal implementation of Hash Tables in Python. No `dict` shortcuts.**

## ⚡ O Projekcie

To repozytorium to techniczny "poedynek" dwóch fundamentalnych strategii rozwiązywania kolizji w tablicach mieszających. Kod demonstruje, co dzieje się "pod maską" (under the hood) systemów bazodanowych i interpreterów języków programowania.

Zaimplementowano od zera:
1.  **Separate Chaining** (Metoda Łańcuchowa)
2.  **Open Addressing** (Adresowanie Otwarte z próbkowaniem liniowym)

---

## 🏗️ Architektura i Algorytmy

### 1. ChainingHashTable
Każdy slot w tablicy jest "wiadrem" (listą).
* **Strategia:** Nieskończona pojemność pojedynczego indeksu.
* **Kolizja:** Elementy o tym samym hashu lądują w tej samej liście.
* **Load Factor:** Może przekraczać 1.0 (więcej elementów niż slotów).

### 2. OpenAddressingHashTable (Linear Probing)
Płaska struktura pamięci. Jeden slot = jeden element.
* **Strategia:** Jeśli miejsce jest zajęte, szukamy pierwszego wolnego `(index + 1)`.
* ** 🔥 Killer Feature: Active Cluster Maintenance**
    W przeciwieństwie do typowych implementacji akademickich, ten kod **nie używa "nagrobków" (Tombstones)** przy usuwaniu.
    
    > **Jak to działa?**
    > Gdy usuwamy element, powstaje "dziura". Algorytm sprawdza kolejne elementy w klastrze i wykonuje **re-insert**, aby przesunąć je w optymalne miejsca. Dzięki temu operacja `find` jest szybsza, bo nie musi przeskakiwać przez flagi `DELETED`.

---

## ⚙️ Porównanie Implementacji

| Cecha | Chaining | Open Addressing |
| :--- | :--- | :--- |
| **Rozwiązywanie Kolizji** | Lista (Bucket) | Linear Probing |
| **Wydajność Pamięci** | Overhead na wskaźniki list | Brak overheadu (płaska tablica) |
| **Cache Locality** | Średnia (skakanie po pamięci) | Wysoka (dane są obok siebie) |
| **Limit elementów** | Ograniczony tylko RAM-em | Ograniczony rozmiarem tablicy |
| **Próg Resize (Góra)** | Load Factor ≥ 10.0 | Load Factor ≥ 0.7 |

---

## 💻 Przegląd Kodu

### Inteligentne Skalowanie (Rehashing)
Obie klasy automatycznie zarządzają pamięcią, ale mają różne progi wyzwalania:

```python
# Chaining: Bardziej "zrelaksowany", pozwala na długie łańcuchy
if self.count / self.size >= 10:
    self._rehash(self.size * 2)

# Open Addressing: Musi być luźny, aby unikać klasteryzacji
if self.count / self.size >= 0.7:
    self._rehash(self.size * 2)
