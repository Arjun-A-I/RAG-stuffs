import os
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader

loader = DirectoryLoader(
    os.path.abspath("./source_docs"),
    glob="**/*.pdf",
    # use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
    sample_size=1
)

docs = loader.load()

with open('out.txt', 'w', encoding='utf-8') as f:
    for doc in docs:
        text_content = doc.page_content  # Assuming `text_content` is the attribute holding the text
        f.write(text_content + '\n')  # Writing the text content to the file
