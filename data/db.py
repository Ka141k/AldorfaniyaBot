import sqlite3

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()

	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchall()
			return bool(len(result))
	
	def add_user(self, user_id, player_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO users (user_id, player_id) VALUES (?, ?)', (user_id, player_id,))
	
	def get_users(self):
		with self.connection:
			return len(self.cursor.execute('SELECT * FROM users').fetchall())
	
	def set_nickname(self, user_id, nickname):
		with self.connection:
			return self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?", (nickname, user_id,))
	
	def get_signup(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				signup = str(row[0])
				return signup
	
	def set_signup(self, user_id, signup):
		with self.connection:
			return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id,))
	
	def get_registered_users(self):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM users WHERE signup = ?', ('done',)).fetchall()
			return len(result)
	
	def get_nickname(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT nickname FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				nickname = str(row[0])
				return nickname
	
	def get_player_id(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT player_id FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				player_id = str(row[0])
				return player_id
	
	def get_player_ruby(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT ruby FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				ruby = int(row[0])
				return int(ruby)
	
	def get_player_karma(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT karma FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				player_karma = str(row[0])
				return player_karma
	
	def set_player_ruby(self, user_id, new_ruby_count):
		with self.connection:
			return self.cursor.execute("UPDATE users SET ruby = ? WHERE user_id = ?", (new_ruby_count, user_id,))
	
	def get_player_avatar(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT avatar FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				avatar = str(row[0])
				return avatar
	
	def set_player_avatar(self, user_id, avatar_id):
		with self.connection:
			return self.cursor.execute("UPDATE users SET avatar = ? WHERE user_id = ?", (avatar_id, user_id,))
	
	def delete_account(self, user_id):
		with self.connection:
			return self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))