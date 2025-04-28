from datetime import datetime

class Medication:
    """
    A class representing a medication with its dosage information and administration schedule.
    
    Attributes:
        name (str): The name of the medication.
        dosage (str): The dosage amount of the medication (e.g., "10mg", "500mg").
        frequency_per_day (int): Number of times the medication should be taken daily.
        times (list[str]): List of specific times the medication should be taken each day.
        #duration (int): amount of days the medication should be taken to completion - Marie V.
        remaining_doses (int): Number of doses remaining of the medication.
    """
    
    def add_medication(self):
        """
        Adds a new medication to the system.
        """
        pass
    
    def remove_medication(self):
        """
        Removes a medication from the system.
        """
        pass
    
    def check_interactions(self, other_medications: list["Medication"]) -> list[dict]:
        """
        Checks for potential interactions with other medications.
        
        Args:
            other_medications (list[Medication]): List of other medications to check against.
            
        Returns:
            list[dict]: List of interaction details, where each dict contains information about 
            the interaction severity, description, and involved medications.
        """
        pass
    
    def get_next_dose_time(self) -> tuple[str, datetime]:
        """
        Returns the next scheduled time to take the medication.
        
        Returns:
            tuple[str, datetime]: A tuple containing the formatted time string and the 
            datetime object of the next scheduled dose.
        """
        pass