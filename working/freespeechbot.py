import discord

client = discord.Client()

@client.event
async def on_ready():
	print('logged in')

@client.event
async def on_message(message):
	msgcontent = message.content
	if not(message.author == client.user) and isinstance(message.channel, discord.DMChannel):
		targetch = client.get_channel([channel id])
		if len(msgcontent) > 0:
			await targetch.send(msgcontent)
		if message.attachments:
			for i in range(len(message.attachments)):
				await targetch.send(message.attachments[i].url)

client.run('bot token')
