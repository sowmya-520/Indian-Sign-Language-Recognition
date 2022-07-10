import cv2
import os
from string import ascii_uppercase
#Creating folders
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")

for i in ascii_uppercase:
    if not os.path.exists("data/train/"+i):
        os.makedirs("data/train/"+i)
    if not os.path.exists("data/test/"+i):
        os.makedirs("data/test/"+i)

mode = 'train'   #train/test
folder = 'data/'+mode+'/'
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    #Retrieving the length of data in a folder
    no_of_img = {                                     
        'A': len(os.listdir(folder + "/A")),
        'B': len(os.listdir(folder + "/B")),
        'C': len(os.listdir(folder + "/C")),
        'D': len(os.listdir(folder + "/D")),
        'E': len(os.listdir(folder + "/E")),
        'F': len(os.listdir(folder + "/F")),
        'G': len(os.listdir(folder + "/G")),
        'H': len(os.listdir(folder + "/H")),
        'I': len(os.listdir(folder + "/I")),
        'J': len(os.listdir(folder + "/J")),
        'K': len(os.listdir(folder + "/K")),
        'L': len(os.listdir(folder + "/L")),
        'M': len(os.listdir(folder + "/M")),
        'N': len(os.listdir(folder + "/N")),
        'O': len(os.listdir(folder + "/O")),
        'P': len(os.listdir(folder + "/P")),
        'Q': len(os.listdir(folder + "/Q")),
        'R': len(os.listdir(folder + "/R")),
        'S': len(os.listdir(folder + "/S")),
        'T': len(os.listdir(folder + "/T")),
        'U': len(os.listdir(folder + "/U")),
        'V': len(os.listdir(folder + "/V")),
        'W': len(os.listdir(folder + "/W")),
        'X': len(os.listdir(folder + "/X")),
        'Y': len(os.listdir(folder + "/Y")),
        'Z': len(os.listdir(folder + "/Z")),
    }

    #Displaying the no. of images in particular folder
    cv2.putText(frame, "A: "+str(no_of_img['A']), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "B: "+str(no_of_img['B']), (10,32 ), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "C: "+str(no_of_img['C']), (10, 44), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "D: " + str(no_of_img['D']), (10,56), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "E: " + str(no_of_img['E']), (10,68), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "F: " + str(no_of_img['F']), (10,80), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "G: " + str(no_of_img['G']), (10, 92), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "H: " + str(no_of_img['H']), (10, 104), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "I: " + str(no_of_img['I']), (10, 206), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "J: " + str(no_of_img['J']), (10, 218), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "K: " + str(no_of_img['K']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "L: " + str(no_of_img['L']), (10, 242), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "M: " + str(no_of_img['M']), (10, 254), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "N: " + str(no_of_img['N']), (10, 266), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "O: " + str(no_of_img['O']), (10, 278), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "P: " + str(no_of_img['P']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Q: " + str(no_of_img['Q']), (10, 302), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "R: " + str(no_of_img['R']), (10, 314), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "S: " + str(no_of_img['S']), (10, 326), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "T: "+str(no_of_img['T']), (10, 338), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "U: "+str(no_of_img['U']), (10,350), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "V: "+str(no_of_img['V']), (10,362), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "W: " + str(no_of_img['W']), (10,374), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "X: " + str(no_of_img['X']), (10,386), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Y: " + str(no_of_img['Y']), (10, 398), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Z: " + str(no_of_img['Z']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    
    #ROI dimensions
    x1 = int(0.5*frame.shape[1])
    x2 = frame.shape[1]-10
    y1 = 10
    y2 = int(0.5 * frame.shape[1])
    cv2.rectangle(frame,(319,9),(620+1,309),(0,255,0),1)
    roi=frame[10:300,320:620]
    cv2.imshow("Frame", frame)

    #Image Pre-processing
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gaussblur = cv2.GaussianBlur(gray,(5,5),2)
    smallthres = cv2.adaptiveThreshold(gaussblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,2.8)
    ret, final_image = cv2.threshold(smallthres, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    final_image = cv2.resize(final_image, (300, 300))
    cv2.imshow("BW", final_image)

    #Inserting the input image into a folder
    interrupt = cv2.waitKey(1)
    if interrupt == ord('A'):
        cv2.imwrite(folder + 'A/' + str(no_of_img['A']) + '.jpg', final_image)
    if interrupt == ord('B'):
        cv2.imwrite(folder + 'B/' + str(no_of_img['B']) + '.jpg', final_image)
    if interrupt == ord('C'):
        cv2.imwrite(folder + 'C/' + str(no_of_img['C']) + '.jpg', final_image)
    if interrupt == ord('D'):
        cv2.imwrite(folder +'D/'+str(no_of_img['D'])+'.jpg', final_image)
    if interrupt == ord('E'):
        cv2.imwrite(folder +'E/'+str(no_of_img['E'])+'.jpg', final_image)
    if interrupt == ord('F'):
        cv2.imwrite(folder +'F/'+str(no_of_img['F'])+'.jpg', final_image)
    if interrupt == ord('G'):
        cv2.imwrite(folder +'G/'+str(no_of_img['G'])+'.jpg', final_image)
    if interrupt == ord('H'):
        cv2.imwrite(folder +'H/'+str(no_of_img['H'])+'.jpg', final_image)
    if interrupt == ord('I'):
        cv2.imwrite(folder +'I/'+str(no_of_img['I'])+'.jpg', final_image)
    if interrupt == ord('J'):
        cv2.imwrite(folder +'J/'+str(no_of_img['J'])+'.jpg', final_image)
    if interrupt == ord('K'):
        cv2.imwrite(folder + 'K/' + str(no_of_img['K']) + '.jpg', final_image)
    if interrupt == ord('L'):
        cv2.imwrite(folder + 'L/' + str(no_of_img['L']) + '.jpg', final_image)
    if interrupt == ord('M'):
        cv2.imwrite(folder + 'M/' + str(no_of_img['M']) + '.jpg', final_image)
    if interrupt == ord('N'):
        cv2.imwrite(folder +'N/'+str(no_of_img['N'])+'.jpg', final_image)
    if interrupt == ord('O'):
        cv2.imwrite(folder +'O/'+str(no_of_img['O'])+'.jpg', final_image)
    if interrupt == ord('P'):
        cv2.imwrite(folder +'P/'+str(no_of_img['P'])+'.jpg', final_image)
    if interrupt == ord('Q'):
        cv2.imwrite(folder +'Q/'+str(no_of_img['Q'])+'.jpg', final_image)
    if interrupt == ord('R'):
        cv2.imwrite(folder +'R/'+str(no_of_img['R'])+'.jpg', final_image)
    if interrupt == ord('S'):
        cv2.imwrite(folder +'S/'+str(no_of_img['S'])+'.jpg', final_image)
    if interrupt == ord('T'):
        cv2.imwrite(folder +'T/'+str(no_of_img['T'])+'.jpg', final_image)
    if interrupt == ord('U'):
        cv2.imwrite(folder +'U/'+str(no_of_img['U'])+'.jpg', final_image)
    if interrupt == ord('V'):
        cv2.imwrite(folder +'V/'+str(no_of_img['V'])+'.jpg', final_image)
    if interrupt == ord('W'):
        cv2.imwrite(folder +'W/'+str(no_of_img['W'])+'.jpg', final_image)
    if interrupt == ord('X'):
        cv2.imwrite(folder +'X/'+str(no_of_img['X'])+'.jpg', final_image)
    if interrupt == ord('Y'):
        cv2.imwrite(folder +'Y/'+str(no_of_img['Y'])+'.jpg', final_image)
    if interrupt == ord('Z'):
        cv2.imwrite(folder +'Z/'+str(no_of_img['Z'])+'.jpg', final_image)
    if interrupt  == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
