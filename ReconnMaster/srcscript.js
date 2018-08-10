window.alert(o);
var count=0;

while (count==0) {
	 var imgs = [];
		 for (var i = 0; i < 15; i++) {
			 imgs[i] = new Image();
			 imgs[i].src = "C:/wamp/www/ReconnMaster/Images2/Image" + i + ".jpg";
		 }
	count++;
}

var img = document.getElementById("MainImg");
	
while(j<imgs.length)
{
	if(j === imgs.length)
	{
		img.src = imgs[0].src;
		j=0;
		break;
	}
	img.src = imgs[j+1].src;
	j=j+1;
	break;
}
	
