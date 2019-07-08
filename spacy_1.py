import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"This is a sentence.")

import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp(u"This is a sentence.")

def test_common_doc_tokens(NLP):
    doc = NLP("Lorem ipsum dolor sit amet.")
    assert len(doc) > 1
    
@pytest.mark.requires('parser', 'tagger')
def test_that_requires_tagger_and_parser(NLP):
  assert 'parser' in NLP.pipe_names
  assert 'tagger' in NLP.pipe_names
