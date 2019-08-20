
# Reconn : A python based photo management app using Folium 
This is a fun project I built to manage the photos I used to take for work. As a civil engineer, I would go out to inspect construction sites, and naturally, take lots of photos.
Post-site-visit, I had to make a photo log and document my inspection, but knowing the location of the photos was always a problem. 
If you look at the photos on the layer "Lagrange Bypass", you will see what exactly what I mean. Imagine sorting through photos that all look alike without easy an geolocation system. 

So, I began geotagging all photos i captured using my smartphone and then built this simple application which maps the lat-long on a Folium map with marker popups showing the photo-thumbnail.   

User workflow: simply paste geotagged photos in folder Images -> run Reconn-master.py -> HTML file will a autopopulate markers with image thumbnails

Project setup: 

Root
|-html_files //each image will be saved as html file. \n
|-Images //contains user generated images
|-FoliumMap.html //html file with leaflet map base layer. Additional layers added based on desired groups of markers (like a photo album) 
|-Reconn-master.py //main app file
|-srcscript.js
