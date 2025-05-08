#Health Journal Class
#Marie Valouiski
#INST326 Final Project

from user import User 
import re

#create a function that takes in medications (list of medication objects) from User class and makes a list of dictionaries 
#acceptable for HealthJournal class

#ill probably add medications to input in init of HealthJournal


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
        
        assert self.medication_object_list == self.user.medications
        
        for medication_object in self.medication_object_list:
            
            med_match = re.compile("=(?:'([^']*)'|(\[.*?\])|(\d+))").finditer(medication_object)
            for match in med_match:
                name = match.group(1)
                dosage = match.group(2)
                frequency_per_day = match.group(3)
                times = match.group(4)
                duration = match.group(5)
                remaining_doses = match.group(6)
            
            dict_input = f"{name}: {dosage: {{dosage}}, frequency_per_day: {{frequency_per_day}}, times: {{times}}, duration: {{duration}}, remaining_doses: {{remaining_doses}}}"
            self.medication_dict.append(dict_input) 
    
    def missed_days(self):
        """takes in missed days from history class to take note of deviations user took from their medication schedule"""  
        #just needs the DAY on which a medication is missed, and the NAME of the medication is missed. this could be in whatever 
        #form you think is best, such as a list of tuples where the first index of the tuple is the day(int), and the second 
        #index is the medciation name(str) that was missed on that day. it doesn't have to be like that just as long as 
        #we have variables that store this information that I could use in the journal_output function
          
    def journal_output(self):
        """uses medication_dict to create text file of journal that considers all of the attributes, goes one medication at a time
        Attribute:
            self (medication_dict)
        Returns:
            journal_output, a string that will be used to create the file medication_journal.txt
        Will look something like this:
        
        “On Day {x}, you took {dosage} of medication {name} {frequency} times, {dosage} of medication {name} 
        {frequency} times, {dosage} of medication {name} {frequency} times…

        On Day {x+1}...”

        Misses:
        “On Day {x} you missed {name}, on day {x} you missed….”
        """
        
        #assert type(self.medication_object) == Medication
        #makes an assert statement that checks that the structure of the input is correct
        
        day_text = [] #where the journal f string texts will go
        medication_list = [] #where all medication names will go, once the duration of a medication goes to zero the medication name will be removed from the list
        count = 0 #tracks the amount of days that the journal goes through
        
        for medication in self.medication_dict:
            medication_list.append(medication) #appends all medication names to the medication_list variable
            
        duration_list = []
        for details in self.medication_dict.values():
            duration = details.get("duration")
            duration_list.append(duration)
        final_day = max(duration_list) #finds the last day a medication(s) will be taken    

        while count >= final_day:
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
                
                if dosage is not None and frequency is not None:
                    text_container = text_container + " " + f"{dosage} of {medication} {frequency} times,"
                    
                if duration == count: #if this is the last day to take a medication, remove it from medication_list after its last use
                    medication_list.remove(medication)
                            
            text_container = f"On day {count}, you took " + text_container
            text_container = text_container[:-1] + "."
            day_text.append(text_container)
            
                
if __name__=="__main__":
    user_journal = journal_output("...")  
    
    with open("medication_journal", "w") as file:
        file.write(user_journal)  

