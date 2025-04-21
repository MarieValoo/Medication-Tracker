#Health Journal Class
#Marie Valouiski
#INST326 Final Project

class healthJournal:
    """takes in medication_list, which contains the name, dosage, frequency, and amount of days of each medication
    included in the list to create full journal of what it would look like if the user took all the medication according 
    to the prescription directions
    Attributes:
        self, medication_list which will probably come from Medication class using composition
        Output of Registers Medication"""
        
    def __init__(self, name, dosage, frequency, duration, medication_list): 
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        #include medication_list 
        
    def missed_days(self):
        """takes in missed days from history class to take note of deviations user took from their medication schedule"""  
        
          
    def journal_output(self):
        """uses object to create text file of journal that considers all of the attributes, goes one medication at a time
        Returns:
            journal_output, a string that will be used to create the file medication_journal.txt
        Will look something like this:
        
        “On Day {x}, you took {dosage} of medication {name} {frequency} times, {dosage} of medication {name} 
        {frequency} times, {dosage} of medication {name} {frequency} times…

        On Day {x+1}...”

        Misses:
        “On Day {x} you missed {name}, on day {x} you missed….”
        """
        
        day_text = []
        
        for med in medication_list:
            for x in range(1, last_day):
                last_day = self.duration
                text = f"On Day {x}, you took {self.dosage} of medication {self.name} {self.frequency} times"
                
if __name__=="__main__":
    user_journal = journal_output("...")  
    
    with open("medication_journal", "w") as file:
        file.write(user_journal)  
