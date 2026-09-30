## Caution the library used here for web search, are not stable, they might go to the bad websites(Write your own scrapper.)

## Create virtual env

```bash
python3 -m venv env_prompting[n]
source env_prompting1/bin/activate
pip install -r requirements.txt
```

`chains_n_m.py` are langchain implementation, `research_engine_seq.py` is python default implementation.

### Prompt engineering shapes three critical stages:
- Search query generation—Converting broad questions into specific, targeted search terms
- Content summarization—Extracting key facts and arguments from raw web pages
- Report generation—Combining partial summaries into coherent findings with citations

### LangChain Expression Language (LCEL)

LCEL chains operations using the pipe operator (`|`) to compose sequential transformations. Each component’s output becomes the next component’s input automatically.

- `RunnableParallel` enables simultaneous execution of multiple operations on the same input. Wrap operations in `RunnableParallel({"key1": operation1, "key2": operation2})` to run them concurrently.
- The `.map()` operator triggers multiple chain instances, one for each item in a list. Use `chain.map()` to process URLs or search results in parallel, with each instance running simultaneously.
- `RunnableLambda` wraps Python functions for use in LCEL chains. Import with:

    ```python
    from langchain_core.runnables import RunnableLambda
    ```

    and use `RunnableLambda(lambda x: your_function(x))`.

- Chains implement the Runnable protocol with the following methods:
    - `.invoke()` (single execution)
    - `.stream()` (streaming output)
    - `.batch()` (batch processing)

    Each method has asynchronous versions for concurrent operations.

- Build chains modularly by creating separate chains for search query generation, URL fetching, content extraction, and summarization. Combine them with LCEL for a clean, maintainable architecture.
- `RunnablePassthrough` preserves input while allowing additional operations. Use it to pass the original question through the chain while also generating search queries from it.