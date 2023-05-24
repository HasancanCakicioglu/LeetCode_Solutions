import 'dart:math' as math;

class Solution {
  int maxArea(List<int> height) {
    int len_list = height.length;

    int result = 0;
    int sayac = 0;
    int first = 0;
    int last = 0;
    for (int z = 0; z < len_list - 1; z++) {
      sayac = 0;
      first = 0;
      last = 0;

      if(result>10000*(len_list-1-z)){
        continue;
      }

      for (int i = len_list - z - 1; i < len_list; i++) {
        if ((math.min(first, last)) > (math.min(height[i], height[sayac]))) {
          sayac++;
          continue;
        } else {
          first = height[sayac];
          last = height[i];
        }

        result =
            math.max(result, math.min(height[i], height[sayac]) * (i - sayac));
        sayac++;
      }
    }

    return result;
  }
}
