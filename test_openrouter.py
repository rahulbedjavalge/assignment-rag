import os
import sys

# Set environment variables directly
os.environ['OPENROUTER_API_KEY'] = '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'
os.environ['OPENROUTER_MODEL'] = 'allenai/molmo-2-8b:free'
os.environ['OPENROUTER_SITE_URL'] = 'http://localhost'
os.environ['OPENROUTER_APP_NAME'] = 'AssignmentRAG'

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'assignment-rag', 'src'))

from assignment_rag.llm.openrouter import chat

# Test the chat function
messages = [{"role": "user", "content": "What is Retrieval Augmented Generation (RAG) in 2-3 sentences?"}]

try:
    print("🚀 Running OpenRouter API test...\n")
    response, data = chat(messages, model="allenai/molmo-2-8b:free")
    print("✅ Success!\n")
    print("Response:")
    print(response)
    print("\n" + "="*60)
    print(f"Model: {data['model']}")
    print(f"Completion tokens: {data['usage']['completion_tokens']}")
    print(f"Prompt tokens: {data['usage']['prompt_tokens']}")
    print("="*60)
except Exception as e:
    print("❌ Error:", str(e))
    import traceback
    traceback.print_exc()
