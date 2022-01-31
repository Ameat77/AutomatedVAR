from kmeans import k_means
from PIL import Image

dic = {0: [115.62280431432974, 128.83035439137134, 60.511402157164866], 1: [112.30386167146975, 121.72391930835735, 55.5535446685879], 2: [116.57994501519318, 137.80306757343365, 82.27608160902908], 3: [114.4098187576984, 117.0777758226289, 57.37392222417737], 4: [121.74208675263775, 138.16803438843297, 115.14849550605706], 5: [118.87855983473513, 140.53283163641728, 94.80640401357533], 6: [107.60404896421845, 123.5613622096673, 50.00690521029504], 7: [139.3046875, 147.33547794117646, 119.73736213235294]}
image = Image.open("196.jpg")
print(k_means(2, image).keys())

'''
{(115.62280431432974, 128.83035439137134, 60.511402157164866): 'Goalkeeper/Referee', 
(112.30386167146975, 121.72391930835735, 55.5535446685879): 0, 
(114.4098187576984, 117.0777758226289, 57.37392222417737): 0, 
(107.60404896421845, 123.5613622096673, 50.00690521029504): 0, 
(116.57994501519318, 137.80306757343365, 82.27608160902908): 1, 
(121.74208675263775, 138.16803438843297, 115.14849550605706): 1, 
(118.87855983473513, 140.53283163641728, 94.80640401357533): 1, 
(139.3046875, 147.33547794117646, 119.73736213235294): 1}
'''