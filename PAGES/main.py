from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Sending data from Python to HTML
    name = "Nimra"
    hobbies = ["Coding", "Sports", "Reading"]
    return render_template("home.html", username=name, user_hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)
