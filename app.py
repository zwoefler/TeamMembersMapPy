from flask import Flask, render_template, request, redirect
from geopy.geocoders import Nominatim
import uuid
import json

app = Flask(__name__)

colleagues = []
geolocator = Nominatim(user_agent="colleague_map")
colleagues_file = "colleagues.json"

@app.route('/', methods=['GET'])
def index():
    colleagues = load_colleagues_from_file()
    return render_template('index.html', colleagues=colleagues)

@app.route("/add_colleague", methods=["POST"])
def add_colleague_via_html():
    name = request.form['name']
    city = request.form['city']
    add_colleague(name, city)
    return redirect("/")


@app.route('/delete/<colleague_id>')
def delete_colleague(colleague_id):
    delete_colleague_by_name(colleague_id)
    return redirect('/')


def add_colleague(name, city):
    location = geolocator.geocode(city)
    colleague_id = generate_colleague_id()
    if location is not None:
        colleague = {'name': name, 'city': city, 'lat': location.latitude, 'lon': location.longitude, 'colleague_id': colleague_id}
        colleagues.append(colleague)
    save_colleagues_to_file(colleagues)


def generate_colleague_id():
    colleague_id = uuid.uuid4()
    colleague_id_str = str(colleague_id)
    return colleague_id_str


def delete_colleague_by_name(colleague_id):
    for colleague in colleagues:
        if colleague['colleague_id'] == colleague_id:
            colleagues.remove(colleague)
            save_colleagues_to_file(colleagues)
            break


def save_colleagues_to_file(colleagues):
    with open(colleagues_file, 'w') as file:
        json.dump(colleagues, file)

def load_colleagues_from_file():
    try:
        with open(colleagues_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    app.run()
