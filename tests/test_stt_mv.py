from bo_text_analyzer.text_analyzer import TextAnalyzer as ta
from config import DATA_DIR

from filter_bad_stt_mv_transcript.filter_stt_mv import (
    add_columns_to_df,
    read_tsv_file,
    save_df_to_tsv,
)


def test_add_columns():
    input_file = DATA_DIR / "test_input.tsv"
    expected_output_file = DATA_DIR / "expected_output.tsv"
    output_file = DATA_DIR / "test_output.tsv"

    text_analyzer = ta(0.02, 0.02)

    df = read_tsv_file(input_file)

    expected_df = read_tsv_file(expected_output_file)

    df_processed = add_columns_to_df(df, text_analyzer)

    save_df_to_tsv(df_processed, output_file)

    assert df_processed.equals(expected_df)
