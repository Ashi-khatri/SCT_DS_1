import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("population_data.csv")

plt.figure(figsize=(8, 5))
plt.hist(data["Age"], bins=8, edgecolor="black")
plt.title("Age Distribution of Population")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x="Gender", data=data)
plt.title("Gender Distribution of Population")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
