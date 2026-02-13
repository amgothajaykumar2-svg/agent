# LangSmith Integration Guide

## What is LangSmith?
LangSmith is a platform for debugging, testing, and monitoring LLM applications. It provides:
- **Tracing**: See every step of your agent's execution
- **Debugging**: Identify issues in your agent workflow
- **Monitoring**: Track performance and costs
- **Testing**: Evaluate your agent's responses

## Setup

### 1. Get Your LangSmith API Key
1. Go to https://smith.langchain.com
2. Sign up or log in
3. Navigate to Settings → API Keys
4. Create a new API key
5. Copy the key (starts with `lsv2_pt_...`)

### 2. Update Your .env File
Replace the placeholder API key in `.env` with your actual key:

```bash
LANGCHAIN_API_KEY=lsv2_pt_YOUR_ACTUAL_KEY_HERE
```

### 3. Configuration Options
The following environment variables are already set in your `.env`:

- `LANGCHAIN_TRACING_V2=true` - Enables tracing
- `LANGCHAIN_ENDPOINT=https://api.smith.langchain.com` - LangSmith API endpoint
- `LANGCHAIN_PROJECT=agent-research-system` - Project name in LangSmith

You can change the project name to organize your traces better.

## Usage

Once configured, LangSmith will automatically trace all your agent executions when you run:

```bash
python main.py
```

## Viewing Traces

1. Go to https://smith.langchain.com
2. Navigate to your project: `agent-research-system`
3. You'll see all traces with:
   - Input/output for each agent
   - Tool calls (search results)
   - Timing information
   - Token usage
   - Error logs (if any)

## Benefits

- **Debug faster**: See exactly where your agent fails
- **Optimize performance**: Identify slow steps
- **Track costs**: Monitor API usage and costs
- **Improve quality**: Analyze agent responses over time

## Disable Tracing

To disable tracing temporarily, set in `.env`:
```bash
LANGCHAIN_TRACING_V2=false
```

Or remove the environment variable entirely.
