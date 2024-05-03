import matplotlib.pyplot as plt

def plot_sales():
    # Sample data for monthly sales (you can replace this with your own data)
    months = ['January', 'February', 'March', 'April', 'May']
    sales = [10000, 12000, 11000, 13000, 15000]

    # Plot the data
    plt.plot(months, sales, marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Sales Amount ($)')
    plt.title('Monthly Sales')

    # Show the plot
    plt.grid(True)  # Add grid for better readability
    plt.show()

# Call the function to generate the plot
plot_sales()