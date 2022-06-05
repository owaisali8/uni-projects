

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * @author Owais
 * @author Mohsin
 * @author Hasin
 */
public class Dictionary{
    
    int words=wordsInFile("Dictionary2.txt");
    HashTable HWord=new HashTable(words);
    DynamicArray Meaning=new DynamicArray(HWord.table.length);
    
    
    public void insertFile(String file){
        
        try{
            File obj=new File(file);
            Scanner sc=new Scanner(obj);
            String[] line=new String[2];

            while(sc.hasNext()){
                String str=sc.nextLine();
                if(!str.isEmpty()){
                    line=str.split("  ");
                 
                    int code=wordToCode(line[0]);
                    int index=HWord.insert(code);
                    
                    Meaning.update(index,line[1]);
                }
            }
            sc.close();
        }
        catch(FileNotFoundException e){
            System.out.println(e);
        }
    }
    
    public int wordsInFile(String file){
        int count=0;
        try{
            File obj=new File(file);
            Scanner sc=new Scanner(obj);
            
            String line;
            while(sc.hasNext()){
                line=sc.nextLine();
                if(!line.isEmpty()){
                    count++;
                }
            }
            sc.close();
        }
        catch(FileNotFoundException e){
            System.out.println(e);
        }
        return count;
    }
    
    public int wordToCode(String word){
        word=word.toLowerCase();
        int code=0;
        for(int i=0; i<word.length();i++){
            if((word.charAt(i)>=97 && word.charAt(i)<=122) || (word.charAt(i)>=48 && word.charAt(i)<=57)){
                if(word.charAt(i)>=97 && word.charAt(i)<=122){
                    code=(int) (code + (word.charAt(i)-96)*(Math.pow(3, i)));
                }
                else if((word.charAt(i)>=48 && word.charAt(i)<=57)){
                    code=(int) (code + (word.charAt(i)-48)*(Math.pow(3, i)));
                }
            }
        }
        return code;
    }
    
    public String wordToMeaning(String word){
        int code=wordToCode(word);
        int index=HWord.search(code);
        
        if(index==-1){
            return "Word does not exist in the Dictionary";
        }
        else{
            return (String)Meaning.arr[index];
        }
    }
    
    public static void main(String[] args){
        
        
    }
}
