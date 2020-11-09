function update() {

    console.log("polling...");

    var xhttp = new XMLHttpRequest();
    xhttp.timeout = 50000;

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("got response");
            document.getElementById("log-container").insertAdjacentHTML("afterbegin", this.responseText);
            update();
        }
        //document.write(this.responseText);
            //document.getElementById("log-container").innerHTML += this.responseText;
    };

    xhttp.open("GET", "poll", true);
    xhttp.send();
}