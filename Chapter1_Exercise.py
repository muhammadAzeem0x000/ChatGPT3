import openai

openai.api_key="OPENAI_API_KEY"

# Requirements
# Write a code so that we have the most random possible answer. Meaning setting the value that determines randomness to max
# Generate 6 responses and pick the best among them
# The completion token limit should be set 25
# Do not include any argument that are not necessary to the requirements

prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=6,
                                    temperature=1,
                                    max_tokens=25,
                                    best_of=6
                                    )
print(response)
