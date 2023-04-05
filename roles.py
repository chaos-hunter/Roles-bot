import discord


TOKEN = 'Enter token here'


class Discord(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 'message id for user to react with for custom roles'

    async def on_ready(self):
        print('{0.user} is now online'.format(client))

    async def on_raw_reaction_add(self, payload):

        # Give a role based on a reaction emoji

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        # Create your custom roles
        if payload.emoji.name == '🤡':
            role = discord.utils.get(guild.roles, name='Clown')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Bad')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '👺':
            role = discord.utils.get(guild.roles, name='Real')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):

        # Remove a role based on a reaction emoji

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🤡':
            role = discord.utils.get(guild.roles, name='Clown')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Bad')
            await member.remove_roles(role)
        elif payload.emoji.name == '👺':
            role = discord.utils.get(guild.roles, name='Real')
            await member.remove_roles(role)


# print(payload.emoji.name)


intents = discord.Intents.default()
intents.members = True

client = Discord(intents=intents)

client.run(TOKEN)
