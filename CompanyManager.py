'''
Author: Ifeoluwa Oyelowo-Paul
Date: April 8, 2025

Company Manager - 
Created an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently. No taxes are put into consideration so all salary is gross
After establishing an employee hierarchy, created a Company class that allows one to manage the employees. 
One is able to hire, fire and raise employees. 
'''
from abc import ABC, abstractmethod

#Employee class
class Employee(ABC):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.monthly_pay = 0

    @abstractmethod
    def calculate_pay(self):
        pass



#HourlyEmployee class
class HourlyEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name=name)
        self.salary = salary #hourly
       
    def calculate_pay(self):
        #monthly pay = hourlypay * (7.5hrs a day) * (5 days a week) * (4 weeks in a month)
        monthly_pay = self.salary * 7.5 * 5 * 4.0
        return monthly_pay

#SalariedEmployee class 
class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name=name)
        self.salary = salary #annual
       
    def calculate_pay(self):
        #monthly pay = annual pay / 12 
        monthly_pay = self.salary/12.0
        return monthly_pay

#Manager class
class Manager(SalariedEmployee):

    def __init__(self, name, salary):
        super().__init__(name=name, salary=salary)
       


#Executive class
class Executive(SalariedEmployee):

    def __init__(self, name, salary):
        super().__init__(name=name, salary=salary)
      


#Company class
class Company:
    
    # A Company has one Executive
    # Multiple Managers
    # Multiple SalariedEmployees and HourlyEmployees reporting to Managers in different teams
    # Use a dictionary for teams. 
    # key = 'team_name'; value = [Manager , SalariedEmployees, HourlyEmployees]


    def __init__(self,name, ceo, teams):
        self.name = name
        self.ceo = ceo
        self.teams = teams

    #hire new employee
    def hire(self, employee, team_name):
        # if new employee is a Manager, insert at index 0, else add to end of list
        if type(employee) == Manager:
            self.teams[team_name].insert(0,employee)
        else:
            self.teams[team_name].append(employee)

    #fire exisiting employee
    def fire(self, employee, team_name):
        self.teams[team_name].remove(employee)

    #raise the salary of an employee
    def raise_salary(self, employee, salary):
        employee.salary = salary
        return employee
    
    #add a new team to the company
    def add_team(self,team_name,team_list):
        self.teams[team_name] = team_list


# main
def main():

     # set up company

    #CEO
    Glacier = Executive("Glacier Doe",250000)
    #print(Glacier.calculate_pay())

    #Cloud team
    Johnny = Manager("Johnny Doe",200000)
    #print(Johnny.calculate_pay())
    John = HourlyEmployee("John Doe",20)
    #print(John.calculate_pay())
    Jane = SalariedEmployee("Jane Doe",150000)
    #print(Jane.calculate_pay())
    Donny = HourlyEmployee("Donny Sullivan",20)
    Alex = SalariedEmployee("Alexandra Darlington",90000)

    #HR team
    Mandy = Manager("Amanda Johannesburg",200000)
    Christian = HourlyEmployee("Christian Jones",20)
    Abel = HourlyEmployee("Abel March",20)
    Dom = SalariedEmployee("Dominic Earl",60000)


   
    # In team list, manager is first and other employees are after
    cloud_team = [Johnny,John,Jane,Donny,Alex]
    hr_team = [Mandy,Christian,Abel,Dom]

    Mars_teams = {'Cloud':cloud_team, 'HR':hr_team}

    #Company = Mars
    Mars = Company('Mars',Glacier,Mars_teams)

    #hire new employee to HR team
    Umar = HourlyEmployee("Umar Moed",22.5)
    Mars.hire(Umar,'HR')
    # confirm Umar was added
    for value in Mars.teams['HR']:
        print(value.name)

    print('\n')

    #fire manager of Cloud team
    Mars.fire(Johnny,'Cloud')
    # confirm Johhny was fired
    for value in Mars.teams['Cloud']:
        print(value.name)

    print('\n')

    #Hire new manager for Cloud team
    Jupiter = Manager("Jupiter Galaxy",190000)
    Mars.hire(Jupiter,'Cloud')
    for value in Mars.teams['Cloud']:
        print(value.name)


    print("\n")
    print(f"Jupiter's old salary {Jupiter.salary}")
    #raise salary of Jupiter
    Jupiter = Mars.raise_salary(Jupiter, 210000)
    print(f"Jupiter's new salary {Jupiter.salary}")

    print("\n")

    # add a new team to the company
    print("Old team list: \n")
    for team_name in Mars.teams:
        print(team_name+": ")
        for value in Mars.teams[team_name]:
            print(value.name)
        print("\n")

    support_team = [John,Abel,Donny]
    Mars.add_team('Support',support_team)

    print("\nNew teams after addition: \n")

    for team_name in Mars.teams:
        print(team_name+": ")
        for value in Mars.teams[team_name]:
            print(value.name)
        print("\n")



main()