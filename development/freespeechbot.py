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
	global lastuser
	msgcontent = message.content
	msgauthor = message.author
	if not(message.author == client.user) and isinstance(message.channel, discord.DMChannel):
		targetch = client.get_channel(targetchid)
		if len(msgcontent) > 0:
			if not (lastuser == msgauthor):
				msgcontent = "--\n" + msgcontent
				lastuser = msgauthor
			await targetch.send(msgcontent)
		if message.attachments:
			if not (lastuser == msgauthor):
				msgcontent = "--\n" + msgcontent
				lastuser = msgauthor
			for i in range(len(message.attachments)):
				await targetch.send(message.attachments[i].url)

client.run(token)
