from urllib import request
import urllib.parse
import re
import nltk
while True:
	try:
		inpt=input("What Do You Want To Know:")
		inpt=inpt.lower()
		listfor20=inpt.split(" ")
		inpt1="%20".join(listfor20)
		if inpt=="q" or inpt=="quit":
			break
		resp=request.urlopen("https://www.wikiwand.com/en/{}".format(inpt1))
		data=resp.read()
		html=data.decode("UTF-8")
		paragraphs=re.findall(r'<meta (.*?)>',str(html))
		s=[]
		senteces_words=[]

		for i in paragraphs:
			s.append(i)
		s[14]=str(s[14])
		tokinze_sent=nltk.sent_tokenize(s[14])

		tokenize_word=nltk.word_tokenize(tokinze_sent[0])
		real_sentence_list=list()
		real_sentece_string=""	
		for k in tokenize_word:
			if k.startswith(".") or k.startswith(":") or k.startswith("property") or k.startswith("''") or k.startswith("content") or k.startswith("=") or k.startswith("og") or k.startswith("description"):
				pass
			else:
				real_sentence_list.append(k)

		for j in real_sentence_list:
			real_sentece_string+=j+" "
		print("\n"+"-"*110)
		print(real_sentece_string)
		print("-"*110+"\n")
	except:
		print("I cant search that :/")