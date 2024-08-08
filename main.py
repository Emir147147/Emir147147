meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FAKE":"Sahte olan",
            "TROLL":"İronik bir şey"}
            
            
            
word = input("Anlamadığınız bir kelime girin:")            

if word in meme_dict.keys():
    print("Girdiğiniz kelimenin anlamı:",meme_dict[word])
    
else:
    print("Üzgünüm girdiğiniz kelime bulunmamaktadır")
