# coding = utf-8
import PyPDF2
def clearBlankLine():
    file1 = open(str(page_num+1)+'.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open(str(page_num+1)+'新的'+'.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()

pdfobject=open('/Users/wangwang/Desktop/8_ECE-TRANS-180a4a3e.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdfobject)
print(pdfreader.numPages)
# page_num=int(input('输入想要的PDF页码，比如想要124页的，那就输入123：'))
for page_num in range(123,133):
    pdfobject=pdfreader.getPage(page_num)
    # print(pdfobject.extractText())
    str1=pdfobject.extractText()
    str1=str1.replace("\n", "")
    str1=str1.replace("\r", "")
    str1=str1.replace(' ','\r')

    with open(str(page_num+1)+'.txt','a',encoding='utf-8') as file_write:
        file_write.write(str1)
    text1=str(page_num+1)+'.txt'
    text2=str(page_num+1)+'新的'+'.txt'
    clearBlankLine()



