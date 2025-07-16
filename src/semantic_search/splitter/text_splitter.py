from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_text_splitter(
    chunk_size: int = 1000, chunk_overlap: int = 200, add_start_index: bool = True
) -> RecursiveCharacterTextSplitter:
    """テキストの分割を行う"""
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, add_start_index=add_start_index
    )
