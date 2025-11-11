# %%
import pandas as pd

cerveja_df = pd.read_excel("data/dados_cerveja.xlsx")
cerveja_df
# %%
features = ['temperatura', 'copo', 'espuma', 'cor']
target = 'classe'

X = cerveja_df[features]
y = cerveja_df[target]


X = X.replace({
    "mud": 1, "pint": 2,
    "sim": 1, "não": 0,
    "clara": 0, "escura": 1
    })
# %%
from sklearn import tree
model = tree.DecisionTreeClassifier()

model.fit(X = X, y=y)

# %%
tree.plot_tree(
                model,
                feature_names=features,
                class_names=model.classes_,
                filled=True
                )
# %%
