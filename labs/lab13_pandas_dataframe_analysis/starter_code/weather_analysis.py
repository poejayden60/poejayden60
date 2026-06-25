import pandas as pd

import matplotlib.pyplot as plt


def load_weather_data(filename):
    # TODO: load the data from csv file
    # TODO: return a Pandas dataframe
    df = pd.read_csv(filename)
    return df


def print_summary(df):
    # TODO: print summary statistics
    # TODO: extract the mean temperature and print it
    print(df.describe())

    mhigh = df["highC"].mean()
    mlow = df["lowC"].mean()
    print(f' Mean high temperature: {mhigh}')
    print(f' Mean low temperature: {mlow}')




def add_celsius(df):
    # TODO: add columns for temperatures converted to Celsius
    # TODO: return modified dataframe
    df["highC"] = (df["high"] - 32) * 5 / 9
    df["lowC"] = (df["low"] - 32) * 5 / 9
    return df


def clean_temperature_range(df, t_low_cut, t_high_cut):
    # TODO: remove days where T_low < t_low_cut or T_high > t_high_cut
    # TODO: return modified dataframe
    df = df[(df["lowC"] >= t_low_cut)]
    df = df[(df["highC"] <= t_high_cut)]

    return df


def plot_temperatures(df):
    # TODO: plot both high and low temperatures on the same graph
    plt.figure(figsize=(10, 5))

    plt.plot(df.index, df["high"], label="High Temperature")
    plt.plot(df.index, df["low"], label="Low Temperature")

    plt.xlabel("Day")
    plt.ylabel("Temperature (°F)")
    plt.title("Daily High and Low Temperatures")
    plt.legend()
    plt.grid(True)

    plt.show()


def main():

    filename = "../data/weather_june.csv"

    dataframe = load_weather_data(filename)


    dataframe = add_celsius(dataframe)

    T_low_cut = 19.0
    T_high_cut = 31.0
    dataframe = clean_temperature_range(dataframe, T_low_cut, T_high_cut)

    print_summary(dataframe)

    plot_temperatures(dataframe)

main()
