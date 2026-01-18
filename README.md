# Algorytmy i Struktury Danych

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Java](https://img.shields.io/badge/Java-17-orange?style=for-the-badge&logo=java)
![CS Concepts](https://img.shields.io/badge/CS-Algorithms-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)

Repozytorium edukacyjne prezentujące różne klasyczne algorytmy do dopasowywania wzorców w tekście oraz struktur danych, takich jak segment tree i problem plecakowy.

---

## Algorytmy

### 1. Porównywanie tekstów (LCS)

- **Opis:** Implementacja Longest Common Subsequence do znajdowania różnic między dwoma tekstami.  
- **Język:** Python  
- **Cel:** Narzędzie do porównywania plików, np. w systemach kontroli wersji.  
- [Przejdź do kodu LCS](./lcs_diff.py)  

---

### 2. Dopasowywanie wzorców w tekście

- **Algorytmy:**
  1. **Naive Algorithm** – sprawdzanie wzorca w każdym możliwym przesunięciu.
  2. **Sunday Algorithm** – optymalizacja przesunięć wzorca w oparciu o znak następujący po oknie dopasowania.
  3. **Sunday Algorithm (Pair Shifts)** – rozszerzenie algorytmu Sunday na pary liter.
  4. **Knuth-Morris-Pratt (KMP)** – użycie tablicy prefiks-sufiks do efektywnego wyszukiwania wzorca.  
- **Język:** Python  
- **Cel:** Porównanie klasycznych algorytmów wyszukiwania wzorca.  
- [Przejdź do kodu wzorców](./string_matching.py)  

---

### 3. Problem Plecakowy z kulami magicznymi

- **Opis:** Rozwiązanie problemu plecakowego z dodatkowym mnożnikiem wartości przedmiotów dzięki kulom magicznym.  
- **Język:** Java  
- **Cel:** Demonstracja dynamicznego programowania oraz dodatkowych ograniczeń i modyfikatorów.  
- [Przejdź do kodu problemu plecakowego](./knapsack_magic.java)  

---

### 4. CannonTree – Drzewo Przedziałowe do czasu trafień celów

- **Opis:** Segment tree przechowujący liczbę trafień w celach i obliczający czas ostatniego trafienia.  
- **Język:** Java  
- **Cel:** Szybkie aktualizacje i zapytania w czasie O(log n).  
- [Przejdź do kodu CannonTree](./CannonTree.java)  

---

## Autorzy

| Rola | Imię | GitHub |
|:---:|:---:|:---:|
| **Developer** | Łukasz Matecki | [GitHub Profile](https://github.com/LukaszMatecki) |

<br>
<i>Projekt stworzony w celach edukacyjnych.</i>
