from datetime import datetime, timedelta

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
    
    def increase_dose_count(self, amount):
        """
        Adds more doses to a previously listed medication.
        Args:
            amount (int): The amount you want to increase the medication by (in doses).
        """
        self.remaining_doses += amount
        return self.remaining_doses
    
    def decrease_dose_count(self, amount):
        """
        Removes doses from a previously listed medication.
        Args:
            amount (int): The amount you want to decrease the medication by (in doses).
        """
        if self.remaining_doses >= amount:
            self.remaining_doses -= amount
        return self.remaining_doses
    
    def get_next_dose(self):
        """
        Returns the next scheduled time to take the medication.
        
        Returns:
            datetime: A datetime object of the next scheduled dose.
        """
        if self.remaining_doses <= 0:
            return None  # No doses remaining
            
        now = datetime.now()
        
        # Convert time strings to datetime objects for today
        today_times = []
        for time_str in self.times:
            time_parts = time_str.split(":")
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            time_obj = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            today_times.append(time_obj)
        
        # Find future times for today
        future_times = [t for t in today_times if t > now]
        
        if future_times:
            # Return the next available time today
            return min(future_times)
        else:
            # Return the first dose time for tomorrow
            tomorrow = now + timedelta(days=1)
            time_parts = self.times[0].split(":")
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            return tomorrow.replace(hour=hour, minute=minute, second=0, microsecond=0)  

    def __repr__(self):
        return (f"Medication(name='{self.name}', dosage='{self.dosage}', "
                f"frequency_per_day={self.frequency_per_day}, times={self.times}, "
                f"duration={self.duration}, remaining_doses={self.remaining_doses})")
