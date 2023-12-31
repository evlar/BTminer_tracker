
# BTminer_tracker

**BTminer_tracker**: A program built to track and visualize variables for all your miners on a given coldkey.

## Description

BTminer_tracker is designed to monitor and visualize stake, trust, consensus, incentive, and emission for registered hotkeys for a given coldkey. It provides functionality for logging real-time data, configuring miner identifiers (hotkeys), and plotting these data.

## Requirements

- **Python Version**: Latest version of Python 3
- **Dependencies**:
  - Bittensor
  - Local or Remote Subtensor Node
  - PM2 (Process Manager)
  - Pandas
  - Matplotlib
  - OS, Subprocess, Time (standard Python libraries)

## Installation

1. **Clone the Repository**:
   
```python
   git clone https://github.com/evlar/BTminer_tracker.git
```

2. **Install Dependencies**:
   Navigate to the project directory and run:

 ```python
   pip install -r requirements.txt
 ```

   This command will install all the required Python packages.

## Usage

To start the application:
1. Run `run.py`:

```python
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
1. **Log Miner Data**: On the first run, you'll be prompted to enter your coldkey address. This will tack all registered hotkeys associated with the address. PM2 must be installed!

2. **Input/Edit Hotkey Names**: Assign meaningful names to your hotkeys for easier identification in logs and visualizations. Repeat this step with each new hotkey registration. *Note: Snapshots occur every 20 minutes (100 blocks)

3. **View Graphs**: Plot stake, trust, consensus, incentive, or emission for select or all hotkeys.

4. **Exit**: Get on outa here!