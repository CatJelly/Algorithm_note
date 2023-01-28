/*
 * 돌게임 3
 * 탁자위 돌 N개를 턴을 번갈아 1,3,4개 가져갈 수 있음
 * 마지막 돌 가져가는 사람이 이김
 * 이기는 사람 구하기 (상근이 선)
 * 규칙을 찾아보쟈
 * 
 * 1 = S
 * 2 = C
 * 3 = S
 * 4 = S
 * 5 = S
 * 6 = S
 * 7 = C
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        if (N % 7 == 0 || N % 7 == 2) {
            System.out.println("CY");
        } else {
            System.out.println("SK");
        }

    }
}