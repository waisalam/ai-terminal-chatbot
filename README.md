# Terminal GPT (Learning Project)

This is a simple terminal-based GPT-style AI assistant built using open-source Large Language Models and Hugging Face Transformers.

The purpose of this project is to learn how modern AI systems actually work behind the scenes instead of only using APIs like ChatGPT or Gemini.

This project helped me learn:

* How open-source LLMs run locally
* Text generation using Transformers
* Prompt formatting
* Tokenization
* GPU acceleration with PyTorch + CUDA
* Model loading and inference
* Chat-style prompting
* Running AI models directly from terminal

## Features

* Runs completely locally
* Uses open-source models like Phi-2
* Accepts terminal prompts
* Generates AI responses in terminal
* Supports GPU acceleration (CUDA)
* Simple GPT-like interaction loop

## Example

```bash
you: can you help with my career

assistant:
Of course! I'd be happy to help you with your career...
```

## Important Note

This project is mainly built for learning and experimentation.

If you run this project for the first time, the AI model may automatically download very large files (around 5GB+ depending on the model).

Example:

* `microsoft/phi-2` → approximately 5GB

So make sure you have:

* Stable internet connection
* Enough storage space
* Python 3.11 recommended
* NVIDIA GPU recommended for faster generation

## Tech Used

* Python
* PyTorch
* Hugging Face Transformers
* CUDA
* Open-source LLMs

## Future Improvements

Planned future improvements include:

* Streaming responses
* Chat memory
* Voice support
* RAG pipelines
* Multi-model workflows
* Fine-tuned coding assistant
* Local AI agent system

This project is not production-ready and is being actively used to learn AI engineering by building real systems from scratch.
