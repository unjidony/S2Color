import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print(client.user.id)
	print('Ready')
	game = discord.Game("S2명령어 입력")
	await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

	def getrole(n):
		return discord.utils.get(message.guild.roles, name = n)

	def getroleplayer(r):
		funcres = ""
		playerlist = getrole(r).members
		for i in range(len(playerlist)):
			funcres = funcres + playerlist[i].display_name + " "
		if funcres == "":
			return "없는 것 같다."
		else:
			return funcres

	if message.content.startswith("S2색변경"):
		try:
			colordic = {"빨강":"빨강", "핑크":"핑크", "주황":"주황", "노랑":"노랑", "연두":"연두", "초록":"초록", "청록":"청록", "시안":"시안", "하늘":"하늘", "파랑":"파랑", "보라":"보라", "연보라":"연보라", "자주":"자주", "색깔닉1":"색깔닉1", "색깔닉2":"색깔닉2", "색깔닉3":"색깔닉3", "색깔닉4":"색깔닉4", "색깔닉5":"색깔닉5", "색깔닉6":"색깔닉6" "양의 축복": "양의 축복"}
			rolename = message.content.split('-')
			role = getrole(colordic[rolename[1]])
		
			colorlist = ["빨강", "핑크", "주황", "노랑", "연두", "초록", "청록", "시안", "하늘", "파랑", "보라", "연보라", "자주", "색깔닉1", "색깔닉2", "색깔닉3", "색깔닉4", "색깔닉5", "색깔닉6"]
			for i in colorlist:	
				delrole = getrole(i)
				if delrole in message.author.roles:
					await message.author.remove_roles(delrole)
			await message.author.add_roles(role)
			await message.channel.send("닉네임 색깔을 " + rolename[1] + "(으)로 변경했습니다.")
		except:
			await message.channel.send("색깔을 추가할 수 없었습니다. 형식에 맞지 않는 명령어를 입력하지는 않았는지 확인해 주세요.")
			
	if message.content.startswith("S2색제거"):
		try:
			colorlist = ["빨강", "핑크", "주황", "노랑", "연두", "초록", "청록", "시안", "하늘", "파랑", "보라", "연보라", "자주", "색깔닉1", "색깔닉2", "색깔닉3", "색깔닉4", "색깔닉5", "색깔닉6"]
			for i in colorlist:	
				delrole = getrole(i)
				if delrole in message.author.roles:
					await message.author.remove_roles(delrole)
			await message.channel.send("색깔이 성공적으로 제거되었습니다.")
		except:
			await message.channel.send("무슨 문제가 있는 것 같습니다......")
			
	
	if message.content.startswith("S2색목록"):
		embed = discord.Embed(title = '색깔 목록', description = '변경 가능한 닉네임 색깔 목록입니다.', colour = discord.Colour.dark_grey())
		embed.add_field(name = '기본 색깔', value = '빨강, 핑크, 주황, 노랑, 연두, 초록, 청록, 시안, 하늘, 파랑, 보라, 연보라, 자주')
		embed.add_field(name = '양의 축복', value = "양의 축복은 추가할 수는 있지만 지워지지는 않습니다.")
		embed.add_field(name = '색깔닉1', value = getrole("색깔닉1").colour.to_rgb())
		embed.add_field(name = '색깔닉2', value = getrole("색깔닉2").colour.to_rgb())
		embed.add_field(name = '색깔닉3', value = getrole("색깔닉3").colour.to_rgb())
		embed.add_field(name = '색깔닉4', value = getrole("색깔닉4").colour.to_rgb())
		embed.add_field(name = '색깔닉5', value = getrole("색깔닉5").colour.to_rgb())
		embed.add_field(name = '색깔닉6', value = getrole("색깔닉6").colour.to_rgb())
		await message.channel.send(embed=embed)

	if message.content.startswith("S2색깔닉유저"):
		embed = discord.Embed(title = '색깔닉 유저 목록', description = "색깔닉 1~6을 사용 중인 유저의 목록입니다.", colour = discord.Colour.light_grey())
		embed.add_field(name = '색깔닉1', value = getroleplayer("색깔닉1"))
		embed.add_field(name = '색깔닉2', value = getroleplayer("색깔닉2"))
		embed.add_field(name = '색깔닉3', value = getroleplayer("색깔닉3"))
		embed.add_field(name = '색깔닉4', value = getroleplayer("색깔닉4"))
		embed.add_field(name = '색깔닉5', value = getroleplayer("색깔닉5"))
		embed.add_field(name = '색깔닉6', value = getroleplayer("색깔닉6"))
		await message.channel.send(embed=embed)

	if message.content.startswith("S2색깔닉설정"):
		splitmsg = message.content.split(' ')
		try:
			cnlist = {"색깔닉1":"색깔닉1", "색깔닉2":"색깔닉2", "색깔닉3":"색깔닉3", "색깔닉4":"색깔닉4", "색깔닉5":"색깔닉5", "색깔닉6":"색깔닉6"}
			changerole = getrole(cnlist[splitmsg[1]])
			ctup = discord.Colour.from_rgb(int(splitmsg[2]),int(splitmsg[3]),int(splitmsg[4]))
			await changerole.edit(colour = ctup)
			await message.channel.send(splitmsg[1] + "의 색깔이 " + splitmsg[2] + "," + splitmsg[3] + "," + splitmsg[4] +" (으)로 변경되었습니다.")
		except:
			await message.channel.send("색깔을 변경할 수 없었습니다. 형식에 맞지 않는 명령어를 입력하지는 않았는지 확인해 주세요.")

	if message.content.startswith("S2M1"):
		splitmsg = message.content.split(' ')
		try:
			changerole = getrole(splitmsg[1])
			ctup = discord.Colour.from_rgb(int(splitmsg[2]),int(splitmsg[3]),int(splitmsg[4]))
			await changerole.edit(colour = ctup)
		except:
			await message.channel.send("실패.")

	if message.content.startswith("S2M2"):
		try:
			rolename = message.content.split('-')
			role = getrole(rolename[1])
			target = message.guild.get_member(int(rolename[2]))
			await target.add_roles(role)
		except:
			await message.channel.send("실패.")

	if message.content.startswith("S2M3"):
		try:
			rolename = message.content.split('-')
			role = getrole(rolename[1])
			target = message.guild.get_member(int(rolename[2]))
			if role in target.roles:
					await target.remove_roles(role)
		except:
			await message.channel.send("실패.")

	if message.content.startswith("S2명령어"):
		embed = discord.Embed(title = '명령어', description = "현재 사용 가능한 명령어 목록입니다.", colour = discord.Colour.lighter_grey())
		embed.add_field(name = 'S2색변경-(색깔)', value = "닉네임 색깔을 (색깔)로 바꿉니다.")
		embed.add_field(name = 'S2색목록', value = "사용 가능한 닉네임 색깔 목록을 보여줍니다.")
		embed.add_field(name = 'S2색깔닉설정 (색깔닉1~6) (r) (g) (b)', value = "색깔닉의 색을 입력한 rgb 색으로 변경합니다.")
		embed.add_field(name = 'S2색깔닉유저', value = "색깔닉1~6 사용하고 있는 유저의 목록을 보여줍니다.")
		embed.add_field(name = 'S2색제거', value = "가지고 있는 색깔 닉네임 역할을 제거합니다.")
		await message.channel.send(embed=embed)

	if message.content.startswith("S2Mhelp"):
		embed = discord.Embed(title = '마스터 명령어', colour = discord.Colour.darker_grey())
		embed.add_field(name = 'S2M1 (역할) (r) (g) (b)', value = "(역할)의 색깔을 변경합니다.")
		embed.add_field(name = 'S2M2-(역할)-(id)', value = "(id)의 유저에게 (역할)을 추가합니다.")
		embed.add_field(name = 'S2M3-(역할)-(id)', value = "(id)의 유저에게서 (역할)을 제거합니다.")
		await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
