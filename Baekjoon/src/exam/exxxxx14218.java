package exam;

import java.io.*;
import java.util.*;

public class exxxxx14218 {
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

		StringBuffer stringBuffer = new StringBuffer(); // 출력할 StringBuffer
		boolean flag; // 문자열을 담을 때 필요한 플래그

		Set[] tree = new Set[] { new HashSet() }; // 도시를 담는 셋이 요소이고 그 도시가 수도를 방문하는 최소 방문 도시 수가 인덱스인 Array
		tree[0].add(1); // 0번인덱스에는 1번도시만 담은 Set만 존재
		Set remove = new HashSet(); // 삭제 예약 목록

		for (int i = 0; i < q; i++) { // 정비할 도로 수 q
			inArr = Arrays.copyOf(inArr, inArr.length + 1); // 정비할 도로를 받을 행 하나씩 추가
			inArr[inArr.length - 1] = new int[2]; // 추가된 행에 도로를 입력할 자리를 만들어준다.

			st = new StringTokenizer(br.readLine()); // 정비할 도로 입력
			inArr[inArr.length - 1][0] = Integer.parseInt(st.nextToken()); // 앞도시
			inArr[inArr.length - 1][1] = Integer.parseInt(st.nextToken()); // 뒷도시

			remove.clear(); // 삭제 예약 목록 비우기

			for (int j = 0; j < tree.length; j++) { // tree에 도시 담기

				tree[j].removeAll(remove); // 삭제할 도시들 삭제
				if (tree[j].isEmpty()) { // 모두 삭제되었다면
					tree = Arrays.copyOf(tree, j); // 가지 치기
					break;
				}

				for (int k = 0; k < m + i + 1; k++) {
					if (tree[j].contains(inArr[k][0])) { // 앞도시를 Set이 포함하고 있다면
						if (j == tree.length - 1) { // tree의 인덱스가 마지막이라면
							tree = Arrays.copyOf(tree, j + 2); // 행 하나 추가
							tree[j + 1] = new HashSet(); // 추가된 행에 뒷도시를 넣을 Set을 만들어준다.
						}
						tree[j + 1].add(inArr[k][1]); // 만들어준 Set에 뒷도시를 넣어준다.
						remove.add(inArr[k][0]); // 앞도시를 삭제목록에 추가
					}
					if (tree[j].contains(inArr[k][1])) { // 뒷도시를 Set이 포함하고 있다면
						if (j == tree.length - 1) { // tree의 인덱스가 마지막이라면
							tree = Arrays.copyOf(tree, j + 2); // 행 하나 추가
							tree[j + 1] = new HashSet(); // 추가된 행에 앞도시를 넣을 Set을 만들어준다.
						}
						tree[j + 1].add(inArr[k][0]); // 만들어준 Set에 앞도시를 넣어준다.
						remove.add(inArr[k][1]); // 뒷도시를 삭제목록에 추가
					}
				}
			}

			for (int j = 0; j < n; j++) { // j = 도시 번호 - 1
				flag = true; // 도시번호가 tree에 있다면 false로 바꿔줄 예정
				for (int k = 0; k < tree.length; k++) { // k = tree의 인덱스 = 수도를 방문하는 최소 방문 도시 수
					if (tree[k].contains(j + 1)) {
						stringBuffer.append(k).append(" "); // k값과 공백 넣기
						flag = false; // 도시번호가 tree에 있음
						break; // for문을 돌며 더 큰 값을 넣기 전에 for문을 중지
					}
				}
				if (flag) { // 도시번호가 tree에 없다면
					stringBuffer.append(-1).append(" "); // -1값과 공백 넣기
				}
			}
			stringBuffer.append("\n"); // 줄바꿈 넣기
		}
		br.close();

		System.out.println(stringBuffer); // 출력
	}
}