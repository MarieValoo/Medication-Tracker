#!/usr/bin/env python3
"""
medication_history.py

Simple CLI tracker for logging and viewing medication intake history.
"""

import json
import csv
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

    def show_by_name(self, name: str) -> None:
        """Print history for a specific medication name."""
        matches = [e for e in self.history if e['name'].lower() == name.lower()]
        if not matches:
            print(f"No entries found for '{name}'.")
            return
        for e in matches:
            mark = '✓' if e['taken'] else '✗'
            note = f" ({e['note']})" if e['note'] else ''
            print(f"{e['timestamp']}: {e['name']} {mark}{note}")

    def export_csv(self, filename='medication_log.csv'):
        """Export history to a CSV file."""
        if not self.history:
            print("No history to export.")
            return
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['timestamp', 'name', 'taken', 'note'])
            writer.writeheader()
            writer.writerows(self.history)
        print(f"Exported history to {filename}")


def main():
    tracker = MedicationHistoryTracker()

    while True:
        cmd = input("\n[L]og dose  [S]how history  [F]ilter by med  [E]xport CSV  [Q]uit > ").strip().lower()
        if cmd in ('q', 'quit'):
            break
        elif cmd in ('l', 'log'):
            name = input("Medication name: ").strip()
            taken_input = input("Taken? (y/n): ").strip().lower()
            while taken_input not in ('y', 'n'):
                taken_input = input("Invalid. Taken? (y/n): ").strip().lower()
            taken = taken_input == 'y'
            note = input("Note (optional): ").strip()
            tracker.log(name, taken, note)
        elif cmd in ('s', 'show'):
            print("\n=== Medication History ===")
            tracker.show()
        elif cmd in ('f', 'filter'):
            name = input("Medication name to filter by: ").strip()
            print(f"\n=== History for {name} ===")
            tracker.show_by_name(name)
        elif cmd in ('e', 'export'):
            tracker.export_csv()
        else:
            print("Unknown command. Choose L, S, F, E, or Q.")

if __name__ == '__main__':
    main()
