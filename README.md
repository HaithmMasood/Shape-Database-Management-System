# Shape Database Management System

## Overview
This Python application is designed to manage a database of geometric shapes. It allows users to load shape data from files, remove duplicates, save the updated database, print shape information to standard output, and provide a summary and detailed information of the shapes in memory.

## Features
- **LOAD**: Load a database of shapes from a specified file.
- **TOSET**: Convert the current multi-set in memory to a set, removing duplicates.
- **SAVE**: Save the current in-memory database to a specified file.
- **PRINT**: Print the current in-memory database to the standard output.
- **SUMMARY**: Print a summary of the in-memory database to the standard output.
- **DETAILS**: Print detailed information of the in-memory database objects to the standard output.
- **QUIT**: Terminate the program.

## Usage
To run the program, simply execute `CommandLine.py` and follow the interactive menu prompts. Here are the steps to interact with the program:

1. Start the program.
2. Enter your choice of action (`LOAD`, `TOSET`, `SAVE`, `PRINT`, `SUMMARY`, `DETAILS`, or `QUIT`).
3. If `LOAD` or `SAVE` is selected, enter the filename when prompted.
4. The program will execute the chosen action and provide output or prompt for the next action.

5. ## Files
- `CommandLine.py`: The main Python script that runs the application.
- `database.txt`: Example input file containing shape data.
- `new_data.txt`: Example of modified shape data.
- `updated_database.txt`: Example output file for saved shape data.

## Installation
Clone this repository or download the source code to your local machine. Make sure Python 3 is installed on your system.

```bash
git clone https://github.com/yourusername/shape-database.git
cd shape-database
python CommandLine.py
