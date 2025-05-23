import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
import matplotlib.pyplot as plt

# Delete existing files if they exist
if os.path.exists('model_params.txt'):
    os.remove('model_params.txt')

if os.path.exists('loss_history.txt'):
    os.remove('loss_history.txt')

# Delete existing plot file if it exists
if os.path.exists('loss_plot.png'):
    os.remove('loss_plot.png')

# Function to estimate the price of a car for a given mileage
def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

# Function to train the linear regression model
def train_model(X, y, learning_rate=0.001, epochs=1000):
    m = len(X)  # Number of training examples
    theta0 = 0.0  # Initialize parameters theta0 and theta1
    theta1 = 0.0

    loss_history = []

    # Gradient descent algorithm
    for epoch in range(epochs):
        # Calculate gradients
        gradient_theta0 = (1 / m) * sum(estimate_price(X[i], theta0, theta1) - y[i] for i in range(m))
        gradient_theta1 = (1 / m) * sum((estimate_price(X[i], theta0, theta1) - y[i]) * X[i] for i in range(m))

        # Update parameters
        theta0 -= learning_rate * gradient_theta0
        theta1 -= learning_rate * gradient_theta1

        # Compute loss (Mean Squared Error)
        loss = (1 / (2 * m)) * sum((estimate_price(X[i], theta0, theta1) - y[i]) ** 2 for i in range(m))
        loss_history.append(loss)

        # Print loss every 100 epochs
        if epoch % 100 == 0:
            print(f'Epoch {epoch}: Loss = {loss}')

    return theta0, theta1, loss_history

# Main function to read data, train model, and save parameters
def main():
    # Check if the data file exists
    if not os.path.exists('data.csv'):
        print("Error: 'data.csv' file not found.")
        return
    
    # Load the dataset
    data = pd.read_csv('data.csv')
    
    # Extract features (mileage) and target values (prices)
    X = data['km'].values
    y = data['price'].values

    # Normalize features
    X_mean = X.mean()
    X_std = X.std()
    X = (X - X_mean) / X_std

    # Train the model
    theta0, theta1, loss_history = train_model(X, y)

    # Save the parameters theta0 and theta1 to a file
    with open('model_params.txt', 'w') as file:
        file.write(f'{theta0}\n{theta1}')

    # Save the loss history to a file
    with open('loss_history.txt', 'w') as file:
        for loss in loss_history:
            file.write(f'{loss}\n')

    # Plot the loss history
    plt.plot(loss_history)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss vs. Epoch')
    plt.savefig("loss_history.png")  # Save the plot as an image file
    print("Plot saved as loss_history.png")

if __name__ == "__main__":
    main()
