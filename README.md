# 🏥 Análise de Fluxo de Atendimento em Clínica

## 📌 Sobre o Projeto

Este projeto tem como objetivo analisar o fluxo de atendimentos de uma clínica médica, identificando padrões de comparecimento dos pacientes, tempo de espera e possíveis gargalos operacionais.

A análise foi realizada utilizando Python, SQL e Power BI, simulando um pipeline real de dados em um ambiente profissional.

---

## 🎯 Problema de Negócio

Clínicas frequentemente enfrentam desafios como:

* Alto tempo de espera para consultas
* Taxa significativa de faltas (no-show)
* Má distribuição de atendimentos ao longo da semana

Este projeto busca responder:

* O tempo de espera influencia a ausência dos pacientes?
* Quais dias possuem maior demanda?
* Onde estão os principais gargalos operacionais?

---

## 🧰 Tecnologias Utilizadas

* Python (Pandas)
* SQL (SQLite)
* Power BI
* Jupyter Notebook

---

## 🔄 Pipeline de Dados (ETL)

* Extração de dados em CSV
* Padronização de colunas
* Conversão de datas
* Criação da métrica `waiting_days` (tempo de espera)
* Armazenamento em base tratada (CSV + SQLite)

---

## 📊 Principais Análises e Insights

### ⏱️ Tempo de Espera

* Tempo médio de espera: **~10 dias**
* Casos extremos chegam a até **179 dias**

---

### 🚨 Taxa de Faltas

* Total de atendimentos: **110.527**
* Pacientes que faltaram: **22.319**
* Taxa de falta: **~20%**

---

### 📅 Padrão por Dia da Semana

* Dias mais movimentados:

  * **Quarta-feira (25.867)**
  * **Terça-feira (25.640)**
* Menor movimento:

  * **Sábado (39 atendimentos)**

---

### 📉 Relação Espera x Faltas

* Pacientes que comparecem:

  * Espera média: **~8,7 dias**
* Pacientes que faltam:

  * Espera média: **~15,8 dias**

👉 Insight: **Quanto maior o tempo de espera, maior a probabilidade de ausência**

---

### 🏘️ Distribuição por Bairro

Top bairros com maior volume:

* Jardim Camburi
* Maria Ortiz
* Resistência
* Jardim da Penha

---

## 📊 Dashboard (Power BI)

O dashboard foi desenvolvido para:

* Monitorar volume de atendimentos
* Analisar faltas por dia da semana
* Avaliar impacto do tempo de espera
* Identificar padrões operacionais

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/Estogler/analise-fluxo-atendimento.git
```

2. Execute o ETL:

```bash
python src/etl.py
```

3. Abra o dashboard no Power BI:

```bash
dashboard/dashboard.pbix
```

---

## 📁 Estrutura do Projeto

* `data/raw/` → dados originais
* `data/processed/` → dados tratados
* `src/` → script de ETL
* `notebooks/` → análises exploratórias
* `dashboard/` → arquivo do Power BI

---

## 💡 Conclusões de Negócio

* Reduzir o tempo de espera pode diminuir significativamente as faltas
* Terça e quarta são dias críticos → necessidade de melhor distribuição
* Sábados possuem baixa demanda → oportunidade de ajuste operacional
* A análise permite decisões mais estratégicas na gestão da clínica

---

## 👨‍💻 Autor

**Kauã Oliveira**
🔗 https://github.com/Estogler
