
from tkinter import *                         # for gui develping 

gui = Tk ()
 # window title 
gui.title('huffman algorithm ')    
#size of pannel 
gui.geometry('1000x800')            
gui.resizable(False ,False )
 # background color 
gui.config(background ='#000000') 
# title of project and its size
title  = Label(gui, text='Huffman Endoding ',font =('courier',18), bg ='black' ,fg ='cyan' )
title.pack(fill =X)

#frame 
fr1 =Frame (gui,width ='950', height ='850' ,bg ='#2F3431' )
fr1.pack(padx =10 ,pady =10)

# comment Above input and output labels 
label_1 = Label(fr1,text='Paste Your Original Text Here...',font =('courier',15),bg='#2F3431')
label_1.place(x =20 ,y=60)

label_2 = Label(fr1,text='Your Zipped file will be Here...',font =('courier',15),bg='#2F3431')
label_2.place(x =550 ,y=60)


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # frequency  of each charachter 
        self.prob = prob

        # single character inside string 
        self.symbol = symbol

        # left root of  node
        self.left = left

        # right root of node
        self.right = right

        # tree binary representation  (0/1)
        self.code = ''

""" A function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()

def node_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        node_Codes(node.left, newVal)
    if(node.right):
        node_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        

""" A  function to calculate the frequency of symbols in given data"""

def letter_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols


""" A function to obtain the encoded output"""
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        #print(coding[c], end = '')
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string
        
""" A function to calculate the space difference between compressed and non compressed data"""    
def Total_Gain(data, coding):
    before_compression = len(data) * 8                 # total bit space to stor the data before compression 8 bit ia required for each character in ASCII representation 
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])                     #calculate how many bit is required for that symbol in total  
   
   #displays Original size in bits          
    label_3 = Label(fr1,text= "Original size  (in bits)  :" + str(before_compression),font =('courier',15),bg='#2F3431',fg='cyan')
    label_3.place(x =20 ,y=480)
   # displaying compresed size in bits 
    label_4 = Label(fr1,text= "compressed size (in bits) :" + str(after_compression),font =('courier',15),bg='#2F3431',fg='cyan')
    label_4.place(x =550 ,y=480)


def Huffman_Encoding(data):
    symbol_with_probs = letter_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    #print("Charachters : ", symbols )
    #print("Frequencies : ", probabilities)
    nodes = []
    
      # converting characters  and frequencies into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their frequency
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:  
        #      print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # mergee the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    huffman_encoding = node_Codes(nodes[0])
  #  print("symbols with codes", huffman_encoding,"\n")
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0] , huffman_encoding 

def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right   
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head
        
    string = ''.join([str(item) for item in decoded_output])
    return string        


# define function which display the zipped message 
def zipp() :
    data = en1.get()

    encoding, tree ,huffman_encoding= Huffman_Encoding(data)
    txt1.delete(0.0,END)            # for removing old content 
    txt1.insert(INSERT,encoding )   # to insert the encoding of message 
   
    details = letter_Probability(data)        # to print datails ferquency and symbols.
   
    txt2.delete(0.0,END)            # for removing old content 
    txt2.insert(INSERT,"Characters And Frequencies : \n " )    # to insert the encoding of message
    txt2.insert(INSERT,details )  

    txt2.insert(INSERT,"\n \n symbols with codes : \n" ) 
    txt2.insert(INSERT,huffman_encoding )

#   identify compress button and its action  
bt1 =Button(fr1,text ='Zipp',font =('courier',18), bg ='cyan' ,fg ='#2F3431',command=zipp)
bt1.place(x= 420,y=275,width=80,height=40)
 
# label for data entering 
en1 =Entry(fr1,font =("bold italic",20),bg ='cyan')
en1.place(x=20, y=100,width=350,height=350)




# text box for display zipped message 
txt1 =Text(fr1,font =("bold italic",17),bg ='cyan')
txt1.place(x= 560,y=100,width=350,height=350)

# text box for display details of message 
txt2 =Text(fr1,font =("bold italic",17),bg ='cyan')
txt2.place(x= 560,y=550,width=350,height=150)

# name 
label_5= Label(fr1,text= "Developed By : Mohamed KHttab",font =('Vladimir Script',17),bg='#2F3431',fg='cyan')
label_5.place(x =50 ,y=700)


gui.mainloop()




