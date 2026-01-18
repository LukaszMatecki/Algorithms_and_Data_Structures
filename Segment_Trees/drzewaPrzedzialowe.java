import java.util.*;

class CannonTree {
    private final int n;
    private int size;
    private final int[] sum;
    private final long[] last_hit_time;
    private static final long NEG = Long.MIN_VALUE / 4;

    public CannonTree(int[] targets) 
    {
        this.n = targets.length;

        size = 1;
        while (size < n) size <<= 1;

        sum = new int[2 * size];
        last_hit_time = new long[2 * size];

        build(targets);
    }

    private void build(int[] targets) 
    {
        for (int i = 0; i < size; i++) 
        {
            int node = size + i;

            if (i < n) 
            {
                int reversed_index = n - 1 - i;
                int target_count = targets[reversed_index];

                sum[node] = target_count;

                if (target_count > 0) { last_hit_time[node] = reversed_index + 2L * (target_count - 1); } 
                else { last_hit_time[node] = NEG; }
            } else {
                sum[node] = 0;
                last_hit_time[node] = NEG;
            }
        }

        for (int v = size - 1; v >= 1; v--) {
            pull(v);
        }
    }

    private void pull(int v) 
    {
        int L = 2 * v;
        int R = 2 * v + 1;

        sum[v] = sum[L] + sum[R];

        long right_shift = (last_hit_time[R] == NEG) ? NEG : last_hit_time[R] + 2L * sum[L];
        last_hit_time[v] = Math.max(last_hit_time[L], right_shift);
    }

    public void update(int index, int new_value) 
    {
        int reversed_index = n - 1 - index;
        int pos = size + reversed_index;

        sum[pos] = new_value;

        if (new_value > 0) { last_hit_time[pos] = index + 2L * (new_value - 1); } 
        else { last_hit_time[pos] = NEG; }

        pos /= 2;
        while (pos >= 1) {
            pull(pos);
            pos /= 2;
        }
    }

    public long getLastHitTime() { return last_hit_time[1] == NEG ? 0 : last_hit_time[1]; }
}

public class SegmentTreesDemo {
    public static void main(String[] args) {
        int[] targets = {0, 2, 0, 0, 3};
        CannonTree cannon = new CannonTree(targets);

        System.out.println("Time to hit all targets: " + cannon.getLastHitTime());
        cannon.update(1, 1);
        System.out.println("After updating index 1 to 1: " + cannon.getLastHitTime());
        cannon.update(2, 3);
        System.out.println("After updating index 2 to 3: " + cannon.getLastHitTime());
    }
}
