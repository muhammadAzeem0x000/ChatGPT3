import os
import openai
import secret
openai.api_key="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"

# WRITE YOUR CODE HERE

prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    frequency_penalty=2,
                                    presence_penalty=0)
for i in (response["choices"]):
  print("----")
  print(i["text"].strip()) 