<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="bbs.BbsDAO"%> 
<%@ page import="java.io.PrintWriter"%>
<%
	request.setCharacterEncoding("UTF-8");
%>

<%@ page import="file.FileDAO" %>
<%@ page import="java.io.File" %>
<%@ page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %>
<%@ page import="com.oreilly.servlet.MultipartRequest" %>
<%@ page import ="java.util.*" %>
<%@ page import ="java.io.*" %>

<jsp:useBean id="bbs" class="bbs.Bbs" scope="page" />
<jsp:setProperty name="bbs" property="bbsTitle" />
<jsp:setProperty name="bbs" property="bbsContent" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSP 게시판 웹사이트</title>
</head>
<body>
<% 
		String userID = null;
		if ((String) session.getAttribute("userID") != null) {
			userID = (String) session.getAttribute("userID");
		}
		BbsDAO bbsDAO = new BbsDAO();
		bbs.setBbsID(bbsDAO.getNewNext());
		int bbsID = bbs.getBbsID();
		String directory = application.getRealPath("/upload/freeupload/"); //상대경로
	
		out.println("경로 : " + directory + "<br/>");
		
		String files[] = new File(directory).list();
		
		
		int maxSize = 50*1024*1024;
		String encType = "utf-8";
		
		try{
			MultipartRequest multi = null;
			multi = new MultipartRequest(request, directory, maxSize, encType, new DefaultFileRenamePolicy());
			
			String fileName = multi.getOriginalFileName("file");
			String fileRealName = multi.getFilesystemName("file");
			
			String bbsTitle = multi.getParameter("bbsTitle");
			String bbsContent = multi.getParameter("bbsContent");
			
			bbs.setBbsTitle(bbsTitle);
			bbs.setBbsContent(bbsContent);
		
		if (userID == null) {
			PrintWriter script = response.getWriter();
			script.println("<script>");
			script.println("alert('로그인을 하세요')");
			script.println("location.href='login.jsp'");
			script.println("</script>");
		} else {
			
			System.out.println("write action : check bbs parameter"  + bbs.getBbsTitle());
			
			if (bbs.getBbsTitle() == null || bbs.getBbsContent() == null) {
				PrintWriter script = response.getWriter();
				script.println("<script>");
				script.println("alert('입력이 안 된 사항이 있습니다.')");
				script.println("history.back()");
				script.println("</script>");
			} else {


				int result = bbsDAO.write(bbs.getBbsTitle(), userID, bbs.getBbsContent());
				
				new FileDAO().upload(fileName, fileRealName, bbs.getBbsID());
				out.write("filename :" + fileName + "<br>");
				out.write("realfilename :" + fileRealName + "<br>");
				
				if (result == -1) {
					PrintWriter script = response.getWriter();
					script.println("<script>");
					script.println("alert('글 쓰기에 실패했습니다.')");
					script.println("history.back()");
					script.println("</script>");
				} else {
					PrintWriter script = response.getWriter();
					script.println("<script>");
					script.print("location.href = 'bbs.jsp'");
					script.println("</script>");
				}
			}

		}
		}catch (IOException ioe){
			System.out.println(ioe);
		}catch (Exception ex){
			System.out.println(ex);
		}
%>
</body>
</html>