package study;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import bbs.Bbs;

public class StudyDAO {
	private Connection conn;
	private ResultSet rs;

	public StudyDAO() {
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
	
	public Study getStudy(int groupID) {
		String SQL = "SELECT * FROM CHAT2 WHERE groupID = ?";
		try {
			PreparedStatement pstmt = conn.prepareStatement(SQL);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				Study s = new Study();
				s.setGroupID(rs.getInt(1));
				s.setUserID(rs.getString(2));
				s.setLeader(rs.getString(3));
				return s;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
}
