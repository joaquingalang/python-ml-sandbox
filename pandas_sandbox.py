import pandas as pd

cars = {
    'Model': ['488 Spider', 'M4 Coupe', 'Corolla Cross'],
    'Brand': ['Ferrari', 'BMW', 'Toyota'],
    'Color': ['Red', 'White', 'Black'],
    'Type': ['Automatic', 'Manual', 'Hybrid'],
}

cars_df = pd.DataFrame(cars)

print(cars_df)