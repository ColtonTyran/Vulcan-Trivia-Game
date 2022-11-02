class Genre:
	def __init__(self, txt_file, image):
		self.setFile(txt_file)
		self.setImage(image)
		self.setGenre()
		
	def setGenre(self):
		if self.file:
			genre = self.file.split('.')[0]
			self.genre = genre
		else:
			self.genre = None

	def setImage(self, img):
		self.image = img

	# changed 1 to -1, should not assume that file is first in array, we can assume it is always last in the array
	def setFile(self, file):
		if file.split('.')[-1] != 'txt':
			self.file = None
		else:
			self.file = file

	def __str__(self):
		return (f'Genre: {self.genre} Image: {self.image} File: {self.file}')