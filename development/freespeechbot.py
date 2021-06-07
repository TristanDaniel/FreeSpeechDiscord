import discord

token = 'bot token'
targetchid = [channel id]
client = discord.Client()
lastuser = client

@client.event
async def on_ready():
	print('logged in')

@client.event
async def on_message(message):
	c = []
	for g in client.guilds:
		c.append(discord.utils.get(g.channels, name="free-speech"))
	global lastuser
	msgcontent = message.content
	msgauthor = message.author
	if not(message.author == client.user) and isinstance(message.channel, discord.DMChannel):
		targetch = client.get_channel(targetchid)
		if len(msgcontent) > 0:
			if not (lastuser == msgauthor):
				msgcontent = "--\n" + msgcontent
				lastuser = msgauthor
			for i in range(len(c)):
				if not(c[i] == None):
					await c[i].send(msgcontent)
		if message.attachments:
			attachments = message.attachments
			if not (lastuser == msgauthor):
				msgcontent = "--\n" + msgcontent
				lastuser = msgauthor
			for j in range(len(c)):
				if not(c[j] == None):
					for i in range(len(attachments)):
						await c[j].send(message.attachments[i].url)

client.run(token)
