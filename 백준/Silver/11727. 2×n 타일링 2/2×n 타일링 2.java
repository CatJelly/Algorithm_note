/*
 * 2xN 직사각형 1x2, 2x1, 2x2 타일 채우기
 * f(n) = f(n-2) * 2(가로2개, 2x2) + f(n-1) * 1(1x2)
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int [] dp = new int[n+3];
        dp[1] = 1;
        dp[2] = 3;
        
        for(int i=3; i<=n; i++) {
            dp[i] = (dp[i-1] + dp[i-2] * 2) % 10_007;
        }
        System.out.println(dp[n]);
    }
}