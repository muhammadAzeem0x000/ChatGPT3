import os
import openai
import secret

with open('C:/Users/AZEEM/Desktop/API.txt') as file:
    api_key = file.read().strip()

openai.api_key = api_key

# WRITE YOUR CODE HERE

prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-003", prompt=prompts)

print(response['choices'][0]['text'].strip())
