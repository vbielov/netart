var imgContainer = document.all["summer"];
var increment = 0;

var links = [
    "http://1x-upon.com/~despens/olia/summer/olia01.gif",
    "http://www.newrafael.com/olia/summer/olia02.gif",
    "http://www.entropy8.com/olia/summer/olia02.gif",
    "http://nikoprincen.com/olia/summer/olia03.gif",
    "http://saskia-aldinger.com/olia/summer/olia03.gif",
    // "http://www.sebastianschmieg.com/olia/summer/misc/olia/olia04.gif",
    "http://www.constantdullaart.com/olia/summer/olia05.gif",
    // "http://GLI.TC/H/olia/summer/not_found",
    "http://jonaslund.biz/olia/summer/olia06.gif",
    "http://bukk.it/olia/summer/olia07.gif",
    "http://thxalot.org/olia/summer/olia07.gif",
    "http://www.raquelmeyers.com/olia/summer/olia08.gif",
    "http://www.anthonyantonellis.com/olia/summer/olia09.gif",
    "http://kevinbewersdorf.org/olia/summer/olia10.gif",
    // "http://www.emiliegervais.com/olia/summer/olia10.gif",
    "http://kimasendorf.com/olia/summer/olia11.gif",
    "http://jamesbridle.com/olia/summer/olia12.gif",
    // "http://www.bram.org/olia/summerolia13.gif",
    "http://todayandtomorrow.net/olia/summer/olia13.gif",
    "http://jaka.org/olia/summer/olia14.gif",
    "http://www.leegte.org/olia/summer/olia15.gif",
    // "http://www.faithholland.com/olia/summer/not_found",
    "http://www.evan-roth.com/olia/summer/olia17.gif",
    "http://k0a1a.net/olia/summer/olia18.gif",
    "http://reas.com/olia/summer/olia18.gif",
];

var images = []
function loadImageAndCache(url) {
    var img = new Image();
    img.src = url;
    img.style.display = "none"; // Hide the image
    imgContainer.appendChild(img); // Append to body to cache
    images.push(img);
}

function updateImage() {
    images[increment].style.display = "none";
    increment = (increment + 1) % images.length;
    images[increment].style.display = "block";
}

for(var i = 0; i < links.length; i++) {
    loadImageAndCache(links[i]);
}

setInterval(updateImage, 1000);


