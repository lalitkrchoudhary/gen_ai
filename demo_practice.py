import giskard
import pandas as pd
from giskard import Model

# Dummy chatbot
def chatbot_predict(df):
    return ["Hello " + q for q in df["question"]]

model = Model(
    model=chatbot_predict,
    model_type="text_generation",
    name="Simple Chatbot",
    description="This is a basic chatbot that replies with greeting messages",
    feature_names=["question"]  
)

# ✅ FIXED DATASET
data = pd.DataFrame({
    "question": ["Hi", "How are you?"]
})

dataset = giskard.Dataset(
    df=data,
    target=None
)

# Scan
report = giskard.scan(model=model, dataset=dataset)
print(report)

