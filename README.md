
# BTminer_tracker

**BTminer_tracker**: A program built to track and visualize variables for all your miners on a given coldkey.

## Description

BTminer_tracker is designed to monitor and visualize stake, trust, consensus, incentive, and emission for registered hotkeys for a given coldkey. It provides functionality for logging real-time data, configuring miner identifiers (hotkeys), and plotting these data using both graphical and text-based visualizations.

## Requirements

- **Python Version**: Latest version of Python 3
- **Dependencies**:
  - Bittensor
  - Local or Remote Subtensor Node
  - PM2 (Process Manager)
  - Pandas
  - Matplotlib (for graphical visualization)
  - asciichartpy (for text-based visualization)
  - OS, Subprocess, Time (standard Python libraries)

## Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/evlar/BTminer_tracker.git
```

2. **Install Dependencies**:
   Navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

   This command will install all the required Python packages.

## Usage

To start the application:
1. Run `run.py`:

```bash
cd BTminer_tracker
python3 run.py
```

   This will launch the main menu of the program.

2. Follow the on-screen instructions to:
   - Log miner data.
   - Input/Edit hotkey names.
   - View graphs and analytics.

## Operation

**From the Main Menu:**
1. **Log Miner Data**: On the first run, you'll be prompted to enter your coldkey address. This will track all registered hotkeys associated with the address. PM2 must be installed!

2. **Input/Edit Hotkey Names**: Assign meaningful names to your hotkeys for easier identification in logs and visualizations. Repeat this step with each new hotkey registration. *Note: Snapshots occur every 20 minutes (100 blocks).

3. **View Graphs**: Choose to plot stake, trust, consensus, incentive, or emission for select or all hotkeys. You can select between graphical visualization, which will display the data in a graphical plot, or text-based visualization, which will display the data as an ASCII chart in the terminal.

4. **Exit**: Get on outa here!

## Visualization Modes

BTminer_tracker supports two modes of visualization:

- **Graphical Visualization**: This mode uses Matplotlib to generate and display graphical plots. It is the default mode and requires a graphical environment to display the plots.

- **Text-based Visualization**: This mode uses asciichartpy to generate ASCII charts that can be displayed directly in the terminal. This is useful for environments without a graphical interface, such as remote servers or headless systems.

When prompted in the main menu, you can choose the preferred visualization mode for viewing the data.
```

Make sure to include `asciichartpy` in your `requirements.txt` file to ensure that users can install all necessary dependencies. If you have any additional instructions or details you'd like to include about the text-based visualization, you can add them to the "Visualization Modes" section of the README.
