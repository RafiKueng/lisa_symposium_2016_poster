#!/usr/bin/env python 


# qr "geo:47.3979,8.5502?z=15" > irchel_geo_qr.png
# qr "tiny.uzh.ch/ys" > homepage_qr.png
# qr "BEGIN:VEVENT
# SUMMARY:LISA Symposium 11
# LOCATION:UZH,ZURICH,CH
# DTSTART:20160905T090000Z
# DTEND:20160909T150000Z
# END:VEVENT" > event_qr.png


data = {
    'irchel_geo_qr.png': ("geo:47.3979,8.5502?z=15",0,None),
    'homepage_qr.png'  : ("tiny.uzh.ch/ys",4, (9,39,129)),
    'event_qr.png'     : ("BEGIN:VEVENT\nSUMMARY:LISA Symposium 11\nLOCATION:UZH,ZURICH,CH\nDTSTART:20160905T090000Z\nDTEND:20160909T150000Z\nEND:VEVENT",0,None)
}


import qrcode

for fn, _ in data.items():
    d, b, c = _

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=b,
    )

    qr.add_data(d)
    qr.make(fit=True)

    img = qr.make_image()

    if c:
        img = img.convert("RGB")
        pixdata = img.load()
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y] == (0, 0, 0):
                    pixdata[x, y] = c
                    
                    
    img.save(fn)

                    
