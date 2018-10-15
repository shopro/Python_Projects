from random import randint

class tripCostCalculator():
    
    def __init__(self, city: str, days: int, spending_money: int):
        self.city = city.title()
        self.days = days
        self.spending_money = spending_money
    
    def hotelCost(self) -> int:
        return int(140 * self.days)
    
    def planeRideCost(self) -> int:
        try:
            planeride_costs = {
                "Charlotte": 183,
                "Tampa": 220,
                "Pittsburgh": 222,
                "Angeles": 475,
            }
            return planeride_costs[self.city]
        except KeyError:
            return randint(120, 999)
    
    def rentalCarCost(self) -> int:
        cost = self.days * 40
        if self.days >= 7:
            cost -= 50
        elif self.days >= 3:
            cost -= 20
        return int(cost)
    
    def calculate_tripCost(self):
        return self.spending_money + self.rentalCarCost() + self.hotelCost() + self.planeRideCost()


if __name__ == "__main__":
    city = "Tampa"
    days = 6
    spending_money = 600
    print("Spending money for the trip", tripCostCalculator(city, days, spending_money).calculate_tripCost())
    
    city = "Atlanta"
    days = 6
    spending_money = 600
    print("Spending money for the trip", tripCostCalculator(city, days, spending_money).calculate_tripCost())
