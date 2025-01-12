from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, TextAreaField, SubmitField, EmailField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[DataRequired(), Length(min=2, max=20)],
        render_kw={"placeholder": "Username"},
    )

    name = StringField(
        label="Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Name"},
    )

    surname = StringField(
        label="Surname",
        validators=[DataRequired()],
        render_kw={"placeholder": "Surname"},
    )

    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20, message="Password must be at least 8 characters long"),
        ],
        render_kw={"placeholder": "Password"},
    )

    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match",
            ),
        ],
        render_kw={"placeholder": "Confirm Password"},
    )
    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"},
    )
    submit = SubmitField(label="Log In")


class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        label="Current Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20, message="Password must be at least 8 characters long"),
            EqualTo(
                "new_password_confirmation",
                message="Passwords must match",
            ),
        ],
        render_kw={"placeholder": "Current Password"},
    )

    new_password_confirmation = PasswordField(
        label="Password Confirmation",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password Confirmation"},
    )
    submit = SubmitField(label="Change Password")


class GivePet(FlaskForm):
    animal_name = StringField(
        label="Animal Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Animal Name"},
    )
    animal_type = SelectField(
        label='Animal Type', default=None, choices=[('Dog', 'Dog'), ('Cat', 'Cat')], coerce=str,
        validators=[DataRequired()],
    )
    animal_gender = SelectField(
        label='Gender', default=None, choices=[('Male', 'Male'), ('Female', 'Female')], coerce=str,
        validators=[DataRequired()],
    )
    animal_age = StringField(
        label="Age",
        validators=[DataRequired()],
        render_kw={"placeholder": "Age(Month)"},
    )
    animal_color = SelectField(
        label='Color', default=None, choices=[('Black', 'Black'), ('White', 'White'), ('Brown', 'Brown'),
                                              ('Grey', 'Grey'), ('Beige', 'Beige'), ('Other', 'Other')], coerce=str,
        validators=[DataRequired()],
    )
    history = TextAreaField(
        label="A brief history of pet",
        validators=[DataRequired()],
        render_kw={"placeholder": "A brief history of pet"},
    )
    character = StringField(
        label="Characteristics",
        validators=[DataRequired()],
        render_kw={"placeholder": "Characteristics"},
    )
    behavioral_features = StringField(
        label="Behavioral Features",
        validators=[DataRequired()],
        render_kw={"placeholder": "Behavioral Features"},
    )
    preferences = StringField(
        label="Preferences",
        validators=[DataRequired()],
        render_kw={"placeholder": "Preferences"},
    )
    image_url = StringField(
        label="Image URL",
        validators=[DataRequired()],
        render_kw={"placeholder": "Image URL"},
    )

    submit = SubmitField(label="Submit")


class EmergencyAnimals(GivePet):
    date_from = DateField(
        label="Date From",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD"},
    )
    date_to = DateField(
        label="Date To",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD"},
    )

    submit = SubmitField(label="Submit")

    # Custom validation method
    @staticmethod
    def validate_date_to(form, field):
        if form.date_from.data and field.data:
            if form.date_from.data >= field.data:
                raise ValidationError("Date From must be earlier than Date To.")
