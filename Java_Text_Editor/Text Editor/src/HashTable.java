/**
 * @author Owais
 * @author Mohsin
 * @author Hasin
 */
public class HashTable{
    
    int[] table;
    int numOfCollisions=0;
    int numOfOccupiedCells=0;
    int words=0;
 
    HashTable(int s){
        // table size should be a prime number and 1/3 extra.
        words=s;
        
        int size=s+(s/3);
        int newSize=getPrime(size);
        
        table=new int[newSize]; // if value is 0 for integer the cell will consider empty.
    }
 
    private int getPrime(int n){
        while(true){
        if(isPrime(n)){
            return n;}
            n++;
        }
    }
 
    private boolean isPrime(int n){
        for(int i=2;i<=n/2;i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
 
    public int hash(int key){
        //compute hash value by taking mod on key value and return remainder
        return key%table.length;
    }
 
    public int rehash(int key, int i){
        // first test linear probing, then test Quadratic probing and compare both technique on same data
        //with respect to number of collision
        numOfCollisions++;
        return (key+i)%table.length;
    }
 
    public int insert(int key){ // keep maintain 1/3 empty cells
        // call Hash(key) and save return hash-value
        // if (no collision on hash-value) then place in table
        //else call rehash function until empty cell found or reached to threshold limit of rehashes
        // also count number of collisions on each key insertion
        System.out.println(words);
        if(numOfOccupiedCells==words){
            System.out.println("Table is Full");
            return -1;
        }
        
        int hash=hash(key);
        
        if(table[hash]==0){
            table[hash]=key;
            numOfOccupiedCells++;
            return hash;
        }
        else{
            int rehash=rehash(hash,1);
            while(table[rehash]!=0){
                rehash=rehash(rehash,1);
            }
            table[rehash]=key;
            numOfOccupiedCells++;
            return rehash;
        }
    }
 
    public int search(int key){
        // search word in a hash table
        // call Hash(key) and save return hash-value
        // if (value match at hash-value index) return true
        //else call rehash function until empty cell found or it reaches threshold limit of rehashes.
        int hash=hash(key);
        if(table[hash]==key){
            return hash;
        }
        else{
            int rehash=rehash(hash,1);
            int rehashCount=1;
            while(table[rehash]!=key && rehashCount!=table.length){
                rehash=rehash(rehash,1);
                rehashCount++;
            }
            if(table[rehash]==key){
                return rehash;
            }
        }
        return -1;
    }
 
    public String toString(){
        String str="";
        for (int i=0;i<table.length;i++){
            str=str+"["+i+"] "+table[i]+"\n";
        }
        return str;
    }
}
