package exam;

import java.util.Scanner;

class ex14659 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] h = new int[n];

		for (int i = 0; i < n; i++) {
			h[i] = sc.nextInt();
		}
		sc.close();

		int max = 0;
		int cnt;

		for (int i = 0; i < n - 1; i++) {
			cnt = 0;
			for (int j = i + 1; j < n; j++) {
				if (h[i] > h[j]) {
					cnt++;
				} else {
					break;
				}
			}
			max = max < cnt ? cnt : max;
		}

		System.out.println(max);
	}
}