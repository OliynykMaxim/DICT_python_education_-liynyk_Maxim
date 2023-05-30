class CarStructure:
    def __init__(self, data=[]):
        self.data = []
        for item in data:
            if item not in self.data:
                self.data.append(item)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def append(self, value):
        if value not in self.data:
            self.data.append(value)

    def insert(self, index, value):
        if value not in self.data:
            self.data.insert(index, value)

    def index(self, value, start=0, stop=None):
        return self.data.index(value, start, stop)

    def remove(self, value):
        self.data.remove(value)
car_structure = CarStructure()

car_structure.append("Audi")
car_structure.append("BMW")
car_structure.append("Audi")
car_structure.append("Mercedes")

print(len(car_structure))  # Виводить: 3
print(car_structure)  # Виводить: ['Audi', 'BMW', 'Mercedes']

car_structure.remove("BMW")

print(len(car_structure))  # Виводить: 2
print(car_structure)  # Виводить: ['Audi', 'Mercedes']





