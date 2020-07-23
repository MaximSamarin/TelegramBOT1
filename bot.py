from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler #Для обработки текстовых сообщений отправленных пользователем импортируем обработчик сообщений MessageHandler
from telegram.ext import Filters #и Filters для выбора с каким типом сообщения (текст, видео, аудио и т.д) будем работать.
from settings import TG_TOKEN

#функция sms будет вызвана при нажатии кнопки /start
def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')  # вывод сообщения в консоль при нажатии /start
    bot.message.reply_text('Привет {} я Бот\n Я пока не умею разговаривать, но  я очень быстро учусь'.format(bot.message.chat.first_name))  #отправляем ответ
    print(bot.message)

def parrot(bot, update):
    print(bot.message.text) #печатаем на экран сообщение пользователя
    bot.message.reply_text(bot.message.text) #возвращаем пользователю его же сообщение

def main():
    # создаем переменную my_bot
    my_bot = Updater(TG_TOKEN, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot)) #обработчик сообщения handler куда помещаем обработчик сообщения MessageHandler и Filters.text с указанием какой тип сообщения обрабатывать (text — текстовое сообщение).

    my_bot.start_polling()  # проверяет наличие сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят



main()
