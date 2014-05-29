# -*- coding: utf-8 -*-
import vk_api
import json

# Auth data
login, password = '****', '******'

# Api for search requests to vkontakte
class VkontakteApi():
	'''Get info about users'''
	def get_users(self):
		items = ''
		vk = vk_api.VkApi(login, password) # Login to vk with AUTH DATA
		values = {'count': 5,  # Count of search result
			'fields': 'first_name, last_name', # Search results field filter
			'sex': '1', # Only Female show
			'status': '1', # And with no boyfrend :)
			'sort': '0'} # Popularity sort
		response = vk.method('users.search', values) # Make response
		dump = json.dumps(response) # Put into json dump
		#for items in response['items']['uid']:
			#items = str(items)
			#items = unicode(items, 'unicode-escape')
		#return items
		print unicode(dump, 'unicode-escape') # Into unicode
app = VkontakteApi()
app.get_users()
