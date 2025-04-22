from datetime import datetime
from medication import Medication
from health_journal import healthJournal

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
        self.journal = healthJournal()
    
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
        self.journal.log(medication_name, taken, note)
    
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
