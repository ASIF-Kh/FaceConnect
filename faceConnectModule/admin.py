from typing import Any, Callable, Optional, Sequence, Union
from django.db.models import Q
from django.contrib import admin
from django.http.request import HttpRequest
from faceConnect.models import UserIndividualImage, UserMultipleImage
from import_export.admin import ImportExportModelAdmin

admin.site.site_title = 'Admin Dashboard'
admin.site.site_header = "Backend App"
admin.site.index_title = "Welcome to the Dashboard"

# class UserProfileAdmin(ImportExportModelAdmin):
# 	list_display = ['user_id', 'mobile_number', 'user_email', 'gender']
# 	search_fields = ['id', 'mobile_number', 'user_email', 'gender']
# 	list_filter = ['gender']
# 	list_per_page = 20
# 	readonly_fields = ['id']

# 	def get_fields(self, request, obj):
# 		return ["id"]+super().get_fields(request, obj)

# 	def user_id(self, obj):
# 		return obj.user_id
	
# 	def user_email(self, obj):
# 		return obj.user.email

# 	user_id.admin_order_field = "user__id"

# class UserIndividualImageAdmin(ImportExportModelAdmin):
# 	list_display = ['user_profile__id', 'mobile_number', 'user_email', 'gender']
# 	search_fields = ['id', 'mobile_number', 'user_email', 'gender']
# 	list_filter = ['gender']
# 	list_per_page = 20
# 	readonly_fields = ['id']

# 	def get_fields(self, request, obj):
# 		return ["id"]+super().get_fields(request, obj)

# 	def user_id(self, obj):
# 		return obj.user_id
	
# 	def user_email(self, obj):
# 		return obj.user.email

# 	user_id.admin_order_field = "user__id"


# class UserMultipleImageAdmin(ImportExportModelAdmin):
# 	list_display = ['user_id', 'mobile_number', 'user_email', 'gender']
# 	search_fields = ['id', 'mobile_number', 'user_email', 'gender']
# 	list_filter = ['gender']
# 	list_per_page = 20
# 	readonly_fields = ['id']

# 	def get_fields(self, request, obj):
# 		return ["id"]+super().get_fields(request, obj)

# 	def user_id(self, obj):
# 		return obj.user_id
	
# 	def user_email(self, obj):
# 		return obj.user.email

# 	user_id.admin_order_field = "user__id"

admin.site.register(UserIndividualImage)
admin.site.register(UserMultipleImage)

