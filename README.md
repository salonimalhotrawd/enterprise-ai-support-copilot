# Enterprise AI Support Copilot

**An Agentic AI-powered Enterprise IT Support Assistant built using Generative AI, Retrieval-Augmented Generation (RAG), and LangGraph.**

## Project Overview

Enterprise AI Support Copilot is an intelligent IT support automation application designed to simplify and streamline enterprise IT support operations.

The application uses Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Agentic AI to understand employee queries, retrieve relevant information from internal IT documentation, and perform support-related operations through intelligent tool selection.

Powered by **Google Gemini and LangGraph**, the system provides three core capabilities:

1. **Knowledge Search:** Answers employee IT-related questions using internal PDF, TXT, and DOCX documentation through a RAG pipeline, providing contextually relevant and source-grounded responses.
2. **Ticket Lookup:** Retrieves existing IT support ticket information using ticket IDs or employee IDs from an SQLite database.
3. **Ticket Creation:** Creates new IT support tickets with structured input validation, duplicate detection, and user confirmation.

The application uses ChromaDB for vector storage, Sentence Transformers for embedding generation, SQLite for ticket management, and Streamlit for an interactive enterprise dashboard.

The LangGraph-based orchestration layer enables intelligent tool selection, conditional workflow execution, state management, and conversational context retention.

## Key Objectives

- Automate repetitive enterprise IT support operations.
- Provide accurate, context-aware answers using internal knowledge sources.
- Enable intelligent interaction with structured ticket management systems.
- Demonstrate practical implementation of Agentic AI and RAG architectures.
- Build a modular and extensible enterprise AI application.

## Technology Stack

- Python
- LangChain
- LangGraph
- Google Gemini
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- ChromaDB
- SQLite
- Pydantic
- Streamlit
- Pytest

## Project Type

IIT Patna – Generative AI & Agentic AI Certification Capstone Project.

**Focus Areas:** Generative AI | Agentic AI | RAG | LangGraph | LLM Tool Calling | Vector Databases | AI Automation
