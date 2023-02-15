import os
from gpt_index import GPTSimpleVectorIndex
from dotenv import load_dotenv
load_dotenv()

MYAPI = os.getenv('MYAPI')
# THEURL = os.getenv('THEURL')
QUESTION2 = os.getenv('QUESTION2')
QUESTION3 = os.getenv('QUESTION3')

os.environ["OPENAI_API_KEY"] = MYAPI
json_path = "./data/wiki.json"
 
index = GPTSimpleVectorIndex.load_from_disk(json_path)
 

# print(index.query("聖書の内容を要約してください。？"))
print(index.query(QUESTION2))
print(index.query(QUESTION3))