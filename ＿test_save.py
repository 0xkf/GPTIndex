import os
from gpt_index import GPTSimpleVectorIndex, SimpleWebPageReader
from dotenv import load_dotenv
# env_path = os.path.join(os.path.dirname(__file__), '../.env')
# load_dotenv(env_path)
load_dotenv()

MYAPI = os.getenv('MYAPI')
THEURL = os.getenv('THEURL')

print(MYAPI)
print(THEURL)


 
os.environ["OPENAI_API_KEY"] = MYAPI
 
json_path = "./data/wiki.json"
 
url = THEURL



documents = SimpleWebPageReader(html_to_text=True).load_data([url])

index = GPTSimpleVectorIndex(documents)
index.save_to_disk(json_path)
