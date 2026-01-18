# Drzewo Przedziałowe do Obliczania Czasu Trafienia Celów w Javie

![Java](https://img.shields.io/badge/Java-17-orange?style=flat&logo=java)
![CS Concepts](https://img.shields.io/badge/CS-Data_Structures-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Educational-green?style=flat)

Projekt edukacyjny w Javie przedstawiający implementację **segment tree** (drzewa przedziałowego) do obliczania czasu ostatniego trafienia celów przez serię dział. Kod demonstruje zaawansowane użycie drzew przedziałowych do szybkiej aktualizacji i zapytań w czasie O(log n).

---

## Opis

**CannonTree** to struktura danych przechowująca:

- Liczbę trafień na poszczególnych celach (`sum`)  
- Czas ostatniego trafienia (`last_hit_time`)  

Umożliwia:

1. Szybkie obliczenie czasu ostatniego trafienia wszystkich celów.  
2. Aktualizację liczby trafień dla pojedynczego celu w czasie O(log n).  

---

## Funkcjonalności

- **Budowa drzewa:** `build(targets)` – inicjalizacja drzewa na podstawie tablicy celów.  
- **Aktualizacja:** `update(index, new_value)` – zmiana liczby trafień na wybranym celu.  
- **Pobranie wyniku:** `getLastHitTime()` – zwraca czas ostatniego trafienia wszystkich celów.  

### Złożoność

| Operacja | Czas |
|-----------|------|
| Budowa drzewa | O(n) |
| Aktualizacja | O(log n) |
| Pobranie wyniku | O(1) |

---

## Przykładowe użycie

```java
int[] targets = {0, 2, 0, 0, 3};
CannonTree cannon = new CannonTree(targets);

System.out.println("Time to hit all targets: " + cannon.getLastHitTime());
cannon.update(1, 1);
System.out.println("After updating index 1 to 1: " + cannon.getLastHitTime());
```

Przykładowy output:
```txt
Time to hit all targets: 8
After updating index 1 to 1: 7
After updating index 2 to 3: 11
```


<div align="center">

### Autorzy 

| Role | Name | GitHub |
|:---:|:---:|:---:|
| **Developer** | **Łukasz Matecki** | [GitHub Profile](https://github.com/LukaszMatecki) |

<br>
<i>Created for educational purposes.</i>
