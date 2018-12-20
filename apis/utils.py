from rest_framework.authtoken.models import Token
import os
import random
import string


def user_detail(user):
	try:
		token = user.auth_token.key
	except:
		token = Token.objects.create(user=user)
		token = token.key
	else:
		if not token:
			token = Token.objects.create(user=user)
			token = token.key
	user_json = {
		'token': token,
		'username': user.username
	}
	return user_json


def generate_number(size=5):
	return ''.join([random.choice(string.digits) for _ in range(size)])
