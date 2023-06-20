class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color
        
    def __lt__(self, other):
        if self.height != other.height:
            return self.height < other.height
        elif self.danger != other.danger:
            return self.danger < other.danger
        else:
            return self.color < other.color
        
    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
        
    def __add__(self, other):
        new_height = (self.height + other.height) // 2
        new_danger = max(self.danger, other.danger)
        new_color = sorted([self.color, other.color])[0]
        return Dragon(new_height, new_danger, new_color)
    
    def __sub__(self, number):
        div = self.height // number
        mod = self.danger % number
        new_height = self.height - div
        new_danger = self.danger + mod
        return Dragon(new_height, new_danger, self.color)
    
    def __call__(self, string):
        return string * self.danger
        
    def change_color(self, color):
        self.color = color
        
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."
    
    def __repr__(self):
        return f"Dragon({self.height}, {self.danger}, '{self.color}')"
# Пример использования:

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")

# Testing comparison methods
print(dr > dr1, dr != dr1, dr <= dr1)

# Testing string representation methods
print(dr) # Dragon with height 69, danger 5 and color brown.
print(dr1) # Dragon with height 69, danger 5 and color gray.

# Testing addition and subtraction methods
dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")

# Testing call method
print(dr("Welcome"))




# import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# one_hot_data = pd.get_dummies(data, columns=['whoAmI'])
# print(one_hot_data.head())