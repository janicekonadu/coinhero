from datetime import date
class Platform:

	def __init__(self, nm, amnt, due_date, url):
		self.name = nm
		self.amount = amnt
		self.date = due_date
		self.pay_url = url
		self.timeleft = self.calcDaysLeft()
		print("******")
		print(self.timeleft)

	def update(self):
		self.timeleft = self.calcDaysLeft()

	def sendNotification(self):
		message = ""
		if self.timeleft < 2:
			message = "Bill tomorrow! Dismiss or Use coinhero?"
		return message

	def calcDaysLeft(self):
		today = date.today()
		tdate = today.strftime("%Y/%m/%d").split('/')
		pdate = self.date.split('/')
		print(tdate)
		print(pdate)

		d0 = date(int(tdate[0]), int(tdate[1]), int(tdate[2]))
		d1 = date(int(pdate[0]), int(pdate[1]), int(pdate[2]))
		delta = d1 - d0
		return delta.days

	def getDate(self):
		d = self.date.split('/')
		df = date(int(d[0]), int(d[1]), int(d[2]))
		return df.strftime("%m/%d/%Y")

class GiftCard():

	def __init__(self, number, cvcnum, exp):
		self.card_num = number
		self.cvc = cvc_num
		self.expdate = exp

	def cardInfo(self):
		return [self.card_num, self.cvc, self.expdate] 



