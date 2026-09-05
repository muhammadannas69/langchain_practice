# Structured Output with LangChain & Google Gemini

This project provides a unified guide and code implementations for extracting structured data from Google Gemini using **LangChain** (`langchain-google-genai`). It covers multiple schema definition patterns including `TypedDict`, raw **JSON Schema**, and **Pydantic** models.

---

## 📋 Overview of Concepts

1. **TypedDict with `Annotated`**: Use Python native `TypedDict` and `Annotated` metadata to define expected fields and docstrings for the LLM.
2. **JSON Schema**: Pass raw JSON Schema dicts to `model.with_structured_output()` for strict structural validation.
3. **Pydantic `BaseModel`**: Define robust data structures with strict field validation rules (e.g., bounds `gt`/`lt`, email formats, default values).
4. **Structured Parsing**: Direct model invocation returning clean Python objects or typed dictionaries.

---

## 🛠 Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Google Gemini API Key

### 2. Environment Setup
Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here