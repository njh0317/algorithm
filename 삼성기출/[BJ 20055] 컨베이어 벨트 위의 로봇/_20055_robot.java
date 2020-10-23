import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class _20055_robot {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
	    int N = Integer.parseInt(s[0]); //컨베이어 가로 길이 
	    int K = Integer.parseInt(s[1]); //로봇의 개수 
	    int[] arr = new int[2*N];
	    int[] robot = new int[N];
	    s = br.readLine().split(" ");
	    for(int i = 0; i<2*N;i++)
	    {
	    	arr[i] = Integer.parseInt(s[i]);
	    }
	    int insert_robot_num = 0;
	    int phase = 1;
	    while(true) {
	    	arr = rotate(arr, 2*N,1);
	    	robot = rotate(robot, N,0);
	    	
	    	for (int i=N-1;i>=0;i--) {
	    		
	    		if(robot[i]==1) { //로봇이 존재하면 
	    			//다음이 이미 내려야하는 곳인데 그 다음 인덱스가 0이게 되면 이 if 문 안에 안들어옴 !! 수정하기  !!!  
	    			
	    			if(i+1 == N-1 && arr[i+1]>0)
	    			{
	    				robot[i] = 0;
	    				arr[i+1]-=1;
	    			}
	    			else if(arr[i+1]>0 && robot[i+1]==0)
	    			{
	    				robot[i+1] = 1;
	    				robot[i] = 0;
	    				arr[i+1]-=1;
	    			}
	    		}
	    	}

		    if(arr[0]!=0 && robot[0] == 0) {
		    	robot[0] = 1;
		    	arr[0]-=1;
		    	
	    	}
	    	if(count(arr, 2*N)>=K) {
	    		break;
	    	}
	    	
	    	phase+=1;
	    	
	    }
	    System.out.println(phase);

	}
	static int[] rotate(int[] arr, int n, int option) {
		int temp = arr[n-1];
		
		for(int i=n-1;i>0;i--)
		{
			arr[i] = arr[i-1];
		}
		if(option == 1) {
			arr[0] = temp;
		}
		else {
			arr[0] = 0;
			arr[n-1] = 0;
		}
		return arr;
	}
	static int count(int[] arr, int n) {
		int num = 0;
		for (int i=0;i<n;i++) {
			if(arr[i]==0) {
				num++;
			}
		}
		return num;
		
	}


}
