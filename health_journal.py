#can ya'll see this

#yes 

#####################################################
#Tracks Medication History
#####################################################
#!/usr/bin/env python3
"""
medication_history.py

Simple CLI tracker for logging and viewing medication intake history.
"""

import json
from datetime import datetime

DATA_FILE = 'history.json'


class MedicationHistoryTracker:
    """Tracks medication history: taken/missed doses with optional notes."""

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.history = []
        self.load_history()

    def load_history(self):
        """Load existing history from JSON, or start empty."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.history = data.get('history', [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []

    def save_history(self):
        """Persist the current history to disk."""
        with open(self.data_file, 'w') as f:
            json.dump({'history': self.history}, f, indent=2)

    def log(self, name: str, taken: bool = True, note: str = '') -> None:
        """
        Record an intake event.

        Args:
            name: Medication name.
            taken: True if dose was taken, False if missed.
            note: Optional note (e.g. side effects).
        """
        entry = {
            'timestamp': datetime.now().isoformat(),
            'name': name,
            'taken': taken,
            'note': note
        }
        self.history.append(entry)
        self.save_history()
        status = 'TAKEN' if taken else 'MISSED'
        print(f"[{status}] {name} @ {entry['timestamp']}")

    def show(self) -> None:
        """Print all logged events in order."""
        if not self.history:
            print("— No history yet —")
            return
        for e in self.history:
            mark = '✓' if e['taken'] else '✗'
            note = f" ({e['note']})" if e['note'] else ''
            print(f"{e['timestamp']}: {e['name']} {mark}{note}")


def main():
    tracker = MedicationHistoryTracker()

    while True:
        cmd = input("\n[L]og dose  [S]how history  [Q]uit > ").strip().lower()
        if cmd in ('q', 'quit'):
            break
        if cmd in ('l', 'log'):
            name = input("Medication name: ").strip()
            taken = input("Taken? (y/n): ").strip().lower() == 'y'
            note = input("Note (optional): ").strip()
            tracker.log(name, taken, note)
        elif cmd in ('s', 'show'):
            print("\n=== Medication History ===")
            tracker.show()
        else:
            print("Unknown command. Choose L, S, or Q.")

if __name__ == '__main__':
    main()

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
