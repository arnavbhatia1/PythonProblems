'''
Arnav Bhatia
CIS 41A Fall 2020
Unit H In-Class Assignment
In this assignment, we demonstrate how to use Variable Keyword Arguments (kwargs) and Overloading Operators
'''

#First Script - Variable-Length Keyword Arguments - kwargs
def overseerSystem (**kwargs):
    for var, message in kwargs.items():
        if "temperature" in message:
            t = int(message.split(":")[1])
            if t > 500:
                print("Warning: temperature is", t)
        elif "CO2level" in message:
            c = float(message.split(":")[1])
            if c > 0.15:
                print("Warning: CO2level is", c)
        if "miscError" in message:
            m = int(message.split(":")[1])
            print("Misc error #", m)

def main():
    overseerSystem(a="message1 is temperature:550")
    overseerSystem(a="message2 is temperature:475")
    overseerSystem(a="message3 is temperature:450", b="miscError:404")
    overseerSystem(a="message4 is CO2level:.18")
    overseerSystem(a="message5 is CO2level:.2", b="miscError:418")

main()
print()

#Second Script - Operator Overloading
class BritCoins:
    __coinValues = {"pounds":240, "shillings":12, "pennies":1}

    def __init__(self, **kwargs):
        self.totalPennies = 0
        self.pounds = 0
        self.shillings = 0
        self.pennies = 0
        for _, coinType in kwargs.items():
            if "pennies" in coinType:
                self.pennies = int(coinType.split(" ")[0])
                self.totalPennies += self.pennies*1
            if "shillings" in coinType:
                self.shillings = int(coinType.split(" ")[0])
                self.totalPennies += self.shillings*12
            if "pounds" in coinType:
                self.pounds = int(coinType.split(" ")[0])
                self.totalPennies += self.pounds*240

    def __add__(self, other):
        total1 = self.totalPennies + other.totalPennies
        totalpounds = self.pounds + other.pounds
        totalshillings = self.shillings + other.pounds
        totalpennies = self.pennies + other.pennies
        if totalshillings > 20:
            newshillings = totalshillings - 19
            newpounds = totalpounds + 1
            return (str(newpounds) + " pounds " + str(newshillings) + " shillings " + str(totalpennies) + " pennies")
        else:
            return (str(totalpounds) + " pounds " + str(totalshillings) + " shillings " + str(totalpennies) + " pennies")

    def __sub__(self, other):
        total2 = self.totalPennies - other.totalPennies
        totalpounds = self.pounds - other.pounds
        totalshillings = self.shillings - other.pounds
        totalpennies = self.pennies - other.pennies
        if totalpennies < 0:
            newshillings = totalshillings - 2
            newpennies = totalpennies + 12
            return (str(totalpounds) + " pounds " + str(newshillings) + " shillings " + str(newpennies) + " pennies")
        else:
            return (str(totalpounds) + " pounds " + str(totalshillings) + " shillings " + str(totalpennies) + " pennies")

    def __str__(self):
        pounds = 0
        shillings = 0
        pennies = 0
        remainder = self.totalPennies
        if remainder > BritCoins.__coinValues["pounds"]:
            pounds = remainder//BritCoins.__coinValues["pounds"]
            remainder = remainder - pounds * BritCoins.__coinValues["pounds"]
        if remainder > BritCoins.__coinValues["shillings"]:
            shillings = remainder//BritCoins.__coinValues["shillings"]
            remainder = remainder - shillings * BritCoins.__coinValues["shillings"]
        if remainder > BritCoins.__coinValues["pennies"]:
            pennies = remainder
        return (str(pounds) + " pounds " + str(shillings) + " shillings " + str(pennies) + " pennies ")

c1 = BritCoins(a = "4 pounds", b = "24 shillings", c = "3 pennies")
c2 = BritCoins(a = "3 pounds", b = "4 shillings", c = "5 pennies")
c3 = c1 + c2
c4 = c1 - c2
print(c1)
print(c2)
print(c3)
print(c4)

'''
Execution Results:
Warning: temperature is 550
Misc error # 404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error # 418

5 pounds 4 shillings 3 pennies 
3 pounds 4 shillings 5 pennies 
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies
'''