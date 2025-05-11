from datetime import datetime

from user import User
from medication import Medication
from journal_output import HealthJournal
from medication_history_tracker import MedicationHistoryTracker
from medication_reminder import MedicationReminders

def main():
    user = User(name="Bella Smith", age=30)
    medication1 = Medication(name="Aspirin", dosage="50mg")
    medication2 = Medication(name="Tylenol", dosage="500mg")

    health_journal = HealthJournal(user=user)
    health_journal.add_medication(medication1, schedule="Daily at 8AM")
    health_journal.add_medication(medication2, schedule="Twice daily at 10AM and 4PM")

    med_tracker = MedicationHistoryTracker(user=user)
    med_tracker.add_entry(medication1, datetime(2025, 5, 11, 8, 0), status="Taken")
    med_tracker.add_entry(medication2, datetime(2025, 5, 11, 10, 0), status="Missed")

    reminders = MedicationReminders(user=user, medications=[medication1, medication2])
    reminders.send_notifications()

    print("Health Journal for", user.name)
    for med, schedule in health_journal.medications.items():
        print(f"Medication: {med.name}, Dosage: {med.dosage}, Schedule: {schedule}")

    print("\nMedication History:")
    for entry in med_tracker.get_history():
        print(f"{entry['medication_name']} taken at {entry['time']} - Status: {entry['status']}")

    print("\nMedication Reminders sent to user:", user.name)

if __name__ == "__main__":
    main()