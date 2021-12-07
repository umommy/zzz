class Cloud:
    population = 0
    def __init__(self, array):
        self.array = array
        Cloud.population += 1
        print('------------------')
        print('initialisation {0:d}'.format(Cloud.population))

    def sayHi(self):
        print('Hello !', self.array)
        print('vsego {0:d}'.format(Cloud.population))

    @staticmethod
    def howMany():
        print('----seychas {0:d}'.format(Cloud.population))

    def __del__(self):
        print('------------------')
        print('Deleting', self.array)
        Cloud.population -= 1
        print('ostalos {0:d}'.format(Cloud.population))


array = (11,22,24)
f = Cloud(array)
array = (11,22)
u = Cloud(array)


array = (11,22)
p = Cloud(array)
p.sayHi()
Cloud.howMany()

array = (33,44,55)
m = Cloud(array)
m.sayHi()
Cloud.howMany()