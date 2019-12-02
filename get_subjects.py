import spacy

nlp = spacy.load('ja_ginza')

def parse_document(sentence):
    doc = nlp(sentence)
    tokens = []

    ## 参照しやすいようにトークンのリストを作る
    for sent in doc.sents:
        for token in sent:
            tokens.append(token)

    ## 主語述語ペアのリスト
    subject_list = []

    for token in tokens:
        ## 依存関係ラベルがnsubjがあれば「＜見出し語＞:＜係り先の見出し語＞」をリストに追加する。
        if  token.dep_ in ["nsubj", "iobj"]:
            subject_list.append(f"{token.lemma_}:{tokens[token.head.i].lemma_}")
    
    return subject_list