class Resume:

	def __init__(self, nm, title, pho, mail):
		self.name = nm
		self.title = title
		self.phone = pho
		self.email = mail
		self.score = 0

		self.jobs = []
		self.education = []
		self.socials = []
		self.projects = []
		self.skills = []

	def addJob(self, job):

		self.jobs.append(job)

	def addEdu(self, edu):

		self.education.append(edu)

	def addSocial(self, social):

		self.socials.append(social)		

	def addProject(self, proj):
		self.projects.append(proj)

	def getName(self):
		return self.name

	def getTitle(self):
		return self.title

	def get(self, stringy):

		lst = []

		if stringy == "projects":
			for i in self.projects:
				lst.append(i.display())
		elif stringy == "jobs":
			for i in self.jobs:
				lst.append(i.display())
		elif stringy == "edu":
			for i in self.education:
				lst.append(i.display())
		elif stringy == "skills":
			for i in self.skills:
				lst.append(i.display())
		else: 
			print ("invalid input!")

		return lst


class Job:

	def __init__(self, c_name, pos, deets):

		self.companyName = c_name
		self.position = pos
		self.details = deets
#		self.responsibilities = []


	def addRespo(self, strg):
		self.responsibilities.append(strg)

	def display(self):
		st =  "<h2>" + str(self.companyName) + " </h2> <br/> " + str(self.position) + " </br> " + str(self.details)   	
		return st

class Education:

	def __init__(self, s_name, maj):

		self.schoolName = s_name
		self.major = maj

	def display(self):
		st =  "<h2>" + str(self.schoolName) + "</h2> <br/> " + str(self.major) + " </br> " 	
		return st

class Social:

	def __init__(self, c_type, ico, hand, lnk):

		self.contactType = c_type
		self.icon = ico
		self.handle = hand
		self.link = link

	def display(self):
		st = str(self.ico) + " <br/> " + str(self.handle) 	
		return st


class Project:

	def __init__(self, p_name, med, des):

		self.projectName = p_name
		self.mediums = med
		self.description = des
		self.award = 'None'

	def addAward(self, awd):
		self.award = awd

	def display(self):
		st = "<h2>" + str(self.projectName) + " </h2> <br/>Mediums: " + str(self.mediums) + "<br/><br/> " + str(self.description) 
		return st



