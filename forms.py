from flask.ext.wtf import Form
from wtforms.fields import IntegerField, SelectField
from wtforms.validators import NumberRange

class SearchForm(Form):
    #country_field = SelectField("Country Field", choices=[('ru', "Russia"), ('ua', "Ukraine"), ('bl', "Belarus"), ('kz', "Kazahstan"), default=('ru', "Russia"))
    #city_field = TextField("City"). [validators.required(), validators.length(max=30)])
    

    number_a_field = IntegerField('A number', validators = [NumberRange(min=999999, max=999999, message="n(A) >= 6 digits")])
    basic_field = SelectField("Basic Filed", choices=[('1', "="), ('2', ">"), ('3', ">"), ('4', ">="), ('5', "<=")], default=('1', "="))
    number_b_field = IntegerField('B number', validators = [NumberRange(min=-999999.999999, max=999999.999999, message="n(B) >= 6 digits")])
