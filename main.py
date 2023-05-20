# pytelegrambotapi
from telebot import TeleBot
from telebot.types import Message

TOKEN = '6094762205:AAEE7nwGkndr3m8XWReYZ_gjJBrjuwQS2c0'
bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help', 'about'])
def start(message):
    # Один к одному id комнаты пользователя == id комнаты
    # В группах
    # В каналах
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id, user_id)
    if message.text == '/start':
        bot.send_message(chat_id, 'Здравствуйте, я бот попугай')
    elif message.text == '/help':
        bot.send_message(chat_id, f'/help - Помощь\n/about - О боте\n/start - Начать работу')
    elif message.text == '/about':
        bot.send_message(chat_id, 'Бот создан спомощью библиотеки pytelegrambotapi на питоне ')


@bot.message_handler(content_types=['text', 'photo', 'video_note', 'sticker','voice', 'animation', 'video'])
def echo(message: Message):
    chat_id = message.chat.id
    if message.text:
        text = message.text
        bot.send_message(chat_id, text)
        bot.send_message(chat_id, '(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)')
        bot.send_message(chat_id, f'<b>{text}</b>')
        bot.send_message(chat_id, f'<i>{text}</i>')
        bot.send_message(chat_id, f'<u>{text}</u>')
        bot.send_message(chat_id, f'<s>{text}</s>')
        bot.send_message(chat_id, f'<code>{text}</code>')
        bot.send_message(chat_id, f'<pre>{text}</pre>')
        bot.send_message(chat_id, f'<tg-spoiler>{text}</tg-spoiler>')
    elif message.photo:
        pphoto = message.photo[0].file_id
        bot.send_photo(chat_id, pphoto)
    elif message.voice:
        voice_id = message.voice.file_id
        bot.send_voice(chat_id,voice_id)
    elif message.video:
        video_id = message.video.file_id
        bot.send_video(chat_id,video_id)
    elif message.animation:
        animation_id = message.animation.file_id
        bot.send_animation(chat_id, animation_id)
    elif message.sticker:
        sticker_id = message.sticker.file_id
        bot.send_sticker(chat_id=chat_id, sticker=sticker_id)
    elif message.video_note:
        video_note_id = message.video_note.file_id
        bot.send_video_note(chat_id, video_note_id)




# Зацикливание бота
bot.polling(none_stop=True)
