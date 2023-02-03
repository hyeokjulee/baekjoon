package exam;

import java.util.Arrays;

public class ex {
	public static void main(String[] args) {
		int[][] arr = new int[2][2];

		for (int i = 0; i < 10; i++) {
			arr = Arrays.copyOf(arr, arr.length + 1);
			System.out.println(arr.length);
		}
	}
}
