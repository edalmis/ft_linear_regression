import pandas as pd
import signal
import sys
import os

def estimate_price(mileage, theta0, theta1):
    """
    Function to estimate the price of a car for a given mileage.
    
    Parameters:
    - mileage: The mileage of the car.
    - theta0: The intercept parameter.
    - theta1: The slope parameter.
    
    Returns:
    - estimated_price: The estimated price of the car.
    """
    estimated_price = theta0 + (theta1 * mileage)
    return estimated_price

def handle_signal(sig, frame):
    print("\nOperation interrupted. Exiting gracefully...")
    sys.exit(0)

def main():
    # Register the signal handlers for Ctrl+C and Ctrl+D
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    
    # Load the trained parameters
    if os.path.exists('model_params.txt'):
        with open('model_params.txt') as f:
            theta0 = float(f.readline())
            theta1 = float(f.readline())
    else:
        print("model_params.txt not found, default values are used")
        theta0 = 0
        theta1 = 0
    
    # Load the dataset to get mean and std for de-normalization
    data = pd.read_csv('data.csv')
    X_mean = data['km'].mean()
    X_std = data['km'].std()

    while True:
        try:
            mileage_km = float(input("Enter the mileage of the car (in km): "))
            if mileage_km < 0:
                print("Error: Mileage cannot be negative. Please enter a valid mileage.")
                continue
            if mileage_km > 1e6:  # example threshold for max mileage, adjust as necessary
                print("Error: Mileage is too large. Please enter a valid mileage.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid mileage (numeric value).")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation interrupted. Exiting gracefully...")
            sys.exit(0)

    # Normalize the mileage input
    mileage_normalized = (mileage_km - X_mean) / X_std

    # Call the estimate_price function to get the estimated price
    estimated_price = estimate_price(mileage_normalized, theta0, theta1)
    
    # Print the estimated price
    print("Estimated price of the car for mileage {} km: ${:.2f}".format(mileage_km, estimated_price))

if __name__ == "__main__":
    main()
