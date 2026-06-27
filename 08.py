class FruitBasket:
    PRICES = {
        "apple": 5,
        "banana": 3,
        "orange": 4,
        "pear": 6
    }
    def __init__(self,data):
        self.fruit=data
        self.price=0
        self.tot=0
        for x in data:
            self.price+=data[x]*self.PRICES[x]
            self.tot+=data[x]
        
    def __gt__(self, other):
        if isinstance(other,FruitBasket):
            return self.price>other.price
        elif isinstance(other,int):
            return self.price>other
        
    def __eq__(self, value):
        return self.fruit==value.fruit
    
    def get_price(self):
        return self.price
    
    def get_count(self):
        return self.tot
    
    def __hash__(self):
        return 0
def parse_fruits(data):
    fruits = {}
    for item in data:
        name, qty = item.split(":")
        fruits[name] = int(qty)
    return fruits

b1_data = input().split()
b2_data = input().split()
compare_num = int(input().strip())

b1 = FruitBasket(parse_fruits(b1_data))
b2 = FruitBasket(parse_fruits(b2_data))

# 创建字典
basket_dict = {b1: "VIP_Gift", b2: "Standard_Gift"}

print(basket_dict[b1])
print(b1 > b2)
print(b1 > compare_num)
print(b1.get_price())
print(b1.get_count())
