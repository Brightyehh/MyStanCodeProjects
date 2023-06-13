"""
File: my_drawing.py
Name: Bright Yeh
----------------------
Draw...draw...draw...
Point...point...point...
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Hunter x Hunter - GON

    This is Gon, the character in my favorite manga Hunter x Hunter.
    The journey of learning coding is like GON becoming a Hunter.
    """
    window = GWindow(width=600, height=700, title='HUNTER')

    # background
    background1 = GRect(600, 700)
    background1.filled = True
    background1.fill_color = 'paleturquoise'
    window.add(background1)
    background2 = GPolygon()
    background2.add_vertex((0, 510))
    background2.add_vertex((100, 580))
    background2.add_vertex((180, 560))
    background2.add_vertex((300, 575))
    background2.add_vertex((410, 585))
    background2.add_vertex((490, 560))
    background2.add_vertex((560, 570))
    background2.add_vertex((600, 580))
    background2.add_vertex((600, 700))
    background2.add_vertex((0, 700))
    background2.filled = True
    background2.fill_color = 'peru'
    window.add(background2)

    # title
    title_1 = GLabel('HUNTER', x=135, y=80)
    title_1.font = 'Verdana-50-bold'
    title_1.color = 'red'
    window.add(title_1)
    title_2 = GLabel('HUNTER', x=135, y=130)
    title_2.font = 'Verdana-50-bold'
    title_2.color = 'maroon'
    window.add(title_2)
    title_3 = GLabel('x', x=307, y=105)
    title_3.font = '-50-bold'
    title_3.color = 'black'
    window.add(title_3)

    # Sleeves
    jay_left_hand = GOval(19, 19, x=226, y=553)
    jay_left_hand.filled = True
    jay_left_hand.fill_color = 'bisque'
    window.add(jay_left_hand)
    jay_right_hand = GOval(19, 19, x=353, y=553)
    jay_right_hand.filled = True
    jay_right_hand.fill_color = 'bisque'
    window.add(jay_right_hand)
    jay_arm = GPolygon()
    jay_arm.add_vertex((261, 490))
    jay_arm.add_vertex((337, 490))
    jay_arm.add_vertex((368, 554))
    jay_arm.add_vertex((230, 554))
    jay_arm.filled = True
    jay_arm.fill_color = 'green'
    window.add(jay_arm)
    jay_cuff1_l = GPolygon()
    jay_cuff1_l.add_vertex((225, 559))
    jay_cuff1_l.add_vertex((233, 543))
    jay_cuff1_l.add_vertex((253, 553))
    jay_cuff1_l.add_vertex((245, 569))
    jay_cuff1_l.filled = True
    jay_cuff1_l.fill_color = 'tomato'
    window.add(jay_cuff1_l)
    jay_cuff2_l = GPolygon()
    jay_cuff2_l.add_vertex((231, 547))
    jay_cuff2_l.add_vertex((227, 555))
    jay_cuff2_l.add_vertex((247, 565))
    jay_cuff2_l.add_vertex((251, 557))
    jay_cuff2_l.filled = True
    jay_cuff2_l.fill_color = 'dimgray'
    window.add(jay_cuff2_l)
    jay_cuff1_r = GPolygon()
    jay_cuff1_r.add_vertex((365, 543))
    jay_cuff1_r.add_vertex((373, 559))
    jay_cuff1_r.add_vertex((353, 569))
    jay_cuff1_r.add_vertex((345, 553))
    jay_cuff1_r.filled = True
    jay_cuff1_r.fill_color = 'tomato'
    window.add(jay_cuff1_r)
    jay_cuff2_r = GPolygon()
    jay_cuff2_r.add_vertex((367, 547))
    jay_cuff2_r.add_vertex((371, 555))
    jay_cuff2_r.add_vertex((351, 565))
    jay_cuff2_r.add_vertex((347, 557))
    jay_cuff2_r.filled = True
    jay_cuff2_r.fill_color = 'dimgray'
    window.add(jay_cuff2_r)

    # Clothes
    jay_clothes = GPolygon()
    jay_clothes.add_vertex((271, 490))
    jay_clothes.add_vertex((327, 490))
    jay_clothes.add_vertex((350, 554))
    jay_clothes.add_vertex((248, 554))
    jay_clothes.filled = True
    jay_clothes.fill_color = 'green'
    window.add(jay_clothes)
    jay_clothes_zip1 = GPolygon()
    jay_clothes_zip1.add_vertex((293, 490))
    jay_clothes_zip1.add_vertex((299, 490))
    jay_clothes_zip1.add_vertex((299, 560))
    jay_clothes_zip1.add_vertex((248, 560))
    jay_clothes_zip1.add_vertex((248, 554))
    jay_clothes_zip1.add_vertex((293, 554))
    jay_clothes_zip1.filled = True
    jay_clothes_zip1.fill_color = 'tomato'
    window.add(jay_clothes_zip1)
    jay_clothes_zip2 = GPolygon()
    jay_clothes_zip2.add_vertex((305, 490))
    jay_clothes_zip2.add_vertex((299, 490))
    jay_clothes_zip2.add_vertex((299, 560))
    jay_clothes_zip2.add_vertex((350, 560))
    jay_clothes_zip2.add_vertex((350, 554))
    jay_clothes_zip2.add_vertex((305, 554))
    jay_clothes_zip2.filled = True
    jay_clothes_zip2.fill_color = 'tomato'
    window.add(jay_clothes_zip2)
    jay_pocket1 = GPolygon()
    jay_pocket1.add_vertex((260, 540))
    jay_pocket1.add_vertex((265, 545))
    jay_pocket1.add_vertex((280, 530))
    jay_pocket1.add_vertex((275, 525))
    jay_pocket1.filled = True
    jay_pocket1.fill_color = 'tomato'
    window.add(jay_pocket1)
    jay_pocket2 = GPolygon()
    jay_pocket2.add_vertex((338, 540))
    jay_pocket2.add_vertex((333, 545))
    jay_pocket2.add_vertex((318, 530))
    jay_pocket2.add_vertex((323, 525))
    jay_pocket2.filled = True
    jay_pocket2.fill_color = 'tomato'
    window.add(jay_pocket2)

    # pants
    jay_pants1 = GPolygon()
    jay_pants1.add_vertex((255, 560))
    jay_pants1.add_vertex((343, 560))
    jay_pants1.add_vertex((340, 585))
    jay_pants1.add_vertex((258, 585))
    jay_pants1.filled = True
    jay_pants1.fill_color = 'green'
    window.add(jay_pants1)
    pants_y = GLabel('Y', 295, 588)
    pants_y.font = 'Helvetica-10'
    window.add(pants_y)
    jay_pants2 = GRect(42, 8, x=256, y=585)
    jay_pants2.filled = True
    jay_pants2.fill_color = 'green'
    window.add(jay_pants2)
    jay_pants3 = GRect(42, 8, x=300, y=585)
    jay_pants3.filled = True
    jay_pants3.fill_color = 'green'
    window.add(jay_pants3)

    # belt
    jay_belt1 = GRect(16, 6, x=291, y=563)
    jay_belt1.filled = True
    jay_belt1.fill_color = 'silver'
    window.add(jay_belt1)
    jay_belt2 = GRect(12, 2, x=293, y=565)
    jay_belt2.filled = True
    jay_belt2.fill_color = 'dimgray'
    window.add(jay_belt2)
    jay_belt3 = GRect(30, 4, x=255, y=564)
    jay_belt3.filled = True
    jay_belt3.fill_color = 'dimgray'
    window.add(jay_belt3)
    jay_belt4 = GRect(30, 4, x=313, y=564)
    jay_belt4.filled = True
    jay_belt4.fill_color = 'dimgray'
    window.add(jay_belt4)

    # legs
    jay_left_leg = GPolygon()
    jay_left_leg.add_vertex((262, 593))
    jay_left_leg.add_vertex((296, 593))
    jay_left_leg.add_vertex((295, 605))
    jay_left_leg.add_vertex((264, 605))
    jay_left_leg.filled = True
    jay_left_leg.fill_color = 'bisque'
    window.add(jay_left_leg)
    jay_right_leg = GPolygon()
    jay_right_leg.add_vertex((336, 593))
    jay_right_leg.add_vertex((302, 593))
    jay_right_leg.add_vertex((303, 605))
    jay_right_leg.add_vertex((334, 605))
    jay_right_leg.filled = True
    jay_right_leg.fill_color = 'bisque'
    window.add(jay_right_leg)

    # boots
    jay_left_boots1 = GRect(33, 6, x=263, y=605)
    jay_left_boots1.filled = True
    jay_left_boots1.fill_color = 'green'
    window.add(jay_left_boots1)
    jay_right_boots1 = GRect(33, 6, x=302, y=605)
    jay_right_boots1.filled = True
    jay_right_boots1.fill_color = 'green'
    window.add(jay_right_boots1)
    jay_left_boots2 = GRect(29, 20, x=265, y=611)
    jay_left_boots2.filled = True
    jay_left_boots2.fill_color = 'green'
    window.add(jay_left_boots2)
    jay_right_boots2 = GRect(29, 20, x=304, y=611)
    jay_right_boots2.filled = True
    jay_right_boots2.fill_color = 'green'
    window.add(jay_right_boots2)
    jay_left_boots3 = GRect(9, 20, x=270, y=611)
    jay_left_boots3.filled = True
    jay_left_boots3.fill_color = 'lightgray'
    window.add(jay_left_boots3)
    jay_right_boots3 = GRect(9, 20, x=319, y=611)
    jay_right_boots3.filled = True
    jay_right_boots3.fill_color = 'lightgray'
    window.add(jay_right_boots3)
    jay_left_boots4 = GOval(27, 10, x=260, y=625)
    jay_left_boots4.filled = True
    jay_left_boots4.fill_color = 'dimgray'
    window.add(jay_left_boots4)
    jay_right_boots4 = GOval(27, 10, x=311, y=625)
    jay_right_boots4.filled = True
    jay_right_boots4.fill_color = 'dimgray'
    window.add(jay_right_boots4)

    # head
    jay_hair = GPolygon()
    jay_hair.add_vertex((208, 449))
    jay_hair.add_vertex((188, 420))
    jay_hair.add_vertex((178, 380))
    jay_hair.add_vertex((156, 327))
    jay_hair.add_vertex((110, 260))
    jay_hair.add_vertex((185, 292))
    jay_hair.add_vertex((175, 186))
    jay_hair.add_vertex((241, 231))
    jay_hair.add_vertex((224, 174))
    jay_hair.add_vertex((260, 220))
    jay_hair.add_vertex((276, 140))
    jay_hair.add_vertex((345, 230))
    jay_hair.add_vertex((380, 170))
    jay_hair.add_vertex((375, 224))
    jay_hair.add_vertex((435, 180))
    jay_hair.add_vertex((420, 296))
    jay_hair.add_vertex((465, 262))
    jay_hair.add_vertex((437, 328))
    jay_hair.add_vertex((421, 373))
    jay_hair.add_vertex((408, 415))
    jay_hair.add_vertex((388, 448))
    jay_hair.add_vertex((299, 490))
    jay_hair.filled = True
    jay_hair.fill_color = 'black'
    window.add(jay_hair)
    jay_face1 = GArc(194, 80, 150, 240, x=202, y=432)
    jay_face1.filled = True
    jay_face1.fill_color = 'bisque'
    window.add(jay_face1)
    jay_face2 = GPolygon()
    jay_face2.add_vertex((213, 452))
    jay_face2.add_vertex((219, 344))
    jay_face2.add_vertex((381, 340))
    jay_face2.add_vertex((386, 450))
    jay_face2.add_vertex((299, 490))
    jay_face2.filled = True
    jay_face2.fill_color = 'bisque'
    jay_face2.color = 'bisque'
    window.add(jay_face2)
    jay_ear_l = GOval(30, 40, x=184, y=417)
    jay_ear_l.filled = True
    jay_ear_l.fill_color = 'bisque'
    window.add(jay_ear_l)
    jay_ear_r = GOval(30, 40, x=386, y=418)
    jay_ear_r.filled = True
    jay_ear_r.fill_color = 'bisque'
    window.add(jay_ear_r)
    jay_eyebrow_l = GArc(30, 60, 30, 120, x=235, y=388)
    window.add(jay_eyebrow_l)
    jay_eyebrow_r = GArc(30, 60, 30, 120, x=335, y=388)
    window.add(jay_eyebrow_r)
    jay_eye_l = GOval(20, 30, x=238, y=410)
    jay_eye_l.filled = True
    jay_eye_l.fill_color = 'black'
    window.add(jay_eye_l)
    jay_eye_r = GOval(20, 30, x=338, y=410)
    jay_eye_r.filled = True
    jay_eye_r.fill_color = 'black'
    window.add(jay_eye_r)
    jay_mouth = GArc(30, 30, 180, 180, x=282, y=448)
    window.add(jay_mouth)


if __name__ == '__main__':
    main()
