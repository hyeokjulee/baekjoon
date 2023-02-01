package exam;

import java.io.*;
import java.util.*;

public class ex14218 {
	public static void main(String[] args) throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
	    int n = Integer.parseInt(st.nextToken()); //도시 수
	    int m = Integer.parseInt(st.nextToken()); //기존 도로 수
	    int[][] inArr = new int[m][2]; //기존 도로
	    
	    int[][] treeArr; //도시번호가 요소인 배열, 행번호가 수도를 방문하는 최소 방문 도시 수를 갖는다.
	    
	    for (int i = 0; i < m; i++) { //기존 도로 입력
	    	st = new StringTokenizer(br.readLine());
	    	inArr[i][0] = Integer.parseInt(st.nextToken());
	    	inArr[i][1] = Integer.parseInt(st.nextToken());
	    }
	    
	    int q = Integer.parseInt(br.readLine()); //정비할 도로 수
	    int[][] outArr = new int[q][n]; //각 도시별 수도를 방문하는 데 최소 방문 도시 수
	    
	    for (int i = 0; i < q; i++) { //정비
	    	inArr = Arrays.copyOf(inArr, inArr.length + i + 1); //정비 후 도로
	    	
	    	st = new StringTokenizer(br.readLine());
	    	inArr[inArr.length + i][0] = Integer.parseInt(st.nextToken());
	    	inArr[inArr.length + i][1] = Integer.parseInt(st.nextToken());
	    	
	    	outArr[i][0] = 0; //1번도시는 무조건 0
	    	for (int j = 1; j < n; j++) { //2번도시부터 시작
			}
	    }
	    
	    br.close();
	    System.out.println();
	}
}