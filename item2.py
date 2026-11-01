import random 
def ps_score(p):
    return p
def mostly_skill (p, l):
    ms = (0.95 * p) + (l * 0.05)
    return ms

simulation = 0
applicants = 0
pSkill = []
lucklist = []
PSscores = []
MSscores = []
allPSastro = []
allMSastro = []
astroluck = []
MSpsastro = []
all_applicant_data = []

while simulation != 1000:
    simulation += 1
    while applicants != 18300:
        applicants += 1
        pure_skill = (random.random()) * 100
        pSkill.append(pure_skill)

        luck = ((random.random()) * 100) 
        lucklist.append(luck)

        pureSkillScore = ps_score(pure_skill)
        PSscores.append(pureSkillScore)

        mostlySkillScore = mostly_skill(pure_skill, luck)
        MSscores.append(mostlySkillScore)

    PSscores.sort()
    for i in range(18289, 18300):
        allPSastro.append(PSscores[i])
    
    for i in range(18300):
    #     all_applicant_data.append((MSscores[i], lucklist[i], PSscores[i]))
    # a_sorted = sorted(all_applicant_data) 
    # for i in range(18289, 18300):
    #     allMSastro.append(a_sorted[i][0])
    #     astroluck.append(a_sorted[i][1])
    #     MSpsastro.append(a_sorted[i][2])
    # a = []
    # for i in range (18300):
    #     a.append((MSscores, PSscores))


#ITEM A1
m_pureskill = sum(PSscores)/18300
numerator_sd = []
for i in range(18300):
    x = (PSscores[i] - m_pureskill)**2
    numerator_sd.append(x)

#ITEM D2
# m_pureskill = sum(PSscores)/18300
# numerator_sd = []
# for i in range(18300):
#     x = (PSscores[i] - m_pureskill)**2
#     numerator_sd.append(x)

print(f"a. {sum(allPSastro)/11000}")
print (f"----a1(bonus). standard deviation : {(sum(numerator_sd)/18300)** (1/2)}")

print(f"c. {sum(astroluck)/11000}")
print(f"d. {sum(MSpsastro)/11000}")

#portion of d
# if (sum(MSpsastro)/11000) < (sum(allPSastro)/11000):
#     print ('d1: Yes')
# else:
#     print('d2: No')
