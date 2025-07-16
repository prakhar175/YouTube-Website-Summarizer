# URL & YouTube Summarizer

A Streamlit-based web application that provides intelligent summarization of content from URLs and YouTube videos using LangChain and Groq's language models.

## Features

- **Multi-Source Support**: Summarize content from any valid URL or YouTube video
- **Multiple AI Models**: Choose from Llama-4, Mistral, Gemma 2, and Llama-3.3 models
- **Smart Content Detection**: Automatically detects YouTube URLs and handles them appropriately
- **Customizable Summaries**: Generates concise summaries (max 300 words)
- **User-Friendly Interface**: Clean, responsive Streamlit interface with sidebar controls

## Prerequisites

Before running the application, ensure you have:

- Python 3.8 or higher (suggested 3.10)
- A valid Groq API key (obtain from [Groq Console](https://console.groq.com/))
- Internet connection for content fetching

## Installation

1. **Clone the repository** (or save the script as `app.py`)

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Configure the application**:
   - Enter your Groq API key in the sidebar
   - Select your preferred AI model from the dropdown
   - Paste the URL you want to summarize

3. **Generate summary**:
   - Click the "Summarize" button
   - Wait for the AI to process the content
   - View the generated summary

## Supported Models

| Model | Description |
|-------|-------------|
| **Llama-4** | Advanced reasoning and comprehension |
| **Mistral** | Efficient multilingual processing |
| **Gemma 2** | Balanced performance and speed |
| **Llama-3.3** | Robust general-purpose model |

## Content Sources

### YouTube Videos
- Automatically extracts video transcripts/captions
- Handles various YouTube URL formats
- Requires videos to have available subtitles/captions

### Web URLs
- Extracts text content from web pages
- Handles various content types (articles, blogs, news)
- Uses custom headers to avoid blocking

## Error Handling

The application includes comprehensive error handling for:
- Invalid URLs
- Missing API keys
- Videos without captions
- Network connectivity issues
- Content extraction failures

## Configuration

### API Key Setup
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and generate an API key
3. Enter the key in the sidebar (stored securely during session)

### Model Selection
Choose the appropriate model based on your needs:
- **Llama-4**: Best for complex content requiring deep understanding
- **Mistral**: Optimal for multilingual content
- **Gemma 2**: Good balance of speed and accuracy
- **Llama-3.3**: Reliable for general summarization tasks

## Limitations

- YouTube videos must have available transcripts/captions
- Content length limitations based on model context windows
- Rate limiting based on Groq API quotas
- Some websites may block automated content extraction

## Troubleshooting

### Common Issues

**"No captions found for this video"**
- Ensure the YouTube video has subtitles/captions enabled
- Try a different video with available transcripts

**"NOT a valid URL"**
- Verify the URL format is correct
- Ensure the URL includes the protocol (http:// or https://)

**API Key Errors**
- Verify your Groq API key is valid and active
- Check your API quota and usage limits

## Technical Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │────│   LangChain      │────│   Groq Models   │
│                 │    │   Processing     │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
    ┌─────────┐           ┌─────────────┐        ┌──────────────┐
    │ Content │           │ Document    │        │ Summary      │
    │ Loaders │           │ Processing  │        │ Generation   │
    └─────────┘           └─────────────┘        └──────────────┘
```
## License

This project is open-source and available under the MIT License.

## Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Refer to the official documentation of dependencies
