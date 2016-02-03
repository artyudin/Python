## Mortgage Calculator

## Make a mortgage calculator that returns your monthly payments based on the following mortgage equation:

## M = P( i/12( 1+i/12 )^n )/( ( 1+i/12 )^n - 1 )


def mortgage_calculator(principal, interest, months):
	m = principal*( interest/12*( 1+i/12 )**months )/( ( 1+interest/12 )**months - 1 )
	return round(m,2)

print(mortgage_calculator(100000, 0.05, 120))


assert mortgage_calculator(100000, 0.05, 120) == 1060.66, str(mortgage_calculator(100000, 0.05, 120)) + " !=  1060.67"
