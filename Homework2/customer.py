import productcheck

def buy(product, num, price):
	if productcheck.check(product, num):
		print("You bought {} and spent {}".format(product, num*price))
	else:
		print("Sorry! We are out of this product.")