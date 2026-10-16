
import pandas as pd
import matplotlib.pyplot as plt

print("PROJETO DE ANALISE DE DADOS")
print("Seguranca do Trabalho")
print("-" * 40)

dados = {
    "setor": ["Armazem", "Operacao", "Manutencao", "Armazem",
              "Operacao", "Manutencao", "Armazem", "Operacao"],
    "tipo_ocorrencia": ["Queda", "Escorregao", "Corte", "Queda",
                        "Impacto", "Corte", "Escorregao", "Queda"],
    "afastamento": ["Sim", "Nao", "Sim", "Nao",
                    "Sim", "Nao", "Nao", "Sim"],
    "dias_afastamento": [3, 0, 2, 0, 5, 0, 0, 1],
    "turno": ["Manha", "Noite", "Tarde", "Manha",
              "Noite", "Tarde", "Manha", "Noite"]
}

df = pd.DataFrame(dados)

print("\nPRIMEIRAS LINHAS DOS DADOS:")
print(df.head())

print("\nTOTAL DE OCORRENCIAS:", len(df))
print("TOTAL DE DIAS DE AFASTAMENTO:", df["dias_afastamento"].sum())

print("\nOCORRENCIAS POR SETOR:")
print(df["setor"].value_counts())

print("\nOCORRENCIAS POR TIPO:")
print(df["tipo_ocorrencia"].value_counts())



# Grafico de ocorrencias por setor

ocorrencias_setor = df["setor"].value_counts()

ocorrencias_setor.plot(kind="bar", color="steelblue")

plt.title("Ocorrencias por Setor")
plt.xlabel("Setor")
plt.ylabel("Quantidade de Ocorrencias")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


# Grafico de ocorrencias por tipo

ocorrencias_tipo = df["tipo_ocorrencia"].value_counts()

ocorrencias_tipo.plot(kind="bar", color="orange")

plt.title("Ocorrencias por Tipo")
plt.xlabel("Tipo de Ocorrencia")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()




# Indicadores da analise

total_ocorrencias = len(df)
total_com_afastamento = (df["afastamento"] == "Sim").sum()
percentual_afastamento = (total_com_afastamento / total_ocorrencias) * 100
media_dias_afastamento = df["dias_afastamento"].mean()

print("\n--- INDICADORES DA ANALISE ---")
print(f"Total de ocorrencias: {total_ocorrencias}")
print(f"Ocorrencias com afastamento: {total_com_afastamento}")
print(f"Percentual com afastamento: {percentual_afastamento:.1f}%")
print(f"Media de dias de afastamento por ocorrencia: {media_dias_afastamento:.2f}")


# Exportar os dados para o Power BI
df.to_csv("ocorrencias_tratadas.csv", index=False, encoding="utf-8-sig")
print("\nArquivo CSV criado para o Power BI!")
