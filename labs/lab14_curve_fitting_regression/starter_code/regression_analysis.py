import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.optimize import curve_fit


def load_data(filename):
    # load data in filename into pandas dataframe and return it
    df = pd.read_csv(filename)
    return df


def fit_polyfit(df):
    # fit a first order polynomial and return slope and intercept
    slope, intercept = np.polyfit(df["hours"], df["score"], 1)
    return slope, intercept


def fit_statsmodel(df):
    # carry out a linear regression fit and return the results object
    X = sm.add_constant(df["hours"])
    model = sm.OLS(df["score"], X).fit()
    return model


def fit_curve_fit(df):
    # fit a first order polynomial and return slope, intercept, dslope, dintercept
    popt, pcov = curve_fit(fitfunc, df["hours"], df["score"])

    slope_cf, intercept_cf = popt
    dslope_cf, dintercept_cf = np.sqrt(np.diag(pcov))

    return slope_cf, intercept_cf, dslope_cf, dintercept_cf


def predict(x, slope, intercept):
    # return y-values based on x, slope, intercept
    return slope * x + intercept


def fitfunc(x, slope, intercept):
    # linear fit function for use with curve_fit
    return slope * x + intercept


def main():

    # Get the file into a dataframe
    filename = "../data/study_scores.csv"
    df = load_data(filename)

    # calculate the slope and intercept of the best fit line
    slope, intercept = fit_polyfit(df)
    print("Best fit: y = {slope:.4f}x + {intercept:.4f}".format(
        slope=slope, intercept=intercept))
    print('-------------------------------------')

    # get the best fit line (as data for plotting)
    y_fit = predict(df['hours'], slope, intercept)

    # make the plot
    plt.figure()
    plt.plot(df['hours'], df['score'], 'o', label='Exam Score')
    plt.plot(df['hours'], y_fit, 'r-',
             label=f'Linear Fit - y = {slope:.4f}x + {intercept:.4f}')
    plt.title('Computer Science 250 Final Exam Score')
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.legend()
    plt.show()

    # Use statsmodels for comparison!
    results = fit_statsmodel(df)
    print(results.summary())
    print('---------------------------------------')

    # Now, use curve_fit for comparison to statsmodels errors
    slope_cf, intercept_cf, dslope_cf, dintercept_cf = fit_curve_fit(df)
    print(f"Curve Fit: y = ({slope_cf:.4f} +/- {dslope_cf:.3f})x + "
          f"({intercept_cf:.4f} +/- {dintercept_cf:.3f})")


main()