# test_runner.py
from user import User
from medication import Medication
from journal_output import HealthJournal
import os

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
med1 = Medication(name="Ibuprofen", dosage="200mg", frequency_per_day=2, times=["09:00", "21:00"], duration=30, remaining_doses=12)
med2 = Medication(name="Lisinopril", dosage="200mg", frequency_per_day=2, times=["09:00", "21:00"], duration=30, remaining_doses=12)
user.add_medication(med1)
user.add_medication(med2)

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



