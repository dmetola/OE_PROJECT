import stanza

nlp = stanza.Pipeline(
    lang='en', 
    processors='tokenize, lemma', 
    tokenizer_model_path='saved_models/tokenize/ang_test_tokenizer.pt',
    lemmatizer_model_path='saved_models/lemma/ang_test_lemmatizer.pt'
)