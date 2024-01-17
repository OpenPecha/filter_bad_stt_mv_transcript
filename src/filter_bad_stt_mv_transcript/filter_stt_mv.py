import pandas as pd
from bo_text_analyzer.text_analyzer import TextAnalyzer as ta


def read_tsv_file(file_path):
    return pd.read_csv(file_path, sep="\t", encoding="utf-8")


def process_transcript(text, text_analyzer):
    tokens = text_analyzer.tokenize_text(text)
    non_word_count = text_analyzer.count_non_words(tokens)
    total_tokens = len(tokens)
    return non_word_count, total_tokens


def add_columns_to_df(df, text_analyzer):
    df["non_word_count"], df["total_tokens"] = zip(
        *df["uni"].apply(lambda text: process_transcript(text, text_analyzer))
    )
    df["non_word_percentage"] = (df["non_word_count"] / df["total_tokens"]) * 100
    df.fillna(0, inplace=True)  # Replace NaN values with 0 in case of division by zero
    return df


def save_df_to_tsv(df, file_path):
    df.to_csv(file_path, sep="\t", index=False, encoding="utf-8")


# Main execution
if __name__ == "__main__":
    input_file = "/home/gangagyatso/Desktop/project13/filter_bad_stt_mv_transcript/data/test_input.tsv"
    output_file = "/home/gangagyatso/Desktop/project13/filter_bad_stt_mv_transcript/data/test_output.tsv"
    text_analyzer = ta(0.02, 0.02)

    df = read_tsv_file(input_file)
    print(df.head())
    df_processed = add_columns_to_df(df, text_analyzer)
    print(df_processed.head())
    save_df_to_tsv(df_processed, output_file)

    # Filter and display DataFrame based on threshold
    threshold = 2.0
    filtered_df = df_processed[df_processed["non_word_percentage"] > threshold]
    print(filtered_df.head())
