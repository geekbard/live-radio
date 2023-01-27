# import required library's
from os import system as cmd

librarys = ['python-vlc' , 'pygame' , 'multiprocessing' , 'time' , 'platform']
for library in librarys:
	try:
		exec(f'import {library}')
	except:
		cmd(f'pip3 install {library}')
		try:
			exec(f'import {library}')
		except:
			exec(f'import vlc')
# default url's
radio_javan = "http://74.115.215.36/"
radio_faaz = "http://www.radiofaaz.com:8000/radiofaaz"

# find platform
if 'Linux' in platform.system():
	ccmd = 'clear'
elif 'Windows' in platform.system():
	ccmd = 'cls'

cmd(ccmd
)
# select radio
print ( "Please select or enter an url to play. Default url's ~> [1]: Radio Javan , [2]: Radio Faaz" )
url = input( "~> " )

if url == '1':
	url = radio_javan
elif url == '2':
	url = radio_faaz
else:
	print("You selected custom radio.")

# play music
def play():
	instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
	player=instance.media_player_new()
	media=instance.media_new(url)
	player.set_media(media)
	player.play()

play()
	
if url == radio_javan:
	print("Enjoy listening to radio javan!!.")
elif url == radio_faaz:
	print("Enjoy listening to radio faaz!!.")
else:
	print("Enjoy listening to your radio!!.")
# loop playing
while True:
	pass
