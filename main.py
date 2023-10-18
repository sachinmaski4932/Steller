
diary = {}

def add_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    mood = input("Enter your mood for the day: ")
    entry = input("Write your diary entry: ")
    diary[date] = {'mood': mood, 'entry': entry}
    print("Entry added successfully!")

def view_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    if date in diary:
        entry = diary[date]
        print(f"Date: {date}")
        print(f"Mood: {entry['mood']}")
        print("Diary Entry:")
        print(entry['entry'])
    else:
        print("Entry not found for the given date.")

def main():
    while True:
        print("\nDiary App Menu:")
        print("1. Add Diary Entry")
        print("2. View Diary Entry")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entry()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
