package exam;

import java.io.IOException;

public class ex {
	public static void main(String[] args) throws IOException {
		String str = "abcde";
		
		StringBuffer sb = new StringBuffer();
		
		sb.append(str);

		System.out.println(str.substring(str.length(), str.length()));
	}
}
