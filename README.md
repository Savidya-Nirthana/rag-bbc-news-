# BBC News Articles Weaviate Indexing and Search

This notebook demonstrates how to load BBC news articles, index them into a Weaviate vector database, and perform various search operations.

## Notebook Contents:

1.  **Setup and Imports**: Imports necessary libraries like `joblib` and `weaviate`, and loads extensions.
2.  **Data Loading**: Loads BBC news article data from a `joblib` file.
3.  **Data Exploration**: Prints properties of a few sample articles to understand the data structure.
4.  **Weaviate Connection**: Connects to a Weaviate cloud instance using API keys.
5.  **Collection Creation**: Creates a `bbc_news` collection in Weaviate with vector and generative configurations.
6.  **Data Indexing**: Batches and adds the BBC news articles to the `bbc_news` collection in Weaviate.
7.  **Verify Indexing**: Checks the number of objects indexed in the collection and retrieves a sample object with its vector.
8.  **Metadata Filtering**: Implements and demonstrates searching for articles based on metadata properties (e.g., title).
9.  **Semantic Search**: Implements and demonstrates semantic search using `near_text` query.
10. **Keyword Search (BM25)**: Implements and demonstrates keyword-based search using `bm25` query.
11. **Hybrid Search**: Implements and demonstrates hybrid search combining semantic and keyword search.
12. **Reranking (Attempt)**: Includes commented-out code for reranking search results, highlighting potential issues with module availability.
13. **Prompt Generation for RAG**: Defines a function to generate a prompt for a Language Model using retrieved data for Retrieval Augmented Generation (RAG).
14. **LLM Integration (Groq)**: Uses the Langchain library to integrate with a Groq LLM and generate a response based on a query and retrieved data.

## How to Use:

1.  Ensure you have a Weaviate instance running and accessible.
2.  Obtain a Weaviate API key and a Groq API key and add them to your Colab secrets named `WEAVIATE_API` and `GROQ_API` respectively.
3.  Upload the `bbc_data.joblib` file and the `utils.py` file (containing the `print_object_properties` function) to your Colab environment.
4.  Run the cells sequentially.

This README provides a high-level overview. Refer to the notebook for detailed code and explanations.
