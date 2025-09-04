n = 3540
thousands = ["", "M", "MM", "MMM"]
hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
thousand = n // 1000
hundred = (n % 1000) // 100
ten = (n % 100) // 10
one = n % 10
roman = thousands[thousand] + hundreds[hundred] + tens[ten] + ones[one]
print(roman)
