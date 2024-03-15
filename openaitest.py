import os
import openai
from openai import OpenAI

from config import apikey
print (apikey)
exit()
#openai.api_key="sk*********************Nh"

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write an email to my boss for my resignation\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
