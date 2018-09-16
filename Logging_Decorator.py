#! python3
import time

def logger_dec(func):
	def logging_func(*args, **kwargs):
		try:
			f = open('logFile.txt', 'a')
			f.write(f'name is {func.__name__}\n')
			f.write(f'args are {args}\n')
			f.write(f'kwargs are {kwargs}\n')
			ti = time.time()
			retVal = func(*args, **kwargs)
			tf = time.time()
			f.write(f'retVal of {func.__name__} was {retVal}\n')
			f.write(f'{func.__name__} took {round(tf - ti, 2)} to execute\n\n')
			f.flush()
			f.close()
		finally:
			return retVal
	return logging_func
	
@logger_dec
def print_func(val):
	print(f'Received input {val}')
	for i in range(3):
		time.sleep(1.47)
	
	return '4321'
	
if __name__ == '__main__':
	print_func('1234')