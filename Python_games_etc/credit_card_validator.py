###Credit Card Validator

# Using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm), 
# also known as "modulus 10", we will be determining the validity of 
# a given credit card number.



class CreditCard:
	def __init__(self, card_number):
		self.card_number = card_number
		self.card_type = "INVALID"
		self.valid = False
		self.run()

#Create and add your method called `determine_card_type` to the CreditCard class here:
	def determine_card_type(self):
		if self.card_number[0] == '4':
			self.card_type = "VISA"
		elif self.card_number[:2] in ['51','52','53','54','55']:
			self.card_type = "MASTERCARD"
		elif self.card_number[:2] in ['34','37']:
			self.card_type = "AMEX"
		elif self.card_number[:4] == "6011":
			self.card_type = "DISCOVER"
		else:
			self.card_type = "INVALID"
			return False
		return True
#Create and add your method called `check_length` to the CreditCard class here:
	def check_length(self):
		if len(self.card_number) == 15:
			return True
		elif len(self.card_number) == 16:
			return True
		else:
			return False

#Create and add your method called 'validate' to the CreditCard class here:
	def validate(self):
		c_list = [int(char) for char in self.card_number]
		b_list = [c_list[idx]*2 for idx in range(len(c_list)-2,-1,-2)]
		d_list = sum((char//10+char%10) for char in b_list if char > 9)
		m_list = sum(char for char in b_list if char < 10)
		e_list = sum(c_list[idx] for idx in range(len(c_list)-1,-1,-2))
		if (e_list + d_list + m_list)%10 == 0:
			return True
		else:
			return False


	def run(self):
		self.determine_card_type()
		if self.card_type != "INVALID":
			if self.check_length():
				if self.validate():
					self.valid = True
					return self.valid
			self.card_type = "INVALID"



cc = CreditCard('6011053711075799')
print(cc.run())
# print(cc.check_length())
# print(cc.validate())








#do not modify assert statements
if __name__ == '__main__':
	cc = CreditCard('9999999999999999')

	assert cc.valid == False, "Credit Card number cannot start with 9"
	assert cc.card_type == "INVALID", "99... card type is INVALID"

	cc = CreditCard('4440')

	assert cc.valid == False, "4440 is too short to be valid"
	assert cc.card_type == "INVALID", "4440 card type is INVALID"

	cc = CreditCard('5515460934365316')

	assert cc.valid == True, "Mastercard is Valid"
	assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

	cc = CreditCard('6011053711075799')

	assert cc.valid == True, "Discover Card is Valid"
	assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

	cc = CreditCard('379179199857686')

	assert cc.valid == True, "AMEX is Valid"
	assert cc.card_type == "AMEX", "card_type is AMEX"

	cc = CreditCard('4929896355493470')

	assert cc.valid == True, "Visa Card is Valid"
	assert cc.card_type == "VISA", "card_type is VISA"

	cc = CreditCard('4329876355493470')

	assert cc.valid == False, "This card does not meet mod10"
	assert cc.card_type == "INVALID", "card_type is INVALID"

	cc = CreditCard('339179199857685')

	assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
	assert cc.card_type == "INVALID", "card_type is INVALID"