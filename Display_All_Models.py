import os
import openai
import secret

with open('C:/Users/AZEEM/Desktop/API.txt') as file:
    api_key = file.read().strip()

openai.api_key = api_key
# WRITE YOUR CODE HERE

models = openai.Model.list()
model_ids = [model["id"] for model in models["data"]]
print(model_ids)

print("-------------------------------")

models = openai.Model.list()
print(len(models["data"]))

models = openai.Model.list()
print(len(models))
