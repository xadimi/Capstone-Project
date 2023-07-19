from tkinter import *
import customtkinter as tk
from customtkinter import *
import customtkinter
import tkinter 
import tksheet
from readability import Readability
import pandas as pd
from pandas import *
from pandastable import Table, TableModel, config
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from deep_translator import GoogleTranslator
from PIL import ImageTk, Image
import re

tk.set_default_color_theme("dark-blue")
tk.set_appearance_mode("system")  # default value
tk.set_appearance_mode("dark")
tk.set_appearance_mode("light")
data = pd.read_csv(r'stories.csv')
df = pd.DataFrame(data, columns=['title', 'body'])

for i in range(len(df)):
            if   len(df.loc[i, "body"].split()) <= 100:
                df = df.drop(data.index[i])
df = df.reset_index()

column_names = df.columns
column_names = column_names.delete(0)
class App(tk.CTk):
    def __init__(self):
        
        super().__init__()
        tk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        tk.set_appearance_mode("dark")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title("children stories app")
        self.geometry("700x800")
        
        
        self.frame = tk.CTkFrame(self, width=500, height=500)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
       
        self.bg = ImageTk.PhotoImage(Image.open("Kids-books-online.jpg"))   
        self.dg = ImageTk.PhotoImage(Image.open("1675912.png"))  
        
        self.label_image = Label(self.frame, image = self.bg)
        self.label_image.configure(image=self.bg)
        self.label_image.pack()
        
        self.label = tk.CTkLabel(self.frame, text="Bienvenue dans mon application, ici vous pouvez explorer de nombreuses histoires françaises pour enfants, si vous voulez continuer, appuyez sur explorer.")
        self.label.pack(padx=20, pady=20)
        self.explorer = tk.CTkButton(master= self, text="Explorer", command= self.explore)
        #self.explorer.configure(image = self.dg)
        self.explorer.pack(side= BOTTOM, padx= 20, pady=20)
        
        #self.button = tk.CTkButton(master=frame, command=self.create_toplevel)
        
        
        
    def explore(self):
        tk.set_appearance_mode("dark")
        ex_window = tk.CTkToplevel(self)
        ex_window.geometry("700x700")
        ex_window.title("Explorer")
        main_frame = tk.CTkFrame(master=ex_window,
                               width=100,
                               height=50,
                               corner_radius=10)
        main_frame.pack(padx=20, pady=20)
        global tst
        tst = " "
        label = tk.CTkLabel(main_frame, text="La fenêtre de l'Explorateur")
        label.pack()
        rt = ImageTk.PhotoImage(Image.open("1256647.png"))  
        #label_image = Label(main_frame, image = self.bg)
        #label_image.configure(image=self.bg)
        #label_image.pack()
        age_button = tk.CTkButton(master=main_frame, text=" Recherche par age", command = self.age_search)
        #age_button.pack()
        age_button.configure(image= rt)
        age_button.pack()
        title_button = tk.CTkButton(master=main_frame, text="Recherche par titre", command = self.title_search)
        title_button.configure(image= rt)
        title_button.pack()
    def title_search(self):
        #update
        def update(data):
            #clear the listbox
            my_list.delete(0, END)
            
            #add tittles
            for item in data:
                my_list.insert(END, item)
        #update the entry box
        def fillout(e):
            #delete entry box content
            my_entry.delete(0, END)  
            
            my_entry.insert(0, my_list.get(ANCHOR))      
        #create a funcion to check
        def check(e):
            typed = my_entry.get()
            if typed == '':
                data = titles
            else:
                data = []
                for item in titles:
                    if typed.lower() in item.lower():
                        data.append(item)
            #update the listbox
            update(data)
        
        #show_selected_story function
        def show_selected_story():
            typed = my_entry.get()
            st_window = tk.CTkToplevel()
            st_window.geometry("1080x1080")
            mainn_frame = tk.CTkFrame(master=st_window,
                               width=200,
                               height=200,
                               corner_radius=10)
            mainn_frame.pack(padx=20, pady=20)
            i=0
            for j, col in enumerate(column_names):
                textbox = Text(mainn_frame, width=16, height=1, bg = "#9BC2E6", wrap=WORD)
                textbox.grid(row=i,column=j+2)
                textbox.insert(INSERT, col)
            
            n_rows = df.shape[0]
            n_cols = df.shape[1]
            text_file = open("f.txt", "w",encoding='utf-8')
            
            tk_textbox = Text(mainn_frame, width=20, height=50, wrap=WORD)
            body_textbox = Text(mainn_frame, width=50, height=50, wrap=WORD)
            
            title = []
            body = []
            titlee =""
            bodyy =""
                
                    
            for i in range(20): 
                if  str(df.loc[i]["title"]) == typed :           
                    tk_textbox.grid(row=i, column = 2)
                    body_textbox.grid(row=i,  column= 3)
                    titlee = str(df.loc[i][1])
                    title.append(titlee)
                    bodyy = str(df.loc[i][2])
                    body.append(bodyy)
                    
            tk_textbox.insert(INSERT, title[0])
            body_textbox.insert(INSERT, body[0])
            body_textbox.get("0.0","end")
            sum_btn = tk.CTkButton(master= mainn_frame, width=120,height=32, border_width=0, text="Afficher le resume",command= self.create_toplevel2)
            sum_btn.grid()
            
                           
                
            
            
            
        root = tk.CTkToplevel(self)
        root.title('Rechereche par titre') 
        root.geometry("700x500")
        root.title("Recherche")
        # creating a label
        #my_label = tk.CTkLabel(root, text="le titre: .....", 
        #                       fg_color=("white", "gray75"), corner_radius=8)
        #my_label.pack(pady=20)
        #creating an entry box
        my_entry = tk.CTkEntry(root, placeholder_text="Le titre ..............")
        my_entry.pack()

        #create a listbox
        
        my_list = Listbox(root, widt=50)
        my_list.pack(pady=40)
        titles = [" "," "]
        #create the lisbox
        for i in range(len(df)):
              titles.append(df.loc[i, "title"])
        
        #add the titles
        update(titles)
        
        #create a binding on the listbox click
        my_list.bind("<<ListboxSelect>>", fillout)
        
        #create a binding on the entry box
        my_entry.bind("<KeyRelease>", check)
        
        #create the button to show the story selected
        btn = tk.CTkButton(root,text="Afficher l'histoire", command= show_selected_story)
        btn.pack()
        
        
        
        
    def age_search(self):
            age_window = tk.CTkToplevel(self)
            age_window.geometry("300x300")
            age_window.title("Recherche par age")
            imagee = ImageTk.PhotoImage(Image.open("3557437.png"))  
            age_frame = tk.CTkFrame(master=age_window,
                               width=300,
                               height=300,
                               corner_radius=10)
            age_frame.grid(padx=20, pady=20)
            global entry
            entry = tk.CTkEntry(master=age_frame, placeholder_text="Entrer l'age de votre enfant",width=200,
                               height=50)
            entry.grid(padx=20, pady=10)
            global tst 
            tst = " "
            #self.bb = tk.CTkButton(master=age_frame,text="confirm the age", command= self.get_input)
            #self.bb.grid()
            text_var = tkinter.StringVar(value=tst)
            find_stories = tk.CTkButton(master=age_frame, text="", command=self.create_toplevel)
            find_stories.configure(image = imagee)
            find_stories.grid()
            print(tst)
            
            

    def get_input(self):
        global tst
        tst = entry.get()    
        
        
        
        
        
        
            
      
        
        
    def create_toplevel(self):
            window = tk.CTkToplevel(self)
            window.geometry("1080x1080")
            window.title("Les Histoire disponibles pour l'age choisis")
            main_frame = tk.CTkFrame(window)
            main_frame.grid()
            
            second_frame = tk.CTkFrame(main_frame)
            second_frame.grid()
            self.get_input()
            i=0
            for j, col in enumerate(column_names):
                textbox = Text(second_frame, width=16, height=1, bg = "#9BC2E6", wrap=WORD)
                textbox.grid(row=i,column=j+2)
                textbox.insert(INSERT, col)
            
            n_rows = df.shape[0]
            n_cols = df.shape[1]
            text_file = open("f.txt", "w",encoding='utf-8')
            global body_textbox
            tk_textbox = Text(second_frame, width=20, height=50, wrap=WORD)
            body_textbox = Text(second_frame, width=50, height=50, wrap=WORD)
            global title
            global body
            title = []
            body = []
            for i in range(10):
                
                    if Readability(df.loc[i, "body"]).ari().ages[0] == int(tst):
                            
                        tk_textbox.grid(row=i, column = 2)
                        body_textbox.grid(row=i,  column= 3)
                        
                        titlee = str(df.loc[i][1])
                        title.append(titlee)
                        bodyy = str(df.loc[i][2])
                        body.append(bodyy)
                        
                        
            tk_textbox.insert(INSERT, title[0])
            body_textbox.insert(INSERT, body[0])
            
            
            
            
            print(title)
            global ix 
            global iz
            ix = 0
            iz = 1
            size = len(title)
            
            def next_str():
                global ix
                size = len(title)
                
                if ix <= size :
                    tk_textbox.delete("1.0","end")
                    body_textbox.delete("1.0","end")
                    tk_textbox.insert(INSERT, title[ix])
                    body_textbox.insert(INSERT, body[ix])
                    ix = ix + 1
                    print("next"+ str(ix))
            def previous_str():
                global iz
                global ix
                tk_textbox.delete("1.0","end")
                body_textbox.delete("1.0","end")
                tk_textbox.insert(INSERT, title[ix-iz])
                body_textbox.insert(INSERT, body[ix-iz])
                iz = iz + 1
                print("previous" + str(iz))
                
                
                
                
            show_stories = tk.CTkButton(master= second_frame, width=120,height=32,text="Histoire suivante", command= lambda: next_str())
            #index = next_str(index)
            show_stories.grid(row=2, column= 2)
            show_stories2 = tk.CTkButton(master= second_frame, width=120,height=32,text="Histoire precedante", command= lambda: previous_str())
            show_stories2.grid(row=2, column= 1)
            sum_btn = tk.CTkButton(master= main_frame, width=120,height=32, border_width=0, text="Afficher le resume",command= self.create_toplevel3)
            sum_btn.grid(row=3, column = 3)
            text_file.close()
    def create_toplevel3(self):
                global body_textbox
                story_caffet = body_textbox.get("0.0","end") 
                
                story_caffet_z = story_caffet[:3000]
                print("the story is :" + story_caffet_z)
                
                
                translated = [ ]
                    
                x = GoogleTranslator(source='auto', target='en').translate(story_caffet_z)
                    
                file='f.txt' 
                
                with open(file, 'w',encoding='utf-8') as filetowrite:
            
                    filetowrite.write("".join(x))
                
                summary = generate_summary("f.txt",6)
                
                x2 = GoogleTranslator(source='auto', target='fr').translate(summary)
                
                window = tk.CTkToplevel(self)
                window.geometry("500x500")
                main_frame = tkinter.Frame(window, width=200,
                                    height=200)
                main_frame.pack(padx=20, pady=20)
                summary_textbox = tkinter.Text(main_frame, wrap=WORD)
                summary_textbox.configure(font=("Times New Roman", 25, "italic"))
                summary_textbox.pack(padx=20, pady=20)
                
                
                
                
                summary_textbox.insert("0.0", x2)
            
            
            
            
            
        
            
                            
            
            
                       
                        
    def create_toplevel2(self):
        global body_textbox
        story_caffet = body_textbox.get("0.0","end") 
        
        story_caffet_z = story_caffet[:3000]
        print("the story is :" + story_caffet_z)
        
        
        translated = [ ]
            
        x = GoogleTranslator(source='auto', target='en').translate(story_caffet_z)
            
        file='f.txt' 
        
        with open(file, 'w',encoding='utf-8') as filetowrite:
    
            filetowrite.write("".join(x))
        
        summary = generate_summary("f.txt",6)
        
        x2 = GoogleTranslator(source='auto', target='fr').translate(summary)
         
        window = tk.CTkToplevel(self)
        window.geometry("500x500")
        main_frame = tkinter.Frame(window, width=200,
                               height=200)
        main_frame.pack(padx=20, pady=20)
        summary_textbox = tkinter.Text(main_frame, wrap=WORD)
        summary_textbox.configure(font=("Times New Roman", 25, "italic"))
        summary_textbox.pack(padx=20, pady=20)
        
        
        
        
        summary_textbox.insert("0.0", x2)
        
         
        
