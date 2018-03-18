#easy_install pdfquery
import pdfquery
#from cStringIO import StringIO
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
#import toke
import re
import difflib
#from nltk.tokenize import word_tokenize
import nltk
import string
from nltk.tokenize import RegexpTokenizer, word_tokenize,sent_tokenize
from nltk.corpus import stopwords
# Given input text, return list with tokens
def input_file_lines(input_text, tokens):
    tokens = input_text.splitlines();
    return tokens

def input_file_words(input_text, tokens):
    tokens = input_text.split();
    return tokens



def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#data=convert("C:/Users/patel/Desktop/rohan/New folder/sukanyacv.pdf")
#print data
#tokens=toke.input_file_lines(data,[])
#word_tokens=toke.input_file_words(data,[])
#import nltk 
#from nltk.corpus import stopwords 
#stop_words=set(stopwords.words('english'))
#clean_tokens = [w for w in tokens if w not in stop_words]
#print clean_tokens
#print clean_tokens


def preprocess(sentence):
   sentence = sentence.lower()
   tokenizer = RegexpTokenizer(r'\w+')
   tokens = tokenizer.tokenize(sentence)
   #more_filter=re.sub(r'[^\x00-\x7f]',r'', tokens)
   filtered_words = filter(lambda token: token not in stopwords.words('english'), tokens)
   return " ".join(filtered_words)


#sentence = data
#new_data = str(preprocess(sentence))
#new_tokens=str(sent_tokenize(new_data))
#new_words=str(word_tokenize(new_data))
#new_tokens_lines=toke.input_file_lines(new_data,[])
#print clean_tokens
#print clean_tokens
#########----------------common words ------------------#########################
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

#common_words= data
#common_new=' '.join(unique_list(common_words.split()))
#common_new1=toke.input_file_words(common_new,[])

##############------------------------- section_score----------------------#################
##############------------------------- exceptional_section_for_resume_parsing------------#################
def sectscore(data):
    section_tokens=toke.input_file_words(data,[])
    currentIndex = -1
    wordCount = [0, 0, 0, 0]
    for x in section_tokens:
        x = x.lower()
        if (x.strip("!@#$%^&*()_+|}{:?") in ["work experience", "employment", "experience"] and currentIndex != 0):
            currentIndex = 0
        elif (x.strip("!@#$%^&*()_+|}{:?") in ["publications", "projects", "research"] and currentIndex != 1):
            currentIndex = 1
        elif (x.strip("!@#$%^&*()_+|}{:?") in ["leadership", "leadership experience"] and currentIndex != 2):
            currentIndex = 2
        elif (x.strip("!@#$%^&*()_+|}{:?") in ["education", "activites", "skills", "interests", "extracurricular","honors", "references", "awards", "acheivements"]and currentIndex!=3):
            currentIndex = 3
        else:
            wordCount[currentIndex] += 1

    return min(((sum(wordCount) - min(wordCount))) / 450.0,1.0) * 10



###########################----------------------email___PHONE-----------------###################################


