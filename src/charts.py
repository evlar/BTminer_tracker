import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import os

def load_hotkey_names(file_path):
    if os.path.exists(file_path):  
        return pd.read_csv(file_path).set_index('hotkey').to_dict()['hotkey_name']
    return {}

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os


def plot_combined_hotkeys(df, variable, hotkey_names, exclude_hotkeys=[]):
    plt.figure(figsize=(15, 8))
    
    # Ensure the variable is numeric, stripping 'τ' if the variable is 'stake'
    if variable == 'stake':
        df[variable] = df[variable].str.replace('τ', '').astype(float)
    
    # Convert timestamps to datetime and sort
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values('timestamp', inplace=True)

    # Get unique hotkeys and sort by their names
    unique_hotkeys = df['hotkey'].unique()
    sorted_hotkeys = sorted(unique_hotkeys, key=lambda x: hotkey_names.get(x, 'Unknown'))

    # Plot each hotkey's data
    for hotkey in sorted_hotkeys:
        if hotkey in exclude_hotkeys:  # Skip the excluded hotkeys
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


def select_hotkey(df, hotkey_names):
    unique_hotkeys = df['hotkey'].unique()
    hotkeys_with_names = [(key, hotkey_names.get(key, 'Unknown')) for key in unique_hotkeys]
    hotkeys_with_names.sort(key=lambda x: x[1])  # Sort by hotkey name

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
                while True:  
                    print("\nSelect the variable to visualize:")
                    print("1. Stake")
                    print("2. Trust")
                    print("3. Consensus")
                    print("4. Incentive")
                    print("5. Emission")
                    print("6. Return to previous menu")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        plot_variable(filename, 'stake', hotkey)
                    elif choice == '2':
                        plot_variable(filename, 'trust', hotkey)
                    elif choice == '3':
                        plot_variable(filename, 'consensus', hotkey)
                    elif choice == '4':
                        plot_variable(filename, 'incentive', hotkey)
                    elif choice == '5':
                        plot_variable(filename, 'emission', hotkey)
                    elif choice == '6':
                        break  
                    else:
                        print("Invalid choice. Please try again.")

        elif main_choice == '2':
            exclude_hotkeys = []
            while True:
                print("\nDo you want to exclude a hotkey? (yes/no)")
                exclude_decision = input("Enter your choice: ").lower()

                if exclude_decision == 'yes':
                    print("Select a hotkey to exclude:")
                    exclude_hotkey = select_hotkey(df, hotkey_names)
                    if exclude_hotkey and exclude_hotkey not in exclude_hotkeys:
                        exclude_hotkeys.append(exclude_hotkey)

                    print("Would you like to exclude another hotkey? (yes/no)")
                    another_exclude_decision = input("Enter your choice: ").lower()
                    if another_exclude_decision != 'yes':
                        break
                else:
                    break

            print("\nSelect the variable for comparison across all hotkeys:")
            print("1. Stake")
            print("2. Trust")
            print("3. Consensus")
            print("4. Incentive")
            print("5. Emission")
            print("6. Return to previous menu")
            comp_choice = input("Enter your choice: ")
            variable = None

            if comp_choice == '1':
                variable = 'stake'
            elif comp_choice == '2':
                variable = 'trust'
            elif comp_choice == '3':
                variable = 'consensus'
            elif comp_choice == '4':
                variable = 'incentive'
            elif comp_choice == '5':
                variable = 'emission'
            elif comp_choice == '6':
                continue
    
            if variable:
                plot_combined_hotkeys(df, variable, hotkey_names, exclude_hotkeys)
            else:
                print("Invalid choice. Please try again.")

        elif main_choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
