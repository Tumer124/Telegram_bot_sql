import sqlite3
import telebot



connect = sqlite3.connect('database.db')  # Создаем к базе данных
cursor = connect.cursor()

create_tabl_task = """
CREATE TABLE IF NOT EXISTS tasks (
	id INTEGER PRIMARY KEY,
	user_id INTEGER,
	task TEXT,
	done BOOLEAN);
"""  # создаем запрос

create_tabl_user = """
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	name TEXT,
	chat_id INTEGER);
"""

cursor.execute(create_tabl_task)  # Выполняет запрос sql на на сздание базы данных
cursor.execute(create_tabl_user)
connect.commit()  # сохранить изменения в бд


def add_execute(message):
	connect = sqlite3.connect("database.db")
	cursor = connect.cursor()
	chat_id = (message.from_user.id,)
	cursor.execute("SELECT * FROM users WHERE chat_id=?", chat_id)
	user = cursor.fetchone()
	if user is None:
		return "Данный пользователь не зарегистрирован"
	else:
		task = message.text.split("/add_task")[1]
		task_data = (user[0],task, False)
		cursor.execute("INSERT INTO tasks (user_id, task, done) VALUES (?, ?, ?)", task_data)
		connect.commit()
	connect.close()
	return "Задача добавлена."

def reg_execute(message):
	connect = sqlite3.connect("database.db")
	cursor = connect.cursor()
	user = (message.from_user.first_name, message.from_user.id)
	cursor.execute("INSERT INTO users (name, chat_id) VALUES (?, ?)",user)
	connect.commit()
	connect.close()
	return "Вы зарегестрированы"

def del_execute(message):
	connect = sqlite3.connect("database.db")
	cursor = connect.cursor()
	chat_id = (message.from_user.id, )
	cursor.execute("SELECT * FROM users WHERE chat_id=?", chat_id)
	user = cursor.fetchone()
	if user is None:
		return "Вы не зарегистрированы!"
	else:
		task_id = message.text.split("/deletetask")[1]
		task_id = (int(task_id),)
		user = (int(user[0]),)
		cursor.execute("SELECT * FROM tasks WHERE id=? AND user_id=? ", task_id + user)
		task = cursor.fetchone()
		if task is None:
			return "Такой записи нет"
		else:
			cursor.execute("DELETE FROM tasks WHERE id=?", task_id)
			connect.commit()
			connect.close()
			return "Ваша запись удалена"

def list_execute(message):
	connect = sqlite3.connect("database.db", )
	cursor = connect.cursor()
	chat_id = (message.from_user.id,)
	cursor.execute("SELECT * FROM users WHERE chat_id=?", chat_id)
	user = cursor.fetchone()
	if user is None:
		return "Ты не зарегистрирован"
	else:
		user = (int(user[0]),)
		cursor.execute("SELECT * FROM tasks WHERE user_id=?", user)
		tasks = cursor.fetchall()
		if tasks:
			task = '\n'
			for i in tasks:
				task += f'ID записи: {i[0]}\nОписание задачи: {i[2]}\nСостояние задачи: {i[3]}\n\n'
			return task
		else:
			return "У вас нет задач"
		connect.close()