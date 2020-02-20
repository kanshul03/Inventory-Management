from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SubmitField
from wtforms.validators import DataRequired,NumberRange



class addproduct(FlaskForm):
    prodname = StringField('Product Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=10000),DataRequired()])
    prodprice = FloatField('Price', validators=[NumberRange(min=1, max=10000), DataRequired()])
    prodsubmit = SubmitField('Save Changes')

class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    editprice = FloatField('Price', validators=[NumberRange(min=1, max=10000),DataRequired()])
    editsubmit = SubmitField('Save Changes')
