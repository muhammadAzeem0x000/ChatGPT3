import os
import openai
import secret
openai.api_key="OPENAI_KEY"

# WRITE YOUR CODE HERE

prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    top_p=0.1)
for i in (response["choices"]):
  print(i["text"].strip())

# This will print out the response 5 times by taking the top 10 probabilities that will be the same so the response will be same
