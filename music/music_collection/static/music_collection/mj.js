const preBtn=document.querySelector('.prev-track');
const btnPlayPause=document.querySelector('.playpause-track');
const nextBtn=document.querySelector('.next-track');
const audioEle=document.querySelector('audio')
const name=document.querySelector('#songName')
const volumeslider=document.querySelector('.volumeSlider')
const seek_slider=document.querySelector('.seek-slider')
const search=document.querySelector('.form-control')




/*
search.addEventListener('input',function(e){

console.log(search.value)


})*/
/*
index=0;

let playList=[{
  'id':'mahi.mp3',
  'name':'mahi',
  'artist-name':'neha-kakkar'
  },
  {
  'id':'vac.mp3',
  'name':'vac',
  'artist-name':'dilgit'
  },
  {
  'id':'saluthilla.mp3',
  'name':'saluthilla',
  'artist-name':'priyanka'
  }]
*/

function musicPlay(){
  /*audioEle.src=playList[index].id;*/
  /*name.innerText=playList[index].name;*/
  audioEle.play()
  btnPlayPause.innerHTML='<i class="fa fa-pause">';
  isPlaying=true

}
function musicPause(){
  audioEle.pause()
  btnPlayPause.innerHTML='<i class="fa fa-play">';
  isPlaying=false
}

let isPlaying=false;
btnPlayPause.addEventListener('click',function(){
  
  if(isPlaying){
    musicPause()
  }else{
    musicPlay()
  }
})
const para=document.querySelector('.para');
nextBtn.addEventListener('click',(e)=>{

location.href="next_song/6";

console.log(url)
})


preBtn.addEventListener('click',()=>{
  if (index>0){
  index-=1;
  musicPlay()
  }else{
    console.log("exceeds limit")
  }
})



function seekTo() { 
  // Calculate the seek position by the 
  // percentage of the seek slider  
  // and get the relative duration to the track 
 
  console.log(seek_slider.value)
  seekto = audioEle.duration * (seek_slider.value / 100); 
 
  
  // Set the current track position to the calculated seek position 
  audioEle.currentTime = seekto; 
} 
  
function VolumeChange() { 
  // Set the volume according to the 
  // percentage of the volume slider set 
  console.log(volumeslider.value)
  audioEle.volume = volumeslider.value / 100; 
} 
  
/*function seekUpdate() { 
  let seekPosition = 0; 
  
  // Check if the current track duration is a legible number 
  if (!isNaN(curr_track.duration)) { 
    seekPosition = curr_track.currentTime * (100 / curr_track.duration); 
    seek_slider.value = seekPosition; 
  
    // Calculate the time left and the total duration 
    let currentMinutes = Math.floor(curr_track.currentTime / 60); 
    let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60); 
    let durationMinutes = Math.floor(curr_track.duration / 60); 
    let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60); 
  
    // Add a zero to the single digit time values 
    if (currentSeconds < 10) { currentSeconds = "0" + currentSeconds; } 
    if (durationSeconds < 10) { durationSeconds = "0" + durationSeconds; } 
    if (currentMinutes < 10) { currentMinutes = "0" + currentMinutes; } 
    if (durationMinutes < 10) { durationMinutes = "0" + durationMinutes; } 
  
    // Display the updated duration 
    curr_time.textContent = currentMinutes + ":" + currentSeconds; 
    total_duration.textContent = durationMinutes + ":" + durationSeconds; 
  } 
} 
*/
