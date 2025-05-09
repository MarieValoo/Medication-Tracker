from datetime import datetime

class Medication:
    """
    A class representing a medication with its dosage information and administration schedule.
    
    Attributes:
        name (str): The name of the medication.
        dosage (str): The dosage amount of the medication (e.g., "10mg", "500mg").
        frequency_per_day (int): Number of times the medication should be taken daily.
        times (list[str]): List of specific times the medication should be taken each day.
        duration (int): amount of days the medication should be taken to completion.
        remaining_doses (int): Number of doses remaining of the medication.
    """
    
    def __init__(self, name: str, dosage: str, frequency_per_day: int, times: list[str], duration: int, remaining_doses: int):
        self.name = name
        self.dosage = dosage
        self.frequency_per_day = frequency_per_day
        self.times = times  # e.g., ["08:00", "14:00", "20:00"]
        self.duration = duration
        self.remaining_doses = remaining_doses
    
    def add_medication(self, amount):
        """
        Adds more doses to a previously listed medication.
        Args:
            amount (int): The amount you want to increase the medication by (in doses).
        """
        self.remaining_doses += amount
    
    def remove_medication(self, amount):
        """
        Removes doses from a previously listed medication.
        Args:
            amount (int): The amount you want to decrease the medication by (in doses).
        """
        self.remaining_doses -= amount
    
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
    
    def get_next_dose(self) -> tuple[str, datetime]:
        """
        Returns the next scheduled time to take the medication.
        
        Returns:
            tuple[str, datetime]: A tuple containing the formatted time string and the 
            datetime object of the next scheduled dose.
        """
        now = datetime.now()
        today_times = [datetime.strptime(t, "%H:%M").replace(year=now.year, month=now.month, day=now.day) for t in self.times]
        future_times = [t for t in today_times if t > now]
        if future_times:
            return future_times[0]
        else:
            # Return first dose tomorrow
            tomorrow_time = datetime.strptime(self.times[0], "%H:%M") + timedelta(days=1)
            return tomorrow_time.replace(year=now.year, month=now.month, day=(now.day + 1))

    def __repr__(self):
        return (f"Medication(name='{self.name}', dosage='{self.dosage}', "
                f"frequency_per_day={self.frequency_per_day}, times={self.times}, "
                f"duration={self.duration}, remaining_doses={self.remaining_doses})")
