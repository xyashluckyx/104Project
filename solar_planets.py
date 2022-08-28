import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (0,0,255)
)

cv2.putText(img,
            "Venus",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (185,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (285,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mars",
            (385,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Jupiter",
            (585,35),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (760,285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Uranus",
            (970,285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Neptune",
            (1120,285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imshow("output",img)

cv2.waitKey(0)
