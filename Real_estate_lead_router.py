from IPython.display import clear_output
import random

my_client = ["Yaro","Musa","Idris","Adam","Manu","Albani"]
available_agents = ["Agent Zee","Agent Bee","Agent Mee","Agent Eee","Agent Dee","Agent All"]
database = []

def user_dashboard():
    print("     Welcome to the Real Estate Lead Router!!!", "\n", "_"*50)
    print("\n--- MAIN MENU ---")
    print("1: Simulate new incoming lead")
    print("2: View All Hot Lead (Assigned)")
    print("3: Exit system")
    return input("Enter a choice 1, 2 or 3 base on your dashboard description: ")
        
user_dashboard()

def simulate_lead():
    current_client = random.choice(my_client)
    budget = random.randint(150000,950000)
    if budget >= 500000:
        tag = "Hot"
    elif budget >= 250000:
        tag = "Warm"
    else:
        tag = "Cold"
    lead_pack = {}
    lead_pack["name"] = current_client
    lead_pack["budget"] = budget
    lead_pack["tag"] = tag
    existing_leads = [lead['name'] for lead in database]
    if current_client in existing_leads:
        print("_"*50)
        print(f"FIREWALL BLOCK!!! {current_client} alread exit in the system. Duplicate rejected")
        print("_"*50)
    else:
        database.append(lead_pack)
        print("_"*50)
        print(f"NEW LEAD ALERT: Lead {current_client} added! Budget: (${budget}) Tag[{tag}]")
        print("_"*50)

def hot_lead_list():
    hot_leads = [lead for lead in database if lead['tag'] == "Hot"]
    print("\n--- HOT LEAD DASHBOARD ---")
    if not hot_leads:
        print("Empty List Here!!! Go simulate more hot lead")
    else:
        for index, (agent,lead) in enumerate(zip(available_agents, hot_leads), start=1):
            print(f"{index}: Lead: {lead['name']} with Budget: (${lead['budget']}) assigned to --- {agent}")
            

program_on = True
while program_on:
    choice = user_dashboard()
    clear_output()

    if choice == '1':
        simulate_lead()
    elif choice == '2':
        hot_lead_list()
    elif choice == '3':
        print("Existing system... Goodbye!!!")
        program_on = False
    else:
        print("_"*35)
        print("Invalid Input: enter using (1, 2 or 3)")
        print("_"*35)