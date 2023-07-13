from time import sleep
import module.notion_api.notion_auto as noiton_a
from ast import Module
from wsgiref import headers
import requests, json



#계정 토큰
token = 'secret_v1kjCdDZMNevI72noKtmksEHtwIzrhI2CykJR2cXVSN'


#부모 page
parent_pageID="df0f2f4b-ca24-46e3-a48e-85650cbd5ba5"


#페이지 id 및 헤더
page_header={
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


##############함수부분

#root 페이지의 캘린더 DB 생성
def CreateRootDB(pageId,headers,UserName):
    createDBURL=f"https://api.notion.com/v1/databases"

    DBData={
        "object": "database",
        
        "title": [
            {
                "type": "text",
                "text": {
                    "content": UserName+"_사용자 캘린더"                   
                },                
                "plain_text": UserName+"_사용자 캘린더"                  
            }
        ],
        "properties": {
            "날짜": {
                "id": "%40diA",
                "name": "날짜",
                "type": "date",
                "date": {}
            },
            "내용": {
                "id": "%5BhX%40",
                "name": "내용",
                "type": "rich_text",
                "rich_text": {}
            },
            "할일": {
                "id": "title",
                "name": "할일",
                "type": "title",
                "title": {}
            }
        },
        "parent": {
        "type": "page_id",
        "page_id": "df0f2f4b-ca24-46e3-a48e-85650cbd5ba5"
        }
        
    }
    
    #DB데이터를 dict에서 JSON 형식으로 파싱
    d = json.dumps(DBData)    
    res = requests.request("POST", createDBURL, headers=headers, data=d)

    #셀레니움으로 자동 캘린더 보기 설정
    #noiton_a.view_cal_auto(find_UserDBid(UserName))
    str=find_UserDBid(UserName)
    new_str=str.replace('-','')
    noiton_a.view_cal_auto(new_str)
    print('캘린더 생성 완료!')




#DB 쿼리 호출
def readDatabase_query(database_ID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{database_ID}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    print(res.text)

    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

#DB 쿼리 스키마
def readDatabase(database_ID, headers):
        readUrl= f"https://api.notion.com/v1/databases/{database_ID}"

        res = requests.request("GET", readUrl, headers=headers)
        data=res.json()
        print(res.status_code)
        
        print(res.text)

        with open('.\db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)




#캘린더 내용 수정
def updateValue(pageId, headers,T,V,D):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
         "properties": {
            "할일": {
                "title": [
                    {
                        "text": {
                            "content": T
                        }
                    }
                ]
            },
            "내용": {
                "rich_text": [
                    {
                        "text": {
                            "content": V
                        }
                    }
                ]            
            },

            "날짜":{
               "date": {
                     "start": D 
                     #date 형식 "start": "2022-08-15"
                }
            }
            
        }
    }
    data = json.dumps(updateData)
    response = requests.request("PATCH", updateUrl, headers=headers, data=data)
    '''
    데이터 출력 확인
    print(response.status_code)
    print(response.text)
    '''

#캘린더 내용 생성
def createvalue(databaseId, headers,T,V,D):

    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": { "type": "database_id", "database_id": databaseId },
          "properties": {
            "할일": {
                "title": [
                    {
                        "text": {
                            "content": T
                        }
                    }
                ]
            },
            "내용": {
                "rich_text": [
                    {
                        "text": {
                            "content": V
                        }
                    }
                ]            
            },

            "날짜":{
               "date": {
                     "start": D 
                     #date 형식 "start": "2022-08-15"
                }
            }
            
        }
    }
    
    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)



#캘린더 특정 내용 삭제 
def deletevalue(find_valueID, headers):
     deleteUrl = f"https://api.notion.com/v1/blocks/{find_valueID}"
     res = requests.request("DELETE", deleteUrl, headers=headers)
   


#root 페이지 블록 정보 가져오기
def root_viewBlock():
    url = "https://api.notion.com/v1/blocks/df0f2f4bca2446e3a48e85650cbd5ba5/children?page_size=100"
    headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "authorization": "Bearer secret_v1kjCdDZMNevI72noKtmksEHtwIzrhI2CykJR2cXVSN"
    }

    response = requests.get(url, headers=headers)

    data=response.json()
    with open('.\\notion_json\\root_block.json', 'w', encoding='utf8') as f:
     json.dump(data, f, ensure_ascii=False)


    i=1    
    while i<len(data["results"]):
        if (data["results"][i]["child_database"]["title"]=="마길동"+"_사용자 캘린더"):
            print(data["results"][i]["last_edited_by"]["id"])
        i+=1


#사용자 id별 캘린더 DB 찾기
def find_UserDBid(userID):
       
    url = "https://api.notion.com/v1/blocks/df0f2f4bca2446e3a48e85650cbd5ba5/children?page_size=100"
    headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "authorization": "Bearer secret_v1kjCdDZMNevI72noKtmksEHtwIzrhI2CykJR2cXVSN"
    }

    response = requests.get(url, headers=headers)

    data=response.json()
    with open('.\\notion_json\\root_block.json', 'w', encoding='utf8') as f:
     json.dump(data, f, ensure_ascii=False)


    i=0
    DBid='' 
    while i<len(data["results"]):
    
        if ((data["results"][i]["child_database"]["title"])==userID+"_사용자 캘린더"):
             DBid=data["results"][i]["id"]                   
        i+=1
    return DBid

      


#캘린더 내용 id 가져오기
def find_valueID(database_ID,headers,find_name):
    #find_name은 할일 제목

    readUrl = f"https://api.notion.com/v1/databases/{database_ID}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()

    with open('.find_value.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    i=0
    valueId=''
    while i<len(data["results"]):
        if data["results"][i]["properties"]["할일"]["title"][0]["text"]["content"] == find_name:
            valueId=data["results"][i]["id"]
        i+=1
    return valueId

    


####함수 실행 부분 (추후 수정)


#root_viewBlock()


#readDatabase(find_UserDBid('마길동'), page_header)
#readDatabase_query(find_UserDBid('마길동'), page_header)


#createvalue(find_UserDBid('마길동'), page_header,'Test제목','내용11',"2022-09-20")

#readDatabase_query(find_UserDBid('마길동'), page_header)

#print(find_valueID(find_UserDBid('마길동'),page_header,'g2'))

#updateValue( find_valueID(find_UserDBid('마길동'),page_header,'수정 전 제목') ,page_header,'수정후 제목22','수정후 내용','2022-09-19')
#deletevalue(find_valueID(find_UserDBid('마길동'),page_header,'ㅎㅇ'), page_header)

#캘린더 생성
#CreateRootDB(parent_pageID,page_header, '홍길동')
#캘린더 내용 추가
#createvalue(find_UserDBid('홍길동'), page_header,'Test제목','내용test',"2022-09-28")
#캘린더 내용 수정
#updateValue( find_valueID(find_UserDBid('홍길동'),page_header,'Test제목') ,page_header,'수정후 제목','수정후 내용','2022-09-21')
#캘린더 내용 삭제
#deletevalue(find_valueID(find_UserDBid('홍길동'),page_header,'수정후 제목'), page_header)

