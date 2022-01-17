class Smarts:
	cnt = 0
	def __init__(self, model, year, owner):
		self.model = model
		self.year = year
		self.owner = owner
		Smarts.cnt = Smarts.cnt + 1
	def get_info(self):
		print(f"{self.model} , {self.year} , {self.owner}")

Iphone = Smarts("12","2021","Hazard")
Iphone = Smarts("12","2021","Hazard")

#Iphone.get_info()
#Samsung.get_info()
print(Smarts.cnt)