# Courier Assignment Project

This project assigns the cheapest courier to orders based on their weight using provided courier rules.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

### Setting Up the Project

1. **Clone the Repository**:
   
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**:

   On macOS and Linux:

   ```sh
   python3 -m venv venv
   ```

   On Windows:

   ```sh
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   On macOS and Linux:

   ```sh
   source venv/bin/activate
   ```

   On Windows:

   ```sh
   venv\Scripts\activate
   ```

4. **Install the Required Packages**:

   Ensure you have a `requirements.txt` file with the necessary dependencies:

   ```sh
   pandas
   ```

   Then, install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

### Running the Unit Tests

1. Ensure you have your `main.py` and `test_main.py` files set up as described.
2. Run the unit tests:

   ```sh
   python -m unittest test_main.py
   ```

### Project Structure

```
.
├── venv/                    # Virtual environment directory
├── main.py                  # Main script with courier assignment logic
├── test_main.py             # Unit tests for the main script
├── orders.py                # Python file with orders data 
├── couriers_rules.json      # JSON file with courier rules
├── requirements.txt         # List of dependencies
└── README.md                # This README file
```

With these steps, you should be able to set up, run, and test this project.