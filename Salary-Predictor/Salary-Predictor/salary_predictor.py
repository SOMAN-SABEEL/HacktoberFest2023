import pandas as pd

data = pd.read_csv("cleandata.csv")
data.drop(columns=["Unnamed: 0"], inplace=True)
# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-09-12T14:09:04.726080Z","iopub.execute_input":"2023-09-12T14:09:04.727553Z","iopub.status.idle":"2023-09-12T14:09:04.734774Z","shell.execute_reply.started":"2023-09-12T14:09:04.727459Z","shell.execute_reply":"2023-09-12T14:09:04.733277Z"}}
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:40.027757Z","iopub.execute_input":"2023-09-12T14:00:40.028920Z","iopub.status.idle":"2023-09-12T14:00:40.038001Z","shell.execute_reply.started":"2023-09-12T14:00:40.028875Z","shell.execute_reply":"2023-09-12T14:00:40.035923Z"},"jupyter":{"outputs_hidden":false}}
X= data.drop(columns=["avg_salary"])
y = data["avg_salary"]

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:40.664506Z","iopub.execute_input":"2023-09-12T14:00:40.664937Z","iopub.status.idle":"2023-09-12T14:00:40.670977Z","shell.execute_reply.started":"2023-09-12T14:00:40.664897Z","shell.execute_reply":"2023-09-12T14:00:40.670018Z"},"jupyter":{"outputs_hidden":false}}
col_trans = ColumnTransformer([('ohe', OneHotEncoder(sparse=False, drop='first', handle_unknown='infrequent_if_exist'), ["Job Title","Location","Company Name"])], remainder="passthrough")

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:41.269954Z","iopub.execute_input":"2023-09-12T14:00:41.271254Z","iopub.status.idle":"2023-09-12T14:00:41.276271Z","shell.execute_reply.started":"2023-09-12T14:00:41.271190Z","shell.execute_reply":"2023-09-12T14:00:41.274984Z"},"jupyter":{"outputs_hidden":false}}
model = RandomForestRegressor()

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:42.130241Z","iopub.execute_input":"2023-09-12T14:00:42.130618Z","iopub.status.idle":"2023-09-12T14:00:42.137067Z","shell.execute_reply.started":"2023-09-12T14:00:42.130589Z","shell.execute_reply":"2023-09-12T14:00:42.135113Z"},"jupyter":{"outputs_hidden":false}}
pipe = make_pipeline(col_trans, model)

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:45.725405Z","iopub.execute_input":"2023-09-12T14:00:45.726104Z","iopub.status.idle":"2023-09-12T14:00:45.734534Z","shell.execute_reply.started":"2023-09-12T14:00:45.726062Z","shell.execute_reply":"2023-09-12T14:00:45.733065Z"},"jupyter":{"outputs_hidden":false}}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:46.416460Z","iopub.execute_input":"2023-09-12T14:00:46.417152Z","iopub.status.idle":"2023-09-12T14:00:49.144597Z","shell.execute_reply.started":"2023-09-12T14:00:46.417112Z","shell.execute_reply":"2023-09-12T14:00:49.143549Z"},"jupyter":{"outputs_hidden":false}}
pipe.fit(X_train, y_train)
y_pred_lr = pipe.predict(X_test)

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:00:55.100858Z","iopub.execute_input":"2023-09-12T14:00:55.101297Z","iopub.status.idle":"2023-09-12T14:00:55.110236Z","shell.execute_reply.started":"2023-09-12T14:00:55.101260Z","shell.execute_reply":"2023-09-12T14:00:55.108906Z"},"jupyter":{"outputs_hidden":false}}
r2_score(y_test, y_pred_lr)

# %% [code] {"execution":{"iopub.status.busy":"2023-09-12T14:02:08.817455Z","iopub.execute_input":"2023-09-12T14:02:08.817890Z","iopub.status.idle":"2023-09-12T14:02:08.833632Z","shell.execute_reply.started":"2023-09-12T14:02:08.817855Z","shell.execute_reply":"2023-09-12T14:02:08.832700Z"},"jupyter":{"outputs_hidden":false}}
import pickle

pickle.dump(pipe, open('salary.pk1', 'wb'))

# %% [code] {"jupyter":{"outputs_hidden":false}}
