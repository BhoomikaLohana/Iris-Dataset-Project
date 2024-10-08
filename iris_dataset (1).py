# -*- coding: utf-8 -*-
"""IRIS Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17_jbObeP5tq7pv5Z-3hDNjVA3Qh77gI5

## AI Python for Beginners Project 1

### **1. Setting Up the Environment**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')
# %matplotlib inline

"""###**2. Loading the Dataset**"""

Data=pd.read_csv("/content/Iris.csv")
Data.head()

"""###**3. Data Structure Information**"""

Data.info()

"""### **4. Check for Missing Values**"""

Data.isnull().sum()

"""### **5. Statistical Summary**

"""

Data.describe()



"""## **6. Data Cleaning**

### **Handle Missing Values**
"""

Data.dropna(inplace=True)

"""### **7. Data Types Verification**"""

Data.dtypes

"""## **8. Performing Data Analysis**"""

# Distribytion of Sepal length
plt.figure(figsize=(6,6))
plt.hist(Data['SepalLengthCm'],bins=10,color="lightgreen",edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Frequency")
plt.show()

"""### **Analyzing Relationships Between Variables**

#### **Sepal Length vs. Petal Length**
"""

#Box plot
plt.figure(figsize=(6,4))
plt.scatter(Data["SepalLengthCm"],Data["PetalLengthCm"],c="lightgreen")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length cm")
plt.ylabel("Petal Length cm")
plt.show()

"""### **Grouping and Aggregation**

#### **Mean Measurements by Species**
"""

Data.groupby("Species").mean()



#Bar plot
plt.figure(figsize=(6,4))
Data.groupby("Species")['SepalLengthCm'].mean().plot(kind='bar',color=['skyblue','lightgreen','lightpink'],edgecolor='black')
plt.title('Mean Sepal Length by Species')
plt.xlabel('Species')
plt.xticks(rotation=45)
plt.ylabel('Mean Sepal Length')
plt.show()

# Box plot for petal length by species
plt.figure(figsize=(6,4))
sns.boxplot(x='Species', y='PetalLengthCm',hue='Species',palette='pastel',data=Data)
plt.title('Box Plot of Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')

plt.show()

# Pair plot of all variables colored by species
plt.figure(figsize=(6,4))
sns.pairplot(Data, hue='Species')
plt.show()

#Corelation Heatmap
plt.figure(figsize=(5,4))
Numeric_df=Data.select_dtypes(include='number')
corr=Numeric_df.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', style= 'Species',hue='Species', data=Data, s=50)
plt.title('Sepal Length vs Petal Length by Species', fontsize=16)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Petal Length (cm)', fontsize=12)
plt.legend(title='Species')
plt.show()

"""## **Conclusion**

The objective of this analysis was to explore the iris dataset using python to understand the relationship between features and classify the different species of iris.
Our analysis revealed several key insights:


*   A positive correlation was observed between Sepal Length and Petal Length, with both features increasing together across the dataset.
*   Iris-Virginica had the highest mean Sepal Length, followed by Iris-Versicolor, and Iris-Setosa had the smallest mean Sepal Length.

*   The box plot analysis of Petal Length showed varying outliers:

       Iris-Virginica had no outliers.
       Iris-Versicolor had one outlier below the minimum.
       Iris-Setosa had three outliers below the minimum and one outlier above the maximum.
*   The correlation analysis found a weak negative relationship between Sepal Width and Sepal Length, a moderate negative relationship between Sepal Length and Petal Length, and strong positive relationships between Petal Length and Sepal Length, as well as between Petal Width and Sepal Length. Additionally, Sepal Width and Petal Width had a moderate negative correlation, while Petal Length and Petal Width showed almost no correlation.


* Overall, this project demonstrates how data analysis and visualization techniques can be used to gain valuable insights from the Iris dataset.
"""