import pandas as pd
import sqlite3

csv_file_path = ('StockMarket.csv')
db_name = 'dados_stockmarket.db'

# Carregar o CSV para um DataFrame do pandas
data = pd.read_csv(csv_file_path, sep=';')

# Criar uma conexao com o banco de dados SQLite
conn = sqlite3.connect(db_name)

# Carregar o DataFrame transformado para uma tabela no banco de dados
data.to_sql('stock_data', conn, if_exists='replace', index=False)

# Fechar a conexao com o banco de dados
conn.close()