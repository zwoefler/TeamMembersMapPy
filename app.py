from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

colleagues = []

@app.route('/add_colleague', methods=['POST'])
def add_colleague():
    colleagues.append(request.json)
    return "Added Colleague to Dataset"


@app.route('/map', methods=['GET'])
def show_map():
    return render_template('map.html')


if __name__ == "__main__":
    app.run()
