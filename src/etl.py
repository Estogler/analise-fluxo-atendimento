import pandas as pd
import os

# caminho base do projeto (independente de onde rodar)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# caminhos dos arquivos
input_path = os.path.join(BASE_DIR, 'data', 'raw', 'KaggleV2-May-2016.csv')
output_dir = os.path.join(BASE_DIR, 'data', 'processed')
output_path = os.path.join(output_dir, 'dados_tratados.csv')

# criar pasta processed se não existir
os.makedirs(output_dir, exist_ok=True)

# carregar dados
df = pd.read_csv(input_path)

# padronizar nomes das colunas
df.columns = df.columns.str.lower()

# converter datas
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# remover horas (ficar só data)
df['scheduledday'] = df['scheduledday'].dt.date
df['appointmentday'] = df['appointmentday'].dt.date

# converter novamente para datetime
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# criar coluna de tempo de espera
df['waiting_days'] = (df['appointmentday'] - df['scheduledday']).dt.days

# salvar dados tratados
df.to_csv(output_path, index=False)

print("✅ Dados processados com sucesso!")