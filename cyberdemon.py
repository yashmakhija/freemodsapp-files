import os
import json
import re
from telethon import *
import requests

try:
    from telethon import *
    import requests
except ImportError as e:
    raise ImportError("Required packages not found. Please install them manually.") from e

path = str(os.getcwd()) + '/'

def uploader(p, FILE_NAME=""):
    SESSION = requests.session()
    
    if not FILE_NAME:
        FILE_NAME = os.listdir(path + "file/")[0]

    print(FILE_NAME)
    print("Main Dir: "+str(os.listdir(path)))
    print("File Dir: "+str(os.listdir(path + "file/")))

    LOGIN_URL = 'https://zeus.protondns.net:2083/login/?login_only=1'
    LOGIN_HEADERS = {
        'Host': 'zeus.protondns.net:2083',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-type': 'application/x-www-form-urlencoded',
        'Content-Length': '48',
        'Origin': 'https://zeus.protondns.net:2083',
        'Connection': 'keep-alive',
        'Referer': 'https://zeus.protondns.net:2083/',
    }
    LOGIN_DATA = {
        'user': "freemods",
        'pass': "Zy3T[urb2K2q",
        'goto_uri': "/",
    }
    LOGIN_REQUEST = SESSION.post(
        url=LOGIN_URL, headers=LOGIN_HEADERS, data=LOGIN_DATA)
    LOGIN_RESPONSE = json.loads(LOGIN_REQUEST.text)
    LOGIN_SECURITY_TOKEN = LOGIN_RESPONSE['security_token']

    LIST_FILES_URL = 'https://zeus.protondns.net:2083/' + \
        LOGIN_SECURITY_TOKEN + '/execute/Fileman/list_files'
    LIST_FILES_HEADERS = {
        'Host': 'zeus.protondns.net:2083',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '98',
        'Origin': 'https://zeus.protondns.net:2083',
        'Connection': 'keep-alive',
        'Referer': 'https://zeus.protondns.net:2083/' + LOGIN_SECURITY_TOKEN + '/frontend/paper_lantern/filemanager/upload-ajax.html?file=&fileop=&dir=%2Fhome%2Ffreemods%2Fpublic_html%2Fdownload&dirop=&charset=&file_charset=&baseurl=&basedir='
    }
    LIST_FILES_DATA = {
        'dir': "/home/freemods/public_html/download",
        'limit_to_list': "1",
        'show_hidden': "1",
        'filepath-0': FILE_NAME
    }
    LIST_FILES_REQUEST = SESSION.post(
        url=LIST_FILES_URL, headers=LIST_FILES_HEADERS, data=LIST_FILES_DATA)

    UPLOAD_FILES_URL = 'https://zeus.protondns.net:2083/' + \
        LOGIN_SECURITY_TOKEN + '/execute/Fileman/upload_files'
    UPLOAD_FILES_HEADERS = {
        'Host': 'zeus.protondns.net:2083',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'multipart/form-data; boundary=---------------------------295557168017077988773696000954',
        'Content-Length': '1191',
        'Origin': 'https://zeus.protondns.net:2083',
        'Connection': 'keep-alive',
        'Referer': 'https://zeus.protondns.net:2083/' + LOGIN_SECURITY_TOKEN + '/frontend/paper_lantern/filemanager/upload-ajax.html?file=&fileop=&dir=%2Fhome%2Ffreemods%2Fpublic_html%2Fdownload&dirop=&charset=&file_charset=&baseurl=&basedir='
    }
    #FILE_NAME = FILE_NAME[1::]
    UPLOAD_FILES_FILE = {'upload_file': open(p, 'rb')}
    UPLOAD_FILES_REQUEST = SESSION.post(
        url=UPLOAD_FILES_URL, headers=UPLOAD_FILES_HEADERS, files=UPLOAD_FILES_FILE)

    MOVE_FILES_URL = 'https://zeus.protondns.net:2083/' + \
        LOGIN_SECURITY_TOKEN + '/json-api/cpanel'
    MOVE_FILES_HEADERS = {
        'Host': 'zeus.protondns.net:2083',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '263',
        'Origin': 'https://zeus.protondns.net:2083',
        'Connection': 'keep-alive',
        'Referer': 'https://zeus.protondns.net:2083/' + LOGIN_SECURITY_TOKEN + '/frontend/paper_lantern/filemanager/index.html'
    }
    MOVE_FILES_DATA = {
        'cpanel_jsonapi_module': "Fileman",
        'cpanel_jsonapi_func': "fileop",
        'cpanel_jsonapi_apiversion': "2",
        'filelist': "1",
        'multiform': "1",
        'doubledecode': "0",
        'op': "move",
        'metadata': "[object HTMLTableRowElement]",
        'sourcefiles': "/home/freemods/" + FILE_NAME,
        'destfiles': "/home/freemods/public_html/download"
    }
    MOVE_FILES_REQUEST = SESSION.post(
        url=MOVE_FILES_URL, headers=MOVE_FILES_HEADERS, data=MOVE_FILES_DATA)
    
    print(FILE_NAME)
    LINK = 'https://freemodsapp-files.xyz/download/' + FILE_NAME

    # Close the file before removing it
    UPLOAD_FILES_FILE['upload_file'].close()
    os.remove(p)

    return LINK

api_id = '1813732'
api_hash = 'd5f978c1b3693624b16a7d18a62ea0e8'
bot_token = '5189239040:AAHj0sAJGbTgOqhtmoEZIaQMGckKWNGoSIo'

sudo = [5084804807, 903563890]
approved_useers = [int(i) for i in sudo] + [int(i) for i in os.listdir(path + 'approved/')]

client = TelegramClient('Tangent', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def my_event_handler(event):
    try:
        sender = str(event.peer_id.user_id)
    except:
        sender = str(event.from_id.user_id)

    if int(sender) not in approved_useers:
        await event.reply("You don't have access")
        return

    if str(event.raw_text) == "/start":
        await event.reply("ok")

    if (int(event.peer_id.user_id) in sudo) and (('/approve' in str(event.raw_text)) or ('/disapprove' in str(event.raw_text))):
        if '/approve ' in str(event.raw_text):
            raw = str(event.raw_text).replace('/approve ', '')
            user = int(raw)
            approved_useers.append(user)
            writer = open(path + 'approved/' + raw, 'w')
            writer.close()
            await event.reply('Sudo user added successfully.')

        elif '/disapprove ' in str(event.raw_text):
            raw = str(event.raw_text).replace('/disapprove ', '')
            user = int(raw)
            approved_useers.remove(user)
            os.remove(path + 'approved/' + raw)
            await event.reply('Sudo user added successfully.')

    else:
        if event.media is None:
            await client.send_message(int(sender), 'You had not sent a file')
        else:
            name1 = str(event.file.name)
            name2 = "_".join(name1.split())
            name = re.sub(r"[\([{})\]]", "", name2)
            message = await event.reply("Processing please wait...")
            await message.edit("0%")

            async def progress_callback(current, total):
                percent = round(current / total * 100, 2)
                await message.edit(f"{percent}%")

            sed = await event.download_media("./" + name, progress_callback=progress_callback)
            link = uploader(sed, name)
            await message.edit(link)

print("ok")
client.run_until_disconnected()