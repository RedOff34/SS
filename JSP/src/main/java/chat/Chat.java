package chat;

public class Chat {
	
	int chatID;
	int bbsID;	
	String chatName;
	String chatContent;
	String chatTime;
	
	public String getChatName() {
		return chatName;
	}
	public void setChatName(String chatName) {
		this.chatName = chatName;
	}
	public String getChatContent() {
		return chatContent;
	}
	public void setChatContent(String chatContent) {
		this.chatContent = chatContent;
	}
	public String getChatTime() {
		return chatTime;
	}
	public void setChatTime(String chatTime) {
		this.chatTime = chatTime;
	}
	public int getChatID() {
		return chatID;
	}
	public void setChatID(int chatID) {
		this.chatID = chatID;
	}
	//bbsID 추가
	public int getbbsID() {
		return bbsID;
	}
	public void setbbsID(int bbsID) {
		this.bbsID = bbsID;
	}
	
	
}
