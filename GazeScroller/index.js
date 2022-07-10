// Inject the iframe to retrieve camera sources
var iframe = document.createElement('iframe');
iframe.style.display = "none";
iframe.src = chrome.extension.getURL('source.html');
iframe.allow = "camera";
document.body.appendChild(iframe);