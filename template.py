
from pathlib import Path

# ==========================================
# Enterprise AI Support Copilot
# Project Structure Generator
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent

# ------------------------------------------
# 1. Folder Structure
# ------------------------------------------

folders = [
    "config",

    "data/knowledge_base",

    "chroma_db",
    "logs",

    "src",
    "src/rag",
    "src/database",
    "src/schemas",
    "src/tools",
    "src/agents",
    "src/graph",
    "src/prompts",
    "src/ui",
    "src/utils",

    "tests",
    "tests/rag",
    "tests/database",
    "tests/tools",
    "tests/graph",
]

# ------------------------------------------
# 2. File Structure
# ------------------------------------------

files = {

    # Root files
    "app.py": "",
    "requirements.txt": "",
    ".env.example": "GOOGLE_API_KEY=your_google_api_key\n",

    # Configuration
    "config/settings.py": "",

    # Source package
    "src/__init__.py": "",

    # RAG module
    "src/rag/__init__.py": "",
    "src/rag/ingestion.py": "",
    "src/rag/splitter.py": "",
    "src/rag/embeddings.py": "",
    "src/rag/vector_store.py": "",
    "src/rag/retriever.py": "",

    # Database module
    "src/database/__init__.py": "",
    "src/database/connection.py": "",
    "src/database/models.py": "",
    "src/database/ticket_repository.py": "",

    # Pydantic schemas
    "src/schemas/__init__.py": "",
    "src/schemas/ticket_schema.py": "",

    # Agent tools
    "src/tools/__init__.py": "",
    "src/tools/knowledge_search.py": "",
    "src/tools/ticket_lookup.py": "",
    "src/tools/ticket_creation.py": "",

    # Agents
    "src/agents/__init__.py": "",

    # LangGraph
    "src/graph/__init__.py": "",
    "src/graph/state.py": "",
    "src/graph/nodes.py": "",
    "src/graph/edges.py": "",
    "src/graph/workflow.py": "",

    # Prompts
    "src/prompts/system_prompt.py": "",

    # Streamlit UI
    "src/ui/__init__.py": "",

    # Utilities
    "src/utils/__init__.py": "",
    "src/utils/helpers.py": "",

    # Tests
    "tests/__init__.py": "",
    "tests/rag/__init__.py": "",
    "tests/database/__init__.py": "",
    "tests/tools/__init__.py": "",
    "tests/graph/__init__.py": "",
}

# ------------------------------------------
# 3. Create Folders
# ------------------------------------------

for folder in folders:
    folder_path = PROJECT_ROOT / folder
    folder_path.mkdir(parents=True, exist_ok=True)

# ------------------------------------------
# 4. Create Files
# ------------------------------------------

created_files = []
existing_files = []

for file_path, content in files.items():

    path = PROJECT_ROOT / file_path

    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")
        created_files.append(file_path)

    else:
        existing_files.append(file_path)

# ------------------------------------------
# 5. Add .gitkeep to Empty Data Folders
# ------------------------------------------

gitkeep_folders = [
    "data/knowledge_base",
    "chroma_db",
    "logs",
]

for folder in gitkeep_folders:

    gitkeep_path = PROJECT_ROOT / folder / ".gitkeep"

    if not gitkeep_path.exists():
        gitkeep_path.touch()

# ------------------------------------------
# 6. Display Summary
# ------------------------------------------

print("\n" + "=" * 55)
print(" ENTERPRISE AI SUPPORT COPILOT")
print(" PROJECT STRUCTURE GENERATION")
print("=" * 55)

print(f"\nProject root: {PROJECT_ROOT}")

print(f"\nFolders defined: {len(folders)}")
print(f"New files created: {len(created_files)}")
print(f"Existing files preserved: {len(existing_files)}")

print("\nCreated files:")

for file in created_files:
    print(f"  + {file}")

print("\nExisting files preserved:")

for file in existing_files:
    print(f"  = {file}")

print("\nProject structure created successfully!")
print("=" * 55)
