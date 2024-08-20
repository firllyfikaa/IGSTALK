import instaloader,sys
from os import system, name
import time
from time import sleep
from pyfiglet import Figlet
import colorama


from instaloader import Instaloader
#sys clear
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
clear()

colorama.init()
f = Figlet(font='big')
print(colorama.Fore.GREEN + f.renderText('IG ‎  STALK'))
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
    
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mBY: Firlly | Tiktok: @firlyfikaa\033[1;33m • \033[0m\033[1;30m]══════════════>")



x = Instaloader()

try:
	uname = input("\033[37mEnter a username \033[0m: \033[32m")
	print('\033[37m‎══════════════════════════════════════════')
	if uname == "":
		print("\033[33mUnknown command!")
		sys.exit()

	f = instaloader.Profile.from_username(x.context,uname)

	print("\033[32m📌Username\033[0m :", f.username)
	print("\033[32m🔖ID\033[0m :", f.userid)
	print("\033[32m🏷️Nama lengkap\033[0m :", f.full_name)
	print("\033[32m💌Biografi\033[0m :", f.biography)
	print("\033[32m📫Nama kategori bisnis\033[0m :", f.business_category_name)
	print("\033[32m🔍Diikuti orang\033[0m :", f.followed_by_viewer)
	print("\033[32m👤Mengikuti\033[0m :", f.followees)
	print("\033[32m👥Pengikut\033[0m :", f.followers)
	print("\033[32m👥Mengikuti orang\033[0m :", f.follows_viewer)
	print("\033[32m🚫Diblokir orang\033[0m :", f.blocked_by_viewer)
	print("\033[32m🚷Pernah memblokir orang\033[0m :", f.has_blocked_viewer)
	print("\033[32m💡Punya sorotan\033[0m :", f.has_highlight_reels)
	print("\033[32m📝Punya cerita publik\033[0m :", f.has_public_story)
	print("\033[32m🔎Telah meminta orang\033[0m :", f.has_requested_viewer)
	print("\033[32m📢Diminta orang\033[0m :", f.requested_by_viewer)
	print("\033[32m📣Memiliki cerita yang dapat dilihat\033[0m :", f.has_viewable_story)
	print("\033[32m🌐Akun bisnis\033[0m :", f.is_business_account)
	print("\033[32m👤Akun pribadi\033[0m :", f.is_private)
	print("\033[32m✅Diverifikasi\033[0m :", f.is_verified)
	print("\033[32m📱Postingan\033[0m :", f.mediacount)
	print("\033[32m🗺️URL foto profil\033[0m :", f.profile_pic_url)

except KeyboardInterrupt:
	print("\033[37mI understand!")

except EOFError:
	print("\033[37mWhy?")
