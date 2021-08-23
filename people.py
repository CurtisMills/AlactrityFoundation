class People:

    # Creating the constructor method for adding a person
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creating the getter method and formatting the output
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age} \n"



class Group:

    # Creating a collection of a group of individual people
    def __init__(People):
        persons = []
        persons.append(People)
        print("Person successfully added.")

    # Creating a string method to return all items in list persons
    def __repr__(self):
        for i in self.persons:
            return f"Name: {persons.name}, Age: {persons.age} \n"

    def calcAverageAge(self):
        
        totalAge = 0
        for i in self:
            totalAge += self[i].age
            i += 1
        averageAge = totalAge / len(self)
        return averageAge

    def oldestPerson(self):
        oldestAge = 0
        oldestName = ''
        for i in persons:
            if persons[i].age > oldest:
                oldestAge = self[i].age
                oldestName = self[i].name
            i += 1
        return f"The oldest person is {oldestName}, who is {oldestAge}"
    
    def youngestPerson(self):
        youngestAge = 0
        youngestName = ''
        for i in persons:
            if persons[i].age > oldest:
                youngestAge = self[i].age
                youngestName = self[i].name
            i += 1
        return f"The oldest person is {youngestName}, who is {youngestAge}"

    



Alice = People("Alice", 20)
Bob = People("Bob", 25)
Carol = People("Carol", 30)
Dave = People("Dave", 35)

print(Alice, Bob, Carol, Dave)

newGroup = Group
newGroup(Alice)
newGroup(Bob)
newGroup(Carol)
newGroup(Dave)


print(newGroup)

print(newGroup.youngestPerson)

print(newGroup.oldestPerson)

print(newGroup.calcAverageAge)