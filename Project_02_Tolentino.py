# Jonathan P. Tolentino
# CS 555
# Project 02
# 02/02/2019

import sys
import os 
cwd = os.path.dirname(os.path.realpath(__file__))

class GEDCOM_Line:

	Level = 0
	Tag = 'default'
	Valid = 'N'
	Args = ''

	def Parse(self, line):
		'''
			Parse an input line into a GEDCOM_Line object
		'''

		token = line.split()

		self.Level = token[0]
		self.Tag = token[1].upper()

		# Check the value of token[2], certaing tags appear after the args
		if len(token) > 2:
			if token[2].upper() == 'INDI' or token[2].upper() == 'FAM' or token[2].upper() == 'SUBM':
				self.Tag = token[2].upper()
				self.Args = token[1]
			else:	
				for i in range(2, len(token)):
					self.Args += (token[i] + ' ')

	def Validate(self):
		'''
			Compare the Tag to the set of valid tags
		'''
		validTags = {'INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 
					 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 
					 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'}

		if self.Tag in validTags:
			self.Valid = 'Y'
		else:
			self.Valid = 'N'	

# Validate command line args
if len(sys.argv) < 2:
	print('Ussage Error: No input file provided')
	quit()

# File validation
fileName, fileExtension = os.path.splitext((cwd + '/' + sys.argv[1]))

if fileExtension != '.ged':
	print('Error input file must be in .ged format')
	quit()

fileName += fileExtension

try:
	with open(fileName) as gedFile:
		
		line = gedFile.readline()

		# Parse the file
		while line:
			gedLine = GEDCOM_Line()
			gedLine.Parse(line)
			gedLine.Validate()
			line = line.rstrip()

			# Output
			print('--> ' + line)
			print('<-- ' + gedLine.Level + '|' + gedLine.Tag + '|' + gedLine.Valid + '|' + gedLine.Args)

			line = gedFile.readline()

except IOError as e:
	print('Error opening ' + sys.argv[1] + ': ' + str(e))

finally:
	gedFile.close()
