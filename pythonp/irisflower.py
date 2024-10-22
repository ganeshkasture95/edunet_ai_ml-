import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("iris.csv")

sns.set(style="whitegrid")


sns.pairplot(data, hue='species')
plt.title("Pair Plot of Iris Dataset")
plt.show()


data.hist(figsize=(10, 8), bins=20)
plt.suptitle("Histograms of Features in Iris Dataset")
plt.show()


plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='sepal_length', data=data)
plt.title("Violin Plot of Sepal Length by Species")
plt.show()


# plt.figure(figsize=(10, 8))
# correlation = data.corr()
# sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Heatmap of Correlation Matrix")
# plt.show()



plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='petal_length', data=data)
plt.title("Box Plot of Petal Length by Species")
plt.show()

