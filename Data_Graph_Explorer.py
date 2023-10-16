import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load a CSV file from the local computer
def load_csv_from_local():
    file_path = input("Enter the local path to the CSV file: ")
    return pd.read_csv(file_path)

# Function to load a CSV file from a URL
def load_csv_from_url():
    url = input("Enter the URL of the CSV file: ")
    return pd.read_csv(url)

# Function to display column names and the first two rows
def display_data_info(data):
    print("Column Names:")
    print(data.columns)
    
    print("\nFirst two rows of data:")
    print(data.head(2))

def graph_scatter_line(data):
    x_column = input("Enter the x-axis column name: ")
    y_column = input("Enter the y-axis column name: ")
    
    x = data[x_column].to_numpy()
    y = data[y_column].to_numpy()

    # graph
    xmin = x.min() - 5
    xmax = x.max() + 5
    ymin = y.min() - 5
    ymax = y.max() + 5

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])  # window size
    plt.plot([xmin, xmax], [0, 0], 'b')  # blue x-axis
    plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis
    plt.plot(x, y, 'ro')  # scatterplot
    plt.plot(x, y, 'b')  # line graph
    plt.show()

if __name__ == "__main__":
    data = None

    while True:
        print("\nData Graph Explorer Menu:")
        print("1. Load CSV from the local computer")
        print("2. Load CSV from a URL")
        print("3. Display data info (column names and first two rows)")
        print("4. Visualize data as a scatter plot and line graph")
        print("5. Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            data = load_csv_from_local()
        elif choice == "2":
            data = load_csv_from_url()
        elif choice == "3":
            if data is not None:
                display_data_info(data)
            else:
                print("Please load data first (option 1 or 2).")
        elif choice == "4":
            if data is not None:
                graph_scatter_line(data)
            else:
                print("Please load data first (option 1 or 2).")
        elif choice == "5":
            print("Exiting Data Graph Explorer.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
