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

let myIcon = L.icon({
    iconUrl: 'https://i.ibb.co/09yrnbc/pin48.png',
    iconSize: [48, 38],
    iconAnchor: [9, 21],
    popupAnchor: [0, -14],
})

for (let i = 0; i < markers.length; ++i) {
    L.marker([markers[i].lat, markers[i].lng], { icon: myIcon })
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
}

const card_preview = document.querySelector('.main_card');
const card = document.querySelector('.show_card');

