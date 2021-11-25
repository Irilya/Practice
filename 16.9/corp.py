class Users():
    def __init__(self, name, status):
        self.name = name
        self.status = status

class City(Users):
    def __init__(self, city, **kwargs):
        super().__init__(**kwargs)
        self.city = city

    def get_vol(self):
        return f'{self.name}, {self.city}, статус - {self.status}'

vol1 = City(name ='Иванов Федор', city ='Саратов', status ='куратор')
vol2 = City(name ='Петров Антон', city='Москва', status='наставник')

print(vol1.get_vol(),vol2.get_vol(),sep='\n')