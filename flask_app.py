from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


workouts = []

@app.route("/")
def home():
    return render_template("index.html", workouts=workouts)

@app.route("/add", methods=["POST"])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")
    if workout and duration and duration.isdigit():
        workouts.append({"workout": workout, "duration": int(duration)})
    return redirect(url_for("home"))

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
