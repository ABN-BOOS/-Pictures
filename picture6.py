#/!/user/bin/env python
#the cood from python

# معالجة الصورة:
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
img = Image.open("D:\python\dog.jpg")
print (img.format) # إخراج المعلومات الأساسية للصورة
print(img.mode)
print(img.size)
 
 
 img_resize = img.resize ((256،256)) # ضبط الحجم
img_resize.save("dogresize.jpg")
 img_rotate = img.rotate (45) # تدوير
img_rotate.save("dogrotate.jpg")
 om = img.convert ('L') # معالجة تدرج الرمادي
om.save('doggray.jpg')
 om = img.filter (ImageFilter.CONTOUR) # مخطط الصورة
om.save('dogcontour.jpg')
 om = ImageEnhance.Contrast (img) .enhance (20) # التباين هو 10 أضعاف القيمة الأولية
om.save('dogencontrast.jpg')
 # تغيير تنسيق الصورة:
from PIL import Image
import os
 
filelist =["dog.jpg",
           "dogcontour.jpg",
           "dogencontrast.jpg",
           "doggray.jpg",
           "dogresize.jpg",
           "dogrotate.jpg",
           ]
for infile in filelist:
  outfile = os.path.splitext(infile)[0] + ".png"
  if infile != outfile:
    try:
      Image.open(infile).save(outfile)
    except IOError:
      print ("cannot convert", infile)