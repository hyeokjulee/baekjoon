package exam;

import java.util.*;

public class ex {
	public static void main(String[] args) {
		Set[] tree = new Set[] {new HashSet<>(1), new HashSet<>(3), new HashSet<>(5)};
		
		tree[1].add(2);
		tree[1].add(3);
		
		int sum = 0;
		
		Iterator<Integer> iterSet = tree[1].iterator();
        while(iterSet.hasNext()) {
            sum += iterSet.next();
        }
        
        System.out.println(sum);
	}
}
