from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired

class SearchStationForm(Form):
	searchstation = StringField('searchstation', validators=[DataRequired()])