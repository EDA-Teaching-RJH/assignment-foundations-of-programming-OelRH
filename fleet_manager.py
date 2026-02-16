ValidRanks = ["Petty Officer", "Ensign", "Lieutenant Junior Grade", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Fleet Captain"]

def init_database():
    n = ["Picard", "Riker", "Data", "Worf", "Spock"]
    r = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Commander"]
    d = ["Command", "Command", "Operations", "Security", "Science"]
    id_ = ["SP-937-215", "SC-231-427", "none", "none", "S179-276SP"]
    return n, r, d, id_
    


def display_menu(names, ranks):
    user = input("input user's full name: ")
    for i in range(len(names)):
        print(f"{names[i]} - {ranks[i]}")
    
    print("current student logged in: ", user )
    choice = input("Choose an option: ")
    return choice


def add_member(names, ranks, divs, ids):
    name = input("Name: ")
    rank = input("Rank: ")
    div = input("Division: ")
    id = input("ID: ")
    if id not in ids: 
        pass
    else:
        print("ID not unique" )
    
    if ranks not in ValidRanks:
        print("Rank not in valid TNG rank" )
    else: 
        pass
    
    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(id)

def remove_member(names,ranks, divs, ids):
    id = input("Provide ID: ")
    idx = ids.index(id)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)

def update_rank(ranks, ids):
    id = input("Provide ID: ")
    new_rank = input("New rank: ")
    idx = ids.index(id)
    ranks[idx] = new_rank

def display_roster(names, ranks, divs, ids):
    print("\n CREW LIST")
    for _ in range(len(names)):
        print(f"\n{names[_], ranks[_], divs[_], ids[_]}")

def search_crew(names, ranks, divs, ids):
    term = input("Provide search term: ")
    found = False

    if term in names:
        idx = names.index(term)
        print(names[idx], ranks[idx], divs[idx], ids[idx])
        found = True

    elif term in ranks:
        for i in range(len(ranks)):
            if ranks[i] == term:
                print(names[i], ranks[i], divs[i], ids[i])
                found = True

    elif term in divs:
        for i in range(len(divs)):
            if divs[i] == term:
                print(names[i], ranks[i], divs[i], ids[i])
                found = True

    elif term in ids:
        idx = ids.index(term)
        print(names[idx], ranks[idx], divs[idx], ids[idx])
        found = True

    if not found:
        print("No matching crew member found")

def filter_by_division(names, divs):
    division = input("Choose either Command, Operations or Sciences: ")
    for _ in divs:
        if division in divs:
            idx = divs.index(division)
            print(names[idx] )

def calculate_payroll(ranks):
    for rank in ranks:
        credit = 0
        if rank == "Captain":
            credit += 1000
        elif rank == "Fleet Captain":
            credit += 2000
        elif rank == "Commander":
            credit += 800
        elif rank == "lieutenant Commander":
            credit += 700
        elif rank == "Lieutenant":
            credit += 500
        elif rank == "Lieutenant Junior Grade":
            credit += 300
        elif rank == "Ensign":
            credit += 200
        elif rank == "Petty Offcifer":
            credit += 100
        else:
            pass
    print("Total cost of Crew: ",credit )

def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Commander":
            count += 1
        elif rank == "Lieutenant Commander":
            count += 1
        elif rank == "Captain":
            count += 1
        elif rank == "Fleet Captain":
            count += 1
        else:
            pass
        print(count)
def main():
    n, r, d, id_ = init_database()
    choice = int(input("Press 1 to display menu:\n" \
    "Press 2 to add member:\n" \
    "Press 3 to remove member:\n"
    "Press 4 to update a user's rank:\n" \
    "Press 5 to display the current roster:\n" \
    "Press 6 to search crew:\n" \
    "Press 7 to Filter crew by division:" \
    "\nPress 8 to calculate current crew's payroll:" \
    "\nPress 9 to Count the amount of officers:\n"
    "Press 0 to quit: "))
    
    if choice == 1:
        display_menu(n, r)
    elif choice == 2:
        add_member(n, r, d, id_)
    elif choice == 3:
        remove_member(n, r, d, id_)
    elif choice == 4:
        update_rank(r, id_)
    elif choice == 5:
        display_roster(n, r, d, id_)
    elif choice == 6:   
        search_crew(n, r, d, id_)
    elif choice == 7:    
        filter_by_division(n, d)
    elif choice == 8:   
        calculate_payroll(r)
    elif choice == 9:    
        count_officers(r)
    elif choice == 0:
        n = 1
    else:
        print("number doesn't correspond to options provided.")
    return n

while True:
    if main() == 1:
        break
    main()



        






