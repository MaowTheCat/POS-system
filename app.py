from flask import Flask, render_template
import os

app = Flask(__name__)

ORDER_FOLDER = r"Your Drive\order logs" # Make sure to change before /order_logs.txt wiht the file path of your order log folder


@app.route("/")
def home():
    orders = []

    for filename in os.listdir(ORDER_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(ORDER_FOLDER, filename)

            with open(path, "r") as file:
                contents = file.read()

            orders.append({
                "name": filename,
                "contents": contents
            })

    return render_template("index.html", orders=orders)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)