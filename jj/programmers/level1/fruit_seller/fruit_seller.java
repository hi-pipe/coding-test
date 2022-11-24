// source: https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=java

import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int getNumForSale(Integer[] score, int m) {

        return score.length / m * m;
    }

    public int getMinScore(
        int m,
        Integer[] score,
        int index
    ) {
        int minScore = 1_000_000;
        
        for (int i = index; i < index + m; i++) {
            minScore = Math.min(minScore, score[i]);
        }
        
        return minScore;
    }

    public int computeProfit(
        int numForSale,
        int m,
        Integer[] score
    ) {
        int profit = 0;

        for (int i = 0; i < numForSale; i += m) {
            profit += getMinScore(m, score, i) * m;
        }

        return profit;
    }

    public int solution(int k, int m, int[] score) {
        Integer[] rank = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(rank, Collections.reverseOrder());

        int numForSale = getNumForSale(rank, m);

        return computeProfit(numForSale, m, rank);
    }
}