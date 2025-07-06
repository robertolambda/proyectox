import os
from src.stats import graphs
from src.scraping import *
import numpy as np
import dotenv

def main():
    print("Hello from proyectox!")
    graphs.plot([1, 2, 3, 4, 5], title="Sample Data", xlabel="Index", ylabel="Value")
    dotenv.load_dotenv()
    fred_token = os.getenv("FRED_TOKEN")
    print(fred_token)
if __name__ == "__main__":
    main()
    
    
