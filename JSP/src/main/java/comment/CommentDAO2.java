package comment;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;


public class CommentDAO2 {
	private Connection conn;	//db�� �����ϴ� ��ü
	private ResultSet rs;
	
	public CommentDAO2() {
		try {
			String dbURL = "jdbc:mysql://172.30.1.17:3306/capston";
			String dbID = "root";
			String dbPassword = "yjh2017E!";
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(dbURL,dbID,dbPassword);
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
	public String getDate() {
		String SQL = "SELECT NOW()";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			rs = pstmt.executeQuery();
			if (rs.next()) {
				return rs.getString(1);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return ""; //�����ͺ��̽� ����
	}
	public int getNext() {
		String SQL = "SELECT commentID FROM comment2 ORDER BY commentID DESC";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			rs = pstmt.executeQuery();
			if (rs.next()) {
				return rs.getInt(1) + 1;
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return 1; //ù��° ����� ���
	}
	public int write(int boardID, int bbsID, String userID, String commentText) {
		String SQL = "INSERT INTO comment2 VALUES(?, ?, ?, ?, ?, ?, ?)";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1, boardID);
			pstmt.setInt(2, getNext());
			pstmt.setInt(3, bbsID);
			pstmt.setString(4, userID);
			pstmt.setString(5, getDate());
			pstmt.setString(6, commentText);
			pstmt.setInt(7, 1);
			pstmt.executeUpdate();
			return getNext();
		}catch(Exception e) {
			e.printStackTrace();
		}
		return -1; //�����ͺ��̽� ����
	}
	public String getUpdateComment(int commentID) {
		String SQL = "SELECT commentText FROM comment2 WHERE commentID = ?";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1, commentID);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				return rs.getString(1);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return ""; //����
	}
	public ArrayList<Comment2> getList(int boardID, int bbsID){
		String SQL = "SELECT * FROM comment2 WHERE boardID = ? AND bbsID= ? AND commentAvailable = 1 ORDER BY bbsID DESC"; 
		ArrayList<Comment2> list = new ArrayList<Comment2>();
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1, boardID);
			pstmt.setInt(2,  bbsID);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				Comment2 cmt = new Comment2();
				cmt.setBoardID(rs.getInt(1));
				cmt.setCommentID(rs.getInt(2));
				cmt.setBbsID(rs.getInt(3));
				cmt.setUserID(rs.getString(4));
				cmt.setCommentDate(rs.getString(5));
				cmt.setCommentText(rs.getString(6));
				cmt.setCommentAvilable(rs.getInt(7));
				list.add(cmt);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return list; //�����ͺ��̽� ����
	}
	
	public int update(int commentID, String commentText) {
		String SQL = "UPDATE comment2 SET commentText = ? WHERE commentID LIKE ?";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, commentText);
			pstmt.setInt(2, commentID);
			return pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return -1; // �����ͺ��̽� ����
	}
	public Comment2 getComment(int commentID) {
		String SQL = "SELECT * FROM comment2 WHERE commentID = ? ORDER BY commentID DESC";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1,  commentID);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				Comment2 cmt = new Comment2();
				cmt.setBoardID(rs.getInt(1));
				cmt.setCommentID(rs.getInt(2));
				cmt.setBbsID(rs.getInt(3));
				cmt.setUserID(rs.getString(4));
				cmt.setCommentDate(rs.getString(5));
				cmt.setCommentText(rs.getString(6));
				cmt.setCommentAvilable(rs.getInt(7));
				return cmt;
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	public int delete(int commentID) {
		String SQL = "DELETE FROM comment2 WHERE commentID = ?";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1, commentID);
			return pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return -1; // �����ͺ��̽� ����
	}
}
