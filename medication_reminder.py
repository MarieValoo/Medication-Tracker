import time
from datetime import datetime

class MedicationReminders:
    """Manages and sends medication reminders to the user based on the medication schedule"""
    def __init__(self, user, medications):
        self.user = user
        self.medications = medications
        self.reminder_times = {}

    def set_reminder(self, medication, time):
        self.reminder_times[medication.name] = time

    def send_notifications(self):
            print(f"\nSending reminders to {self.user.name}.")
            for med in self.medications:
                times = med.times if med.times else ["No time set"]
                times_str = ", ".join(times)
                print(f"Reminder: Take {med.name} ({med.dosage}) at {times_str}.")