def nice(z):
    file = open(z, "r",encoding='utf-8')
    filedata = file.readlines(-1)
    return filedata       
def read_article(z):
    file = open(z, "r",encoding='utf-8')
    filedata = file.readlines()
    print(filedata)
    text = ""
    for s in filedata:
        text=text+s.replace("\n","")
        text=re.sub(' +', ' ', text) #remove space
        text=re.sub('—',' ',text)
    
    article = text.split(". ")
    sentences = []

    for sentence in article:
        
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    new_sent=[]
    for lst in sentences:
        newlst=[]
        for i in range(len(lst)):
            if lst[i].lower()!=lst[i-1].lower():
                newlst.append(lst[i])
            else:
                newlst=newlst
        new_sent.append(newlst)
    return new_sent

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(z, top_n):
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    print(stop_words)
    summarize_text = []

    # Step 1 - Read text anc split it
    new_sent =  read_article(z)
    

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(new_sent, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph, max_iter=600)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(new_sent)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    
    i = 0
    for i in range(10):
        
        #if ranked_sentence[i][1][0] == ranked_sentence[i+1][1][0] :
            #print(ranked_sentence[i+1][1][0])
            
            #i = i+2
        #else:
            #print(ranked_sentence[i][1])
            summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize text
    print("Summarize Text: \n", " ".join(summarize_text))
    
    return ".".join(summarize_text)

                
        
         
        
        
        
        
    
  
                    

                      
        

if __name__ == "__main__":
    app = App()
    app.mainloop()