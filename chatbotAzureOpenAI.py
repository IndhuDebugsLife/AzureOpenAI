
import os  
import base64
from openai import AzureOpenAI  



# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint="INSERT ENDPOIN HERE",  
    api_key="INSERT API KEY HERE",  
    api_version="2024-05-01-preview",
)
    
    


#Prepare the chat prompt 
chat_prompt = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Capital of Delhi."
            }
        ]
    }
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt  
    
# Generate the completion  
completion = client.chat.completions.create(  
    model="gpt-4o",
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False
)

print(completion.to_json())  
    