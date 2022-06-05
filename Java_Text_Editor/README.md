
# Java Text Editor 
Data Structures Project
Made on Netbeans along with Swing GUI

Text editors are the most commonly used software for writing documentation, plain texts and project source codes. Notepad, WordPad, etc. are some of the popular text editing tools with various features and options. After our basic UI we added more unique features, including Vocabulary Check, Dictionary and Find and Replace. These all features use various Data Structures including:

- Stacks for Undo/Redo
- Dynamic Array for Clipboard
- Hash Table for Dictionaries
- Rope DS for String Manipulation

A rope is a type of binary tree i.e. each node can have maximum of 2 children, where every leaf node holds a String or a Sub-string and the length (Also known as the "weight" for the corresponding leaf node). Parent node holds the total sum of the weights of the leaf nodes in its left sub-tree, which in turn is described as the weight of the said node.

### Screenshot: 
![Demo](https://github.com/owaisali8/uni-projects/blob/main/Java_Text_Editor/Capture.PNG?raw=true)
