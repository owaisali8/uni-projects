/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 23053
 * Syed Owais Ali
 */
class StackNode<T> {
 T info;
 StackNode<T> next;
 //Constructor
 StackNode(T data){
 info=data;
}}


public class Stack<T>{
 StackNode<T> top;
 
public Stack(){
    top = null;
}
// methods
public void PUSH(T c){
    StackNode<T> n = new StackNode(c); 
    if (this.isEmpty()){
       top = n;
    }
    else{
        n.next = top;
        top = n;
    }
}
 public T POP() {
     if(this.isEmpty()){
     System.out.println("Stack is empty.");
     return null;
     }
     else{
        T temp = top.info;
        top = top.next;
        return temp;
     }
 }
 
 public T PEEK() {
     return top.info;
 }
 
 public boolean isEmpty() {
     return top == null;
 }
 public String toString(){
     StackNode<T> temp = top;
     String s = "";
     while(temp != null){
     s += temp.info +",";
     temp = temp.next;
     }
     return s;
 }
}

