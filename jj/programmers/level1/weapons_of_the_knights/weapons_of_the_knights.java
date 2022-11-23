// source: https://school.programmers.co.kr/learn/courses/30/lessons/136798

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> countDivisorNumber(int number) {
        List<Integer> divisorNumber = new ArrayList<>();

        for (int i = 0 ; i < number + 1; i++) {
            divisorNumber.add(0);
        }

        for (int i = 1; i < number + 1; i++) {
            int j = 1;

            while (i * j < number + 1) {
                divisorNumber.set(i * j, divisorNumber.get(i *j) + 1);
                j += 1;
            }
        }

        return divisorNumber;
    }

    public int getRequiredIron(
        List<Integer> divisorNumber,
        int limit,
        int power
    ) {
        int ironRequired = 0;

        for (int i = 1; i < divisorNumber.size(); i++) {
            if (divisorNumber.get(i) > limit) {
                ironRequired += power;
            } else {
                ironRequired += divisorNumber.get(i);
            }
        }

        return ironRequired;
    }

    public int solution(int number, int limit, int power) {
        List<Integer> divisorNumber = countDivisorNumber(number);

        return getRequiredIron(divisorNumber, limit, power);
    }
}