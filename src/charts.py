import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os

def load_hotkey_names(file_path):
    if os.path.exists(file_path):  
        return pd.read_csv(file_path).set_index('hotkey').to_dict()['hotkey_name']
    return {}

def plot_combined_hotkeys(df, variable, hotkey_names, exclude_hotkeys=[]):
    plt.figure(figsize=(15, 8))
    
    # Convert 'stake' variable to numeric if needed
    if variable == 'stake':
        df[variable] = df[variable].str.replace('τ', '').astype(float)
    
    # Convert timestamps to datetime and sort
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values('timestamp', inplace=True)

    # Get unique hotkeys and sort by their names
    unique_hotkeys = df['hotkey'].unique()
    sorted_hotkeys = sorted(unique_hotkeys, key=lambda x: hotkey_names.get(x, 'Unknown'))

    # Plot data for each hotkey, excluding specified hotkeys
    for hotkey in sorted_hotkeys:
        if hotkey in exclude_hotkeys:
            continue

        hotkey_data = df[df['hotkey'] == hotkey]
        if not hotkey_data.empty:
            plt.plot(hotkey_data['timestamp'], hotkey_data[variable], label=hotkey_names.get(hotkey, hotkey), marker='o', linestyle='-')

    # Formatting the plot
    plt.title(f'{variable.capitalize()} over time for all hotkeys')
    plt.xlabel('Time')
    plt.ylabel(variable.capitalize())
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def select_hotkey(df, hotkey_names, list_all=False):
    unique_hotkeys = df['hotkey'].unique()
    hotkeys_with_names = [(key, hotkey_names.get(key, 'Unknown')) for key in unique_hotkeys]
    hotkeys_with_names.sort(key=lambda x: x[1])

    if list_all:
        return hotkeys_with_names

    print("Available hotkeys:")
    for idx, (key, name) in enumerate(hotkeys_with_names, 1):
        print(f"{idx}. {key} ({name})")
    choice = input("Select a hotkey (number) or type 'exit' to quit: ")
    if choice.lower() == 'exit':
        return None
    try:
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(unique_hotkeys):
            return hotkeys_with_names[selected_index][0]
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def plot_variable(df, variable, hotkey, hotkey_names):
    plt.figure(figsize=(15, 8))
    
    if variable == 'stake':
        df[variable] = df[variable].str.replace('τ', '').astype(float)

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values('timestamp', inplace=True)

    hotkey_data = df[df['hotkey'] == hotkey]
    if not hotkey_data.empty:
        plt.plot(hotkey_data['timestamp'], hotkey_data[variable], label=hotkey_names.get(hotkey, hotkey), marker='o', linestyle='-')

    plt.title(f'{variable.capitalize()} over time for {hotkey_names.get(hotkey, hotkey)}')
    plt.xlabel('Time')
    plt.ylabel(variable.capitalize())
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, 'hotkeys.log')
    hotkey_names_file = os.path.join(current_dir, 'hotkey_names.csv')

    if not os.path.exists(hotkey_names_file):
        print(f"Error: The file {hotkey_names_file} was not found.")
        return
    hotkey_names = load_hotkey_names(hotkey_names_file)

    if not os.path.exists(filename):
        print(f"Error: The file {filename} was not found.")
        return
    df = pd.read_csv(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  

    while True:
        print("\nSelect an action:")
        print("1. Plot variable for a single hotkey")
        print("2. Plot all hotkeys")
        print("3. Exit")
        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            hotkey = select_hotkey(df, hotkey_names)
            if hotkey:
                print("\nSelect the variable to visualize:")
                print("1. Stake")
                print("2. Trust")
                print("3. Consensus")
                print("4. Incentive")
                print("5. Emission")
                print("6. Return to previous menu")
                choice = input("Enter your choice: ")

                variable_map = {
                    '1': 'stake',
                    '2': 'trust',
                    '3': 'consensus',
                    '4': 'incentive',
                    '5': 'emission'
                }

                variable = variable_map.get(choice)
                if variable:
                    plot_variable(df, variable, hotkey, hotkey_names)
                elif choice == '6':
                    continue
                else:
                    print("Invalid choice. Please try again.")

        elif main_choice == '2':
            exclude_hotkeys = []
            hotkeys_with_names = select_hotkey(df, hotkey_names, list_all=True)  # Get all hotkeys with names
            
            print("\nDo you want to exclude any hotkeys? (yes/no)")
            exclude_decision = input("Enter your choice: ").lower()

            if exclude_decision == 'yes':
                print("Select hotkeys to exclude (enter numbers separated by commas, e.g., 1,2,3):")
                for idx, (key, name) in enumerate(hotkeys_with_names, 1):
                    print(f"{idx}. {key} ({name})")
                
                choices = input("Enter hotkey numbers or 'exit' to quit: ")
                if choices.lower() != 'exit':
                    try:
                        selected_indexes = [int(choice.strip()) - 1 for choice in choices.split(',')]
                        for index in selected_indexes:
                            if 0 <= index < len(hotkeys_with_names):
                                exclude_hotkey = hotkeys_with_names[index][0]
                                if exclude_hotkey not in exclude_hotkeys:
                                    exclude_hotkeys.append(exclude_hotkey)
                                    print(f"Excluded hotkey: {exclude_hotkey}")
                            else:
                                print(f"Warning: Invalid selection '{index + 1}'. It will be ignored.")
                    except ValueError:
                        print("Invalid input. Please enter numbers separated by commas.")

            print("\nSelect the variable for comparison across all hotkeys:")
            print("1. Stake")
            print("2. Trust")
            print("3. Consensus")
            print("4. Incentive")
            print("5. Emission")
            print("6. Return to previous menu")
            comp_choice = input("Enter your choice: ")
            variable = None

            variable_map = {
                '1': 'stake',
                '2': 'trust',
                '3': 'consensus',
                '4': 'incentive',
                '5': 'emission'
            }

            variable = variable_map.get(comp_choice)
            if variable:
                plot_combined_hotkeys(df, variable, hotkey_names, exclude_hotkeys)
            elif comp_choice == '6':
                pass  # Return to the main menu
            else:
                print("Invalid choice. Please try again.")


        elif main_choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()