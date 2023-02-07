package exam;

import java.io.*;

class exx5397 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); // 테스트 케이스의 개수 입력
		char[] charArr; // 테스트 케이스를 입력받을 배열
		StringBuffer sb1 = new StringBuffer(); // 출력할 한줄의 문자열
		StringBuffer sb2 = new StringBuffer(); // 출력할 n줄의 전체 문자열
		int cursor; // 커서의 위치 (출력할 한줄의 문자열에서의 인덱스)
		int sb1length; // 출력할 한줄 문자열의 길이
		int strLength; // 데이터 한줄의 길이

		for (int i = 0; i < n; i++) { // n줄의
			sb1.setLength(0); // sb1 초기화
			charArr = br.readLine().toCharArray(); // 데이터 입력
			strLength = charArr.length; // 데이터 한줄의 길이
			cursor = 0; // 커서 위치 초기화
			sb1length = 0; // 출력할 한줄 문자열의 현재 길이
			
			for (int j = 0; j < strLength; j++) {
				if (charArr[j] != '-' && charArr[j] != '<' && charArr[j] != '>') {
					if (cursor == sb1length) {
						sb1.append(charArr[j]);
						sb1length++;
					} else {
						sb1.insert(cursor, charArr[j]);
						sb1length++;
					}
					cursor++;
				} else if (charArr[j] == '-' && cursor > 0) {
					sb1.deleteCharAt(cursor - 1);
					sb1length--;
					cursor--;
				} else if (charArr[j] == '<' && cursor > 0) {
					cursor--;
				} else if (charArr[j] == '>' && cursor < sb1length) {
					cursor++;
				}
			}
			sb2.append(sb1).append("\n");
		}
		System.out.println(sb2);
		br.close();
	}
}