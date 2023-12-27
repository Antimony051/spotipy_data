# Spotipy Data Analysis

## Description

The project comprises several modules and functionalities to extract, analyze, and visualize data from Spotify listening history.

### Files

#### `script.py`

This script handles the core functionalities:

- **Imported Modules:** `json`, `fmanager`, `utils`
- **Functions:**
  - `json_handler`: Loads JSON data from a file
  - Data extraction using `utils` functions: `get_all`, `bar_chart_drawer`, `no_of_songs_by_time`, `song_by_month`
  - Other utility functions for analyzing and visualizing song data

#### `utils.py`

Contains utility functions for plotting and data analysis:

- **Functions:**
  - `setup_plt`: Sets up matplotlib parameters
  - `plotter`: Plots the number of songs played as a function of time
  - `bar_chart_drawer`: Draws bar charts based on provided data
  - `find_total_time`: Calculates the total time spent listening
  - `no_of_songs_by_time`: Analyzes the number of songs played over time
  - `song_by_month`: Analyzes song counts per month

#### `fmanager.py`

Manages files and data processing:

- **Functions:**
  - `mange_files`: Combines relevant JSON files into a single processed file, eliminating unnecessary fields

## Usage

1. Run `script.py` and provide the path to your extracted Spotify data.
2. The script will generate various statistics and visualizations based on your listening history.

### Modules and Functionalities

- **`utils.py`:** Handles visualization and analysis using matplotlib and numpy.
- **`fmanager.py`:** Manages file operations and combines relevant data into a single file.

## Installation

Clone the repository and ensure you have the required dependencies installed:
- `matplotlib`
- `numpy`

## How to Run

1. Install the required dependencies.
2. Execute `script.py` and provide the path to your Spotify data.
3. Follow the prompts to view various analyses and visualizations.

## Credits

This project uses:
- `matplotlib` for plotting
- `numpy` for array operations
