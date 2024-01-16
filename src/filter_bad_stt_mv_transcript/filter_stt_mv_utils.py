def process_transcript(text, tokenizer):
    tokens = tokenizer.tokenize(text)
    non_word_count = sum(
        1 for token in tokens if token.pos == "NON_WORD" and not token.skrt
    )
    total_tokens = len(tokens)
    return non_word_count, total_tokens
