package chat;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ChatListServlet2")
public class ChatListServlet2 extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		String listType = request.getParameter("listType");
		int bbsID= Integer.parseInt(request.getParameter("bbsID")); 
		
		if(listType == null || listType.equals("")) response.getWriter().write("");
		else if(listType.equals("today")) response.getWriter().write(getToday());		
		else if(listType.equals("ten")) response.getWriter().write(getTen(bbsID));
		else {
			try { 
				Integer.parseInt(listType);
				response.getWriter().write(getID(listType, bbsID));
			} catch (Exception e) {
				response.getWriter().write("");
			}
		}
	
	}
	
	public String getToday() {
		StringBuffer result = new StringBuffer("");
		result.append("{\"result\":[");
		ChatDAO2 ChatDAO2 = new ChatDAO2();
		ArrayList<Chat> chatList = ChatDAO2.getChatList(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
		for(int i = 0; i < chatList.size(); i++) {
			result.append("[{\"value\": \"" + chatList.get(i).getChatName() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatContent() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatTime() + "\"}]");
			if(i != chatList.size() -1) result.append(",");
		}
		result.append("], \"last\":\"" +  chatList.get(chatList.size() - 1).getChatID() + "\"}");
		//result.append("]}");
		return result.toString();
	}
	
	
	public String getTen(int bbsID) {
		StringBuffer result = new StringBuffer("");
		result.append("{\"result\":[");
		ChatDAO2 ChatDAO2 = new ChatDAO2();
		ArrayList<Chat> chatList = ChatDAO2.getChatListByRecent(10, bbsID);
		for(int i = 0; i < chatList.size(); i++) {
			result.append("[{\"value\": \"" + chatList.get(i).getChatName() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatContent() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatTime() + "\"}]");
			if(i != chatList.size() -1) result.append(",");
		}
		result.append("], \"last\":\"" +  chatList.get(chatList.size() - 1).getChatID() + "\"}");
		//result.append("]}");
		return result.toString();
	}
	
	
	public String getID(String chatID, int bbsID) {
		StringBuffer result = new StringBuffer("");
		result.append("{\"result\":[");
		ChatDAO2 ChatDAO2 = new ChatDAO2();
		ArrayList<Chat> chatList = ChatDAO2.getChatListByRecent(chatID, bbsID);
		for(int i = 0; i < chatList.size(); i++) {
			result.append("[{\"value\": \"" + chatList.get(i).getChatName() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatContent() + "\"},");
			result.append("{\"value\": \"" + chatList.get(i).getChatTime() + "\"}]");
			if(i != chatList.size() -1) result.append(",");
		}
		result.append("], \"last\":\"" +  chatList.get(chatList.size() - 1).getChatID() + "\"}");
		return result.toString();
	}
	
}
