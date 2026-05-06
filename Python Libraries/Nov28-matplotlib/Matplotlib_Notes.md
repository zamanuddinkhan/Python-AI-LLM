# Introduction to Matplotlib

## 1. Data Analysis & Visualization Libraries

### Numpy
- Numerical / data analysis library.

### Pandas
- Data analysis library.
- Supports basic visualization.

### Visualization Libraries
- Matplotlib
- Seaborn
- Plotly

---

## 2. Need for Data Visualization
- Data can be represented in text or graphic form.
- Helps in:
  - Easy comparison
  - Identifying relationships
  - Detecting symmetry/patterns
  - Quick analysis

---

## 3. Python Visualization Libraries
- Matplotlib
- Seaborn
- Plotly

---

## 4. Introduction to Matplotlib
- Most popular and oldest visualization library in Python.
- Python’s alternative to MATLAB.
- Open-source and free.
- Supports 2D & 3D plots.
- Can generate static, animated, interactive plots.
- Built on top of NumPy & SciPy.
- Created by John Hunter.
- Very large community support.

---

## 5. Installing Matplotlib

### Using Anaconda
```
conda install matplotlib
```

### Using pip
```
pip install matplotlib
```

---

## 6. Types of Plots in Matplotlib
1. Line Plots  
2. Bar Charts  
3. Pie Charts  
4. Histograms  
5. Scatter Plots  

---

## 7. Matplotlib Structure

### matplotlib
- Main package/library.

### pyplot
- Module containing plotting functions.

### Common Functions
| Function | Use |
|---------|-----|
| `plt.plot()` | Line plot |
| `plt.bar()` | Bar chart |
| `plt.pie()` | Pie chart |
| `plt.hist()` | Histogram |
| `plt.scatter()` | Scatter plot |

---

## 8. Line Plot Basics
- Plots data points and connects them with lines.
- Shows relationship between two datasets.
- Example datasets:
```
wickets = [1,2,3,4,5,6,7,8,9,10]
overs = [1,4,8,12,16,20]
```

---

## 9. Basic Code Example
```python
import matplotlib.pyplot as plt

plt.plot()      # Line plot
plt.bar()       # Bar chart
plt.pie()       # Pie chart
plt.hist()      # Histogram
plt.scatter()   # Scatter plot

help(plt.plot)
```
