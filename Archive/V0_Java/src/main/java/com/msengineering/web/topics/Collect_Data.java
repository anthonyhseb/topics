package com.msengineering.web.topics;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

public class Collect_Data {

    public static final String USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 58.0.3029.81 Safari/537.36";
	    
    public static void main(String[] args) throws Exception {
    	//System.out.println(args.length);
    	
    	/*
    	 * J'ai ajout� des arguments (les requ�tes) dans "Run Configuration".
    	 */
    	System.out.println("LISTE DES REQUETES:");
    	System.out.println("====================");
    	int i = 0;
    	String rec=args[0];
    	for (i=1; i<args.length; i++){
    		
    		rec = rec.concat(" "+args[i]);
    	}
    	String strurl="https://google.com/search?q="+rec;
        //Fouiller les resultats de la recherche
    	
    	System.out.println(rec+"\n");
        //final Document doc = Jsoup.connect("https://google.com/search?q=farine").userAgent(USER_AGENT).get();
    	final Document doc = Jsoup.connect(strurl).userAgent(USER_AGENT).get();
    	//System.out.println(strurl);
        //Parcourir les resultats
      int count = 1;
      try {
    	  // Rediriger les resultats dans un fichier
    	  File ff=new File("C:\\Users\\Nirina\\Resultat.txt"); // d�finir l'arborescence
    	  ff.createNewFile();
    	  FileWriter fwrite =new FileWriter(ff);
    	  //write = new FileWriter ("Fichier.txt");
       for (Element result : doc.select("h3.r a")){
        //for (Element result : doc.select("a h3.r")){
    	   
    	  
            final String title = result.text();
            final String url = result.attr("href");       
            System.out.println(title + " -> " + url);
          
        	
    		/**/
    			//while (count < 10){
    				try {
    					String temporaire = (count + "  " +title + " -> " + url +"\n" );
    					
    					//System.out.println(temporaire);
    					// Enregistrement dans un fichier
    					
    						fwrite.write(temporaire);
    						fwrite.flush();
    			
    				}
    				catch (IOException e){
    				System.err.println(e.getMessage());
    				}
    				//System.out.println(count);
    				count +=1;
    			}
    			
    			fwrite.close();
    			}catch (IOException e){
    				System.err.println(e.getMessage());
    		}
    	}
       		
    }   