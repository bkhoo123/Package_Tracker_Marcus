from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from .map import map

tuple_map = list((k, tuple(v)) for k, v in map.items())
# print(tuple_map)
origination = list(k for k in map.keys())
placeholder_destination = ["Seattle"]

class ShippingForm(FlaskForm):
    sender_name = StringField("sender name", validators=[DataRequired()])
    recipient_name = StringField("recipient name", validators=[DataRequired()])
    origin = SelectField("Origin", choices=origination, validators=[DataRequired()])
    destination = SelectField("Destination", choices=placeholder_destination, validators=[DataRequired()])
    #! ^^ Check for this logic

    express_shipping = BooleanField("Express Shipping", validators=[DataRequired()])
    submit_button = SubmitField("Submit")
    cancel_button = SubmitField("Cancel")
