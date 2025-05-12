from datetime import datetime

from user import User
from medication import Medication
from journal_output import HealthJournal
from medication_history_tracker import MedicationHistoryTracker
from medication_reminder import MedicationReminders
import os

def main():
    # Delete or rename the old history file to start fresh
    # Eventually I would think that we remove the history file, or make it empty, but this is a temp solution
    if os.path.exists("history.json"):
        # Option 1: Delete the file
        os.remove("history.json")
        # Option 2: Rename it to keep a backup
        # os.rename("history.json", "history_backup.json")

    # Create user
    user = User("Alice")
             
    # Add medications
    med1 = Medication(name="Ibuprofen", dosage="150mg", frequency_per_day=1, times=["08:30"], duration=45, remaining_doses=12)
    med2 = Medication(name="Lisinopril", dosage="200mg", frequency_per_day=2, times=["09:00", "21:00"], duration=30, remaining_doses=12)
    user.add_medication(med1)
    user.add_medication(med2)
    
    print("Health Journal for", user.name)
        
    # Check interactions
    user.check_all_interactions()

    # Log a dose
    user.take_medication("Ibuprofen", taken=True, note="No side effects")

    # Show next dose times
    next_doses = user.get_next_dose_time()
    for med_name, (formatted, dt_obj) in next_doses.items():
        print(f"Next dose for {med_name}: {formatted}")

    # Show history
    user.journal.show()

    #run MedicationReminders class
    reminders = MedicationReminders(user=user, medications=[med1, med2])
    reminders.send_notifications()

    
    #optional function of importing text file of health journal output
    answer = input("Would you like a text file of the taken medications journal? yes or no ").lower()
    if answer == "yes":
        health_journal = HealthJournal(user.medications)   
        health_journal.add_to_dict()
        health_journal.journal_output()
    else:
        print("Okay")


if __name__ == "__main__":
    main()