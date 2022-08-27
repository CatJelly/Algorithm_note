import java.util.Scanner;

public class Main {
	public int factorial(int N) {
		if(N==0)
			return 1;
		else return N*factorial(N-1);
	}
    public static void main(String[] args) {
    	Main func = new Main();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        System.out.println(func.factorial(N));
    }
} 