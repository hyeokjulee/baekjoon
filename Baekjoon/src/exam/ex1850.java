package exam;

import java.io.*;
import java.util.Scanner;

class ex1850 {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long m = sc.nextLong();
		sc.close();

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 0; i < div(m, n); i++) {
			bw.write(String.valueOf(1));
		}
		bw.close();
	}

	public static long div(long a, long b) {
		if (a % b == 0) {
			return b;
		} else {
			return div(b, a % b);
		}
	}
}