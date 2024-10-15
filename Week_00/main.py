import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = 'LaborSupply1988.csv'
AGE_COLUMN = 'age'
KIDS_COLUMN = 'kids'
WAGE_COLUMN = 'lnwg'
HOURS_COLUMN = 'lnhr'
DISABILITY_COLUMN = 'disab'


def load_data(file_path):
    """1a), 2a) Load dataset and return pandas DataFrame."""
    return pd.read_csv(file_path)


def summarize_data(df):
    """1b), c), d) Print basic information about the dataset."""
    features = len(df.columns)
    datapoints = len(df.index)
    print(f'Number of features columns: {features}\tNumber of datapoints (rows): {datapoints}\n')
    print(f'Attributes: {", ".join(df.columns)}\n')
    print(f'First 10 datapoints:\n{df.head(10)}\n')


def print_age_range(df):
    """1e) Print the value range of the age column."""
    age_max = df[AGE_COLUMN].max()
    age_min = df[AGE_COLUMN].min()
    print(f'Age range: {age_min} - {age_max}\n')


def average_lnwg_by_kids(df):
    """1f) Print the average log hourly wage for different number of kids."""
    grouped_avg = df.groupby(KIDS_COLUMN)[WAGE_COLUMN].mean()
    print('Average log hourly wage (lnwg) for individuals with:')
    for i in range(7):
        print(f'{i} kids: {grouped_avg[i]:.2f}')
    print('')


def average_kids_of_40_year_olds(df):
    """1g) Print the average number of kids for 40-year-olds."""
    filtered = df[df[AGE_COLUMN] == 40]
    average_kids = filtered[KIDS_COLUMN].mean()
    print(f'Average number of kids of 40-year-olds: {average_kids:.2f}\n')


def plot_age_distribution(df):
    """2b) Plot a histogram of the age distribution."""
    df[AGE_COLUMN].hist(bins=30)
    plt.title('Age distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Laborers')
    plt.show()


def plot_kids_by_age(df):
    """2c) Plot the average number of kids by age."""
    average_kids_by_age = df.groupby(AGE_COLUMN)[KIDS_COLUMN].mean()
    plt.plot(average_kids_by_age.index, average_kids_by_age.values)
    plt.title('Number of Kids by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Kids')
    plt.show()


def plot_wage_by_age(df):
    """2d) Plot wage against age."""
    plt.scatter(df[AGE_COLUMN], df[WAGE_COLUMN])
    plt.title('Wage by Age')
    plt.xlabel('Age')
    plt.ylabel('Log of Hourly Wage')
    plt.show()


def plot_average_wage_by_age(df):
    """2e) Plot the average log of hourly wage by age."""
    average_wage_by_age = df.groupby(AGE_COLUMN)[WAGE_COLUMN].mean()
    plt.plot(average_wage_by_age.index, average_wage_by_age.values)
    plt.title('Average Wage by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Logarithmic Hourly Wage')
    plt.show()


def plot_lnhr_by_disability(df):
    """2f) Plot log of hours worked (lnhr) by age with color-coded disability status."""
    plt.scatter(df[df[DISABILITY_COLUMN] == 0][AGE_COLUMN], df[df[DISABILITY_COLUMN] == 0][HOURS_COLUMN], color='blue',
                label='No Disability')
    plt.scatter(df[df[DISABILITY_COLUMN] == 1][AGE_COLUMN], df[df[DISABILITY_COLUMN] == 1][HOURS_COLUMN], color='green',
                label='Disability')
    plt.title('Log Hours Worked (lnhr) by Age with and without Disability')
    plt.xlabel('Age')
    plt.ylabel('Log of Hours Worked (lnhr)')
    plt.legend()
    plt.show()


def plot_lnhr_by_kids(df):
    """2g) Create a boxplot of log of hours worked (lnhr) by number of kids."""
    df.boxplot(column=HOURS_COLUMN, by=KIDS_COLUMN)
    plt.title('Log of Hours Worked (lnhr) by Number of Kids')
    plt.xlabel('Number of Kids')
    plt.ylabel('Log of Hours Worked (lnhr)')
    plt.show()


def main():
    # Load data
    df = load_data(FILE_PATH)

    # Summarize data
    summarize_data(df)

    # Print ranges and averages
    print_age_range(df)
    average_lnwg_by_kids(df)
    average_kids_of_40_year_olds(df)

    # Plotting
    plot_age_distribution(df)
    plot_kids_by_age(df)
    plot_wage_by_age(df)
    plot_average_wage_by_age(df)
    plot_lnhr_by_disability(df)
    plot_lnhr_by_kids(df)


if __name__ == "__main__":
    main()
