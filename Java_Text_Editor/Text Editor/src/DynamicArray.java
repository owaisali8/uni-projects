
 public class DynamicArray <T extends Comparable<T>>{
	 T [] arr;
	 int currIndex;
	 
	 public DynamicArray(){
		arr = (T[])new Comparable[10];
		currIndex=-1;
	 }
	 
	 public DynamicArray(int size) {
	arr = (T[])new Comparable[size];
	currIndex=-1;
	}
	
	public String toString(){
	String str="";
	for(int i=0; i<arr.length;i++)
            if(arr[i] != null)
                str=str+arr[i]+"\n";
	return str;
	}
	
	public void add (T data) {
		 if(currIndex == arr.length-1){ this.resize();
     }
     
     else if(currIndex == -1) {
         this.arr[0] = data;
         currIndex++;
     }
     else{
     arr[currIndex+1] = data;
     currIndex++;
     }
	}
	
	private void resize(){
     T[] arr2 = (T[])new Comparable[arr.length*2];
	for(int i = 0; i<arr.length;i++)
		arr2[i] = arr[i];
	
	arr = arr2;
 }
 
	public int find(T value) {
		for(int i = 0; i<arr.length; i++)
		if(arr[i].equals(value)) return i;
	
	return -1;
	}
	public void clear() { arr= null;}
	
	public T get(int index){ return arr[index];}
	
	public void update(int index, T value) {
		if(arr[index] == null){
            currIndex++;
            arr[index] = value;
        }
        else arr[index] = value;
	}

	public void remove(T value) { 
		int index = this.find(value);
	
	for(int i =index; i<arr.length-1; i++)
		arr[i] = arr[i+1];
	
	T[] arr2 =  (T[])new Comparable[arr.length-1];
	for(int i =0; i<arr2.length;i++)
		arr2[i] = arr[i];
	
	arr = arr2;
        currIndex--;
	}
 }