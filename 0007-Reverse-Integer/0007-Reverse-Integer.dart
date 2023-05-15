import 'dart:math' as math;

class Solution {
  int basamak(int x) {

    bool negatif = false;

    if (x < 0) {
      x = x * -1;
      negatif = true;
    }

    List<int> reversed = [];

    while (x >= 1) {
      reversed.add(x % 10);
      x = x ~/ 10;
    }

    int newNumber = 0;
    int multiple = 0;
    for (int i = 0; i < reversed.length; i++) {
      newNumber = newNumber +
          (reversed[i] * math.pow(10, reversed.length - i - 1).toInt());
    }

    if (negatif == true) {
      newNumber = newNumber * -1;
    }
    if (math.pow(-2, 31) <= newNumber && newNumber <= (math.pow(2, 31) - 1)) {
      print(x.bitLength);
    } else {
      print(x.bitLength);
      return 0;
    }
    return newNumber;
  }

  int reverse(int x) {
    return basamak(x);
  }
}
