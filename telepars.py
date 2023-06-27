from telethon import TelegramClient
import config

client = TelegramClient('Helper_of_Ivan', config.api_id, config.api_hash)

client.start('+375292015733')
# client.send_message('config.gvin_phone', 'Hello! My name is Gustavo!')
# member = client.get_entity(849107865)
# print(client.get_me())
#
# for dialog in client.iter_dialogs():
#     print(dialog.id, dialog.title)
#
file = open('messages2.txt', 'a', encoding='utf-8')

for message in client.iter_messages(config.id_bardel):
    for member in client.iter_participants(config.id_bardel):
        if 1588790816 == message.from_id:
            print('OK')
    # print(message.from_id.user_id, member.id)
    # file.write(str(message.message))

print(client.get_entity(config.id_bardel))
print('Well done!')
