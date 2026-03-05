from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Your original prime-checking function
def isPrime(n):
    for i in range(1, n):
        if n % i == 0:
            if i == 1:
                i = i
            else:
                return False
    return True

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            x = int(request.form["number"])  # Get number from user

            if isPrime(x):
                result = str(x) + " is a prime"
            else:
                result = str(x) + " is not a prime"

        except:
            result = "Please enter a valid positive integer"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render assigns PORT automatically
    app.run(host="0.0.0.0", port=port)
