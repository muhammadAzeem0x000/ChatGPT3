import os
import openai
import secret
openai.api_key="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"

# WRITE YOUR CODE HERE

prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", prompt=prompts, 
                                    temperature=0, 
                                    max_tokens=6)
print(response)

print(response['usage'])