from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'  # Change this if you're using a different database
db = SQLAlchemy(app)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    diseases = db.relationship('Disease', backref='plant', lazy=True)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    stage = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('plant_selection'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/plant_selection')
def plant_selection():
    plants = Plant.query.all()
    return render_template('plant_selection.html', plants=plants)

@app.route('/disease_management/<int:plant_id>', methods=['GET'])
def disease_management(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    diseases = Disease.query.filter_by(plant_id=plant_id).all()
    return render_template('disease_management.html', plant=plant, diseases=diseases)

@app.route('/disease_info/<int:disease_id>', methods=['GET'])
def disease_info(disease_id):
    disease = Disease.query.get_or_404(disease_id)
    return render_template('disease_info.html', disease=disease)

if __name__ == '__main__':
    app.run(debug=True)
