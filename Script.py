class script(object):
    START_TXT = """ Hส๐๐ป {}\t
Mส Nแดแดแด Is  <a href=https://t.me/{}>{}</a>  ,I Cแดษด Pสแดแด ษชแดแด Mแดแด ษชแดs, Jแดsแด Jแดษชษด แดแดส ษขสแดแดแด\n
แดแดษชษดแดแดษชษดษชษดษข : <a href=https://t.me/uzx_bots>Uแดข๐ สแดแดs</a>"""
    HELP_TXT = """๐ท๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐"""
    ABOUT_TXT = """
โข>Coded By: <a href=https://t.me/illuzX3>๐๐ฅ๐ฅ๐ฎ๐ณ๐</a>
โข>L๐ธB๐๐ฐ๐Y: ๐ฟY๐๐พG๐A๐ผ 2.0.35
โข>L๐ฐN๐ถ๐A๐ถE: ๐ฟY๐๐ทร๐ฝ 3+
โข>D๐ฐ๐AB๐ฐS๐ด: M๐พ๐ฝG๐พ D๐ฑ
โข>H๐พS๐S๐ดR๐๐ดR: HแดRแดแดแด / Vแดs
โข>Bแดsแด Rแดแดแด : <a href=https://github.com/EvamariaTG>Eแด แด Mแดสษชแด</a>
โข>Bแดษชสแด Sแดแดแดแดs :> 1.0.-A</a>
"""
    OWN_BOT_TXT = """ <b>How I Own This Bot ? </b>
    
- add this bot as a admin in you're group 
- after you need to send this command in youre group /connect"""
    SETTINGS_CMD = """<b>settings:</b>
- use /settings command in bot pm !
- configure bot in you're group how want to perform 
- if no need imdb filter picture then turn off it !
- double button filter button no more works ! 
- this settings module rest every day so note it"""


    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particularkeyword and
  meenu will respond whenever a keywordfound the message

<b>NOTE:</b>
1. meenu should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    DIMR = """
โ ๏ธ๐ฟ๐๐๐พ๐๐ผ๐๐๐๐
๐ฐ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐. ๐๐ ๐๐๐'๐ ๐๐ ๐ ๐๐๐ข ๐๐ ๐๐๐ ๐ผ๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐.
๐ธ๐ ๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐ ๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐ข ๐๐๐๐๐๐๐ ๐๐๐๐๐, ๐ฟ๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐, ๐ ๐ ๐๐๐ ๐๐๐๐๐ข ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐ ๐ ๐๐๐!
๐ฐ๐๐๐๐ ๐ธ๐ ๐ฝ๐๐ ๐๐๐๐๐๐๐๐๐๐๐ ๐ต๐๐ ๐๐๐ข ๐ณ๐๐๐๐๐ & ๐๐๐๐๐๐๐๐ ๐ฟ๐๐๐๐๐ ๐๐๐๐"""


    BUTTON_TXT = """Help: <b>Buttons</b>

- Meenu Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/meow_pm_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of meenu
<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โญโโ
โ<b>โCแดแดษดแด แดา Fษชสแดs</b>: <code>{}</code>
โ<b>โTแดTแดส Usแดสs</b>: <code>{}</code>
โ<b>โTแดTแดส Gสแดแดแดs</b>: <code>{}</code>
โ<b>โUsแดแด Sแดแดสแดษขแด</b>: <code>{}</code>
โ<b>โAแด แดษชสแดสสแด Sแดแดแดแด</b>: <code>{}</code>
โฐโโโโ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#newuserfound
ID - <code>{}</code>
Name - {}
"""
