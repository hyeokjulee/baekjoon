package exam;

import java.io.*;

class exxx5397 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); // 테스트 케이스의 개수 입력
		StringBuffer str = new StringBuffer(); // 테스트 케이스를 입력받을 문자열
		int length; // 문자열 길이
		int index; // 인덱스
		StringBuffer sb = new StringBuffer(); // 출력할 문자열

		for (int i = 0; i < n; i++) { // n줄의
			str.append(br.readLine()); // 데이터 입력

			do {
				index = str.indexOf("<");
				if (index > 0) {
					str.insert(index - 1, str.substring(index + 1, str.length())).setLength(str.length() - 1);
				} else {
					str.deleteCharAt(0);
				}
			} while (index != -1);
			
			do {
				index = str.indexOf(">");
				if (index < str.length()) {
					str.insert(index - 1, str.substring(index + 1, length)).setLength(length - 1);
				} else {
					str.deleteCharAt(str.length());
				}
			} while (index != -1);
			

			sb.append(str).append("\n");
		}
		System.out.println(sb);
		br.close();
	}
}