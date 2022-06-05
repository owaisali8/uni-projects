/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author User
 */
class RopeNode {

    RopeNode left, right;
    String data;
    int weight;

    public RopeNode(String data) {
        this.data = data;
        weight = data.length();
    }

    public RopeNode() {
        data = null;
        weight = 0;
    }
}

public class Rope {

    RopeNode root;

    public Rope() {
        root = new RopeNode("");
    }

    public void Empty() {
        root = new RopeNode("");
    }

    public void add(String [] arr){
        for(String s: arr){
            add(s);
        }
    }
    public void add(String str) {
        RopeNode nptr = new RopeNode(str);
        RopeNode newRoot = new RopeNode();
        newRoot.left = root;
        newRoot.right = nptr;
        newRoot.weight = newRoot.left.weight;
        if (newRoot.left.right != null) {
            newRoot.weight += newRoot.left.right.weight;
        }
        root = newRoot;
    }

    public char indexAt(int ind) {
        RopeNode t = root;
        if (ind > t.weight) {
            ind -= t.weight;
            return t.right.data.charAt(ind);
        }
        while (ind < t.weight) {
            t = t.left;
        }
        ind -= t.weight;
        return t.right.data.charAt(ind);
    }

    public String substring(int start, int end) {
        String str = "";
        boolean found = false;
        RopeNode tmp = root;
        if (end > tmp.weight) {
            found = true;
            end -= tmp.weight;
            if (start > tmp.weight) {
                start -= tmp.weight;
                str = tmp.right.data.substring(start, end);
                return str;
            } else {
                str = tmp.right.data.substring(0, end);
            }
        }
        if (!found) {
            while (end <= tmp.weight) {
                tmp = tmp.left;
            }
            end -= tmp.weight;
            if (start >= tmp.weight) {
                start -= tmp.weight;
                str = tmp.right.data.substring(start, end) + str;
                return str;
            }
            str = tmp.right.data.substring(0, end);
        }
        tmp = tmp.left;
        while (start < tmp.weight) {
            str = tmp.right.data + str;
            tmp = tmp.left;
        }
        start -= tmp.weight;
        str = tmp.right.data.substring(start) + str;

        return str;

    }

    public void print() {
        print(root);
        System.out.println();
    }

    private void print(RopeNode r) {
        if (r != null) {
            print(r.left);
            if (r.data != null) {
                System.out.print(r.data);
            }
            print(r.right);
        }
    }
    
    private String getText(RopeNode r){
        if(r == null) return "";
        if (r.left == null && r.right == null)
            return r.data+" ";
        else
            return getText(r.left) + getText(r.right);
        
    }
    public String getText(){
        return this.getText(root);
    }
    
    public int length(){
        int r = 0;
        RopeNode temp = root.right;
        while(temp != null){
            r += temp.weight;
            temp = temp.right;
        }
        return root.weight + r;
    }
    
    public int wordLength(){
        return wordLength(root);
    }
    
    private int wordLength(RopeNode r){
        if(r == null) return 0;
        if (r.left == null && r.right == null)
            return 1;
        else
            return wordLength(r.left) + wordLength(r.right);
    }
    
    
    public static void main(String [] args){
        Rope r = new Rope();
        r.add("Hello World");
        r.add("What");
        r.add("is");
        r.add("life?");
        r.add("Amazing");
        System.out.println(r.length());
        System.out.println(r.wordLength());
        System.out.println(r.getText(r.root));
}
}
