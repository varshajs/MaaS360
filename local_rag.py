import os
import sys
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.web import SimpleWebPageReader

# ==========================================
# 1. SETUP: MISTRAL ON MAC
# ==========================================
print("🚀 Connecting to Ollama (Mistral)...")

# Use Mistral running locally
Settings.llm = Ollama(model="mistral", request_timeout=60.0)

# Use standard embeddings
print("⏳ Loading Embeddings...")
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# ==========================================
# 2. LOAD DATA (PDFs + Links)
# ==========================================
DATA_DIR = "./data"
LINKS_FILE = "links.txt"
all_documents = []

print(f"\n📂 Scanning '{DATA_DIR}' for content...")

# --- A. Load PDFs ---
if os.path.exists(DATA_DIR):
    pdf_docs = SimpleDirectoryReader(DATA_DIR).load_data()
    all_documents.extend(pdf_docs)
    print(f"   -> Found {len(pdf_docs)} PDF pages.")
else:
    print(f"❌ ERROR: Folder '{DATA_DIR}' not found. Please create it.")
    sys.exit()

# --- B. Load Links from links.txt ---
links_path = os.path.join(DATA_DIR, LINKS_FILE)
target_urls = []

if os.path.exists(links_path):
    print(f"   -> Found links file: {LINKS_FILE}")
    with open(links_path, "r") as f:
        # Read lines, strip whitespace, and ignore empty lines
        target_urls = [line.strip() for line in f if line.strip()]
    
    if target_urls:
        print(f"   -> Scraping {len(target_urls)} websites...")
        try:
            # html_to_text=True cleans the website to plain text
            web_docs = SimpleWebPageReader(html_to_text=True).load_data(target_urls)
            all_documents.extend(web_docs)
            print(f"   -> ✅ Website content loaded.")
        except Exception as e:
            print(f"   -> ⚠️ Warning: Could not scrape some sites. Error: {e}")
else:
    print(f"   -> ℹ️ No '{LINKS_FILE}' found in data folder. Skipping.")

# ==========================================
# 3. INDEXING & CHAT
# ==========================================
if not all_documents:
    print("❌ No data found (PDFs or Links). Exiting.")
    sys.exit()

print(f"\n🧠 Indexing {len(all_documents)} documents (This runs on your M4 Max)...")
index = VectorStoreIndex.from_documents(all_documents)
query_engine = index.as_query_engine(similarity_top_k=5)

print("\n" + "="*50)
print("✅ Local RAG Ready! I know your PDFs and Links.")
print("="*50 + "\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    
    print("Thinking...")
    response = query_engine.query(user_input)
    print(f"\nMistral: {response}\n{'-'*30}")