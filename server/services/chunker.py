import uuid
import textwrap

def chunk_text_blocks(blocks: list[dict], max_chunk_size: int = 500) -> list[dict]:
    all_chunks = []

    for block in blocks:
        source = block.get("source_file", "unknown")
        origin = block.get("page") or block.get("sheet") or "unknown"
        base_metadata = {
            "source_file": source,
            "origin": origin,
            "type": block.get("type"),
        }

        # Clean and wrap text into chunks
        wrapped = textwrap.wrap(block["text"], max_chunk_size, break_long_words=False, break_on_hyphens=False)

        for i, chunk in enumerate(wrapped):
            all_chunks.append({
                "chunk_id": str(uuid.uuid4()),
                "text": chunk,
                "chunk_index": i,
                **base_metadata
            })

    return all_chunks
