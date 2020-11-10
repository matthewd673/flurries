function update() {

    var date = new Date();
    document.getElementById("polling-info-text").innerHTML = "Polling at " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

    var xhttp = new XMLHttpRequest();
    xhttp.timeout = 50000;

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("log-container").insertAdjacentHTML("afterbegin", this.responseText);
            update();
        }
        //document.write(this.responseText);
            //document.getElementById("log-container").innerHTML += this.responseText;
    };

    xhttp.open("GET", "poll", true);
    xhttp.send();
}