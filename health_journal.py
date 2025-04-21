#can ya'll see this

#yes 

import datetime

class SendReminders:
    def __init__(self, user):
        self.user = user
        self.schedule = self.generate_schedule()
## Function that generate schedules for multiple different medications or just one large schedule
## function with an If statement that checks if reminder should be sent




def send(self, reminder):
    user = reminder['user']
    med = reminder['medication']
    print(f"Hi {user}, time to take {med}.")
## Maybe make it more specific like their dose?
