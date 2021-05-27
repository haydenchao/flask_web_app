from flask import Flask, render_template
from helper import pets, comments_list
from form import CommentForm
from datetime import date

app = Flask(__name__)
## must be set in order to enable CSRF protection
app.config["SECRET_KEY"] = "secret_string"

@app.route('/')
def index():
  return render_template('index.html', template_pets=pets.keys())

@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_dict = pets[pet_type]
  pet_name = []
  return render_template("animals.html", template_pet_type=pet_type, template_pets=pet_dict)


@app.route('/animals/<pet_type>/<int:pet_id>', methods=['GET','POST'])
def pet(pet_type, pet_id):
  form = CommentForm(csrf_enabled=False)
  today = date.today()
  if form.validate_on_submit():
      new_comment = form.comment.data
      comments_list[pet_type].append(new_comment)


  pet = pets[pet_type][pet_id]['name']
  image = pets[pet_type][pet_id]['url']
  desc = pets[pet_type][pet_id]['description']
  age = pets[pet_type][pet_id]['age']
  breed = pets[pet_type][pet_id]['breed']
  return render_template('pet.html', template_pet=pet, template_image=image,template_desc=desc,
  template_breed=breed, template_age=age, template_form=form, 
  template_comment=comments_list[pet_type], template_date=today)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
