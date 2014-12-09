# -*- coding: utf-8 -*-
import Image
import sys

from facepy import GraphAPI
from facepy.exceptions import OAuthError

"""
Depends on:
* facepy
* PIL
"""

def fb_validate_token(token):
	graph = GraphAPI(token)
	try:
		graph.get('me')
	except OAuthError:
		return False

	return True

def fb_get_profile_pic(token):
	if fb_validate_token(token):
		graph = GraphAPI(token)
		try:
			picture = graph.get('me/picture?redirect=false&type=large')
			return picture['data']['url']
		except OAuthError:
			print 'oautherror'

		return None

if __name__ == "__main__":
	token = ''
	for arg in sys.argv:
		token = arg
		break

	url = fb_get_profile_pic(token)
	if url:
		# download(url, "avatar.png")
		profile = Image.open("avatar.png")
		sticker = Image.open("sticker.png")
		profile.paste(sticker, (0, 0), sticker)
		profile.show()
