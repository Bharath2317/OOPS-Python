class Bill:
  def __init__(self,amount,period):
    self.amount = amount
    self.period = period


class Flatmate:
  def __init__(self,name,days_in_the_house):
    self.name = name
    self.days_in_the_house = days_in_the_house

  def pays(self,bill,flatmate2):
    day_bill = self.days_in_the_house / (self.days_in_the_house+flatmate2.days_in_the_house)
    to_pay = bill.amount * day_bill
    return to_pay
  
the_bill = Bill(180,"March 30")
flatmate1 = Flatmate("john",25)
flatmate2 = Flatmate("Arjun",28)

print(flatmate1.pays(the_bill,flatmate2))
print(flatmate2.pays(the_bill,flatmate1))

