from datetime import datetime

class Date:
    def __init__(self):
        self._init_time = datetime.today()

    def __str__(self):
        return self.format()

    def get_month(self):
        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
        return months[self._init_time.month - 1]

    def get_weekday(self):
        week = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
        return week[self._init_time.weekday()]

    def format(self):
        return self._init_time.strftime("%d/%m/%Y %H:%M:%S")

    def delta(self):
        return datetime.today() - self._init_time
