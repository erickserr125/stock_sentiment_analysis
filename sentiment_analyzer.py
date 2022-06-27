#from transformers import AutoTokenizer
#from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

#MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
#tokenizer = AutoTokenizer.from_pretrained(MODEL)
#model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def sentiment_scoring(sentence, model, tokenizer):
    encoded_text = tokenizer(sentence, return_tensors='pt')
    output = model(**encoded_text)
    scores = softmax(output[0][0].detach().numpy())

    scores_dict = {
        'neg':scores[0],
        'neu':scores[1],
        'pos':scores[2],
    }
    return scores_dict

#scores = sentiment_scoring("THIS PLACE blows haha", model, tokenizer)
#print(scores)