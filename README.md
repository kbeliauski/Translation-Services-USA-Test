# Задачи на общий уровень владения языком

This solution provides several functions to manipulate arrays of dictionaries, allowing you to filter, sort, and transform data. You can run these functions from the command line and execute unit tests to ensure their correctness.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Main Script](#running-the-main-script)
  - [Running Tests](#running-tests)

## Installation

1. **Go to the python test folder:**
   ```bash
   cd python_assignment
   ```

2. **Set up a virtual environment: Create a virtual environment to manage dependencies:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
    
    On Windows:
   ```bash
   venv\Scripts\activate
   ```
    On MacOS/Linux:
    ```bash
   source venv/bin/activate
   ```

4. **Install any required packages:**
    (You can add required packages to a requirements.txt file and use it here.)
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Main Script
To run the main script, use the following command structure:
```bash
   python -m src <command> <input_file> [additional_arguments]
   ```

### Available Commands:

- **filter_unique_records:** Filter unique records by 'id'.
   ```bash
   python -m src filter_unique_records path/to/input.json
   ```

- **sort_array_by_key:** Sort the array by a specified key.
   ```bash
   python -m src sort_array_by_key path/to/input.json <key>
   ```

- **filter_by_condition:** Filter the array based on a specific condition.
   ```bash
   python -m src filter_by_condition path/to/input.json <condition_key> <condition_value>
   ```

- **transform_to_key_value:** Transform the array into a key-value map.
   ```bash
   python -m src transform_to_key_value path/to/input.json
   ```

### Example:
```bash
python -m src filter_unique_records inputs/input.json
```

### Running Tests
To run the unit tests, ensure your virtual environment is activated and execute the following command:
```bash
python -m unittest discover -s tests -p "*.py"
```
This command will discover and run all test files in the tests directory.

## Notes

- Ensure you have Python installed on your system. This project is compatible with Python 3.x.
- Modify the directory paths as necessary.<br>


# Задачи на уровень владения SQL

### First solution is located at 
```bash
cd sql_assignments/sql/task1_query.sql
```

### Second solution is located at 
```bash
cd sql_assignments/sql/task2_optimize_bio_search.md
```

# Архитектурные задачи
### Both solutions located at 
```bash
cd php_assignment/solution.md
```
