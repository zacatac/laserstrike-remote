// function timedRefresh(timeOutPeriod){
//     // setTimeout("location.reload(true);",timeOutPeriod);
//     js = "$('.refresh-row').load(document.URL +  '.refresh-row');"
//     setTimeout(js,timeOutPeriod);
// }

setInterval( function() {
    $('#refresh-row').load('http://192.168.10.101:5000 #refresh-row');
}, 1000); //repeat function every 5000 milliseconds


setInterval( function() {
	if (parseInt($('#timer').text().slice(0,1)) > 5){
		alert('The next game should begin soon');
	}
}, 30000);