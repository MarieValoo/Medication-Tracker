#Health Journal Class
#Marie Valouiski
#INST326 Final Project

from user import User
from medication import Medication 

#create a function that takes in medications (list of medication objects) from User class and makes a list of dictionaries 
#acceptable for HealthJournal class


class HealthJournal:
    """takes in medication_list (a list of dictionaries containing Medication objects (from User class) with the name of each 
    dictionairy being the medication name and the keys and values being the dosage[str], frequency_per_day[int], 
    times[list], duration[int], and remaining_doses[int]) to create full journal of what it would look like if the user took all the medication according 
    to the prescription directions
    Attributes:
        medication_list """
        
    def __init__(self, medication_object_list): 
        self.medication_object_list = medication_object_list
        self.medication_dict = {}
        
    def add_to_dict(self):
        """populates medication_dict with medication_object_list containing medication objects in a format that's workable by the 
        journal_output function"""
        
        assert type(self.medication_object_list) == list #tests that medication_object_list is a list
        
        for med in self.medication_object_list: #tests that the objects within the list are Medication objects
            assert type(med) == Medication
        
        for medication_object in self.medication_object_list:
            
            name = medication_object.name
            self.medication_dict[name] = {
                "dosage": medication_object.dosage,
                "frequency_per_day": medication_object.frequency_per_day,
                "times": medication_object.times,
                "duration": medication_object.duration,
                "remaining_doses": medication_object.remaining_doses
        }
    
          
    def journal_output(self):
        """uses medication_dict to create text file of journal that considers all of the attributes, goes one medication at a time
        Attribute:
            self (medication_dict)
        Returns:
            journal_text, a string that will be used to create the file medication_journal.txt
            medication_journal.txt, text file containing journal_text string
        """
        
        day_text = [] #where the journal f string texts will go
        medication_list = [] #where all medication names will go, once the duration of a medication goes to zero the medication name will be removed from the list
        count = 0 #tracks the amount of days that the journal goes through
        
        for medication in self.medication_dict:
            medication_list.append(medication) #appends all medication names to the medication_list variable
            
        duration_list = []
        for details in self.medication_dict.values():
            duration = details.get("duration")
            if duration > 100:
                duration_list.append(100)
            else: 
                duration_list.append(duration)
        try:
            final_day = max(duration_list) #finds the last day a medication(s) will be taken
        except:
            print(f"{self.medication_dict}")    

        while count < final_day:
            count += 1
            text_container = ""
            for medication, information in self.medication_dict.items():
                if medication not in medication_list: #check to make sure medication is not used up
                    continue
                
                dosage = None
                frequency = None
                
                dosage = information.get("dosage")
                frequency = information.get("frequency_per_day")
                duration = information.get("duration")
                
                time = "times"
                if frequency == 1:
                    time = "time"
                    
                if dosage is not None and frequency is not None:
                    text_container = text_container + " " + f"{dosage} of {medication} {frequency} {time},"
                    
                if duration == count: #if this is the last day to take a medication, remove it from medication_list after its last use
                    medication_list.remove(medication)
                            
            text_container = f"On day {count}, you took " + text_container
            text_container = text_container[:-1] + "." + "\n" + "\n"
            day_text.append(text_container)
            
        day_text = "".join(day_text)
        journal_text = "MY HEALTH JOURNAL - TAKEN MEDICATIONS: " + "\n"*3 + day_text
        with open("medication_journal", "w") as file:
            file.write(journal_text)
        
        print("File 'medication_journal' successfully created!")
                
if __name__=="__main__":
    
    user = User("Alice")
    
    med1 = Medication(name="Ibuprofen", dosage="100mg", frequency_per_day=1, times=["09:00"], duration=25, remaining_doses=12)
    med2 = Medication(name="Lisinopril", dosage="200mg", frequency_per_day=2, times=["09:00", "21:00"], duration=30, remaining_doses=12)
    user.add_medication(med1)
    user.add_medication(med2)
    
    health_journal = HealthJournal(user.medications)
    
    health_journal.add_to_dict()
    health_journal.journal_output()

