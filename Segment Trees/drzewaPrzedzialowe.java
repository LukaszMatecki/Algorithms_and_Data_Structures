import java.util.*;

class CannonTree
{
    private final int n;
    private int rozmiar;
    private final int[] suma;
    private final long[] najpozniejszy_czas_zestrzelenia;
    private static final long NEG = Long.MIN_VALUE / 4;

    public CannonTree(int[] cele)
    {
        this.n = cele.length;

        rozmiar = 1;
        while (rozmiar < n) rozmiar <<= 1;

        suma = new int[2 * rozmiar];
        najpozniejszy_czas_zestrzelenia = new long[2 * rozmiar];

        build(cele);
    }

    private void build(int[] cele)
    {
        for (int i = 0; i < rozmiar; i++)
        {
            int node = rozmiar + i;

            if (i < n) {
                int odwrocony_indeks = n - 1 - i;
                int liczba_celow = cele[odwrocony_indeks];

                suma[node] = liczba_celow;

                if (liczba_celow > 0) { najpozniejszy_czas_zestrzelenia[node] = odwrocony_indeks + 2L * (liczba_celow - 1); }
                else { najpozniejszy_czas_zestrzelenia[node] = NEG; }
            }
            else {
                suma[node] = 0;
                najpozniejszy_czas_zestrzelenia[node] = NEG;
            }
        }
        for (int v = rozmiar - 1; v >= 1; v--) { pull(v);}
    }

    private void pull(int v)
    {
        // v - indeks węzła rodzica
        int L = 2 * v; // lewe dziecko
        int R = 2 * v + 1; // prawe dziecko

        suma[v] = suma[L] + suma[R];

        long przesuniecie_w_prawo = (najpozniejszy_czas_zestrzelenia[R] == NEG) ? NEG : najpozniejszy_czas_zestrzelenia[R] + 2L * suma[L];
        najpozniejszy_czas_zestrzelenia[v] = Math.max(najpozniejszy_czas_zestrzelenia[L], przesuniecie_w_prawo);
    }

    public void update(int indeks, int nowa_wartosc) {
        int odwrotny_indeks = n - 1 - indeks;
        int pos = rozmiar + odwrotny_indeks;

        suma[pos] = nowa_wartosc;

        if (nowa_wartosc > 0) { najpozniejszy_czas_zestrzelenia[pos] = indeks + 2L * (nowa_wartosc - 1); }
        else { najpozniejszy_czas_zestrzelenia[pos] = NEG; }

        pos /= 2;
        while (pos >= 1)
        {
            pull(pos);
            pos /= 2;
        }
    }
    public long getLastHitTime() { return najpozniejszy_czas_zestrzelenia[1] == NEG ? 0 : najpozniejszy_czas_zestrzelenia[1]; }
}

public class drzewaPrzedzialowe
{
    public static void main(String[] args)
    {
        int[] targets = {0, 2, 0, 0, 3};
        CannonTree cannon = new CannonTree(targets);

        System.out.println("Czas zestrzelenia wszystkich celów: " + cannon.getLastHitTime());
        cannon.update(1, 1);
        System.out.println("Po zmianie odległości 1 na 1: " + cannon.getLastHitTime());
        cannon.update(2, 3);
        System.out.println("Po zmianie odległości 2 na 3: " + cannon.getLastHitTime());
    }
}