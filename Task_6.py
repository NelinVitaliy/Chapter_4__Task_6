class House:
    furniture = {'bed': 4, 'wardrobe': 2, 'table': 1.5}

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def furniture_in_house(self, *args):
        furniture_in = {}
        self.furniture.update(furniture_in)
        return self.furniture

    def area(self):
        area_of_furniture = 0
        for value in self.furniture.values():
            area_of_furniture += value
        print('Площадь мебели: ', area_of_furniture)

        area_of_house = self.length * self.width
        print('Площадь всего дома: ', area_of_house)

        difference = area_of_house - area_of_furniture
        print('Площадь дома без мебели: ', difference)


house1 = House(10, 7)
house1.area()


