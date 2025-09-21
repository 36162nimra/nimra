# student_performance.py
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = pd.read_csv("StudentsPerformance.csv")

# Step 2: Basic statistics
print("\n--- Overall Statistics ---")
print("Mean Scores:\n", data.mean(numeric_only=True))
print("Median Scores:\n", data.median(numeric_only=True))
print("Mode Scores:\n", data.mode().iloc[0])
print("Standard Deviation:\n", data.std(numeric_only=True))

# Step 3: Top performers
top_students = data.nlargest(5, "math score")
print("\n--- Top Performers (Math) ---")
print(top_students[["gender", "math score", "reading score", "writing score"]])

# Step 4: Visualization
plt.figure(figsize=(8,5))
plt.hist(data["math score"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Math Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.savefig("math_scores.png")
plt.show()
