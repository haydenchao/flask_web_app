from flask import Flask, render_template
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', template_pets=pets.keys())

@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_dict = pets[pet_type]
  pet_name = []
  return render_template("animals.html", template_pet_type=pet_type, template_pets=pet_dict)


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]['name']
  image = pets[pet_type][pet_id]['url']
  desc = pets[pet_type][pet_id]['description']
  age = pets[pet_type][pet_id]['age']
  breed = pets[pet_type][pet_id]['breed']
  return render_template('pet.html', template_pet=pet, template_image=image,template_desc=desc, template_breed=breed, template_age=age)


@app.route('/about')
def about():
    return """ <h1> Welcome to the 'About Me' page </h1>
    <img src="https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/147453034-pit-bull-myths-reality-632x475.jpg" width="200" height="150"/>
    <p> We are a little shop that take cares of a lot of pets </p>
    <p> The first few days in your home are special and critical for a pet. Read these tips about making it as smooth of a transition as possible.</p>
    <a href="/">Return to Home Page</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
