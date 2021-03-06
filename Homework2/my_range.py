if __name__ == '__main__':
	
	def my_range(n: int):
	    for i in range(n+1):
	        yield i 
	    print("there are no values left")