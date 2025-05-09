from datetime import datetime
from medication import Medication
from health_journal import HealthJournal

class User:
    """
    A class representing a user who takes medications and maintains a health journal.
    
    Attributes:
        name (str): The name of the user.
        medications (list[Medication]): List of medications the user is currently taking.
        journal (HealthJournal): The user's health journal for tracking symptoms and medication effects.
    """

    def __init__(self, name: str):
        """
        Initializes the User object.

        Args:
            name (str): The name of the User.
        """
        self.name = name
        self.medications: list[Medication] = []
        self.journal = HealthJournal()
    
    def add_medication(self, medication: Medication):
        """
        Adds a new medication to the user's medication list.
        
        Args:
            medication (Medication): The medication to add to the user's list.
        """
        self.medications.append(medication)
    
    def remove_medication(self, medication_name: str) -> bool:
        """
        Removes a medication from the user's medication list.
        
        Args:
            medication_name (str): The name of the medication to remove.
            
        Returns:
            bool: True if medication was found and successfully removed, False if not found.
        """
        for med in self.medications:
            if med.name.lower() == medication_name.lower():
                self.medications.remove(med)
                return True
        return False
    
    def take_medication(self, medication_name: str, taken: bool = True, note: str = ""):
        """
        Logs the intake of a medication in the user's medication history.

        Args:
            medication_name (str): The name of the medication being taken or missed.
            taken (bool): Indicates whether the medication was taken (True) or missed (False). Defaults to True.
            note (str): Optional note to include with the log entry (e.g., side effects, reasons for missing). Defaults to empty string.

        """
        med = next((m for m in self.medications if m.name.lower() == medication_name.lower()), None)
        if med and taken:
            med.remaining_doses = max(0, med.remaining_doses - 1)
        self.journal.log(medication_name, taken, note)

    def check_all_interactions(self):
        """
        Checks and prints potential drug interactions among the user's medications.
        """
        print("\nChecking for drug interactions:")
        reported_pairs = set() # Keep track of already-reported interactions
        found = False # Marking a found interaction

        for i, med in enumerate(self.medications):
            others = self.medications[:i] + self.medications[i+1:]
            for other in others:
                # Try to find interaction info using both possible pair orders
                pair = (med.name, other.name)
                reverse_pair = (other.name, med.name)
                interaction_info = interaction_db.get(pair) or interaction_db.get(reverse_pair)

                if interaction_info:
                    # Sort names to standardize key (so A+B is same as B+A)
                    name1, name2 = sorted([med.name, other.name])
                    key = f"{name1}+{name2}"

                    # Only report each interaction once
                    if key not in reported_pairs:
                        reported_pairs.add(key)
                        found = True
                        # Print the interaction information
                        print(f"- {name1} + {name2}: {interaction_info['description']} (Severity: {interaction_info['severity']})")

        if not found:
            print("No interactions found.")
    
    def get_next_dose_time(self) -> dict[str, tuple[str, datetime]]:
        """
        Returns the next scheduled medication dose time for the user.
        
        Returns:
            dict[str, tuple[str, datetime]]: A dictionary with medication names as keys and
            tuples of formatted time string and datetime object as values, representing the next dose time
            for each medication. Only includes medications with upcoming doses.
        """
        upcoming_doses = {}
        for med in self.medications:
            next_dose = med.get_next_dose()
            if next_dose and isinstance(next_dose, datetime) and next_dose > datetime.now():
                formatted_time = next_dose.strftime('%Y-%m-%d %H:%M')
                upcoming_doses[med.name] = (formatted_time, next_dose)
        return upcoming_doses
