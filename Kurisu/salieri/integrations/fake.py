from discord.ext import commands

class FakeRole:
    name = "@everyone"

class FakeUser:
    name = "Test"
    display_name = "Test"
    id = "1"
    bot = False
    top_role = FakeRole
    roles = [FakeRole]
    avatar = ''

    @staticmethod
    def is_avatar_animated():
        return False

    def __str__(self):
        return self.name

class FakeMessage:
    author = FakeUser()
    mentions = []

class FakeCtx:
    messages = []

    message = FakeMessage()

    async def send(self, *args, **kwargs):
        self.messages.append([args, kwargs])

    def reset(self):
        self.messages = []


client = commands.Bot(command_prefix='!', description='Salieri Systems')
ctx = FakeCtx()
