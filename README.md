# LiteLLM Proxy Project

## Overview

This project demonstrates how to use LiteLLM as a proxy for AI model requests, providing a flexible and unified interface for interacting with different AI language models.

## Prerequisites

- Python 3.8+
- pip package manager
- Internet connection

## Installation

1. Install LiteLLM:
   ```bash
   pip install litellm
   ```

2. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd litellm-proxy
   ```

## Project Structure

```
litellm/
│
├── start.py         # Example script demonstrating LiteLLM proxy usage
└── README.md        # This documentation
```

## Running the LiteLLM Proxy

### Start the Proxy Server

```bash
# Basic proxy setup for OpenAI's GPT-3.5-turbo
litellm --model openai/gpt-3.5-turbo
```

### Running the Example Script

```bash
python start.py
```

## Key Features

- **Unified API**: Simplifies interactions with multiple AI model providers
- **Local Proxying**: Allows local testing and routing of AI requests
- **Flexible Configuration**: Easy to switch between different models and providers

## Configuration Options

### Supported Model Providers

LiteLLM supports various providers, including:
- OpenAI
- Anthropic
- Google
- Cohere
- Azure OpenAI
- And many more!

### Proxy Configuration

Modify the `start.py` script to customize:
- Base URL
- API Key
- Model Selection

## Example Code Breakdown

```python
import openai

# Configure client with proxy settings
client = openai.OpenAI(
    api_key="anything",  # Placeholder for proxy
    base_url="http://0.0.0.0:4000"  # Local proxy endpoint
)

# Make a chat completion request
response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[{
        "role": "user",
        "content": "Write a short poem"
    }]
)

print(response)
```

## Troubleshooting

- Ensure the proxy server is running before executing the script
- Check your internet connection
- Verify API keys and base URLs
- Install required dependencies

## Advanced Usage

For more complex configurations, refer to the [LiteLLM Documentation](https://docs.litellm.ai/)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/litellm-proxy](https://github.com/yourusername/litellm-proxy)