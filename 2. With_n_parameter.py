import os
import openai
import secret
openai.api_key="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"

# Codio solution begins
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5)
print(response)


for i in (response["choices"]):
  print(i["text"].strip()) 

#Codio solution ends