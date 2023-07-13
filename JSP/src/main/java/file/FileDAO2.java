package file;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import bbs.Bbs;

public class FileDAO2 {
	
	private Connection conn;
	private ResultSet rs;
	
	public FileDAO2() {
		try {
			String dbURL = "jdbc:mysql://172.30.1.17:3306/capston";
			String dbID = "root";
			String dbPassword = "yjh2017E!";
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(dbURL, dbID, dbPassword);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	
	public int upload(String fileName, String fileRealName, int bbsID) {
		String SQL = "INSERT INTO bbs_file2 VALUES (?,?,?)";
		try {
			
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setString(1, fileName);
			pstmt.setString(2, fileRealName);
			pstmt.setInt(3, bbsID);
			return pstmt.executeUpdate();
		} catch (Exception e) {
			
		}
		return -1;
		
	}
	public FileDTO2 getfileName(int bbsID){
		String SQL = "SELECT * FROM bbs_file2 WHERE bbsID = ?";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			pstmt.setInt(1, bbsID);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				FileDTO2 f = new FileDTO2();
				f.setFileName(rs.getString(1));
				f.setFileRealName(rs.getString(2));
				return f;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	

}
