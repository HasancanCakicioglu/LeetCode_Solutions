class Romen:
    one = "I"
    five = "V"
    ten = "X"
    fifty = "L"
    oneHundred = "C"
    fiveHundred = "D"
    thousand = "M"


class Solution:
    def find_str(self, x):
        fir = 0
        romen = ""

        while x >= 1000:
            romen += Romen.thousand
            x -= 1000

        if x > 500 and 1000 - x < x - 799:
            fir = x // 100
            fir = 10 - fir
            x -= 1000
            for i in range(fir):
                romen += Romen.oneHundred
                x += 100
            romen += Romen.thousand

        while x >= 500:
            romen += Romen.fiveHundred
            x -= 500

        if x > 100 and 500 - x < x - 299:
            fir = x // 100
            fir = 5 - fir
            x -= 500
            for i in range(fir):
                romen += Romen.oneHundred
                x += 100
            romen += Romen.fiveHundred

        while x >= 100:
            romen += Romen.oneHundred
            x -= 100

        if x > 50 and 100 - x < x - 79:
            fir = x // 10
            fir = 10 - fir
            x -= 100
            for i in range(fir):
                romen += Romen.ten
                x += 10
            romen += Romen.oneHundred

        while x >= 50:
            romen += Romen.fifty
            x -= 50

        if x > 10 and 50 - x < x - 29:
            fir = x // 10
            fir = 5 - fir
            x -= 50
            for i in range(fir):
                romen += Romen.ten
                x += 10
            romen += Romen.fifty

        while x >= 10:
            romen += Romen.ten
            x -= 10

        if x > 5 and (10 - x < x - 6.9):
            fir = 10 - x
            x -= 10
            for i in range(fir):
                romen += Romen.one
                x += 1
            romen += Romen.ten

        while x >= 5:
            romen += Romen.five
            x -= 5

        if x > 1 and 5 - x < x - 1.9:
            fir = 5 - x
            x -= 5
            for i in range(fir):
                romen += Romen.one
                x += 1
            romen += Romen.five

        while x >= 1:
            romen += Romen.one
            x -= 1

        return romen

    def intToRoman(self, num):
        x = num

        basamak = []
        romenList = []

        while num >= 1:
            basamak.append(num % 10)
            num = num // 10

        return self.find_str(x)
