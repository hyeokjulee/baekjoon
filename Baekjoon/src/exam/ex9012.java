package exam;

import java.io.*;

class ex9012 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine()); // 데이터 수 입력

		String ps; // 데이터 입력받을 변수
		String[] splitedStr = new String[2];
		StringBuffer stringBuffer = new StringBuffer();
		
		for (int i = 0; i < t; i++) { // t줄의
			ps = br.readLine(); // 데이터 입력

			while (ps.contains("()")) {
				splitedStr = ps.split("\\(\\)", 2);
				ps = splitedStr[0] + splitedStr[1];
			}

			if (ps.equals("")) {
				stringBuffer.append("YES\n");
			} else {
				stringBuffer.append("NO\n");
			}
		}
		br.close();

		System.out.println(stringBuffer);
	}
}