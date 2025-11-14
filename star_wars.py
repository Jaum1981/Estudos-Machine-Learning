# %%
import pandas as pd

clones_df = pd.read_parquet("data/dados_clones.parquet")
clones_df.head()
# print(clones_df.columns.tolist())

# %%
features = ['p2o_master_id', 'Massa(em kilos)', 'General Jedi encarregado', 'Estatura(cm)', 'Distância Ombro a ombro', 'Tamanho do crânio', 'Tamanho dos pés', 'Tempo de existência(em meses)']
target = ['Status ']
features_num = ['Massa(em kilos)', 'Estatura(cm)']

#%%
X = clones_df[features]
y = clones_df[target]

#%%
clones_df.groupby('Status ')[features_num].mean()
