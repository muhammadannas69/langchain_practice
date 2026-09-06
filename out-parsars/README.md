# LangChain Structured Output & Chains

This project contains simple LangChain examples using Google Gemini and different output parsing techniques.

## Topics Covered

### 1. Sequential Chain

Creates a chain that:

- Generates detailed information about a topic.
- Converts the generated text into a short summary.
- Uses `PromptTemplate`, `StrOutputParser`, and LCEL (`|`) syntax.

Flow:

```text
PromptTemplate
      ↓
Gemini Model
      ↓
StrOutputParser
      ↓
PromptTemplate
      ↓
Gemini Model
      ↓
StrOutputParser