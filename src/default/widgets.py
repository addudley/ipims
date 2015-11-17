from django.forms import ModelChoiceField
from django.utils.encoding import smart_text
class UserFullnameChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return smart_text(obj.get_full_name())