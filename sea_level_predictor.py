import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit (using all data from 1880 to the latest year)
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_all = range(1880, 2051)
    sea_levels_fit_all = [slope_all * year + intercept_all for year in years_extended_all]
    plt.plot(years_extended_all, sea_levels_fit_all, color='red', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (using data from 2000 to the latest year)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = range(2000, 2051)
    sea_levels_fit_2000 = [slope_2000 * year + intercept_2000 for year in years_extended_2000]
    plt.plot(years_extended_2000, sea_levels_fit_2000, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
