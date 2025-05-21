
"""
Iris Dataset Analysis & Visualization
-------------------------------------
Loads the Iris dataset, performs exploratory analysis, computes summary
statistics, groups by species, and creates four basic matplotlib plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    # Load dataset
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
    df["date"] = pd.date_range(start="2024-01-01", periods=len(df), freq="D")

    # Exploration
    print(df.head())
    print("\nInfo:")
    df.info()
    print("\nMissing values:\n", df.isna().sum())
    print("\nSummary statistics:\n", df.describe())

    # Group means
    group_means = df.groupby("species").mean(numeric_only=True).round(2)
    print("\nMean measurements per species:\n", group_means)

    # --- Plots ---
    # Line chart
    plt.figure()
    plt.plot(df["date"], df["sepal length (cm)"])
    plt.title("Sepal Length Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sepal Length (cm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Bar chart
    plt.figure()
    plt.bar(group_means.index, group_means["petal length (cm)"])
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.tight_layout()
    plt.show()

    # Histogram
    plt.figure()
    plt.hist(df["sepal width (cm)"])
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Scatter plot
    plt.figure()
    for sp in df["species"].unique():
        subset = df[df["species"] == sp]
        plt.scatter(subset["sepal length (cm)"], subset["petal length (cm)"], label=sp)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
