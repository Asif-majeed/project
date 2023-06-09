
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import textblob

def summarize():
    url = utext.get('1.0',"end").strip()

    article = Article(url)
    
    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    


    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = textblob(article.text) 
   
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    

root = tk.Tk()
root.title("news Summarizer")
root.geometry('1200x600')

tlable = tk.Label(root, text="Title")
tlable.pack()

title = tk.Text(root,height=1,width=140)
title.config(state='disable', bg='#dddddd')
title.pack()

alable = tk.Label(root, text="Author")
alable.pack()

author = tk.Text(root,height=1,width=140)
author.config(state='disable', bg='#dddddd')
author.pack()

plable = tk.Label(root, text="Publishing Date")
plable.pack()

publication = tk.Text(root,height=1,width=140)
publication.config(state='disable', bg='#dddddd')
publication.pack()

slable = tk.Label(root, text="Summary")
slable.pack()

summary = tk.Text(root,height=20,width=140)
summary.config(state='disable', bg='#dddddd')
summary.pack()

selable = tk.Label(root, text="Sentiment Analysis")
selable.pack()


ulable = tk.Label(root, text="URL")
ulable.pack()

utext = tk.Text(root,height=1,width=140)
utext.pack()


btn = tk.Button(root, text="Summarize",command=summarize)
btn.pack()

root.mainloop()