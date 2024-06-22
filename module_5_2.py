class House:
    def __init__(self):
        self.numberOfFloors = 0 #Этажность здания

    def setNewNumberOfFloors(self, floors): #Функция(метод) изменяет автрибут - этажность здания
        self.numberOfFloors = floors
        return self.numberOfFloors

num_floor = House()
num_floor.setNewNumberOfFloors(10)
print('Здание состоит из', num_floor.numberOfFloors, 'этажей')
