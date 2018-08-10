from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image,ImageTk
import os, os.path
import Tkinter, webbrowser
import folium
import shutil

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    #info = image._getexif()
    info = getattr(image, '_getexif', lambda: None)()

    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data

def _get_if_exist(data, key):
    if key in data:
        return data[key]

    return None

def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return lat, lon


################
# Example- FOLIUM INTEGRATION
################

map_1 = folium.Map(location=[33.786915, -84.398074], zoom_start=12,
                   tiles='Stamen Terrain')


if __name__ == "__main__":
    imgs = []
    path = "C:\wamp\www\ReconnMaster\Images"
    valid_images = [".jpg",".gif",".png",".tga"]
    Loc={}

    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue


        address=path+'\\'+f
        imgs.append(address)

        image=Image.open(address)
        exif_data = get_exif_data(image)


        #collect get_lat_lon(exif_data)

        (x,y)= get_lat_lon(exif_data)
        if x is 'None':
            print 'there no location data'
            continue
        else:
            Loc[f]=(x,y)
#print imgs

imagearray=dict()
i=0



for j in Loc.keys():
    address="C:\wamp\www\ReconnMaster\html_files"
    name,ext=j.split('.')
    filename= name+'.html'
    filepath=os.path.join(address,filename)

    file=open(filepath,'w')
    file.write("<html>\n")
    file.write("<h> Filename: "+j+"\n")
    file.write('<img src="http://localhost:8000/ReconnMaster/Images/' + j + '" alt="WTH" style="width:300px;height:300px;"><br>')
    file.write("</html>")
    file.close()

    f=open(filepath,'r')
    text=f.read()

    iframe = folium.element.IFrame(html=text, width=300, height=300)
    imagepopup=folium.Popup(iframe, max_width=2650)
    folium.Marker(Loc[j], popup=imagepopup).add_to(map_1)

    map_1.create_map(path='C:\wamp\www\ReconnMaster\FoliumMap-Sangy.html')

    #os.rename("C:\wamp\www\ReconnMaster\Images2\\renamed.jpg","C:\wamp\www\ReconnMaster\Images2"+"\\"+j)
    #os.remove("C:\wamp\www\ReconnMaster\Images2\\renamed.jpg")

webbrowser.open_new_tab('http:\\localhost:8000\ReconnMaster\FoliumMap-Sangy.html')
print 'THIS WORKS'

