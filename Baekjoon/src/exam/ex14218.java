package exam;

import java.io.*;
import java.util.*;

public class ex14218 {
	public static void main(String[] args) throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
	    //도시 수, 기존 도로 수 입력
		StringTokenizer st = new StringTokenizer(br.readLine());
	    int n = Integer.parseInt(st.nextToken()); //도시 수
	    int m = Integer.parseInt(st.nextToken()); //기존 도로 수
	    int[][] inArr = new int[m][2]; //도로 배열
	    
	    //기존 도로 입력
	    for (int i = 0; i < m; i++) {
	    	st = new StringTokenizer(br.readLine());
	    	inArr[i][0] = Integer.parseInt(st.nextToken());
	    	inArr[i][1] = Integer.parseInt(st.nextToken());
	    }

	    //정비할 도로 수 입력
	    int q = Integer.parseInt(br.readLine());
	    
	    int[][] outArr = new int[q][n]; //출력할 배열

	    for (int i = 0; i < q; i++) {
			for (int j = 0; j < n; j++) {
				outArr[i][j] = -1; //일단 -1 값으로 초기화
			}
		}
	    
	    for (int i = 0; i < q; i++) { //한번에 도로 하나씩 q번의 정비
	    	int[] insertArray1 = new int[1];
		    int[] insertArray2 = new int[2];
	    	
	    	inArr = Arrays.copyOf(inArr, inArr.length + 1); //정비할 도로를 받을 행 하나씩 추가
	    	inArr[inArr.length - 1] = insertArray2;
	    	
	    	//정비할 도로 입력
	    	st = new StringTokenizer(br.readLine());
	    	inArr[inArr.length - 1][0] = Integer.parseInt(st.nextToken());
	    	inArr[inArr.length - 1][1] = Integer.parseInt(st.nextToken());
	    	
	    	int[][] copiedInArr = Arrays.copyOf(inArr, inArr.length);
	    	
		    int[][] treeArr = {{1}}; //도시번호가 요소이고 수도를 방문하는 최소 방문 도시 수가 행번호인 배열, 1번도시는 무조건 0
	    	//트리에 도시 넣기
	    	for (int j = 0; j < treeArr.length; j++) {
	    		for (int k = 0; k < treeArr[j].length; k++) {
	    			for (int l = 0; l < copiedInArr.length; l++) {
	    				
	    				if(j > 0) {
	    					List<Integer> intList = new ArrayList<>();
		    		        for (int element : treeArr[j - 1]) {
		    		            intList.add(element);
		    		        }
		    		        if (treeArr[j][k] == copiedInArr[l][0] && treeArr[j][k] == copiedInArr[l][1]
		    						|| treeArr[j][k] == copiedInArr[l][0] && intList.contains(copiedInArr[l][1])
		    						|| treeArr[j][k] == copiedInArr[l][1] && intList.contains(copiedInArr[l][0])) {
		    					continue;
		    				}
	    				}else {
	    					if (treeArr[j][k] == copiedInArr[l][0] && treeArr[j][k] == copiedInArr[l][1]) {
		    					continue;
		    				}
						}
	    				
	    				if (treeArr[j][k] == copiedInArr[l][0]) {
							if (j == treeArr.length - 1) { //treeArr[j]가 마지막행이라면
	    						treeArr = Arrays.copyOf(treeArr, treeArr.length + 1); //다음 행을 만들어준다.
	    						treeArr[treeArr.length - 1] = insertArray1;
	    					}
	    					treeArr[j + 1] = Arrays.copyOf(treeArr[j + 1], treeArr[j + 1].length + 1); //treeArr[j + 1]에 도시번호를 넣을 새 열을 만들어준다.
							treeArr[j + 1][treeArr[j + 1].length - 1] = copiedInArr[l][1]; //만들어준 새 열에 도시번호를 넣어준다.
						}
	    				if (treeArr[j][k] == copiedInArr[l][1]) {
	    					if (j == treeArr.length - 1) { //treeArr[j]가 마지막행이라면
	    						treeArr = Arrays.copyOf(treeArr, treeArr.length + 1); //다음 행을 만들어준다.
	    						treeArr[treeArr.length - 1] = insertArray1;
	    					}
	    					treeArr[j + 1] = Arrays.copyOf(treeArr[j + 1], treeArr[j + 1].length + 1); //treeArr[j + 1]에 도시번호를 넣을 새 열을 만들어준다.
							treeArr[j + 1][treeArr[j + 1].length - 1] = copiedInArr[l][0]; //만들어준 새 열에 도시번호를 넣어준다.
						}
					}
				}
			}
	    	
	    	//출력할 배열에 각 도시별로 수도를 방문하는 데 최소 방문 도시들 넣어주기
	    	for (int j = treeArr.length - 1; j >= 0; j--) { //j = 수도를 방문하는 최소 방문 도시 수
	    		for (int k = 0; k < treeArr[j].length; k++) { //treeArr[j][k] = 도시 번호
	    			if(treeArr[j][k] != 0) {
	    				outArr[i][treeArr[j][k] - 1] = j;
	    			}
	    		}
			}
	    }
	    br.close();
	    
	    //출력
	    for (int i = 0; i < outArr.length; i++) {
			for (int j = 0; j < outArr[i].length; j++) {
				System.out.print(outArr[i][j] + " ");
			}
			System.out.println();
		}
	}
}