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
            time = self.reminder_times.get(med.name, "No time set")
            print(f"Reminder: Take {med.name} ({med.dosage}) at {time}.")