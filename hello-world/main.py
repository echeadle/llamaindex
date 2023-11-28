import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    print('Hello, world llamaIndex Course')
    print(f"OPENAI_API_KEY is: {os.environ['OPENAI_API_KEY']}")