import cv2
 
car_cascade = cv2.CascadeClassifier('cars3.xml')

class ImageProc():
	'''
	Image Proccesing Unit

	video -> #cars in left lane/s, #cars in center lane/s, #cars in right lane/s

	This Function takes Video source & ranges of left and right lanes 
	Return the number of cars in each lane (right, center, left) per frame.
	'''

	def __init__(self, source, left=0, right=0, left_lane=0, right_lane=0):

		self.source = source
		self.left = left
		self.right = right
		self.left_lane = left_lane
		self.right_lane = right_lane


	def run(self):

		self.live_stream = cv2.VideoCapture(self.source)

		if self.live_stream.isOpened():
			pass
		else:
			self.rval = False
			print("check your Video Source configuration!")

		self.check()

		self.status = 1

		while self.status:
			self.rval, self.frame = self.live_stream.read()
			self.cars = car_cascade.detectMultiScale(self.frame, 1.1, 2)
			self.left_cars = 0
			self.center_cars = 0
			self.right_cars = 0

			for (self.x, self.y, self.w, self.h) in self.cars:
				
				if(self.left < self.x < self.left_lane):
					self.left_cars += 1
					# cv2.rectangle(self.frame,(self.x,self.y),(self.x+self.w,self.y+self.h),(255,0,0),2)

				elif(self.left_lane < self.x < self.right_lane):
					self.center_cars += 1
					# cv2.rectangle(self.frame,(self.x,self.y),(self.x+self.w,self.y+self.h),(0,255,0),2)

				elif(self.right_lane < self.x < self.right):
					self.right_cars += 1
					# cv2.rectangle(self.frame,(self.x,self.y),(self.x+self.w,self.y+self.h),(0,0,255),2)

			# cv2.imshow("Result",self.frame)
		return self.right_cars, self.center_cars, self.left_cars


	def check(self):

		if self.left_lane < self.left:
			self.left_lane = self.left

		if self.right == 0 :
			self.right = self.live_stream.get(3)

		if self.right_lane < self.right:
			self.right_lane = self.right
