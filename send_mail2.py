"""
https://imapclient.readthedocs.io/en/master/
"""

from imapclient import IMAPClient

server = IMAPClient('imap.yandex.ru', use_uid=True, ssl=True)
# imObj = imapclient.IMAPClient("imap.yandex.ru", ssl=True, port=993)
server.login("mylogin@yandex.ru", "mypass")

# Нужно на сервере Яндекса сгенерировать пароль приложений для почты IMAP
select_info = server.select_folder('INBOX')
print(select_info)
messages = server.search(['FROM', 'news@mail.fl.ru'])
print(messages)