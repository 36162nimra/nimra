# student_performance.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# Which columns are considered "subjects" in this dataset
SUBJECT_COLS = ['math score', 'reading score', 'writing score']

def load_data(filepath=None, fileobj=None):
    """
    Load CSV into a pandas DataFrame.
    - If 'fileobj' is provided (e.g. Flask uploaded file), pandas can read it directly.
    - If 'filepath' is provided, read from disk.
    """
    if fileobj is not None:
        df = pd.read_csv(fileobj)
    elif filepath is not None:
        df = pd.read_csv(filepath)
    else:
        raise ValueError("Provide filepath or fileobj to load_data()")
    return df

def compute_statistics(df):
    """
    Compute mean, median, mode, and standard deviation for the subject columns.
    Returns four dictionaries (mean, median, mode, std) with subject -> value.
    """
    numeric = df[SUBJECT_COLS]
    mean = numeric.mean().to_dict()
    median = numeric.median().to_dict()
    # mode() can return multiple rows if multiple modes; pick the first row safely
    mode_df = numeric.mode()
    if not mode_df.empty:
        mode = mode_df.iloc[0].to_dict()
    else:
        mode = {k: None for k in SUBJECT_COLS}
    std = numeric.std().to_dict()
    return mean, median, mode, std

def top_performers(df, subject='math score', n=5):
    """
    Return the top-n students ordered by `subject`.
    Returns a DataFrame containing columns: gender, math score, reading score, writing score.
    """
    cols = ['gender'] + SUBJECT_COLS
    return df.nlargest(n, subject)[cols]

def subjects_needing_improvement(df):
    """
    Simple heuristic: find subjects whose mean is below the overall subject mean.
    Returns a dict subject -> mean (sorted ascending, lowest first).
    You can change the heuristic as needed (e.g. threshold).
    """
    mean = df[SUBJECT_COLS].mean()
    overall_mean = mean.mean()
    needs = mean[mean < overall_mean].sort_values()
    return needs.to_dict()

def save_plots(df, out_dir='static'):
    """
    Save two plots to the 'static' folder:
     - math_scores.png: histogram of math scores
     - mean_by_subject.png: bar chart of subject means
    Returns the filenames (not full paths): (math_fname, mean_fname)
    """
    os.makedirs(out_dir, exist_ok=True)

    # Histogram for math scores
    plt.figure(figsize=(8,5))
    plt.hist(df['math score'], bins=10, edgecolor='black')
    plt.title("Distribution of Math Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    math_fname = 'math_scores.png'
    plt.savefig(os.path.join(out_dir, math_fname), bbox_inches='tight')
    plt.close()

    # Bar chart for mean scores
    means = df[SUBJECT_COLS].mean()
    plt.figure(figsize=(6,4))
    means.plot(kind='bar')
    plt.title("Mean Score by Subject")
    plt.ylabel("Mean score")
    plt.ylim(0, 100)  # optional: keep y-axis consistent (assuming scores are 0-100)
    mean_fname = 'mean_by_subject.png'
    plt.savefig(os.path.join(out_dir, mean_fname), bbox_inches='tight')
    plt.close()

    return math_fname, mean_fname
