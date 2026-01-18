# Algorytmy wyszukiwania wzorca w Pythonie

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CS Concepts](https://img.shields.io/badge/CS-Algorithms-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Educational-green?style=flat)

Projekt edukacyjny prezentujący klasyczne **algorytmy wyszukiwania wzorca w tekście**.  
Celem jest pokazanie, jak różne podejścia znajdują wszystkie wystąpienia podciągu (wzorca) w danym tekście.

---

## Zaimplementowane algorytmy

### 1. Algorytm naiwny
Porównuje wzorzec z każdym możliwym podciągiem tekstu.

- **Złożoność czasowa:** O(n * m)  
- Prosty, ale mało wydajny dla dużych tekstów i wzorców.

### 2. Algorytm Sunday
Algorytm z przesunięciami oparty na następnym znaku po oknie dopasowania.

- **Tabela przesunięć:** Określa, o ile przesunąć wzorzec przy niedopasowaniu.  
- **Średnia złożoność:** O(n / m)  

### 3. Algorytm Sunday z parami liter
Rozszerzenie Sunday, wykorzystujące **pary liter** do obliczania przesunięć.  

- **Tabela przesunięć:** Mapuje pary liter we wzorcu na wartości przesunięcia.  
- Zazwyczaj **szybszy**, gdy w tekście powtarzają się znaki.

### 4. Algorytm Knutha-Morrisa-Pratta (KMP)
Wykorzystuje **tabelę prefiks-sufiks** do uniknięcia powtarzanych porównań.  

- **Tabela prefiks-sufiks:** Najdłuższy prefiks będący też sufiksem.  
- **Złożoność:** O(n + m)  
- Bardzo wydajny przy dużych tekstach i wzorcach z powtarzającymi się fragmentami.

---

## Przykład użycia

```python
text = "BACABADEABADDEAABCCABAD"
pattern = "ABAD"
```

# Algorytm naiwny
```python
naive_algorithm(pattern, text)
```

# Algorytm Sunday
```python
sunday_algorithm(pattern, text)
```

# Algorytm Sunday z parami liter
```python
sunday_algorithm_pairs(pattern, text)
```

# Algorytm Knutha-Morrisa-Pratta
```python
knuth_morris_pratt(pattern, text)
```
## Wynik to lista indeksów, w których wzorzec występuje w tekście

<div align="center">

### Autorzy 

| Role | Name | GitHub |
|:---:|:---:|:---:|
| **Developer** | **Łukasz Matecki** | [GitHub Profile](https://github.com/LukaszMatecki) |

<br>
<i>Created for educational purposes.</i>

