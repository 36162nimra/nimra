from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv("StudentsPerformance.csv")

    mean_scores = data.mean(numeric_only=True).to_dict()
    median_scores = data.median(numeric_only=True).to_dict()
    top_students = data.nlargest(5, "math score").to_dict(orient="records")

    # Save graph automatically
    if not os.path.exists("static"):
        os.makedirs("static")
    plt.figure(figsize=(8,5))
    plt.hist(data["math score"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Math Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.savefig("static/math_scores.png")
    plt.close()

    return render_template("index.html", 
                           mean=mean_scores, 
                           median=median_scores,
                           top=top_students)

if __name__ == '__main__':
    app.run(debug=True)
