class Employee:
    def __init__(self,first_name,last_name,birth_year,salary):
        self._first_name=first_name
        self._last_name=last_name
        self._birth_year=birth_year
        self._salary=salary

    def show(self):
        print(f'I am {self.first_name} {self.last_name} born in {self.birth_year}')

        
