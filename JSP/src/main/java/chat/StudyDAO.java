package chat;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class StudyDAO {
	private Connection conn;
	 
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
	
	//사용자별 groupID 가져오기
	public int getgroupID(String userID) {
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		int result=0;
		
		String SQL = "select groupID FROM study WHERE userID=?";
		try {
			pstmt=conn.prepareStatement(SQL);
			pstmt.setString(1, userID);
			
			//쿼리 실행
			rs = pstmt.executeQuery();
			while (rs.next()) {
				result=rs.getInt("groupID");
			}
			result=rs.getInt("groupID");
			//System.out.println("sql print: ~~ : " +rs);
			
		}catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		return result;
	}
}