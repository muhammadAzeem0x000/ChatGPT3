import openai
import secret

with open('C:/Users/AZEEM/Desktop/API.txt') as file:
    api_key = file.read().strip()

openai.api_key = api_key

def fix_spelling(text: str) -> str:
  #please put your code below this line
  edi= openai.Edit.create(
  model="text-davinci-edit-001",
  input=text,
  instruction="fix_spelling."
  )
  return edi['choices'][0]['text'].strip()

# WRITE YOUR CODE HERE

# FREEZE CODE BEGIN
input_texts = [
    "I hve a bananna for brekfast.",
    "The colur of the sky is rde.",
    "The grass is greneer on the other side."
]

for input_text in input_texts:
    output_text = fix_spelling(input_text)
    print(f"Input: {input_text}\nOutput: {output_text}\n")
# FREEZE CODE END