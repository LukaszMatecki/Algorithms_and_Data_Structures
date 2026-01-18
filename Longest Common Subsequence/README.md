# Narzędzie do porównywania tekstów z użyciem LCS

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Algorithms-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Edukacyjny-green?style=flat)

Projekt dostarcza prostą **użyteczną funkcję do porównywania plików tekstowych** opartą na algorytmie **Longest Common Subsequence (LCS)**. Przydatna do wizualizacji różnic między dwiema wersjami dokumentu lub pliku z kodem, podobnie jak w systemach kontroli wersji (np. Git) lub w narzędziach typu diff.

---

## Opis

Narzędzie wczytuje dwa pliki tekstowe i oblicza różnice linia po linii z wykorzystaniem **algorytmu LCS**:

- Linie obecne w obu plikach są oznaczane jako niezmienione.  
- Linie obecne tylko w jednym z plików są oznaczone jako dodane lub usunięte.  
- Pozwala to łatwo wizualizować zmiany między dwiema wersjami pliku.

---

## Użycie

1. Przygotuj dwa pliki tekstowe do porównania, np.:

```sh
file_1 = "file_1.txt"
file_2 = "file_2.txt"
```

2. Zaimportuj funkcję print_diff i wywołaj ją:
```sh
file_1 = "file_1.txt"
file_2 = "file_2.txt"
print_diff(file_1, file_2)
```
3. Wynik pokazuje:

```txt
- linie usunięte z pierwszego pliku
+ linie dodane w drugim pliku
```
Linie bez symboli pozostają niezmienione

## Uwagi

Oba pliki wejściowe muszą być zwykłymi plikami tekstowymi.
Porównanie odbywa się linia po linii. Aby porównywać słowa lub znaki, kod należy zmodyfikować.
Projekt przeznaczony do celów edukacyjnych i małych/średnich plików tekstowych.

### Przykładowy wynik

## Pliki:

```sh
file_1.txt
```
```txt
Hello World
To jest test
Do widzenia
```
```sh
file_2.txt
```
```txt
Hello World
To jest przykład
Do widzenia
```

## Wynik:
```txt 
  Hello World
- To jest test
+ To jest przykład
  Do widzenia
```
