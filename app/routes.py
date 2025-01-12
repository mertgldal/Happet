from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from .models import User, Animal
from .forms import RegisterForm, LoginForm, GivePet, EmergencyAnimals
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)


@main.route('/')
def index():
    animals = Animal.query.limit(5).all()
    return render_template('index.html', animals=animals)


@main.route('/adopt')
def adopt():
    animal_type = request.args.get('type', '')
    gender = request.args.get('gender', '')
    color = request.args.get('color', '')
    age = request.args.get('age', '')
    page = request.args.get('page', 1, type=int)

    animals_query = db.session.query(Animal)
    if animal_type:
        animals_query = animals_query.filter(Animal.animal_type == animal_type)
    if gender:
        animals_query = animals_query.filter(Animal.animal_gender == gender)
    if color:
        animals_query = animals_query.filter(Animal.animal_color == color)
    if age:
        animals_query = animals_query.filter(Animal.animal_age == age)

    animals_paginated = animals_query.paginate(page=page, per_page=9, error_out=False)
    animals = animals_paginated.items

    return render_template('adopt.html', animals=animals, pagination=animals_paginated)

@main.route('/pet_page/<int:animal_id>')
@login_required
def pet_page(animal_id):
    animal = db.get_or_404(Animal, animal_id)
    return render_template('petpage.html', animal=animal)

@main.route('/rehome', methods=['GET', 'POST'])
@login_required
def rehome():
    form = GivePet()
    if form.validate_on_submit():
        new_pet = Animal(
            user_id=current_user.id,
            animal_name=form.animal_name.data,
            animal_type=form.animal_type.data,
            animal_gender=form.animal_gender.data,
            animal_age=form.animal_age.data,
            animal_color=form.animal_color.data,
            history=form.history.data,
            character=form.character.data,
            behavioral_features=form.behavioral_features.data,
            preferences=form.preferences.data,
            image_url=form.image_url.data,
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('main.pet_page', animal_id=new_pet.id))
    return render_template('rehome.html', form=form)

@main.route('/temporary-care', methods=['GET', 'POST'])
@login_required
def temporary_care():
    form = EmergencyAnimals()
    if form.validate_on_submit():
        temporary_pet = Animal(
            user_id=current_user.id,
            animal_name=form.animal_name.data,
            animal_type=form.animal_type.data,
            animal_gender=form.animal_gender.data,
            animal_age=form.animal_age.data,
            animal_color=form.animal_color.data,
            history=form.history.data,
            character=form.character.data,
            behavioral_features=form.behavioral_features.data,
            preferences=form.preferences.data,
            image_url=form.image_url.data,
            date_from=form.date_from.data,
            date_to=form.date_to.data,
        )
        db.session.add(temporary_pet)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('temporary_care.html', form=form)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = db.get_or_404(User, user_id)
    return render_template('profile.html', user=user)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered!", "danger")
        else:
            user = User(
                username=form.username.data,
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash("Invalid credentials", "danger")
    return render_template('login.html', form=form)
