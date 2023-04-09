from employee import Employee

class Caelum(Employee):
    def display_tasks(self):
        print('Things done, Caelum')

    def search_courses_of_month(self, month=None):
        print(f'Displaying courses - {month}' if month else 'Displaying courses from this month')
