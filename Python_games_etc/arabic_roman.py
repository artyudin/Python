def to_roman(num):
	
	table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
	roman=''

	for pair in table:

		while num-pair[1]>=0:

			num-=pair[1]
			roman+=pair[0]

	return roman


print(to_roman(11))




assert to_roman(11) == "XI", "11 should return XI"
assert to_roman(60) == "LX", "60 should return LX"
assert to_roman(78) == "LXXVIII", "78 should return LXXVIII"
assert to_roman(4) == "IV", "4 should return IV"
assert to_roman(99) == "XCIX", "99 should return XCIX"

# Add your own assert tests below
