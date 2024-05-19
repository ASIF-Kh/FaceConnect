import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator
import numpy as np
import base64
import io


class BaseModelWithCreatedInfo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	index = models.PositiveBigIntegerField(default = 0)
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	# created_by = models.ForeignKey(User, models.SET_NULL, related_name="+", editable=False, blank=True, null=True, verbose_name=_('Created By'))

	class Meta:
		abstract = True
		ordering = ['created_at']

class UserInfoAbstract(BaseModelWithCreatedInfo):
	mobile_number = models.CharField(max_length=32, null=True, blank=True)
	class Meta:
		abstract = True


class UserInfoAbstractWithEmail(BaseModelWithCreatedInfo):
	name = models.CharField(max_length=64, null=True, blank=True)
	mobile_number = models.CharField(max_length=32, null=True, blank=True)
	email = models.CharField(max_length=256, blank=True, null=True)

	class Meta:
		abstract = True


def validate_file_extension(value):
	ext = value.name.split(".")[-1]
	allowed_extensions = ["jpg", "jpeg", "png"]
	if ext.lower() not in allowed_extensions:
		raise ValidationError("Only image files are allowed.")

class UserIndividualImage(UserInfoAbstractWithEmail):
	i_image = models.ImageField(upload_to='individual_face_images/') # validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_extension]
	numpy_array = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "User Individual Image"
		verbose_name_plural = "User Individual Images"

	def __str__(self):return self.i_image.name

	def set_numpy_array(self, encoding):
		buffer = io.BytesIO()
		np.save(buffer, encoding)
		self.numpy_array = base64.b64encode(buffer.getvalue()).decode('utf-8')

	def get_numpy_array(self):
		if self.numpy_array:
			encoded_data = base64.b64decode(self.numpy_array.encode('utf-8'))
			buffer = io.BytesIO(encoded_data)
			return np.load(buffer, allow_pickle=True)
		return None



class UserMultipleImage(UserInfoAbstractWithEmail):
	m_image = models.ImageField(upload_to='multiple_face_images/') # validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_extension]
	numpy_array = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "User Multiple Image"
		verbose_name_plural = "User Multiple Images"

	def __str__(self):return self.m_image.name

	def set_numpy_array(self, encoding):
		buffer = io.BytesIO()
		np.save(buffer, encoding)
		self.numpy_array = base64.b64encode(buffer.getvalue()).decode('utf-8')

	def get_numpy_array(self):
		if self.numpy_array:
			encoded_data = base64.b64decode(self.numpy_array.encode('utf-8'))
			buffer = io.BytesIO(encoded_data)
			return np.load(buffer, allow_pickle=True)
		return None