def convert_forEMPH(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue().encode('ascii', 'ignore')
    output.close
    return text

from nltk.tokenize.punkt import PunktSentenceTokenizer
tokenizer = PunktSentenceTokenizer()

#### email_id extraction from resume ######

def email_id(fname, pages=None):
    email_id=[]
    mysent=[]
    #data=convert_forEMPH(fname)
    data1=str(fname)
    paragraphs = [p for p in data1.split('\n') if p]
    for paragraph in paragraphs:
        sentences = tokenizer.tokenize(paragraph)
        mysent.append(sentences)
    str_list = list(filter(None, mysent))
    flag=1 
    for i in range(0,len(str_list)):
        str_list1=str(str_list[i])
        mystring = str_list1.replace('\\\\n', ' ').replace('\r', '')
        match = re.findall(r'[\w\.-]+@[\w\.-]+', mystring)
        if len(match) != 0:
            email_id.append(match)
            flag=1
            return match
        else:
            flag=0
    if flag==0:
        return ""
    #return(email_id)
    
###### contact number extraction from resume ########
'''
def contact_no(fname, pages=None):
    contact_no=[]
    mysent=[]
    data=convert_forEMPH(fname)
    data1=str(data)
    paragraphs = [p for p in data1.split('\n') if p]
    for paragraph in paragraphs:
        sentences = tokenizer.tokenize(paragraph)
        mysent.append(sentences)
    str_list = list(filter(None, mysent)) 
    for i in range(0,len(str_list)):
        str_list1=str(str_list[i])
        phone=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', str_list1)
        if len(phone) != 0:
            contact_no.append(phone)
    return(contact_no)
'''

def contact_no_mod(fname, pages=None):
    contact_no=[]
    mysent=[]
    #data=convert_forEMPH(fname)
    data1=str(fname)
    paragraphs = [p for p in data1.split('\n') if p]
    for paragraph in paragraphs:
        sentences = tokenizer.tokenize(paragraph)
        mysent.append(sentences)
    str_list = list(filter(None, mysent)) 
    flag=1
    for i in range(0,len(str_list)):
        str_list1=str(str_list[i])
        phone=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', str_list1)
        if len(phone) != 0:
            for j in range(0,len(phone)):
                phone1=str(phone[j])
                phone2=phone1.replace("-","")
                phone2=phone2.replace(")","")
                phone3=phone2.replace("(","")
                phone4=phone3.replace(" ","")
                if len(phone4) >=10:
                    contact_no.append(phone4)
                    flag=1
                    return phone4
                else:
                    flag=0
    if flag==0:
        return ""
   # return(contact_no)

###########################---------------------------- location_score --------------------######################
def location_matched(word_tokens,location_words):
    count = 0
    location_list=['Ahmedabad','Banglore','Kolkata','Delhi','Eluru']
    userLocation = location_words
    #for _ in location_words:
     #   userLocation.append(location_list[int(_)-1])
    location_lower = [x.lower() for x in userLocation]
    word_tokens_lower = [x.lower() for x in word_tokens]
    #print(userLocation)
    temp=[]
    for i in location_lower:
        for j in word_tokens_lower:
            if i == j:
                count+=1
                temp.append(i)
    #print(temp)
    if count!=0:
        return {'locMatch':temp,'locScore':float(100.00)}
    else:
        return {'locMatch':temp,'locScore':float(0.00)}
        #desire_location=difflib.get_close_matches(i,word_tokens_lower,1,1) ######by default is 60%
        #if len(desire_location)>=1:
        #    count+=1
        #else:
        #    count=0
    #return count
#location_matched_score = location_matched(word_tokens)

#print("location match score : " +str(location_matched_score))

################--------------------------- programming_skills----------------------################
def programming_skills(resume, progWords):
    count =0
    programming_list = ["Python","Machine Learning","C","Java","R"]
    userProgramming = progWords
    #for _ in progWords:
    #    userProgramming.append(programming_list[int(_)-1])
    programmingTotal = 0
    programmingLower=[]
    for i in userProgramming:
        programmingLower.append(i.lower())
    temp = []
    for i in resume:
        if i.lower() in programmingLower:
            if i.lower() not in temp:
                temp.append(i)
                programmingTotal += 1
    progScore = (programmingTotal/len(programming_list))*100
    return {'skiMatch':temp,'skiScore':progScore}
    #print("programming match score : " +str(programmingTotal))

#programming_skills_matched = programming_skills(data)


##########################------------------------college_score------------------##########################
def collegeScore(tokens,universityList):
    university = ["University of Delhi","Indian Institue of Technology","National Institute of Technology","Indian Institute of Information and Technology","West Bengal University of Technology"]
    short_words = ["university", "for","get", "the", "art", "ice", "town", "park", "van", "los", "of"]
    count = 0
    temp=[]
    for college in university:
        for word in tokens:
            if((word.lower() not in short_words) and (word in college) and (len(word) > 2)):
                count+=1
                temp.append(university[university.index(college)])
    #print(temp)

    if count!=0:
        return {'colMatch':temp,'colScore':float(100.00)}
    else:
        return {'colMatch':temp,'colScore':float(0.00)}
#college_match=collegeScore(tokens) 
#print("college match score " +str(college_match) )
#############################--------------------------------- Company score -----------------------################

def companies_matched(data,companies_words=None):
    company_list=["Cognizant Technology Solutions","Infosys Technologies","Fujitsu India","Huawei India","DataBytes Analytics Pvt Ltd"]
    userCompany = companies_words
    #for _ in companies_words:
    #    userCompany.append(company_list[int(_)-1])
    companyTotal = 0
    temp=[]
    for i in range(len(userCompany)):
        if userCompany[i].lower() in data.lower() != -1:
            companyTotal += 1
            temp.append(userCompany[i])
    companyScore=(companyTotal/len(company_list))*100
    #print(temp,companyScore)
    return {'compMatch':temp,'compScore':companyScore}
'''
 if(companies_words==None):
     companies_list=['Cognizant Technology Solutions','Infosys Technologies','Wipro','Hewlett-Packard India','HCL Technologies','Tech Mahindra','IBM India','Ingram Micro India','Redington India',
'Dell India','Oracle India','SAP India','Cisco Systems India','Microsoft India','IGATE','APC by Schneider Electric India','Capgemini India','Intel India','HCL Infosystems','Lenovo India',
'Savex Computers','Mphasis','Syntel','L&T Infotech','Samsung India','Acer India','Rolta India','Mindtree','Genpact','KPIT Technologie','Rashi Peripherals','CSC India','Vakrangee','Cyient'
,'Hexaware Technologies','Tata Technologies','Zensar Technologies','Iris Computers','Apple India','CMC','EMC India','NIIT Technologies','Asus India','Compuage Infocom','Texas Instruments India','Canon India'
,'Lycos Internet','Supertron Electronics','Polaris Consulting & Services','Persistent Systems','Infinite Computer Solutions','Sonata Software','Ricoh India','Neoteric Infomatique','Symantec India'
,'ITC Infotech India','NetApp India','SFO Technologies','3i Infotech','Sify Technologies','Seagate India','CSS Corp','icom Electronic Security Systems','Geometric','Epson India','Mastek'
,'Xerox India','Birlasoft','NIIT Limited','eClerx','OnMobile Global','AGC Networks','Tata Elxsi','Intex Technologies','TAKE Solutions','Adobe Systems India','Aurionpro','Juniper Networks India','Cybage Software'
,'R Systems International','VMware','CORE Education & Technologies','D-Link','Fujitsu India','AMD India','Intellect Design Arena','Fortune Marketing','Trigyn Technologies','Accel Frontline','LG India','Team Computers'
,'CA Technologies India','RS Software','Sasken Communication Technology','Zylog Systems','Subex','Nucleus Software','Huawei India','SQS India BFSI','DataBytes Analytics Pvt Ltd']
 else:
     companies = companies_words
 companiesTotal = 0
 for i in range(len(companies_list)):
        if companies_list[i].lower() in data.lower() != -1:
            companiesTotal += 1
            print(companies_list[i])
   # progScore = min(programmingTotal/10.0, 1) * 5.0
 #print("Comapnies match score : " +str(companiesTotal))
    #company_lower = [x.lower() for x in companies_list]
     #word_tokens_lower = [x.lower() for x in word_tokens]
     #for i in company_lower:
       #desire_companies=difflib.get_close_matches(i,word_tokens_lower,1,.55)
       #if len(desire_companies)==1:
               #count += 1
       #else:
        #count=0
 #return count
#companies_matched_score = companies_matched(data)

#print "Companies  match score : " +str(companies_matched_score)

'''

################----------------------degree_score--------------------####################
def degree_matched(word_tokens,tokens,degreeList,majorList,data):
     count = 0
     count1=0
     degree_list=['Phd.','Msc.','Bsc.','B.E.','B.Tech.']
     specialisation_list=['Mathemnatics','Physics','Electrical Engnieering','Computer Science Engineering','Litrature']
     userDegree=[]
     userMajor=[]
     for _ in degreeList:
        userDegree.append(degree_list[int(_)-1])
     for _ in majorList:
        userMajor.append(specialisation_list[int(_)-1])
           
     word_token_lower=[x.lower() for x in word_tokens]
     degree_lower=[x.lower() for x in userDegree]
     specialisation_lower=[x.lower() for x in userMajor]
     tokens_lower=[x.lower() for x in tokens]
     temp = []
     for  i in degree_lower:
         desire_degree=difflib.get_close_matches(i,word_token_lower,1,1) ##### cut-off value by default is 60%
         #print(desire_degree)
         if len(desire_degree)>=1:
            temp.append(desire_degree)
            count1+=1
     for j in specialisation_lower:
         desire_specialisation=difflib.get_close_matches(j,tokens_lower,1)
         if len(desire_specialisation)>=1:
            temp.append(desire_specialisation)
            count+=1        
     #temp.append(count)

     #for i in range(len(specialisation_list)):
     #   if specialisation_list[i].lower() in data.lower() != -1:
     #      print(specialisation_list[i])
     #      specialisationTotal+= 1
     #      temp.append(specialisation_list[i])
     degreeScore = ((count+count1)/(len(degree_list)+len(specialisation_list)))*100

     return {'degMatch':temp,'degScore':degreeScore}
#degree_score = degree_matched(word_tokens,tokens)

#print("degree match score : " +str(degree_score))





##############################------------------------------------ Word_count score ---------------################
def wordcountscore(word_tokens):
    count = 0
    score = 10
    for i in word_tokens:
        if i!="":
            count +=1
    if count ==550: score -=0 ###### average resume words acc to research from ziprecruiter.com

    else :
        score-=min(abs(550-count)/20,5) ###### accounts for too short and too long resume

#    print count
    return score
#wordcountscore=wordcountscore(word_tokens)

#print("word count score " +str(wordcountscore))

##################-------------------- cgpa calculator -----------------------#############################
import numpy as np
def cgpamatch(resume,cgapwords=None):
   y=[]
   count =0
   for i in word_tokens:
       m=re.findall(r'^(\d{0,1}|\d{0,1}\.\d{1,2})$',i)
       if m:
            y.append(m)
            count +=1
   x = np.array([y])
   y = x.astype(np.float)
   print(count)
   z=np.sum(y)/count
   return z

#cgpamatch=cgpamatch(data)
#print("cgpa match : " + str(cgpamatch))
###################------------------------ job role calculator ------------------------#########################
def jobrole(word_tokens,job_role_words=None):
    count = 0
    if (job_role_words == None):
        job_role_list = ['Data Analyst', 'Data Scientist', 'Data Analytics', 'Big Data Architect']
        job_role_lower = [x.lower() for x in job_role_list]
        word_tokens_lower = [x.lower() for x in word_tokens]
        for i in job_role_lower:
            desire_job = difflib.get_close_matches(i, word_tokens_lower, 1,.4)  ######by default is 60%
            if len(desire_job) == 1:
                count += 1
            else:
                count = 0
    return count

#job_match_score=jobrole(word_tokens)

#print("job match : " + str(job_match_score))
####################-----------------------  work_experience_extractor ----------------------########################


####################-----------------------  avg score extractor ----------------------########################

def overall_weightage_cal(score1,weight1,score2,weight2,score3,weight3,score4,weight4,score5,weight5):
  return ((score1*weight1+score2*weight2+score3*weight3+score4*weight4+score5*weight5)/100)