# API do Discord
import discord

# Cria uma subclasse personalizada que pode ser usada para criar um bot do Discord. A classe discord. Client fornece funcionalidades básicas para interagir com o Discord, como manipular eventos, gerenciar o estado do bot e enviar mensagens.
class MyClient(discord.Client):
    
    # Declara um método assíncrono, este método é um tipo especial de função chamada manipulador de eventos que será automaticamente chamado pela biblioteca discord quando o bot estiver pronto para interagir com o servidor do Discord
    async def on_ready(self):
        # Esta linha imprime uma mensagem no console indicando que o bot se conectou com sucesso
        print('Logged on as {0}!'.format(self.user))
        
    # Este método assíncrono on_message é chamado sempre que uma mensagem é enviada em um canal do servidor ao qual o bot está conectado
    async def on_message(self, message):
        
        # verifica se a mensagem foi enviada pelo próprio bot
        if message.author == self.user:
            return

        # verifica se a mensagem começa com o comando $hello
        if message.content.startswith('$hello'):
            await message.channel.send('Fala Galera!')

# Cria um objeto Intents, que especifica os tipos de eventos que o bot deseja receber do Discord. Intents são cruciais porque controlam quais eventos a biblioteca discord envia para o bot. Sem habilitar os intents necessários, o bot pode não receber certas notificações de eventos (por exemplo, mensagens sendo enviadas) e seria incapaz de reagir adequadamente.
intents = discord.Intents.default()

# Habilita explicitamente o intent message_content.
intents.message_content = True

# Cria uma nova instância da classe MyClient e a atribui à variável client
client = MyClient(intents=intents)

# Este método pega o token do bot como argumento
client.run('TOKEN')

#Enquanto deixar o programa rodando o bot vai estar online