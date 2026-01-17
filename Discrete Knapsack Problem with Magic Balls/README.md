# Magiczny Problem Plecakowy

![Java](https://img.shields.io/badge/Java-17-orange?style=flat&logo=java)
![CS Concepts](https://img.shields.io/badge/CS-Dynamic_Programming-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Edukacyjny-green?style=flat)

Projekt edukacyjny w Javie przedstawiający wariant **problemu plecakowego (0/1)** z dodatkiem „magicznych kul”.

Program oblicza **maksymalną wartość** przedmiotów, które można zmieścić w plecaku, uwzględniając zarówno wagę, jak i strategiczne użycie kul, które podwajają wartość wszystkich przedmiotów w plecaku za każdą kulę użytą.

## Opis Problemu

- Standardowy **Problem Plecakowy**: wybierz przedmioty z określoną wagą i wartością, tak aby maksymalizować sumę wartości, nie przekraczając pojemności plecaka.  
- **Magiczne Kule**: każda kula podwaja całkowitą wartość przedmiotów aktualnie w plecaku.  
- Wykorzystano **programowanie dynamiczne**, aby znaleźć najlepszą kombinację przedmiotów i liczby kul.  
- Złożoność: `O(n * W + m)`, gdzie `n` = liczba przedmiotów, `W` = pojemność plecaka, `m` = liczba kul.

### Klasy

#### Plecak

Reprezentuje plecak:

- `pojemnosc` – maksymalna pojemność

#### Przedmiot

Reprezentuje pojedynczy przedmiot:

- `nazwa` – nazwa przedmiotu  
- `waga` – waga  
- `wartosc` – wartość  

#### MagicznaKula

Reprezentuje magiczne kule:

- `ilosc` – liczba kul dostępnych  
- `waga` – waga jednej kuli  

#### KnapsackSolver

Zawiera algorytm rozwiązujący problem:

- Tworzy standardową tablicę DP dla problemu plecakowego  
- Sprawdza wszystkie możliwe liczby kul, aby znaleźć optymalne rozwiązanie  
- Wyświetla maksymalną wartość, liczbę kul użytych oraz listę wybranych przedmiotów

## Przykładowe użycie

```java
Plecak p1 = new Plecak(7);
MagicznaKula kule = new MagicznaKula(5, 3);

List<Przedmiot> przedmioty = new ArrayList<>();
przedmioty.add(new Przedmiot("Encyklopedia zwierząt", 3, 2));
przedmioty.add(new Przedmiot("Kartka świąteczna", 1, 2));
przedmioty.add(new Przedmiot("Lusterko", 3, 4));
przedmioty.add(new Przedmiot("Lampka", 4, 5));
przedmioty.add(new Przedmiot("Czasopismo naukowe", 2, 3));
```

## Przykładowy output:
```yaml
Maksymalna wartość w plecaku (z kulami): <wartość>
Użyto kul magicznych: <liczba_kul>
Przedmioty w plecaku: ...
Przedmiot: ...
Waga: ...
Wartość: ...
```
## Uruchomienie

Sklonuj repozytorium:
```bash
git clone https://github.com/your-user/magic-knapsack-solver.git
```
## Skompiluj i uruchom program:
```bash
javac problemPlecakowy.java
java problemPlecakowy
```

<div align="center">

### Autorzy 

| Role | Name | GitHub |
|:---:|:---:|:---:|
| **Developer** | **Łukasz Matecki** | [GitHub Profile](https://github.com/LukaszMatecki) |

<br>
<i>Created for educational purposes.</i>
