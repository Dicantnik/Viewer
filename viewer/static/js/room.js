
const RoomCode = JSON.parse(document.getElementById('json-code').textContent)
const username = document.querySelector('.user').textContent
const Input = document.querySelector('.input_message')
const SendMessage = document.querySelector('.send_message')
const chat = document.querySelector('.messages')
const videocode = JSON.parse(document.getElementById('videocode').textContent)

var player;

const Socket = new WebSocket(
    'ws://' + window.location.host + '/ws/' + RoomCode + '/'
)

Socket.onopen = (e) => {
    console.log('Websocket - Open')
}

Socket.onmessage = (e) => {
    data = JSON.parse(e.data) 
    console.log('MESSAGE')
    
    if (data.type === 'message'){
        chat.innerHTML += `<div class="message">`
        chat.innerHTML += `<p>${data.sender}</p>`
        chat.innerHTML += `<p>${data.message}</p>`
        chat.innerHTML += `</div>`
    }
    else if (data.type === 'video') {
        if (data.message === 'playing') {


            // player.seekTo(data.time, false)
            // setTimeout(player.playVideo, 2000)
            player.playVideo()
        }
        else if (data.message === 'paused') {



            // player.seekTo(data.time, false)
            // setTimeout(player.pauseVideo, 2000)
            player.pauseVideo()
        }
    }

}

Socket.onclose = (e) => {
    console.log('CLOSE')
}

SendMessage.addEventListener('click', () => {
    Socket.send(
        JSON.stringify({
            'type': 'message',
            'message': Input.value,
            'sender': username,
        })
    )
    Input.value = ''
})



var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[2];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '360',
        width: '640',
        videoId: videocode,
        events: {
        // 'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
        }
        
        });
        // var duration = player.getDuration()
        // player.seekTo(0, true)
}

// 4. The API will call this function when the video player is ready.
//   function onPlayerReady(event) {
//     event.target.playVideo();
//   }

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        console.log('playing')
        console.log(player.getCurrentTime())
        Socket.send(
            JSON.stringify({
                'type': 'video',
                'message': 'playing',
                'time': player.getCurrentTime(),
            })
        )
    }
    if (event.data == YT.PlayerState.PAUSED) {
        console.log('paused')
        console.log(player.getCurrentTime())
        Socket.send(
            JSON.stringify({
                'type': 'video',
                'message': 'paused',
                'time': player.getCurrentTime(),
            })
        )
    }
}

// function onPlayerReady(event) {
//     console.log('START')
//     player.seekTo(0, true)
// }
  

