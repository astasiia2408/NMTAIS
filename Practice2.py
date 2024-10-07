from typing import List, Union


class Employee:
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self) -> float:
        if self.experience > 5:
            return self.base_salary * 1.2 + 500
        elif self.experience > 2:
            return self.base_salary + 200
        else:
            return self.base_salary


class Developer(Employee):
    pass


class Designer(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, eff_coeff: float):
        super().__init__(first_name, last_name, base_salary, experience)
        if eff_coeff > 1:
            self.eff_coeff = 1
        elif eff_coeff < 0:
            self.eff_coeff = 0
        else:
            self.eff_coeff = eff_coeff

    def calculate_salary(self) -> float:
        base_salary = super().calculate_salary()
        return base_salary * self.eff_coeff



class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, team: List[Union[Developer, Designer]]):
        super().__init__(first_name, last_name, base_salary, experience)
        self.team = team

    def calculate_salary(self) -> float:
        base_salary = super().calculate_salary()

        if len(self.team) > 10:
            base_salary += 300
        elif len(self.team) > 5:
            base_salary += 200

        developers_count = sum(isinstance(member, Developer) for member in self.team)
        if developers_count > len(self.team) / 2:
            base_salary *= 1.1  # Додаткові 10%

        return base_salary


class Department:
    def __init__(self, managers: List[Manager]):
        self.managers = managers

    def give_salary(self):
        for manager in self.managers:
            print(f"{manager.first_name} {manager.last_name} received {round(manager.calculate_salary())} shekels.")

            for employee in manager.team:
                print(f"{employee.first_name} {employee.last_name} received {round(employee.calculate_salary())} shekels.")



dev1 = Developer("Анастасія", "Косогор", 6700, 7)
dev2 = Developer("Павло", "Страшко", 8800, 5)
des1 = Designer("Нікіта", "Кириндась", 3580, 2, 0.8)
des2 = Designer("Глєб", "Мікляєв", 1000, 6, 15)

manager1 = Manager("Дмитро", "Міночкін", 9999, 9, [dev1, dev2, des1, des2])

department = Department([manager1])

department.give_salary()
