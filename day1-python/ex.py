numbers = [1, 2, 3, 4, 5, 6]

even_squares = [number ** 2 for number in numbers if number % 2 == 0]

with open("result.txt", "w") as file:
    for square in even_squares:
        file.write(f"{square}\n")

print(f"Saved {len(even_squares)} results to result.txt")


class NewClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age

    def getName(self):
        return self.name

student = [NewClass("Alice", 20), 
NewClass("Bob", 22)]

for i,s in enumerate(student):
    print(f"Student {i+1}: Name: {s.getName()}, Age: {s.getAge()}")

