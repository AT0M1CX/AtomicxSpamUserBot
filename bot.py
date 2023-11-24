from pyrogram import Client, filters, errors, types
import random
import time

a = input('Session: ')
1
app = Client(str(a), api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

print('UserBot Has STARTED')

@app.on_message(filters.command('test', prefixes='.') & filters.me)
def test(app: Client, message: types.Message):
    message.edit_text('✅')
    time.sleep(1)
    message.delete()

@app.on_message(filters.command('spam', prefixes='.') & filters.me)
def spam(app: Client, message: types.Message):
    message.edit('УСПЕХ')
    time.sleep(1)
    message.delete()
    
    try:
        text = message.reply_to_message.text
    except AttributeError:
        _list = str(message.text).split('\n')
        text = str(_list[1])
        count = int(_list[2])
        delay = float(_list[3])
        tag = bool(_list[3])

    else:
        _list = str(message.text).split('\n')		
        count = int(_list[2])
        delay = float(_list[3])
        tag = bool(_list[3])
    
    print(f'Text: {text}\nCount: {count}\nDelay: {delay}\nTag: {tag}')
    members = []
    for _ in range(count):
        if bool(tag):
            for msg in app.get_chat_history(message.chat.id, limit=1000):
                if msg.from_user:
                    members.append(msg.from_user.id)
            _text = f'{text}\n'
            for i in range(10):
                _text += f'[{i}](tg://user?id={random.choice(list(set(members)))})\n'
        

        msg = app.send_message(message.chat.id, _text)
        msg.edit(text)
        time.sleep(delay)
        
app.run()