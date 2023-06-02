from flask import Flask, render_template, request

app = Flask(__name__)

cities = ["Flensburg", "Nürnberg"]

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form["name"]
        city = request.form["city"]

    return render_template("index.html")


@app.route('/search_cities')
def search_cities():
    user_input = request.args.get('q')
    # Perform the Nominatim API request here and extract city names
    cities = ['City 1', 'City 2', 'City 3']  # Replace with your logic

    return render_template('city_dropdown.html', cities=cities)


if __name__ == "__main__":
    app.run()
