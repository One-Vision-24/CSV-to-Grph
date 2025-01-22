import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(file_path)

def explore_data(df):
    """Display basic information about the dataset."""
    print("Data Head:\n", df.head())
    print("\nData Info:\n", df.info())
    print("\nData Description:\n", df.describe())

def plot_line_chart(df, x_col, y_col):
    """Plot a line chart."""
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title(f"Line Chart: {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

def plot_bar_chart(df, x_col, y_col):
    """Plot a bar chart."""
    plt.figure(figsize=(10, 6))
    df.groupby(x_col)[y_col].sum().plot(kind='bar')
    plt.title(f"Bar Chart: {y_col} by {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.show()

def plot_pie_chart(df, column):
    """Plot a pie chart."""
    plt.figure(figsize=(8, 8))
    df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(f"Pie Chart: Distribution of {column}")
    plt.ylabel('')
    plt.show()

def plot_scatter_plot(df, x_col, y_col):
    """Plot a scatter plot."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], color='blue')
    plt.title(f"Scatter Plot: {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

def plot_histogram(df, column):
    """Plot a histogram."""
    plt.figure(figsize=(10, 6))
    df[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.title(f"Histogram: Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def main():
    file_path = input("Enter the CSV file path: ")
    df = load_data(file_path)
    
    # Explore data
    explore_data(df)

    # Allow user to choose what kind of plot to generate
    print("\nSelect plot type:")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Pie Chart")
    print("4. Scatter Plot")
    print("5. Histogram")
    
    choice = input("Enter the number of the plot type you want to generate: ")
    
    if choice == '1':  # Line Chart
        x_col = input("Enter the x-axis column name: ")
        y_col = input("Enter the y-axis column name: ")
        plot_line_chart(df, x_col, y_col)
    elif choice == '2':  # Bar Chart
        x_col = input("Enter the x-axis column name: ")
        y_col = input("Enter the y-axis column name: ")
        plot_bar_chart(df, x_col, y_col)
    elif choice == '3':  # Pie Chart
        column = input("Enter the column name to visualize as a pie chart: ")
        plot_pie_chart(df, column)
    elif choice == '4':  # Scatter Plot
        x_col = input("Enter the x-axis column name: ")
        y_col = input("Enter the y-axis column name: ")
        plot_scatter_plot(df, x_col, y_col)
    elif choice == '5':  # Histogram
        column = input("Enter the column name for the histogram: ")
        plot_histogram(df, column)
    else:
        print("Invalid choice! Exiting.")

if __name__ == "__main__":
    main()
    
