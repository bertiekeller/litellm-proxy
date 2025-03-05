import openai  # Import the openai library.  This assumes openai version 1.0.0 or higher.

# Configure the OpenAI client to use the proxy.
# api_key is set to "anything" because it's not actually used when a proxy is set.
# base_url is set to "http://0.0.0.0:4000" which is the default address for the LiteLLM proxy.
client = openai.OpenAI(api_key="anything", base_url="http://0.0.0.0:4000")

# Create a chat completion request using the client.
# The model used will be the one set in the LiteLLM proxy using `litellm --model`.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Specify the model to use (this will be overridden by the proxy).
    messages=[
        {
            "role": "user",  # Define the role of the message as a user.
            "content": "this is a test request, write a short poem",  # The content of the user's message.
        }
    ],
)

# Print the response from the chat completion.
print(response)