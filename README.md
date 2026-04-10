# ft_linear_regression

A simple linear regression project that predicts car price from mileage using gradient descent.

## Project files

- `training_program.py`: Trains a linear model using data from `data.csv`
- `prediction_program.py`: Loads trained parameters and predicts a price from user mileage input
- `data.csv`: Training dataset with `km` and `price` columns

## Requirements

- Python 3.8+
- pandas
- matplotlib

Install dependencies:

```bash
pip install pandas matplotlib
```

## How to run

### 1. Train the model

```bash
python3 training_program.py
```

What this generates:

- `model_params.txt`: learned `theta0` and `theta1`
- `loss_history.txt`: loss value for each epoch
- `loss_history.png`: training loss plot

### 2. Predict a price

```bash
python3 prediction_program.py
```

Then enter mileage in km when prompted.

## Notes

- If `model_params.txt` is missing, prediction runs with default values (0, 0).
- Input validation in prediction prevents negative and unrealistically high mileage.
- The training script normalizes mileage before gradient descent.

## Demo

See `DEMO.md` for a complete run-through with real command output.
