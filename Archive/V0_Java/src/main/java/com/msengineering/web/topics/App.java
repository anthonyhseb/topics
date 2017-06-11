package com.msengineering.web.topics;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class App {
	/**
	 * accepts search terms as command line arguments and prints the most
	 * frequent n-grams in the search results in descending order
	 * 
	 * @param args
	 *            search terms
	 */
	public static void main(String[] args) {
		//normalize input arguments into an array of single words
		List<String> termList = new LinkedList<String>();
		for (String arg : args) termList.addAll(Arrays.asList(arg.split("\\s+")));
		String[] terms = (String[])termList.toArray();
		
		//forward query to google and return a list of documents
		List<Document> results = new Search().search(terms);
		
		//find the most frequent n-grams (using apache Solr ??)
		List<String> ngrams = new Analyzer(results).topNgrams(5, 5);
		
		System.out.println("Top n-grams:");
		for (String ngram : ngrams) System.out.println(ngram);
	}
}
