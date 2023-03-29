
import {AccessButton} from './accessButton.js';
import {sendTimeStamp} from './audio_request.js';

var manifestUri =
    'https://storage.googleapis.com/shaka-demo-assets/angel-one/dash.mpd';

async function init() {
  // When using the UI, the player is made automatically by the UI object.
  const video = document.getElementById('video');
  const ui = video['ui'];
  console.log(ui);
  const controls = ui.getControls();
  shaka.ui.OverflowMenu.registerElement('accessibility', new AccessButton.Factory());
  const player = controls.getPlayer();
  const config = {
    'overflowMenuButtons' : ['cast', 'quality', 'language', 'accessibility']
  }
  ui.configure(config);  
// Attach player and ui to the window to make it easy to access in the JS console.
  window.player = player;
  window.ui = ui;

  // Listen for error events.
  player.addEventListener('error', onPlayerErrorEvent);
  controls.addEventListener('error', onUIErrorEvent);

  const accessibilityButton = document.getElementById('accessibilityButton');
  accessibilityButton.addEventListener('click', getAudioTranscription);


  // Try to load a manifest.
  // This is an asynchronous process.
  try {
    await player.load(manifestUri);
    // This runs if the asynchronous load is successful.
    console.log('The video has now been loaded!');
  } catch (error) {
    onPlayerError(error);
  }
}

function getAudioTranscription(){
    console.log(video.currentTime);
    sendTimeStamp(video.currentTime);
}



function onPlayerErrorEvent(errorEvent) {
  // Extract the shaka.util.Error object from the event.
  onPlayerError(event.detail);
}

function onPlayerError(error) {
  // Handle player error
  console.error('Error code', error.code, 'object', error);
}

function onUIErrorEvent(errorEvent) {
  // Extract the shaka.util.Error object from the event.
  onPlayerError(event.detail);
}

function initFailed() {
  // Handle the failure to load
  console.error('Unable to load the UI library!');
}

// Listen to the custom shaka-ui-loaded event, to wait until the UI is loaded.
document.addEventListener('shaka-ui-loaded', init);
// Listen to the custom shaka-ui-load-failed event, in case Shaka Player fails
// to load (e.g. due to lack of browser support).
document.addEventListener('shaka-ui-load-failed', initFailed);


