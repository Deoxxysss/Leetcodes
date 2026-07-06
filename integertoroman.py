class Solution:
    def intToRoman(self, num: int) -> str:
        a = num//1000
        b = (num-a*1000)//100
        c = (num - a*1000 - b*100)//10
        d = (num - a*1000 - b*100 - c*10)//1
        roman_m = {"": 0, "M": 1, "MM": 2, "MMM": 3}
        hundreds = {"": 0, "C": 1, "CC": 2, "CCC": 3, "CD": 4, "D": 5, "DC": 6, "DCC": 7, "DCCC": 8, "CM": 9}
        tens = {"": 0, "X": 1, "XX": 2, "XXX": 3, "XL": 4, "L": 5, "LX": 6, "LXX": 7, "LXXX": 8, "XC": 9}
        ones = {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
        for key, value in roman_m.items():
            if value == a:
                T = key
                
        for key, value in hundreds.items():
            if value == b:
                M = key
                
        for key, value in tens.items():
            if value == c:
                N = key
                
        for key, value in ones.items():
            if value == d:
                X = key
                
        Z = T + M + N + X
        return Z