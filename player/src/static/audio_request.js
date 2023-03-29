export async function sendTimeStamp(timeStamp){
    let response_url = parse('/audio/123/%s', timeStamp);
    let response = await fetch(response_url, {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json;charset=utf-8'
        },
    });
    
    
    let json_response = await response.json();
    
    let predicted_text = json_response["predictions"]


    console.log(response);
    if ('speechSynthesis' in window) {
        var synthesis = window.speechSynthesis;

        // Get the first `en` language voice in the list
        var voice = synthesis.getVoices().filter(function (voice) {
            console.log(voice.name);
            return voice.name === 'Milena';
        })[0];
        console.log(synthesis.getVoices());

        console.log(voice);

        // Create an utterance object
        var utterance = new SpeechSynthesisUtterance(predicted_text);

        // Set utterance properties
        utterance.voice = voice;
        utterance.pitch = 1.3;
        utterance.rate = 0.9;
        utterance.volume = 0.8;

        // Speak the utterance
        synthesis.speak(utterance);
    } else {
        console.log('Text-to-speech not supported.');
    }
}

function parse(str) {
    var args = [].slice.call(arguments, 1),
        i = 0;

    return str.replace(/%s/g, () => args[i++]);
}
