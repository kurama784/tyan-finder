# -*- coding: utf-8 -*-
import vk_api
import json

login, password = 'kolabrod@gmail.com', 'afiftcent'

class VkontakteApi():
	def get_users(self):
		items = ''
		vk = vk_api.VkApi(login, password)
		values = {'count': 5, 
			'fields': 'first_name, last_name',
			'sex': '1',
			'status': '1',
			'sort': '0'}
		response = vk.method('users.search', values)
		dump = json.dumps(response)
		#for items in response['items']['uid']:
			#items = str(items)
			#items = unicode(items, 'unicode-escape')
		#return items
		print unicode(dump, 'unicode-escape')
app = VkontakteApi()
app.get_users()
