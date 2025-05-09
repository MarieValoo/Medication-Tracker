# test_runner.py
from user import User
from medication import Medication

# Create user
user = User("Alice")

# Add medications
med1 = Medication(name="Ibuprofen", dosage="200mg", frequency_per_day=2, times=["09:00", "21:00"], duration=30, remaining_doses=12)
user.add_medication(med1)

# Log a dose
user.take_medication("Ibuprofen", taken=True, note="No side effects")

# Show next dose times
next_doses = user.get_next_dose_time()
for med_name, (formatted, dt_obj) in next_doses.items():
    print(f"Next dose for {med_name}: {formatted}")

# Show history
user.journal.show()
