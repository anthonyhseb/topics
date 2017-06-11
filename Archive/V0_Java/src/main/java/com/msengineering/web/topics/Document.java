package com.msengineering.web.topics;

public class Document {
	String url;
	/**
	 * Raw content returned by retreiving the url
	 */
	String title;
	String rawContent;
	/** optional field */
	String textContent;
	
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getRawContent() {
		return rawContent;
	}
	public void setRawContent(String rawContent) {
		this.rawContent = rawContent;
	}
	public String getTextContent() {
		return textContent;
	}
	public void setTextContent(String textContent) {
		this.textContent = textContent;
	}
}
