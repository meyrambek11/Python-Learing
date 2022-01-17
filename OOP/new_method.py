class Some_Class():
	def __new__(self):
		return super(Some_Class, self).__new__(self)
	def __init__(self):
	 	print("init")

obj = Some_Class()
