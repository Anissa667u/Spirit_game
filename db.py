import psycopg2

try:
    conn = psycopg2.connect(dbname = 'spirit_game', user = 'postgres', password = '021840', host = '5432')
except:
    print('Проблемы с подключением к базе данных')


cursor = conn.cursor()
