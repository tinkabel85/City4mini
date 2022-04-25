let map = L.map('map').setView([53.551, 9.993], 12);

// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//     maxZoom: 18,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: 'pk.eyJ1Ijoib2tzYW5hLW1lIiwiYSI6ImNrenM4b29yZzA1cjkybm82eGhmMDZuc2gifQ.XbrYwR72arrukTcyyOn6sQ'
// }).addTo(map);

// var map = L.map('map', {
//     center: [20.0, 5.0],
//     minZoom: 2,
//     zoom: 2,
// })

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a', 'b', 'c'],
}).addTo(map)

// let myIcon = L.icon({
//     iconUrl: 'https://i.ibb.co/09yrnbc/pin48.png',
//     iconSize: [48, 38],
//     iconAnchor: [9, 21],
//     popupAnchor: [0, -14],
//     className: 'myIcon',
// })

let myIcon = L.divIcon({
    html: "<div  class='marker_pin'></div>",
    iconAnchor: [9, 21],
    popupAnchor: [0, -14]
})
let myIconActive = L.divIcon({
    html: "<div  class='marker_pin_active'></div>",
    iconAnchor: [9, 21],
    popupAnchor: [0, -14]
})
// let markers = [
//     {
//         name: 'Museum of Illisuons',
//         url: 'https://hamburg.museumderillusionen.de/en/',
//         imgUrl: 'https://i.ibb.co/grRBM2d/icon-illus.png',
//         lat: 53.55292,
//         lng: 10.0021,
//     },
//     {
//         name: 'Hamburger Puppentheater',
//         url: 'https://hamburgerpuppentheater.de',
//         imgUrl: 'https://i.ibb.co/7X0TsGT/puppen.jpg',
//         lat: 53.583240,
//         lng: 10.043950,
//     },
//     {
//         name: 'Zoological Museum',
//         url: 'https://hamburg.leibniz-lib.de/en/ausstellungen/museum-zoologie.html',
//         imgUrl: 'https://i.ibb.co/mSnV1Cx/zoo.jpg',
//         lat: 53.567315,
//         lng: 9.978716,
//     },
//     {
//         name: 'Indoor Playground Rabatzz',
//         url: 'https://www.rabatzz.de/',
//         imgUrl: 'https://i.ibb.co/fXV7JH9/rabatzz4.jpg',
//         lat: 53.599832,
//         lng: 9.915805,
//     },
//     {
//         name: 'Emigration Museum',
//         url: 'https://www.ballinstadt.de/en/',
//         imgUrl: 'https://i.ibb.co/g40DKMF/ballin.jpg',
//         lat: 53.520396,
//         lng: 10.016970,
//     },
//     {
//         name: 'The Chocolate Museum ',
//         url: 'https://www.chocoversum.de/',
//         imgUrl: 'https://i.ibb.co/HCTdf7Q/choco.jpg',
//         lat: 53.547935,
//         lng: 10.002276,
//     },
//     {
//         name: 'Miniature Wonderland',
//         url: 'https://www.miniatur-wunderland.com/',
//         imgUrl: 'https://i.ibb.co/3W4fDBw/miniatur.jpg',
//         lat: 53.543729,
//         lng: 9.988516,
//     },

//     {
//         name: 'The Puppenmuseum Falkenstein',
//         url: 'https://www.elke-droescher.de/',
//         imgUrl: 'https://i.ibb.co/WPNkv4J/dolls1.jpg',
//         lat: 53.56599,
//         lng: 9.763900000000035,
//     }
// ]

let icons = [];
let s;
for (let i = 0; i < markers.length; ++i) {
    s = L.marker([markers[i].lat, markers[i].lng], { icon: myIcon })
        .bindTooltip(
            '<a href="' +
            markers[i].url +
            '" target="_blank">' +
            markers[i].name +
            '</a> <div><img src=" ' + markers[i].imgUrl + ' " style="width: 100%" /> </div>',
            {
                direction: 'top'
            }
        )
        .addTo(map)

    let obj = {
        marker: s,
        id: markers[i].id
    }
    icons.push(obj)
}
console.log(icons)
console.log(icons[1].marker)

let list = document.querySelector('.main_list')
let cards = document.querySelectorAll('.main_card');
console.log(cards)


// cards.forEach(list => {
//     list.addEventListener("mouseover", () => {
//         cards.forEach(item => item.classList.remove("active"));
//         list.classList.add("active");
//     }),
//         list.addEventListener("mouseout", () => {
//             cards.forEach(item => item.classList.remove("active"));
//         })
// });


cards.forEach(item => {
    let match = icons.find(element => element.id == item.id)
    item.addEventListener("mouseover", () => {
        console.log(match)
        console.log(item.id)
        match.marker.setIcon(myIconActive)
        // icons.forEach(i => i.setIcon(myIconActive));
        console.log(item.getAttribute("id"))
    });

    item.addEventListener("mouseout", () => {
        match.marker.setIcon(myIcon)
    })
});



