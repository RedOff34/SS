package chat;

import java.io.IOException;
import java.net.URLDecoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ChatSubmitServlet2")
public class ChatSubmitServlet2 extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
	//System.out.println("서블");
  
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		String chatName = URLDecoder.decode(request.getParameter("chatName"), "UTF-8");
		String chatContent = URLDecoder.decode(request.getParameter("chatContent"), "UTF-8");
		String bbsID = URLDecoder.decode(request.getParameter("bbsID"), "UTF-8");
		if (chatName == null || chatName.equals("") || chatContent == null || chatContent.equals("") || bbsID==null || bbsID.equals("")) {
			response.getWriter().write("0");
		} else { 
			int bbsIDInt=Integer.parseInt(bbsID);
			response.getWriter().write(new ChatDAO2().submit(bbsIDInt, chatName, chatContent)+ "");
		}  

	}

}
