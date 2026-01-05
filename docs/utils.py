import os
import logging
from typing import List, Dict

def create_logger(log_name: str) -> logging.Logger:
    """Create a logger with a given name."""
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def load_data(file_path: str) -> List[Dict]:
    """Load data from a file and return it as a list of dictionaries."""
    with open(file_path, 'r') as f:
        data = []
        for line in f:
            line = line.strip()
            if line:
                column_names = line.split(',')
                data.append({column_name: None for column_name in column_names})
    return data

def save_data(file_path: str, data: List[Dict]) -> None:
    """Save data to a file."""
    with open(file_path, 'w') as f:
        for row in data:
            row_values = [str(row[column_name]) for column_name in sorted(row.keys())]
            f.write(','.join(row_values) + '\n')

def create_dir(directory: str) -> None:
    """Create a directory with the given name if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)