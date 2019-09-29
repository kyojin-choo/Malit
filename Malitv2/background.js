// background.js
// Scripts to fetch usernames from the comment page
//console.log('here');

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
      var data = new Array(request);
      //console.log(request);
      sendResponse();
      console.log(data);
  }
);



