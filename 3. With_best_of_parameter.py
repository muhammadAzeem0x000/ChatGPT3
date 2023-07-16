import os
import openai
import secret
openai.api_key="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"

# Codio solution begins
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-003", 
                                    prompt=prompts,
                                    n=2,
                                    best_of=2)

print(response)

#Codio solution ends