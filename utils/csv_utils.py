import csv
import os
import time
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_csv_data(csv_file: str, sample_size: Optional[int] = None) -> List[str]:
    """
    Load usernames from CSV file into memory.
    
    Args:
        csv_file (str): Path to the CSV file
        sample_size (Optional[int]): Number of usernames to randomly sample. If None, loads all usernames.
        
    Returns:
        List[str]: List of usernames
    """
    try:
        # Check if file exists
        if not os.path.exists(csv_file):
            logger.error(f"File not found at path: {csv_file}")
            logger.error(f"Current working directory: {os.getcwd()}")
            return []

        usernames = []
        start_time = time.time()
        
        logger.info(f"Starting to load usernames from {csv_file}")
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            # Skip header row
            next(csv_reader, None)
            
            for row in csv_reader:
                if len(row) >= 2:
                    username = row[1].strip()
                    usernames.append(username)
        
        # If sample size is provided, randomly sample usernames
        if sample_size and sample_size < len(usernames):
            logger.info(f"Sampling {sample_size} usernames from {len(usernames)} total usernames")
            import random
            usernames = random.sample(usernames, sample_size)
        else:
            logger.info(f"Loading all {len(usernames)} usernames")
        
        elapsed_time = time.time() - start_time
        logger.info(f"Successfully loaded {len(usernames)} usernames in {elapsed_time:.2f} seconds")
        
        return usernames
        
    except Exception as e:
        logger.error(f"Error loading usernames: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return [] 