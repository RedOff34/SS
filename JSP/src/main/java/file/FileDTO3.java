package file;

public class FileDTO3 {
	
	private String fileName;
	private String fileRealName;
	
	public String getFileName() {
		return fileName;
	}

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}

	public String getFileRealName() {
		return fileRealName;
	}

	public void setFileRealName(String fileRealName) {
		this.fileRealName = fileRealName;
	}


	@Override
	public String toString() {
		return "FileDTO [fileName=" + fileName + ", fileRealName=" + fileRealName + "]";
	
}
}
