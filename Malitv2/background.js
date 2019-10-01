chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
      var data = new Array(request);
      sendResponse();
      console.log(data);
  }
);
