from db import DB

database=DB(filename = 'logs.sqlite3', dbtype='sqlite')

#print(database.tables)

log_df = database.tables.log.all() #pega todos os dados da tabela indicada

#print(log_df)


log_df = database.query('select * from log where user_id = 3')

print(log_df)

log_df = database.query('select * from log where path like "%pandas%"')

print(log_df)


log_df['date'] = pd.to_datetime(log_df['date'], format ='%Y-%m-%d %H:%M:%S.%f')


