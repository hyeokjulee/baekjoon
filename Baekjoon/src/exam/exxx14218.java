package exam;

import java.io.*;
import java.util.*;

public class exxx14218 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine()); // 도시 수, 기존 도로 수 입력
		int n = Integer.parseInt(st.nextToken()); // 도시 수
		int m = Integer.parseInt(st.nextToken()); // 기존 도로 수
		int[][] inArr = new int[m][2]; // 도로 배열

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine()); // 기존 도로 입력
			inArr[i][0] = Integer.parseInt(st.nextToken()); // 앞도시
			inArr[i][1] = Integer.parseInt(st.nextToken()); // 뒷도시
		}

		int q = Integer.parseInt(br.readLine()); // 정비할 도로 수 입력

		int[][] outArr = new int[q][n]; // 출력할 배열
		for (int i = 0; i < q; i++) {
			for (int j = 0; j < n; j++) {
				outArr[i][j] = -1; // 요소들은 일단 모두 -1 로 초기화
			}
		}

		int beforeIndex = 2147483647;
		boolean flag;
		Set<Integer> removeSet = new HashSet<>(); // 제거할 도시들
		int[][] treeArr = new int[][] { { 1 } }; // 도시번호가 요소이고 수도를 방문하는 최소 방문 도시 수가 행번호인 배열, 첫행에는 1번도시만 존재
		for (int j = 0; j < treeArr.length; j++) {
			for (int k = 0; k < treeArr[j].length; k++) {
				flag = false;
				// 추가한 행의 뒷행들에 추가한 뒷도시가 존재하는 경우 그 요소를 배열에서 제거한다.
				if (j > beforeIndex && removeSet.contains(treeArr[j][k])) {
						treeArr[j][k] = treeArr[j][treeArr[j].length - 1];
						treeArr[j] = Arrays.copyOf(treeArr[j], treeArr[j].length - 1);

						// 제거 예약 요소 제거
						removeSet.remove(treeArr[j][k]);

						flag = true;
						break;
					}

				if(flag) {
					continue;
				}
				
				for (int l = 0; l < m; l++) {
					if (treeArr[j][k] == inArr[l][0]) {
						if (j == treeArr.length - 1) { // treeArr[j]가 마지막행이라면
							treeArr = Arrays.copyOf(treeArr, treeArr.length + 1); // 뒷도시를 넣을 행 하나 추가
							treeArr[treeArr.length - 1] = new int[0]; // 추가된 행에 뒷도시를 넣을 자리를 만들어준다.
						}
						treeArr[j + 1] = Arrays.copyOf(treeArr[j + 1], treeArr[j + 1].length + 1); // 뒷도시를 넣을 열 하나 추가
						treeArr[j + 1][treeArr[j + 1].length - 1] = inArr[l][1]; // 추가된 새 열에 뒷도시를 넣어준다.

						// 제거할 요소들을 제거 예약 목록에 담는다.
						removeSet.add(inArr[l][1]);

						beforeIndex = j + 1;
					}
				}
			}
		}

		for (int i = 0; i < q; i++) { // 정비할 도로 수 q
			removeSet.clear(); // 제거 예약 목록 비우기

			inArr = Arrays.copyOf(inArr, inArr.length + 1); // 정비할 도로를 받을 행 하나씩 추가
			inArr[inArr.length - 1] = new int[2]; // 추가된 행에 도로를 입력할 자리를 만들어준다.

			// 정비할 도로 입력
			st = new StringTokenizer(br.readLine());
			inArr[inArr.length - 1][0] = Integer.parseInt(st.nextToken()); // 앞도시
			inArr[inArr.length - 1][1] = Integer.parseInt(st.nextToken()); // 뒷도시
			
			beforeIndex = 2147483647;
			
			// 트리에 도시 넣기
			for (int j = 0; j < treeArr.length; j++) {
				for (int k = 0; k < treeArr[j].length; k++) {
					flag = false;
					// 추가한 행의 뒷행들에 추가한 뒷도시가 존재하는 경우 그 요소를 배열에서 제거한다.
					
						if(j > beforeIndex && removeSet.contains(treeArr[j][k])) {
							treeArr[j][k] = treeArr[j][treeArr[j].length - 1];
							treeArr[j] = Arrays.copyOf(treeArr[j], treeArr[j].length - 1);

							// 제거 예약 요소 제거
							removeSet.remove(treeArr[j][k]);

							flag = true;
							break;
						}
					
					if(flag) {
						continue;
					}

					for (int l = m; l < m + i + 1; l++) {
						if (treeArr[j][k] == inArr[l][0]) {
							if (j == treeArr.length - 1) { // treeArr[j]가 마지막행이라면
								treeArr = Arrays.copyOf(treeArr, treeArr.length + 1); // 뒷도시를 넣을 행 하나 추가
								treeArr[treeArr.length - 1] = new int[0]; // 추가된 행에 뒷도시를 넣을 자리를 만들어준다.
							}
							treeArr[j + 1] = Arrays.copyOf(treeArr[j + 1], treeArr[j + 1].length + 1); // 뒷도시를 넣을 열 하나 추가
							treeArr[j + 1][treeArr[j + 1].length - 1] = inArr[l][1]; // 추가된 새 열에 뒷도시를 넣어준다.

							// 제거할 요소들을 제거 예약 목록에 담는다.
							removeSet.add(inArr[l][1]);
							
							beforeIndex = j + 1;
						}
					}
				}
			}

			// 출력할 배열에 각 도시별로 수도를 방문하는 데 최소 방문 도시들 넣어주기
			for (int j = treeArr.length - 1; j >= 0; j--) { // j = 수도를 방문하는 최소 방문 도시 수
				for (int k = 0; k < treeArr[j].length; k++) { // treeArr[j][k] = 도시 번호
					outArr[i][treeArr[j][k] - 1] = j;
				}
			}
		}
		br.close();

		// 출력
		StringBuffer stringBuffer = new StringBuffer();
		for (int i = 0; i < outArr.length; i++) {
			for (int j = 0; j < outArr[i].length; j++) {
				stringBuffer.append(outArr[i][j]);
				if (j != outArr[i].length - 1) {
					stringBuffer.append(" ");
				}
			}
			if (i != outArr.length - 1) {
				stringBuffer.append("\n");
			}
		}
		System.out.println(stringBuffer);
	}
}