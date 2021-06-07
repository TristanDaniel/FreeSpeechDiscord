import discord

token = 'bot token'
client = discord.Client()
lastuser = client

@client.event
async def on_ready():
	print('logged in')

@client.event
async def on_message(message):
	global lastuser
	msgcontent = message.content
	msgauthor = message.author
	if not(message.author == client.user) and not (isinstance(message.channel, discord.DMChannel)):
		if (message.channel.name != "free-speech"):
			return
		c = []
		for g in client.guilds:
			c.append(discord.utils.get(g.channels, name="free-speech"))
		msgchannel = message.channel.id
		if not (lastuser == msgauthor):
			msgcontent = "--\n" + msgcontent
			lastuser = msgauthor
		if message.attachments:
			attachments = message.attachments
			for i in range(len(attachments)):
				msgcontent = msgcontent + "\n" + attachments[i].url
		for i in c:
			if not(i == None or i.id == msgchannel):
				await i.send(msgcontent)

client.run(token)
