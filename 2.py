f1=open("marks.txt","r")
names=[]
total=[]
subject=[]
english=[]
maths=[]
physics=[]
chemistry=[]
biology=[]
topperEng=[]
topperMath=[]
topperPhy=[]
topperChe=[]
topperBio=[]
goldmedalist=[]
for i in range(0,26,1):
   
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
   
   
    list2=list1[3].split(":")
    subject.append(list2[0])   #for subject name
    english.append(int(list2[1]))   #for marks scored

    list2=list1[4].split(":")
    subject.append(list2[0])   #for subject name
    maths.append(int(list2[1]))    #for marks scored

    list2=list1[5].split(":")
    subject.append(list2[0])   #for subject name
    physics.append(int(list2[1]))    #for marks scored

    list2=list1[6].split(":")
    subject.append(list2[0])   #for subject name
    chemistry.append(int(list2[1]))    #for marks scored

    list2=list1[7].split(":")
    subject.append(list2[0])   #for subject name
    biology.append(int(list2[1]))    #for marks scored

    total.append(english[i]+maths[i]+physics[i]+chemistry[i]+biology[i]) #for total marks
    
   
maxEng=max(english)
maxMath=max(maths)
maxPhy=max(physics)
maxChe=max(chemistry)
maxBio=max(biology)
maxTotal=max(total)
for i in range(0,26,1):
    if english[i]==maxEng:
        topperEng.append(names[i])
    if maths[i]==maxMath:
        topperMath.append(names[i])
    if physics[i]==maxPhy:
        topperPhy.append(names[i])
    if chemistry[i]==maxChe:
        topperChe.append(names[i])
    if biology[i]==maxBio:
        topperBio.append(names[i])
    if total[i]==maxTotal:
        goldmedalist.append(names[i])
       
       
print(topperEng,"are the toppers in "+subject[0]+" with marks",maxEng)
print(topperMath,"are the toppers in "+subject[1]+" with marks",maxMath)
print(topperPhy," are the toppers in "+subject[2]+" with marks",maxPhy)
print(topperChe,"are the toppers in "+subject[3]+" with marks",maxChe)
print(topperBio,"are the toppers in "+subject[4]+" with marks ",maxBio)
print()
print(goldmedalist,"are the gold medalist with total marks",maxTotal)
