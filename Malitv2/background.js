// background.js
// Scripts to fetch usernames from the comment page
//console.log('here');

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
      var data = new Array(request);
      //console.log(request);
      sendResponse();
      console.log(data);
      

      // creating list of users from pulled data
      //for(let name of data){
      //  users.push(name);
     // }
  }
);
/*
document.getElementById("")

function createTable(){
  var body = document.body, tbl = document.createElement('table');
  tbl.setAttribute("id", "data");

  for(var i = 0; i < users.length; i++){
    var tr = tbl.insertRow();
    var td = tr.insertCell();
    td.appendChild(document.createTextNode(users[i]));
  }
  body.appendChild(tbl);
}
*/