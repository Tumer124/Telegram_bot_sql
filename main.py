import sqlite3
import telebot
from database import add_execute,reg_execute,del_execute,list_execute

bot = telebot.TeleBot("5794093768:AAHGnx8cOkGGM9jzr796ssy-HyVxizooIos")


@bot.message_handler(commands = ['start'])
def start_hendler(message):
	bot.send_message(chat_id = message.chat.id, text = "Бот запущен")
	
@bot.message_handler(commands = ['register'])
def register_handler(message):
	bot.reply_to(message, "Вы зарегестрированы")
	
@bot.message_handler(commands = ['deletetask'])
def delete_handler(message):
	bot.reply_to(message, del_execute(message))


@bot.message_handler(commands = ["add_task"])
def add_task_handler(message):
	bot.reply_to(message, add_execute(message))
	
	
@bot.message_handler(commands = ["list_task"])
def get_tasks_hendler(message):
	bot.reply_to(message, list_execute(message))
	
bot.set_my_commands([
	telebot.types.BotCommand("/start","Перезапустить бота"),
	telebot.types.BotCommand("/list_task","Список задач"),
	telebot.types.BotCommand("/register","Регистрация")
])
		
bot.polling()