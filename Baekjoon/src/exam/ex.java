package exam;

public class ex {
	public static void main(String[] args) {
		String phone = "010()4741()3159";
		String[] splitedStr = phone.split("\\(\\)");
		String str = "";
		for (int i = 0; i < splitedStr.length; i++) {
			str += splitedStr[i];
		}
		System.out.println(str);
	}
}
