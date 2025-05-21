# 🌸 Iris Dataset Analysis with Pandas & Matplotlib

This project performs data analysis and visualization on the famous **Iris Dataset** using Python, `pandas`, and `matplotlib`. It includes data exploration, basic statistics, error handling, and four types of visualizations.

---

## 📁 Project Structure

   ```text
   iris_analysis/
   │
   ├── venv/               # Virtual environment (excluded from version control)
   ├── iris.csv            # The dataset (can be loaded from sklearn or downloaded) (excluded from version control)
   ├── iris_analysis.py    # Python script with analysis and visualizations
   ├── get-pip.py          # Only used if pip is missing (excluded from version control)
   └── README.md           # Project instructions and documentation
   ```

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8 or higher (from [python.org](https://www.python.org/downloads/))
- VS Code with Python extension
- Git (for version control)

---

### ⚙️ Step 1: Set Up Virtual Environment

1. Open the project folder in VS Code.
2. Create the virtual environment:

   ```bash
   python -m venv venv
   ```

   If this fails due to ensurepip error, use:

   ```bash
   python -m venv venv --without-pip
   venv\Scripts\activate
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python get-pip.py
   ```

3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```

### 📦 Step 2: Install Required Packages

   ```bash
   pip install pandas matplotlib seaborn
   ```

## 📊 Dataset: Iris

A classic dataset used for classification and pattern recognition.

Consists of 150 samples of iris flowers with features like:

- Sepal length & width

- Petal length & width

- Species (Setosa, Versicolor, Virginica)
  
## 🧠 Features Implemented

### 📝 Task 1: Load and Explore Dataset

- Load data from CSV (or from sklearn.datasets.load_iris)

- Display first few rows using .head()

- Check data types and missing values

- Clean the data

### 📈 Task 2: Basic Data Analysis

- Compute statistics: mean, std, median

- Group by species and compute average petal/sepal lengths

### 📊 Task 3: Data Visualization

- Line Chart – Trend over samples

- Bar Chart – Average petal length per species

- Histogram – Distribution of sepal length

- Scatter Plot – Sepal vs. petal length

### Customizations

- Titles

- Labels

- Legends

- Color themes using seaborn

### 🧪 Error Handling

Gracefully handles:

- File not found errors

- Missing data

- Type errors in numeric operations

## 🚀 Running the Script

After activating the virtual environment:

   ```bash
   python iris_analysis.py
   ```

### 📸 Sample Output

- output.png (optional): Contains saved visualizations.

- Console: Displays summary statistics and success messages.

### 🗃️ Additional Notes

Dataset can be downloaded or imported directly using:

   ```bash
    from sklearn.datasets import load_iris
   ```

## ✅ Learning Outcomes

- File handling and error management in Python
- Data analysis using pandas
- Data visualization using matplotlib & seaborn
- Using virtual environments in VS Code

***Happy Analyzing! 🌸📊🐍***
