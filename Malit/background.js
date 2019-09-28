chrome.browserAction.onClicked.addListener(function(tab) {
  console.log('Injecting content script(s)');
  chrome.tabs.executeScript(tab.id,{
      code: 'document.body.innerText;'
  },receiveText);
});

function receiveText(resultsArray){
  console.log(resultsArray[0]);
  console.log("TESTTTTTTTTTTTTTTTTTTT");
  console.log(resultsArray[0].search('n'));
}
