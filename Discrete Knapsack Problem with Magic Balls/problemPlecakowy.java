import java.util.ArrayList;
import java.util.List;

class Plecak {
    int pojemnosc;

    public Plecak(int pojemnosc){
        this.pojemnosc = pojemnosc;
    }
    public int getPojemnosc(){return pojemnosc;}
}

class Przedmiot {
    String nazwa;
    int waga;
    int wartosc;

    public Przedmiot(String nazwa, int waga, int wartosc) {
        this.nazwa = nazwa;
        this.waga = waga;
        this.wartosc = wartosc;
    }

    public String getNazwa() {return nazwa;}
    public int getWaga() {return waga;}
    public int getWartosc() {return wartosc;}
}

class MagicznaKula {
    int ilosc;
    int waga;

    public MagicznaKula(int ilosc, int waga) {
        this.ilosc = ilosc;
        this.waga = waga;
    }

    public int getWagaKuli() {return waga;}
    public int getIlosc() {return ilosc;}
}

class KnapsackSolver
{
    // Złożoność O(n * W + m), gdzie n to liczba przedmiotów, W to pojemność plecaka, m to liczba kul
    public static void rozwiazProblem(Plecak plecak, List<Przedmiot> przedmioty, MagicznaKula kule)
    {
        int liczbaPrzedmiotow = przedmioty.size();
        int pojemnoscPlecaka = plecak.getPojemnosc();
        int iloscKul = kule.getIlosc();
        int wagaKuli = kule.getWagaKuli();

        int[][] dp = new int[liczbaPrzedmiotow + 1][pojemnoscPlecaka + 1];

        for (int i = 1; i <= liczbaPrzedmiotow; i++)
        {
            Przedmiot p = przedmioty.get(i - 1);
            for (int w = 0; w <= pojemnoscPlecaka; w++)
            {
                if (p.getWaga() <= w)
                {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - p.getWaga()] + p.getWartosc());
                }
                else
                {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        long najlepszaWartosc = 0;
        int najlepszaKula = 0;
        int pozostalaPojemnoscDlaPrzedmiotow = pojemnoscPlecaka;

        for (int b = 0; b <= iloscKul; b++)
        {
            if (b * wagaKuli > pojemnoscPlecaka) break;
            
            int wagaUzytaPrzezKule = b * wagaKuli;
            if (wagaUzytaPrzezKule > pojemnoscPlecaka) break;

            int pozostalaPojemnosc = pojemnoscPlecaka - wagaUzytaPrzezKule;
            long wartoscBazowa = dp[liczbaPrzedmiotow][pozostalaPojemnosc];
            double total = wartoscBazowa * Math.pow(2, b);

            if (total > najlepszaWartosc) {
                najlepszaWartosc = (long) total;
                najlepszaKula = b;
                pozostalaPojemnoscDlaPrzedmiotow = pozostalaPojemnosc;
            }
        }

        System.out.println("\nMaksymalna wartość w plecaku (z kulami): " + najlepszaWartosc);
        System.out.println("Użyto kul magicznych: " + najlepszaKula);
        System.out.println("\nPrzedmioty w plecaku o pojemności " + pojemnoscPlecaka + ":");

        int wynik = dp[liczbaPrzedmiotow][pozostalaPojemnoscDlaPrzedmiotow];
        int waga = pozostalaPojemnoscDlaPrzedmiotow;

        for (int i = liczbaPrzedmiotow; i > 0 && wynik > 0; i--)
        {
            if (wynik != dp[i - 1][waga])
            {
                Przedmiot p = przedmioty.get(i - 1);
                System.out.println("Przedmiot: " + p.getNazwa() + "\nWaga: " + p.getWaga() + "\nWartość: " + p.getWartosc() + "\n");
                wynik -= p.getWartosc();
                waga -= p.getWaga();
            }
        }
    }
}

public class problemPlecakowy{
    public static void main(String[] args)
    {
        Plecak p1 = new Plecak(7);
        MagicznaKula kule = new MagicznaKula(5, 3);

        List<Przedmiot> przedmioty = new ArrayList<>();
        przedmioty.add(new Przedmiot("Encyklopedia zwierząt", 3, 2));
        przedmioty.add(new Przedmiot("Kartka świąteczna", 1, 2));
        przedmioty.add(new Przedmiot("Lusterko", 3, 4));
        przedmioty.add(new Przedmiot("Lampka", 4, 5));
        przedmioty.add(new Przedmiot("Czasopismo naukowe", 2, 3));
        KnapsackSolver.rozwiazProblem(p1, przedmioty, kule);
    }
}
