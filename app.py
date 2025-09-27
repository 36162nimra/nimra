# app.py
from flask import Flask, render_template, request, redirect, url_for
import os
from student_performance import load_data, compute_statistics, top_performers, subjects_needing_improvement, save_plots

app = Flask(__name__)

# Optional upload folder (keeps uploads separate if you want to save them)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    - GET: load the default CSV 'StudentsPerformance.csv' (must be in project root).
    - POST: accept a CSV file upload (form field 'file'); if provided, use it.
    Compute stats, save plots to static, and render index.html.
    """
    # Try to use uploaded file if POST and file provided
    if request.method == 'POST':
        uploaded = request.files.get('file')
        if uploaded and allowed_file(uploaded.filename):
            df = load_data(fileobj=uploaded)
        else:
            # fallback to default CSV on disk
            df = load_data(filepath='StudentsPerformance.csv')
    else:
        df = load_data(filepath='StudentsPerformance.csv')

    # Compute statistics
    mean, median, mode, std = compute_statistics(df)
    top_df = top_performers(df, subject='math score', n=5)
    top = top_df.to_dict(orient='records')  # list of dicts for template
    needs = subjects_needing_improvement(df)

    # Save plots and get filenames
    math_fname, mean_fname = save_plots(df, out_dir='static')

    return render_template(
        'index.html',
        mean=mean,
        median=median,
        mode=mode,
        std=std,
        top=top,
        needs=needs,
        math_img=math_fname,
        mean_img=mean_fname
    )

if __name__ == '__main__':
    # For development only. In production run with a WSGI server.
    app.run(debug=True)
