# Demo

This demo was run in this project folder on Linux.

## 1) Train

Command:

```bash
python3 training_program.py
```

Observed output (sample):

```text
Epoch 0: Loss = 20839224.556025073
Epoch 100: Loss = 17100415.933447845
Epoch 200: Loss = 14039644.630930372
Epoch 300: Loss = 11533947.78682264
Epoch 400: Loss = 9482661.998365533
Epoch 500: Loss = 7803379.288718958
Epoch 600: Loss = 6428636.464103077
Epoch 700: Loss = 5303204.859897142
Epoch 800: Loss = 4381871.594455682
Epoch 900: Loss = 3627623.1951423064
Plot saved as loss_history.png
```

Expected files after training:

- `model_params.txt`
- `loss_history.txt`
- `loss_history.png`

## 2) Predict with sample mileage

Command:

```bash
printf '50000\n' | python3 prediction_program.py
```

Observed output:

```text
Enter the mileage of the car (in km): Estimated price of the car for mileage 50000.0 km: $4681.64
```

## 3) Interactive prediction mode

You can also run:

```bash
python3 prediction_program.py
```

Then type mileage manually when prompted.
