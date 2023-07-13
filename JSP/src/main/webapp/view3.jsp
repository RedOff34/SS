<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="java.io.PrintWriter"%>
<%@ page import="bbs.Bbs3"%>
<%@ page import="bbs.BbsDAO3"%>
<%@ page import="file.FileDAO3"%>
<%@ page import="file.FileDTO3"%>
<%@ page import="comment.Comment3"%>
<%@ page import="comment.CommentDAO3"%>
<%@ page import="java.io.File"%>
<%@ page import="java.util.ArrayList"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width" , initial-scale="1">
<link rel="stylesheet" href="css/bootstrap.css">
<link rel="stylesheet" href="css/custom.css">

<title>JSP 게시판 웹사이트</title>
</head>
<body>
	<%
	String userID = null;
	if ((String) session.getAttribute("userID") != null) {
		userID = (String) session.getAttribute("userID");
	}
	int bbsID = 0;
	if (request.getParameter("bbsID") != null) {
		bbsID = Integer.parseInt(request.getParameter("bbsID"));
	}
	int boardID = 0;
	if (request.getParameter("boardID") != null) {
		bbsID = Integer.parseInt(request.getParameter("boardID"));
	}
	if (bbsID == 0) {
		PrintWriter script = response.getWriter();
		script.println("<script>");
		script.println("alert('유효하지 않은 글입니다.')");
		script.println("location.href='bbs3.jsp'");
		script.println("</script>");
	}
	Bbs3 bbs = new BbsDAO3().getBbs(bbsID);

	FileDTO3 f = new FileDAO3().getfileName(bbsID);
	%>

	<nav class="navbar navbar-default">
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed"
				data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
				aria-expanded="false">
				<span class="icon-bar"></span>
				<!-- 게시판 아이콘 작대기(-) 하나를 의미 -->
				<span class="icon-bar"></span>
				<!-- 게시판 아이콘 작대기(-) 하나를 의미 -->
				<span class="icon-bar"></span>
				<!-- 게시판 아이콘 작대기(-) 하나를 의미 -->
			</button>
			<a class="navbar-brand" href="main.jsp">SS</a>
		</div>
		<div class="collapse navbar-collapse"
			id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li><a href="main.jsp">메인</a></li>
				<li><a href="bbs.jsp">자유게시판</a></li>
				<li><a href="bbs2.jsp">질문/답변 게시판</a></li>
				<li class="active"><a href="bbs3.jsp">스터디그룹 게시판</a></li>
			</ul>
			<%
			if (userID == null) {
			%>
			<ul class="nav navbar-nav navbar-right">
				<li class="dropdown"><a href="#" class="dropdown-toggle"
					data-toggle="dropdown" role="button" aria-haspopup="true"
					aria-expanded="false">접속하기<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="login.jsp">로그인</a></li>
						<li><a href="join.jsp">회원가입</a></li>
					</ul></li>
			</ul>
			<%
			} else {
			%>
			<ul class="nav navbar-nav navbar-right">
				<li class="dropdown"><a href="#" class="dropdown-toggle"
					data-toggle="dropdown" role="button" aria-haspopup="true"
					aria-expanded="false">회원관리<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="logoutAction.jsp">로그아웃</a></li>
					</ul></li>
			</ul>
			<%
			}
			%>

		</div>
	</nav>
	<div class="container">
		<div class="row">

			<table class="table table-striped"
				style="text-align: center; border: 1px solid #dddddd;">
				<tr>
					<th colspan="3"
						style="background-color: #eeeeee; text-align: center">게시판 글보기
					</th>


				</tr>
				<tr>
					<td style="width: 20%;">글 제목</td>
					<td colspan="2"><%=bbs.getBbsTitle().replaceAll(" ", "&nbsp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll("\n",
		"<br>")%></td>
				</tr>
				<tr>
					<td style="width: 20%;">작성자</td>
					<td colspan="2"><%=bbs.getUserID()%></td>
				</tr>
				<tr>
					<td style="width: 20%;">작성일자</td>
					<td colspan="2"><%=bbs.getBbsDate().substring(0, 11) + bbs.getBbsDate().substring(11, 13) + "시"
		+ bbs.getBbsDate().substring(14, 16) + "분"%></td>
				</tr>
				<tr>
					<td style="width: 20%;">내용</td>
					<td colspan="2" style="min-height: 200px; text-align: left;">
						<%=bbs.getBbsContent().replaceAll(" ", "&nbsp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll("\n",
		"<br>")%></td>
				</tr>
				<tr>
					<td style="width: 20%;">첨부파일</td>
					<td colspan="2" style="min-height: 200px; text-align: left;"><a
						href="filedownload3.jsp?fileName=<%=f.getFileRealName()%>"><%=f.getFileName()%></a></td>
				</tr>
			</table>
			<a href="bbs3.jsp" class="btn btn-primary">목록</a>
			<%
			if (userID != null && userID.equals(bbs.getUserID())) {
			%>
			<a href="update3.jsp?bbsID=<%=bbsID%>" class="btn btn-primary">수정</a>
			<a onclick="return confirm('정말로 삭제하시겠습니까?')"
				href="deleteAction3.jsp?bbsID=<%=bbsID%>" class="btn btn-primary">삭제</a>
				<a onclick="return confirm('정말로 스터디그룹 모집을 마감하시겠습니까?')"
				href="deleteAction3.jsp?bbsID=<%=bbsID%>" class="btn btn-primary">마감</a>

			<%
			}
			%>
		</div>
	</div>

	<div class="container">
		<div class="row">
			<table class="table table-striped"
				style="text-align: center; border: 1px solid #dddddd">
				<%--
					<tbody>
					 --%>
				<tr>
					<td align="left" bgcolor="beige">댓글</td>
				</tr>
				<tr>
					<%
					CommentDAO3 commentDAO = new CommentDAO3();
					ArrayList<Comment3> list = commentDAO.getList(boardID, bbsID);
					for (int i = 0; i < list.size(); i++) {
					%>
					<div class="container">
						<div class="row">
							<table class="table table-striped"
								style="text-align: center; border: 1px solid #dddddd">
								<tbody>
									<tr>
										<td align="left"><%=list.get(i).getUserID()%>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<%=list.get(i).getCommentDate().substring(0, 11) + list.get(i).getCommentDate().substring(11, 13) + "시"
		+ list.get(i).getCommentDate().substring(14, 16) + "분"%></td>
										<td colspan="2"></td>
										<td align="right">
											<%
											if (list.get(i).getUserID() != null && list.get(i).getUserID().equals(userID)) { // 댓글 쓴 사람 아이디 구별
											%> <a onclick="return confirm('정말로 삭제하시겠습니까?')"
											href="commentDeleteAction3.jsp?bbsID=<%=bbsID%>&commentID=<%=list.get(i).getCommentID()%>" <%-- bbsID와 commentID 를 가져와 해당 댓글 삭제 --%>
											class="btn-primary">삭제</a> <%
 }
 %>
										
										<%-- 수락 버튼 부분 --%>
										
											<%
											if (userID != null && userID.equals(bbs.getUserID())) {  // 게시글 쓴 사람 아이디 구별
											%> <a onclick="return confirm('정말로 스터디 그룹원으로 수락하시겠습니까?')"
											href="commentAcceptAction.jsp?bbsID=<%=bbsID%>&commentID=<%=list.get(i).getCommentID()%>&userID<%=list.get(i).getUserID()%>"   <%-- bbsID 게시글 id /commentID 댓글 id로 댓글쓴 id 가져올용도 /userId 댓글 쓴이 id  --%>
											class="btn-primary">수락</a> <%
 }
 %>
										</td>

									</tr>

									<tr>
										<td colspan="5" align="left"><%=list.get(i).getCommentText()%><br>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<%
					}
					%>
				</tr>
			</table>
		</div>
	</div>
	<div class="container">
		<div class="form-group">
			<form method="post"
				action="commentAction3.jsp?bbsID=<%=bbsID%>&boardID=<%=boardID%>">
				<table class="table table-striped"
					style="text-align: center; border: 1px solid #dddddd">
					<tr>
						<td style="border-bottom: none;" valign="middle"><br> <br><%=userID%></td>
						<td><input type="text" style="height: 100px;"
							class="form-control" placeholder="상대방을 존중하는 댓글을 남깁시다."
							name="commentText"></td>
						<td><br> <br> <input type="submit"
							class="btn-primary pull" value="댓글 작성"></td>
					</tr>
					<tr>
					</tr>
				</table>
			</form>
		</div>
	</div>
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script src="js/bootstrap.js"></script>
</body>
</html>