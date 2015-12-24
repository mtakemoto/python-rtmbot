from plexapi.server import PlexServer

plex = PlexServer('http://192.168.0.110:32400')
outputs = []
contable = []

def reply(channel, message):
	outputs.append([channel, message])

def format_list(list):
    return ''.join(list)

def listall(argv, channel):
    list = []
    sectitle = argv[2]
    for show in plex.library.section(sectitle).all():
    	list.append(show.title + '\n')
    reply(channel, format_list(list))

def setplayer(argv, channel):
    list = []
    for client in plex.clients():
        list.append(client.name + '\n')
    reply(channel, format_list(list))

def process_message(data):
    channel = data["channel"]
    text = data["text"]

    #DM only
    if channel.startswith("D"):
    	if text.startswith("plexcmd"):
    		argv = text.split()
                
                options = {"list" : listall,
                           "setplayer" : setplayer,
                }
                options[argv[1]](argv, channel)
                
#shows = plex.library.section(shows)
#showsize = len(shows)
#random.randint(0, showsize - 1)
'''Planned functions:
    list <library>
    shuffle <library> <show, if one> [-p]
    setplayer
        --list connected devices & respond with number
        --respond within 30 secs  or with 'cancel' to cancel
    plexcmd
        --print usage and availible functions

'''

    

