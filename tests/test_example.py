from botok.tokenizers.wordtokenizer import WordTokenizer

from filter_bad_stt_mv_transcript.filter_stt_mv_utils import process_transcript

# Initialize the tokenizer
tokenizer = WordTokenizer()
text = "འཁྱེད་ལ་སུན་པོ་ཀཟོས་པར་དགོངས་དག་ཞུ་ཨུམ་ཨུམ་་་།"


def test_process_transcript():
    exepcted_non_word_count = 4
    expected_total_tokens = 10
    non_word_count, total_tokens = process_transcript(text, tokenizer)
    assert non_word_count == exepcted_non_word_count
    assert total_tokens == expected_total_tokens
