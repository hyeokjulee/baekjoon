package exam;

import java.io.*;
import java.util.StringTokenizer;

public class ex13305 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		//입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine()); //도시 수 입력
		int[] arr1 = new int[n - 1]; //거리 배열 선언
		int[] arr2 = new int[n]; //가격 배열 선언
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n - 1; i++) {
			arr1[i] = Integer.parseInt(st.nextToken()); //거리 값 넣기
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr2[i] = Integer.parseInt(st.nextToken()); //가격 값 넣기
		}
		br.close();

		//처리
		for (int i = 1; i < n; i++) {
			arr2[i] = arr2[i - 1] < arr2[i] ? arr2[i - 1] : arr2[i]; //거리 배열 처리
		}
		long minCost = 0; //최소 비용
		for (int i = 0; i < n - 1; i++) {
			minCost += (long) arr1[i] * arr2[i]; //최소 비용 계산
		}

		//출력
		System.out.println(minCost); //최소 비용 출력
	}
}