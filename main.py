#!/usr/bin/env python
# coding: utf-8


# ██████╗   ███████╗ ██╗    ██╗ ███████╗            ██████╗    ██████╗             ██████╗   ██████╗    ██████╗   ███████╗
# ██╔══██╗ ██╔════╝ ██║    ██║ ██╔════╝            ██╔══██╗ ██╔═══██╗         ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝
# ██║    ██║ █████╗     ██║    ██║ ███████╗            ██║    ██║ ██║      ██║         ██║           ██║      ██║ ██║    ██║ █████╗  
# ██║    ██║ ██╔══╝    ╚██╗  ██╔╝ ╚════██║           ██║    ██║ ██║      ██║         ██║           ██║      ██║ ██║    ██║ ██╔══╝  
# ██████╔╝ ███████╗  ╚████╔╝  ███████║            ██████╔╝╚██████╔╝         ╚██████╗ ╚██████╔╝  ██████╔╝ ███████╗
# ╚═════╝  ╚══════╝    ╚═══╝     ╚══════╝            ╚═════╝    ╚═════╝             ╚═════╝   ╚═════╝    ╚═════╝   ╚══════╝


# # Made With 💓 By - [Devs Do Code](https://www.youtube.com/channel/@devsdocode)
# 
# 
# For any questions or concerns, reach out to us via our social media handles. Our top choice for contact is [Telegram](https://t.me/devsdocode). You can also find us on other platforms listed above. We're here to help!
# 
# - **YouTube Channel**: [https://www.youtube.com/@DevsDoCode](https://www.youtube.com/@DevsDoCode)
# - **Telegram Group**: [https://t.me/devsdocode](https://t.me/devsdocode)
# - **Discord Server**: [https://discord.gg/ehwfVtsAts](https://discord.gg/ehwfVtsAts)
# - **Instagram**:
#   - **Personal**: https://www.instagram.com/sree.shades_/
#   - **Channel**: https://www.instagram.com/devsdocode_/
# 
# ---
# 
# 🚀 Dive into the world of coding with [Devs Do Code](https://www.youtube.com/channel/@devsdocode) - where passion meets programming! Make sure to hit that Subscribe button to stay tuned for exciting content! 😊✨
# 
# **Pro Tip:** For optimal performance and a seamless experience, we recommend using the default library versions demonstrated in this demo. Your coding journey just got even better! Happy coding! 🖥️💻
# 

# # Overview

# ### Imports

# Importing Required Modules
import requests


# ### Defining Required Payloads

# Define the API endpoint URL

url = "https://alkalimakersuite-pa.clients6.google.com/$rpc/google.internal.alkali.applications.makersuite.v1.MakerSuiteService/GenerateContent"
model = "models/gemini-1.5-pro-latest"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
origin_url = "https://aistudio.google.com"
content_type = "application/json+protobuf"

# Authorization Tokens. 
# Could be Found in the Cookie list of https://aistudio.google.com/ 
# or Check out the Response Headers of a request made in from gemini 1.5 Pro Model (Check the Network Tab in the Developers Console for more infromation)

Authorization = ""
Cookie = ""
X_Google_Api_Key = ""
User_id = ""


# Other Tuning Parameters (Optional)

max_tokens = 8192
temperature = 2
top_p = 0.4

stop_words = None
safety_settings = None
system_prompt = None

# Formatted Other Params
other_params = [[[None, None, 7, 2], [None, None, 8, 2], [None, None, 9, 2], [None, None, 10, 2]], [stop_words, safety_settings, system_prompt, max_tokens, temperature, top_p, 32]] 


# ### Requesting Endpoint

# Requesting Endpoint

# Set up the request headers
headers = {
    "Content-Type": content_type,
    "Authorization": Authorization,
    "Cookie": Cookie,
    "Origin": origin_url,
    "User-Agent": user_agent,
    "X-Goog-Api-Key": X_Google_Api_Key
}

# Prepare the payload data
payload = [
    model,
    [[[[None, "write something about the beauty of india"]], "user"]],
    other_params[0],
    other_params[1],
    User_id]

# Make a POST request to the API endpoint with the payload data and headers
response = requests.post(url, json=payload, headers=headers)

# Handle the response
if response.status_code == 200:
    print(response.text)
else:
    # If there was an error, print the error message
    print("Error:", response.status_code, response.reason)


# # Final Punchline

# #### Functions

# Function to extract the response content

def extract_before_model(data_list):
    extracted_list = []  # Initialize an empty list to store extracted strings
    
    # Iterate through the nested lists to find strings before "model"
    for item in data_list:
        if isinstance(item, list):  # Check if the item is a list
            extracted_list.extend(extract_before_model(item))  # Recursively call the function to handle nested lists
        elif isinstance(item, str) and item.strip() == 'model':  # Check if the item is "model"
            break  # Stop iterating when "model" is found
        elif isinstance(item, str):  # Check if the item is a string
            extracted_list.append(item)  # Add the string to the list
    
    return extracted_list

# format the output

def formatter(json_response):
    content = ""
    for object_string in json_response[0]:
        extracted_content = extract_before_model(object_string)
        content = content + extracted_content[0]

    return content

# Main Function

def Gemini_1_5(query):

    # Set up the request headers
    headers = {
        "Content-Type": content_type,
        "Authorization": Authorization,
        "Cookie": Cookie,
        "Origin": origin_url,
        "User-Agent": user_agent,
        "X-Goog-Api-Key": X_Google_Api_Key
    }

    # Prepare the payload data
    payload = [
        model,
        [[[[None, query]], "user"]],
        other_params[0],
        other_params[1],
        User_id
        ]

    # Make a POST request to the API endpoint with the payload data and headers
    response = requests.post(url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 200:
        output = formatter(response.json())
        return output
    else:
        # If there was an error, print the error message
        print("Error:", response.status_code, response.reason)


# #### Calling the Function

# Testing and debugging

output = Gemini_1_5("Describe about the beauty of India")
print(output)

