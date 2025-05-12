from datetime import datetime
from medication import Medication
from medication_history_tracker import MedicationHistoryTracker
from interaction_db import interaction_db

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
        self.journal = MedicationHistoryTracker()
    
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
    
    def find_medication(self, medication_name: str):
        """
        Finds a medication in the user's list by name.
        
        Args:
            medication_name (str): The name of the medication to find.
            
        Returns:
            The medication object if found, None otherwise. 
        """
        for med in self.medications:
            if med.name.lower() == medication_name.lower():
                return med
        return None
    
    def take_medication(self, medication_name: str, taken: bool = True, note: str = ""):
        """
        Records that a medication was taken or missed.
        
        Args:
            medication_name (str): The name of the medication being taken/missed.
            taken (bool): Indicates whether the medication was taken (True) or missed (False).
            note (str): Optional note to include (e.g., side effects).
            
        Returns:
            bool: True if the medication was found and the action was recorded, False otherwise.
        """
        medication = self.find_medication(medication_name)
        
        if medication:
            # Record in journal
            self.journal.log(medication_name, taken, note)
            
            # Update dose count if taken
            if taken and medication.remaining_doses > 0:
                medication.decrease_dose_count(1)
            return True
        return False

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
