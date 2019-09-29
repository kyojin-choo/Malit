console.log('Injecting content script(s)');


document.addEventListener('DOMContentLoaded', function() {
    var dataButton = document.getElementById('clickme');  
    chrome.tabs.executeScript({
        code: 'document.body.innerHTML;'
    },receiveText);
});

function receiveText(resultsArray){
    var x = document.createElement("div")
    x.innerHTML = resultsArray[0];
    var usernames = x.innerHTML.match(/(?<=data-author=").{3,20}(?=".*?data-replies)/g);
    console.log(usernames);
    chrome.runtime.sendMessage(
        usernames,
        function (response) {
        console.log(response);
    });
}
