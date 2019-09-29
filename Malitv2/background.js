console.log('here');
// background.js
// Scripts to fetch usernames from the comment page
//console.log('here');

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
      console.log("background.js got a message")
      var data = request;
      //console.log(request);
      sendResponse();
      console.log(data);
  }
);


